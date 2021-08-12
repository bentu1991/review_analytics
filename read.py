import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		bar.update(count)
print("finish reading, there're", len(data), 'data')	
		
#print(data[0])
start_time = time.time()
wc = {} #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #add new key into dictionary

for word in wc:
	if wc[word] > 100000:
		print(word, wc[word])
end_time = time.time()
print('used', end_time - start_time, 'seconds')

print(len(wc))



new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('theres total of', len(new), 'reviews under 100 letters')
print(new[0])
print(new[1])


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('there are total of', len(good), 'good reviews')	

bad = [d for d in data if 'bad' in d]
print('there are total of', len(bad), 'bad reviews')


while True: #count word
	word = input('what word you wanted to search? ')
	if word == 'q':
		print('see ya')
		break
	elif word in wc:
		print(word, 'appeared for ', wc[word], 'times')
	else:
		print("there's no such word like that")


