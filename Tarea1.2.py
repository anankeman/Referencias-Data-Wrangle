# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 18:03:31 2016

@author: Pippo
"""

import timeit
start = timeit.default_timer()

import nltk
import os
import numpy
import codecs
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ruta = 'C:/Users/Pippo/Documents/TareaT/'   # Cambia la ruta de los documentos
vocab = {}
corpus = []
stop = nltk.corpus.stopwords.words('Spanish')
stop2 = ['.',',',':',';','!','¡','?','¿','#','&','%','(',')','/','-','$','\n']
for files in os.listdir(ruta):
    filename = codecs.open(ruta + files, 'r', 'utf-8')
    text = filename.read().lower().replace('-','').replace('*','').replace('"','').replace("'",'').replace(".",'')
    token = nltk.word_tokenize(text)
    token2 = [w for w in token if w not in (stop and stop2)]
    for tok in token2:
        if tok not in vocab:
            vocab[tok] = 1
        else:
            vocab[tok] += 1
    corpus.append(text)
# Calular vectores
tfidf = TfidfVectorizer(tokenizer=nltk.word_tokenize)
tfs = tfidf.fit_transform(corpus)

# calcular similitud coseno

simil = {}
matrix = cosine_similarity(tfs, tfs)

for i in range(0, len(matrix)):
    t= matrix[i]
    t2 = numpy.argpartition(t, -2)[-2]
    simil['file' + str(i)] = {'file' + str(t2):{t[t2]}}

f = open ('similitud.txt', 'w')
for wrd in simil:
    f.write(str(wrd)+ ' ' + str(simil[wrd])+ '\n')
f.close()

f = open('vocabulario.txt','w')
for wrd in vocab:
    f.write(str(wrd) + ' ' + str(vocab[wrd]) + '\n')
f.close()

stoprrr = timeit.default_timer()

print stoprrr - start 