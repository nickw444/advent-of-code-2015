from hashlib import md5

key = 'yzbqklnj'

for i in xrange(1, 9999999):
	val = '{}{}'.format(key, i)
	h = md5(val).hexdigest()
	if h.startswith('00000'):
		print(i)
		break
	# print(i)

