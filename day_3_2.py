from collections import defaultdict
from itertools import islice

houses = defaultdict(lambda: 0)
x = 0
y = 0

with open('day_3_1.txt') as fh:
	text = fh.read()
	houses[(x,y)] += 1
	for s in [islice(text, 0, None, 2), islice(text, 1, None, 2)]:
		x = 0
		y = 0
		for ch in s:
			print(ch)
			if ch == '>':
				x += 1
			elif ch == '<':
				x -= 1

			elif ch == '^':
				y -= 1

			elif ch == 'v':
				y += 1

			houses[(x,y)] += 1

	# for ch in :
	# 	print(ch)

	# for ch in :
	# 	print(ch)



	# 
	# for ch in text:
	# 	print(ch)
	# 	


print(len(houses.values()))