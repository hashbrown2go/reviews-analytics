data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('檔案讀取完了, 總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
print('留言的平均長度為', sum_len/len(data))

new = [] 
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		food.append(d)
print('一共有', len(good), '筆留言提到good')

words = []
wc = {}
for d in data:
	words = d.split(' ')
	for word in words:
		if word not in wc:
			wc[word] = 1
		else:
			wc[word] += 1

for word in wc:
	if wc[word] > 100:
		print(word, wc[word])
print(len(wc))

while True:
	word = input('你想查詢什麼呢?: ')
	if word == 'q':
		print('感謝使用!')
		break
	print('您所蒐尋的', word, '一共出現了', wc[word], '次')
