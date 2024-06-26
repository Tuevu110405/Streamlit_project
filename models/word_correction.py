def load_vocab(file_path):
    with open(file_path,'r') as f:
        lines = f.readlines()
    
    words = sorted(set([lines.strip(). lower() for _ in lines]))
    return words

vocabs = load_vocab ( file_path ="G:\AIO2024\Home_work\module 1\Project1\source\source\data\vocab.txt")

import numpy as np


def levenshtein_distance(str1, str2):
    # distance variable
    a = np.zeros((len(str1)+1, len(str2)+1))
    # create inserting row
    for i in range(1, len(str2)+1):
        a[0][i] = i

    # deleting column
    for j in range(1, len(str1)+1):
        a[j][0] = j

    # handeling remaining entry
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2)+1):
            insert = a[i-1][j] + 1
            delete = a[i][j-1] + 1
            if str1[i-1] == str2[j-1]:
                sub = a[i-1][j-1]
            else:
                sub = a[i-1][j-1] + 1
            a[i][j] = min(insert, delete, sub)

    return a[len(str1)][len(str2)]


import streamlit as st

def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words
vocabs = load_vocab(file_path='./vocab.txt')

def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input('Word:')

    if st.button("Compute"):

        # compute levenshtein distance
        leven_distances = dict()
        for vocab in vocabs:
            leven_distances[vocab] = levenshtein_distance(word, vocab)
        
        # sorted by distance
        sorted_distences = dict(sorted(leven_distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distences.keys())[0]
        st.write('Correct word: ', correct_word)

        col1, col2 = st.columns(2)
        col1.write('Vocabulary:')
        col1.write(vocabs)
        
        col2.write('Distances:')
        col2.write(sorted_distences)

if __name__ == "__main__":
    main()
