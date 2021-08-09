
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		count += 1
		data.append(line)
		if count % 1000 == 0:
			print(count)
print('finish loading, there are', len(data), ' reviews')


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('theres total of', len(new), 'reviews under 100 letters')
	

	


	
