import nltk
import re
import time
import urllib

exampleContent ="""
CNN) -- Riot police evicted scores of protesters from Taiwan's executive building early Monday morning as rallies over a controversial trade deal between Taiwan and mainland China entered their seventh day.
Hundreds of protesters stormed the Executive Yuan in Taipei on Sunday evening, shortly after Taiwan's president Ma Ying-jeou dismissed protesters' demands to scrap a service trade agreement with China. Opponents of the deal say it could harm Taiwan's economy, democratic system and national security.
Police used high-pressure water cannons to disperse the demonstrators, who were mostly university students.
"""

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = urllib.urlopen(url).read()
#print html[:60]

raw = nltk.clean_html(html)
#print raw
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)
text.concordance("gene")
#print tokens
