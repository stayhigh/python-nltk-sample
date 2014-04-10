from nltk.book import *
import nltk

fdist1 = nltk.FreqDist(text1)
vocabulary1 = fdist1.keys()
print vocabulary1[:50]
print fdist1['whale']


#print out a list of hapaxes, the words that occur once only
#print fdist1.hapaxes()
