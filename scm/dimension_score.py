import numpy as np
import pandas as pd
import sys
import os
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt



current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.append(os.path.join(project_root, "utils"))
sys.path.append(os.path.join(project_root, "Words"))
from word_lists import DIMENSION_TUPLE_LIST
from utility import get_embedding

def find_top_similar_words(target_word, vocab, embeddings, word_to_index, top_n=1000):
    """找到与 target_word 余弦相似度最高的 top_n 个词"""
    if target_word not in word_to_index:
        return []
    
    target_vector = embeddings[word_to_index[target_word]].reshape(1, -1)
    similarities = cosine_similarity(target_vector, embeddings).flatten()
    
    word_similarity_pairs = [(vocab[i], similarities[i]) for i in range(len(vocab)) if vocab[i] != target_word]
    word_similarity_pairs.sort(key=lambda x: x[1], reverse=True)
    
    return [word for word, sim in word_similarity_pairs[:top_n]]


def compute_sweat_score(word, category_list_1, category_list_2, word_to_index, embeddings):
    """计算 word 对于两个类别的 S-WEAT 分数"""
    ## S-weat分数可以反映这个词是更倾向于cold还是warmth，进一步获得warmth的分数
    if word not in word_to_index:
        return None

    word_vector = embeddings[word_to_index[word]].reshape(1, -1)
    
    # 计算两个类别的平均余弦相似度
    avg_sim_1 = np.mean([
        cosine_similarity(word_vector, embeddings[word_to_index[w]].reshape(1, -1))[0][0]
        for w in category_list_1 if w in word_to_index
    ])
    
    avg_sim_2 = np.mean([
        cosine_similarity(word_vector, embeddings[word_to_index[w]].reshape(1, -1))[0][0]
        for w in category_list_2 if w in word_to_index
    ])
    
    # 计算 S-WEAT 分数 (公式： (avg_sim_1 - avg_sim_2) / pooled_std_dev )
    combined_sim = category_list_1 + category_list_2
    pooled_std_dev = np.std([
        cosine_similarity(word_vector, embeddings[word_to_index[w]].reshape(1, -1))[0][0]
        for w in combined_sim if w in word_to_index
    ])
    
    if pooled_std_dev == 0:
        return None
    
    sweat_score = (avg_sim_1 - avg_sim_2) / pooled_std_dev
    return sweat_score


def get_yearly_sweatscore(target_word, embedding_type, category_list_1, category_list_2, year, k):
    
    vocab, embeddings, word_to_index = get_embedding(year, embedding_type)
    top_similar_words = find_top_similar_words(target_word, vocab, embeddings, word_to_index,k)
    word_score = compute_sweat_score(target_word, category_list_1, category_list_2, word_to_index, embeddings)
    
    similarities = []
    word_sweat_scores = []
    for word in top_similar_words:
        word_sweat = compute_sweat_score(word, category_list_1, category_list_2, word_to_index, embeddings)
        #warmth_sweat = compute_sweat_score(word, category_list_1, category_list_2, word_to_index, embeddings)
        
        if word_sweat is not None:
            sim = cosine_similarity(embeddings[word_to_index[word]].reshape(1, -1), 
                                    embeddings[word_to_index[target_word]].reshape(1, -1))[0][0]
            similarities.append(sim)  # 记录相似度
            if word_sweat is not None:
                word_sweat_scores.append(word_sweat)

    # 归一化权重
    similarities = np.array(similarities)
    if similarities.sum() != 0:
        weights = similarities / similarities.sum()  # 归一化
    else:
        weights = np.ones_like(similarities) / len(similarities)  # 避免除零错误
    
    return word_score, np.average(word_sweat_scores, weights=weights)

def get_list_sweatscore(target_word, embedding_type, category_list_1, category_list_2, year, k, given_list):
    
    vocab, embeddings, word_to_index = get_embedding(year, embedding_type)
    
    word_score = compute_sweat_score(target_word, category_list_1, category_list_2, word_to_index, embeddings)
    
    similarities = []
    word_sweat_scores = []
    for word in given_list:
        word_sweat = compute_sweat_score(word, category_list_1, category_list_2, word_to_index, embeddings)
        #warmth_sweat = compute_sweat_score(word, category_list_1, category_list_2, word_to_index, embeddings)
        
        if word_sweat is not None:
            sim = cosine_similarity(embeddings[word_to_index[word]].reshape(1, -1), 
                                    embeddings[word_to_index[target_word]].reshape(1, -1))[0][0]
            similarities.append(sim)  # 记录相似度
            if word_sweat is not None:
                word_sweat_scores.append(word_sweat)

    # 归一化权重
    similarities = np.array(similarities)
    if similarities.sum() != 0:
        weights = similarities / similarities.sum()  # 归一化
    else:
        weights = np.ones_like(similarities) / len(similarities)  # 避免除零错误
    
    return word_score, np.average(word_sweat_scores, weights=weights)

K_values = [10,20,50,100,200,500,1000]
embedding_type = "coha"
EMBEDDINGS = ["coha","google"]

if __name__ == "__main__":
    embedding_type = "google"
    for dimension_tuple in DIMENSION_TUPLE_LIST:
        for k in K_values:
            years = list(range(1800, 1991, 10))  # 从1800到1990，每10年一个
            yearly_dict = {}
            for year in years:
                yearly_dict[year] = get_yearly_sweatscore("chinese", embedding_type, dimension_tuple[0], dimension_tuple[1], year, k)

            chinese_scores = [yearly_dict[year][0] for year in years]  # Chinese 词的 S-WEAT 分数
            top_k_avg_scores = [yearly_dict[year][1] for year in years]  # Top-k 相似词的平均 S-WEAT 分数
    
            df = pd.DataFrame({
                "Chinese_score": chinese_scores,
                "top_k_avg_scores": top_k_avg_scores,
                "year": years,
                "Type": [dimension_tuple[2]] * len(years)  # Type 列全填 dimension_tuple[2]
            })
    
            csv_filename = f"Outputs/{embedding_type}/{dimension_tuple[2]}_{embedding_type}_{k}.csv"
            df.to_csv(csv_filename, index=False, encoding="utf-8")
            plt.figure(figsize=(10, 6))
            plt.plot(years, chinese_scores, marker='s', linestyle='-', label=f"Chinese {dimension_tuple[2]} Score - top {k}", color='red')
            plt.plot(years, top_k_avg_scores, marker='^', linestyle='--', label=f"Top Words {dimension_tuple[2]} S-WEAT Average - top {k}", color='coral')
            plt.title(f"Trend of {dimension_tuple[2]} Scores Over Time - top {k}")
            plt.xlabel("Year")
            plt.ylabel("S-WEAT Normalized Score")
            plt.legend()
            plt.grid(True)
            plt.savefig(f'Figures/Dimension_Trend/{embedding_type}/{dimension_tuple[2]}_{embedding_type}_{k}.jpg', format='jpg', dpi=300)
            plt.close()



