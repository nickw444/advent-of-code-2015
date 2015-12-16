"""
(0,0)		... 		(999,0)
			...
			...
(0,999)					(999,999)

"""

from collections import defaultdict
import re

lights = defaultdict(lambda: 0)
m = re.compile(r'^(toggle|turn off|turn on) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)$')

with open('day_6_1.txt') as fh:
	for i, line in enumerate(fh.readlines()):
		r = m.search(line)
		mode = r.group(1)
		start = map(int, (r.group(2), r.group(3)))
		end = map(int, (r.group(4), r.group(5)))
		print(mode, start, end)

		for y in range(start[1], end[1] + 1):
			for x in range(start[0], end[0]+1):
				# if i == 1:
				# 	print(x,y)

				if mode == 'toggle':
					lights[(x,y)] += 2
				elif mode == 'turn off':
					lights[(x,y)] -= 1
					if lights[(x,y)] < 0:
						lights[(x,y)] = 0

				elif mode == 'turn on':
					lights[(x,y)] += 1

		# for y in range(start[1], end[1]+1):


		# 	for x in range(0, 1000):
		# 		if y == start[1] and x < start[0]:
		# 			continue

		# 		if y == end[1] and x > end[0]:
		# 			break
				
		# 		


		# 		# break
		# 		# print(row_start, row_end)
		# 		# print(y)
		# 	# for x in range(start[0]
		# if i == 1:
		# 	break

# print(lights)
brightness = 0
for key,value in lights.items():
	# print(key, value)
	if value:
		brightness += value

print("ON: {}".format(brightness))