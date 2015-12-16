from collections import defaultdict


def rule_1(s):
	vowels = 0
	for ch in s:
		if ch in 'aeiou':
			vowels += 1

		if vowels >= 3:
			return True

	return False

def rule_2(s):
	for i, ch in enumerate(s):
		if i + 1 < len(s) and ch == s[i + 1]:
			return True

	return False

def rule_3(s):
	for c in ['ab', 'cd', 'pq', 'xy']:
		if c in s:
			return False
	return True

def is_nice(s):
	return rule_1(s) and rule_2(s) and rule_3(s)



with open('day_5_1.txt') as fh:
	nice_num = 0 
	for line in fh.readlines():
		if is_nice(line):
			nice_num += 1
	
	print(nice_num)



# print(is_nice('ugknbfddgicrmopn'))