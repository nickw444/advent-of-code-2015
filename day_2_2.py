

with open('day_2_1.txt') as fh:
	sq_feet_total = 0
	lines = fh.readlines()
	for line in lines:
		l, w, h = map(int, line.strip().split('x'))
		volume = l * w * h
		sides = sorted([l, w, h])
		total = sides[0] * 2 + sides[1] * 2 + volume
		sq_feet_total += total

	print(sq_feet_total)
