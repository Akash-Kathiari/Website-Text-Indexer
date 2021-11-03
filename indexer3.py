#Akash Kathiari
#Developing an Indexer
#IS 392

#import packages in Python as we did in HW2
from bs4 import BeautifulSoup
from urllib.request import urlopen
import nltk
import re
import ssl
import os
import sys
import json

inLst = {}
dcNum = 0
'''           
with open('Akira Toriyama  Wikipedia.html', encoding ='utf-8', errors = 'ignore') as f:
            soup = BeautifulSoup(f, 'html.parser')
'''
directory ='./pages/'
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        fname = os.path.join(directory,filename)
        with open(fname, encoding ='utf-8', errors = 'ignore') as f:
            soup = BeautifulSoup(f.read(),'html.parser')
            
            #The soup.get_text() function retrieves all the text from the HTML document
            text = soup.get_text()
            #import nltk to tokenize the text basically split()
            tokens = nltk.word_tokenize(text)    
            #set everything lowercase
            text = text.lower()
            #remove all text looking like \[.*\]
            text = re.sub("\[.*\]", " ", text)
            #remove all punctuation
            text = re.sub("[!#$&'()*+\,-._/:;<\=>?@[\]^`{|}~""''...']", " ", text)
            text = text.replace("\\"," ")
            #print to compare again
            tokens = nltk.word_tokenize(text)
            
            C ={}
            dcNum+=1
            for t in tokens:
                if t not in C:
                    C[t]=[1]
                else:
                    C[t][0]+=1
            for key, value in C.items():
                if key not in inLst:
                    inLst[key]=[]
                inLst[key].append(dcNum)
                inLst[key].append(value)


with open('index.txt', 'w') as file:
     file.write(json.dumps(inLst))
'''
with open('unique-terms.txt', 'w') as file:
     file.write(json.dumps(inLst))
'''
