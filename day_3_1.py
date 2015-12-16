from collections import defaultdict

houses = defaultdict(lambda: 0)
x = 0
y = 0

with open('day_3_1.txt') as fh:
	text = fh.read()
	houses[(x,y)] += 1
	for ch in text:
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


print(len(houses.values()))