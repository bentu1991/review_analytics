
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		count += 1
		data.append(line)
		if count % 1000 == 0:
			print(count)
print('finish loading, there are', len(data), ' reviews')

sum_len = 0
for d in data:
	sum_len += len(d)
	

print('avg review length are', sum_len/ len(data))

	
