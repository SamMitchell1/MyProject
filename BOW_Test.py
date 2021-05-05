
#following tutorial from https://stackabuse.com/python-for-nlp-creating-bag-of-words-model-from-scratch/
#import packages

import nltk
import numpy as np
import random
import string

import bs4 as bs
import urllib.request
import re

#insert and scrape data from corpus
raw_html= urllib.request.urlopen('https://en.wikipedia.org/wiki/Paris_Commune')
raw_html= raw_html.read()

article_html = bs.BeautifulSoup(raw_html, 'lxml')
#filter the text through paras
article_paragraphs = article_html.find_all('p')

article_text= ''

#concatenate paras
for para in article_paragraphs:
	article_text += para.text


#split corpus into individual sentences
corpus= nltk.sent_tokenize(article_text)

#remove uppercase letters, punc marks, empty spaces
for i in range(len(corpus )):
	corpus[i] = corpus [i].lower()
	corpus[i] = re.sub (r'\W',' ',corpus[i])
	corpus[i] = re.sub (r'\s+',' ',corpus[i])

print(len(corpus))

print(corpus[25])

#WORKING UP TO HERE
#creating a dict called 'wordfreq'

wordfreq= {}
for sentence in corpus:
	tokens= nltk.word_tokenize(sentence)
	for token in tokens:
		if token not in wordfreq.keys():
			wordfreq[token] = 1
		else:
			wordfreq[token] += 1

#select most frequent words

import heapq
most_freq = heapq.nlargest(200, wordfreq, key=wordfreq.get)

#convert sentences into a vector representation (why???)

sentence_vectors =[]
for sentence in corpus: 
	sentence_tokens = nltk.word_tokenize(sentence)
	sent_vec=[]
	for token in most_freq: 
		if token in sentence_tokens: 
			sent_vec.append(1)
		else: 
			sent_vec.append(0)
	sentence_vectors.append(sent_vec)

#convert BOW model from list of lists to matrix

sentence_vectors = np.asarray(sentence_vectors)

#So now I believe I have a BOW from the wikipedia page on the Paris Commune. 

print(sentence_vectors)