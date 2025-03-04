import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import KeyedVectors
from tabulate import tabulate

# Get the trained embedding for a given year
def get_embedding(year):
    v_filepath = "../../coha-sgns/{}-vocab.pkl".format(year)
    e_filepath = "../../coha-sgns/{}-w.npy".format(year)

    with open(v_filepath, 'rb') as f:
        vocab = pickle.load(f)
    embeddings = np.load(e_filepath)

    word_to_index = {}
    for idx, word in enumerate(vocab):
        word_to_index[word] = idx
    return vocab, embeddings, word_to_index



def find_top_k_similar_words(ethic_word, year, k=10):
    """
    Find the top k words most similar to 'ethic_word' in the word embedding of the given year.
    
    Parameters:
    - ethic_word: The target word (e.g., "chinese").
    - year: The year to load the word embedding model for.
    - k: The number of top similar words to return.
    
    Returns:
    - A list of tuples containing the top k words and their cosine similarities.
    """
    # Load vocab and embeddings for the given year
    vocab, embeddings, word_to_index = get_embedding(year)
    
    if ethic_word not in word_to_index:
        print(f"'{ethic_word}' not found in the vocabulary for year {year}.")
        return []
    
    # Get the vector for the target word
    target_index = word_to_index[ethic_word]
    target_vector = embeddings[target_index].reshape(1, -1)
    
    # Compute cosine similarities between target word and all other words
    similarities = cosine_similarity(target_vector, embeddings).flatten()
    
    # Create a list of (word, similarity) for all words
    similar_words = [(vocab[i], similarities[i]) for i in range(len(vocab))]
    
    # Sort by similarity in descending order and get the top k results
    similar_words_sorted = sorted(similar_words, key=lambda x: x[1], reverse=True)[:k]
    
    return similar_words_sorted