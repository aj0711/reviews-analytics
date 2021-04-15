data = [] #第三步 建立空清單
count = 0
with open('reviews.txt', 'r') as f: #第一步 讀取檔案 並當作f
	for line in f: #第二步 每次從f讀取line(可隨意取名),讀取後要放入空清單
		data.append(line.strip()) #第四步 line加入空清單中
		count += 1 # count = count + 1
		if count % 100000 == 0: #記數滿100000次後
			print(len(data)) #列印出來
print('Total', len(data), '筆data') #看清單長度

print(data[0])

wc = {} #word_wount, dict {key: value}
for d in data: #data是清單
	words = d.split() #d是每筆留言,遇到空白鍵(留空預設為空白鍵)就分割,放在words中 
	for word in words: #讀words清單中的每個字為word
		if word in wc: #如果word有出現在wc過
			wc[word] += 1 #去wc的字典中，查找word的字, 如果沒有的話, 就把次數+1
		else:
			wc[word] = 1 #去wc的字典中，查找word的字, 如果沒有的話, 就新增key到wc字典

for word in wc: #把wc中的每個key(word)叫出來
	if wc[word] > 100000: #超過100000次的才印出來
		print(word, wc[word]) #把key印出來, 把查找的次數印出來

print(len(wc))

print(wc['Allen']) #查詢Allen字串在wc中出現的次數

while True:
	word = input ('look for: ',  )
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過', wc[word], '次')
	else:
		print('No this word.')


print('謝謝使用')



























print(data[0]) #列印第一筆
print('---------------------')
print(data[1])
#進階
sum_len = 0 #2.加總
for d in data: #1.data中所有留言命名為d
	sum_len += len(d) # sum_len = sum_len + len(d)  新目前總數=留言數+舊目前的總數 

print('平均是', sum_len/len(data)) #每筆留言平均長度

#清單做篩選 (低於100的放在清單中)

new = []
for d in data: #把data清單中的資料一筆筆用d的名稱叫出來，d是每筆留言，data是全部清單
	if len(d) < 100:
		new.append(d)
print('Total 有', len(new), '筆留言長度小於100') #如果沒有退到最前面 就會一直印
print(new[0])
print(new[2])

#篩選Good出來

good = []
for d in data:
	if 'good' in d: #是否 good有在d裡面 
		good.append(d) #就把d放在good清單
print('Total 有', len(good), '筆留言有good')



