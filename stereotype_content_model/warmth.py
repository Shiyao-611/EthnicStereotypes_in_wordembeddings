import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt




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
years = list(range(1800, 1991, 10))  # 从1800到1990，每10年一个

warmth = [
    "sociability", "sociable", "friendliness", "friendly", "warm", "warmth",
    "likable", "pleasant", "liked", "outgoing", "sensitive", "affectionate",
    "unreserved", "open", "caring", "sympathetic", "sympathy", "helpful",
    "understanding", "supportive", "polite", "civil", "social", "humorous",
    "funny", "popular", "nice", "sentimental", "forthcoming", "tender",
    "agreeable", "welcoming", "hospitable", "thoughtful"
]

cold = [
    "unsociability", "unsociable", "unfriendliness", "unfriendly", "cold",
    "coldness", "repellent", "unpleasant", "unlikable", "disliked", "shy",
    "insensitive", "unaffectionate", "distant", "uncaring", "unsympathetic",
    "unhelpful", "unsupportive", "impolite", "aloof", "rude", "antisocial",
    "unsocial", "asocial", "boring", "unpopular", "nasty", "disagreeable",
    "rough", "inhospitable", "inconsiderate", "timid"
]

incompetence = [
    "incompetent", "uncompetitive", "unintelligent", "stupid", "stupidity",
    "ignorant", "ignorance", "dumb", "dumbness", "unable", "uneducated",
    "irrational", "uncreative", "incapable", "impractical", "clumsy",
    "unimaginative", "foolish", "naive", "undiscriminating", "maladroit",
    "folly", "unwise", "inefficient", "ineffective", "illogical",
    "unperceptive", "inept", "inability"
]

competence = [
    "competence", "competent", "competitive", "smart", "bright",
    "intelligent", "intelligence", "able", "skillful", "skill", "skilled",
    "educated", "education", "rational", "creative", "capable",
    "practical", "graceful", "felicitous", "imaginative", "shrewd",
    "critical", "discriminating", "inventive", "clever", "wise",
    "wisdom", "efficient", "effective", "logical", "brilliant",
    "insightful", "ability"
]

competence_scores = {}
warmth_scores = {}
top_words_competence_avg = {}
top_words_warmth_avg = {}
for year in years:
    vocab, embeddings, word_to_index = get_embedding(year)
    
    # 找出与 "chinese" 余弦相似度最高的 1000 个词
    top_similar_words = find_top_similar_words("chinese", vocab, embeddings, word_to_index)
    
    # 计算 "chinese" 本身的 S-WEAT 分数
    chinese_competence = compute_sweat_score("chinese", competence, incompetence, word_to_index, embeddings)
    chinese_warmth = compute_sweat_score("chinese", warmth, cold, word_to_index, embeddings)
    competence_scores[year] = chinese_competence
    warmth_scores[year] = chinese_warmth

    # 计算各词的 S-WEAT 分数
    competence_sweat_scores = []
    warmth_sweat_scores = []
    similarities = []
    
    for word in top_similar_words:
        comp_sweat = compute_sweat_score(word, competence, incompetence, word_to_index, embeddings)
        warmth_sweat = compute_sweat_score(word, warmth, cold, word_to_index, embeddings)

        if comp_sweat is not None or warmth_sweat is not None:
            sim = cosine_similarity(embeddings[word_to_index[word]].reshape(1, -1), 
                                    embeddings[word_to_index["chinese"]].reshape(1, -1))[0][0]
            similarities.append(sim)  # 记录相似度
            if comp_sweat is not None:
                competence_sweat_scores.append(comp_sweat)
            if warmth_sweat is not None:
                warmth_sweat_scores.append(warmth_sweat)

    # 归一化权重
    similarities = np.array(similarities)
    if similarities.sum() != 0:
        weights = similarities / similarities.sum()  # 归一化
    else:
        weights = np.ones_like(similarities) / len(similarities)  # 避免除零错误

    # 计算加权平均 S-WEAT 分数
    if competence_sweat_scores:
        top_words_competence_avg[year] = np.average(competence_sweat_scores, weights=weights)
    else:
        top_words_competence_avg[year] = None

    if warmth_sweat_scores:
        top_words_warmth_avg[year] = np.average(warmth_sweat_scores, weights=weights)
    else:
        top_words_warmth_avg[year] = None
