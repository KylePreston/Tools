# Simple program that returns a list of the 10 most common words in Shakespeare's Romeo and Juliet.

import string
shakes = open('romeo.txt')
counts = {}

for line in shakes:
	line = line.translate(None, string.punctuation)
	line = line.lower()
	words = line.split()
	for word in words:
		if word not in counts:
			counts[word] = 1
		else:
			counts[word] += 1

# Sorting the dictionary by value
lst = list()
for key, val in counts.items():
	lst.append( (val, key) )

lst.sort(reverse = True)

for key, val in lst[:10]:
	print key, val

shakes.close()
