
data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		count += 1
		data.append(line)
print('finish loading, there are', len(data), ' reviews')


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('theres total of', len(new), 'reviews under 100 letters')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('there are total of', len(good), 'good reviews')	

bad = [d for d in data if 'bad' in d]
print('there are total of', len(bad), 'bad reviews')
