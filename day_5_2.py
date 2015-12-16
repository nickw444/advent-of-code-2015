from collections import defaultdict

def pairs(s):
	for i, ch in enumerate(s):
		if i + 1 < len(s):
			yield(ch, s[i + 1])


def rule_1(s):
	for c1, c2 in pairs(s):
		print(c1, c2)
		_s = s.split('{}{}'.format(c1, c2))
		if len(_s) > 2:
			return True

	return False


def rule_2(s):
	for i, ch in enumerate(s):
		if i + 2 < len(s) and ch == s[i + 2]:
			return True

	return False

# def rule_3(s):
# 	for c in ['ab', 'cd', 'pq', 'xy']:
# 		if c in s:
# 			return False
# 	return True

def is_nice(s):
	return rule_1(s) and rule_2(s)



with open('day_5_1.txt') as fh:
	nice_num = 0 
	for line in fh.readlines():
		if is_nice(line):
			nice_num += 1
	
	print(nice_num)



# print(is_nice('ieodomkazucvgmuy'))