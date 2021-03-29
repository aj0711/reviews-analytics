data = [] #第三步 建立空清單
count = 0
with open('reviews.txt', 'r') as f: #第一步 讀取檔案 並當作f
	for line in f: #第二步 每次從f讀取line(可隨意取名)
		data.append(line.strip()) #第四步 line加入空清單中
		count += 1
		if count % 10000 == 0:
			print(len(data))
print(len(data)) #看清單長度

print(data[0]) #列印第一筆
print('---------------------')
print(data[1])