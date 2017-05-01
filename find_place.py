#!/usr/bin/python
#-*-coding: utf-8 -*-
f = open('korea.txt','r').read().splitlines()
word='ไปเที่ยวSights in South Koreaแล้วไปChangdeokgungแล้วไปDeoksugungแล้วไปGyeongbokgungJogye-saนากาน่าKorean Folk Villageอยากจะไปไหนก็ได้ไปเช่นไปวัดวัดพุลกุกซาหรือจะไปอุทยานพูกันซานคุณอยากจะไปไหนก็ไปได้ถ้ามีเงินหาดแฮอึนแด'

word=word.replace(" ","")

def find_place(word,dict_place):
    sign=[]
    for i in dict_place:
        sample = i.replace(" ","")
        if word.find(sample)!=-1:
            sign.append(i)
    return sign
result=find_place(word,f)
print(result)
