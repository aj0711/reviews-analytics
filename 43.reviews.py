data = [] #第三步 建立空清單
count = 0
with open('reviews.txt', 'r') as f: #第一步 讀取檔案 並當作f
	for line in f: #第二步 每次從f讀取line(可隨意取名)
		data.append(line.strip()) #第四步 line加入空清單中
		count += 1
		if count % 10000 == 0: #記數滿10000次後
			print(len(data)) #列印出來
print('Total', len(data), '筆data') #看清單長度

print(data[0]) #列印第一筆
print('---------------------')
print(data[1])
#進階
sum_len = 0 #2.加總
for d in data: #1.data中所有留言命名為d
	sum_len += len(d) # sum_len = sum_len + len(d)  新目前總數=留言數+舊目前的總數 

print('平均是', sum_len/len(data)) #每筆留言平均長度