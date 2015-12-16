

with open('day_2_1.txt') as fh:
	sq_feet_total = 0
	lines = fh.readlines()
	for line in lines:
		l, w, h = map(int, line.strip().split('x'))
		# print(l, w, h)
		sides = [l*w, w*h, h*l]
		additional = min(sides)
		total = sum(map(lambda x: x*2, sides)) + additional
		# print(total)
		sq_feet_total += total

	print(sq_feet_total)
