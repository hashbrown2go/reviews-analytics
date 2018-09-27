data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
i = 0
for words in line:
	nums = len(words)
	nums = int(nums)
	print(i)
	i += nums

print((i)/len(data))
