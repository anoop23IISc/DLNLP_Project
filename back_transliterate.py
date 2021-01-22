import os
import sys
import numpy as np
import requests
import pandas as pd

sentim=0
id_sent=0
word_list =[]
file1 = open("Hindi_test_unalbelled_conll.txt","r")
fi = open("Transliterated_Hindi_test.txt","a+")

line =file1.readline()

transTweetTokens=[]
trans_tweet = ""
hindi_list =[]

count = 0

while(line):
    if(line=="\n"):
        if(len(word_list)):
            count+=1
            transTweetTokens += [str(id_sent), "\t"] + word_list[:-1]
            transTweetTokens += ["\t", str(sentim), "\t", str(sentim), "\n" ]

            hindi_list = dummy_list
            hindi_sent = " ".join(hindi_list)
            URL = "https://www.google.com/inputtools/request?text="+str(hindi_sent)+"&ime=transliteration_en_hi&num=5&cp=0&cs=0&ie=utf-8&oe=utf-8&app=jsapi&uv"
            PARAMS = {} 
            r = requests.get(url = URL, params = PARAMS) 
            data = r.json()
    else:
        array = line.split("\t")
        if(array[0]=='meta'):
            id_sent = array[1]
            sentiment_label_map = {"negative":0, "positive":2, "neutral":1}
            sentim = sentiment_label_map[array[2][:-1]]
        else:
            if(array[1][:-1]=="Hin"):
                hindi_list.append(array[0])
                word_list += ["qwertyuiopasdfghjklzxcvbnm", " "]
            else:
                word_list += [array[0], " "]
    line = file1.readline()

fi.write(trans_tweet)