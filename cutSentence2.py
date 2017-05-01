#!/usr/bin/python
# -*- coding: utf-8 --

word = open('sample_word.txt','r').read().replace(" ","").replace("\n","").replace("\t","") #ตัดช่องว่าง ตัดเว้นบรรทัด ตัดแท๊บ
#print(word)

#--------------------------variable------------------------
check_day =['วันแรก','วันที่สอง','วันที่สาม','วันที่สี่','วันที่1','วันที่2','วันที่3','วันที่4',
			'วันที่5','วันที่6','วันที่7','วันที่8']
cut_sentence=[] 
position_check=[]
index=0
#--------------------------function----------------------
def find_index(word,index_now):
	#output -> [0, 22, 53, 81]
	#want to get positions of keyword
	temp_position=[]
	for i in check_day:
		if word.find(i) != -1: #is found
			get_index=word.find(i)
			temp_position.append(get_index)
			#print(temp_position) 
	return temp_position
def cut_sentence(position_check,word):
	#position_check->[7782, 7877, 1, 1490, 3316, 5334, 6959, 11478, 13879, 16178] 
	#.................^temp...^start
	sentence=[]
	temp=0
	for i in range(1,len(position_check)): #1,2,3,4...last
		if position_check[i-1]>position_check[i]: #ถ้าเจอตำแหน่งก่อนหน้ามากกว่าให้ข้ามไปทำลูปต่อไป 7877:1 มันจะ return none
			temp=position_check[i]
			continue
		#------------------------core----------------
		sentence.append(word[temp:position_check[i]])
		temp=position_check[i]
		#-------------------------------------------
		if i == len(position_check)-1:#ปรินท์ตำแหน่งสุดท้ายใน list จนจบข้อความ
			sentence.append(word[position_check[i]::])
	return sentence

#------------------------execute--------------------
position_check=find_index(word,index)
# word.close
print(position_check) #[7782, 7877, 1, 1490, 3316, 5334, 6959, 11478, 13879, 16178]
result=cut_sentence(position_check,word)
#-----------------------print senence -> result[0],result[1]
for i in result: 
	print(i,end='\n\n')
