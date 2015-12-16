from hashlib import md5
from itertools import islice
import sys
key = 'yzbqklnj'

if len(sys.argv) < 3:
	print("Usage: {} <num workers> <worker num starting from 1>")
	exit(1)

workers = int(sys.argv[1])
worker = int(sys.argv[2])

print("Starting Worker {} of {}".format(worker, workers))

for i in xrange(worker, 99999999999, workers):
	val = '{}{}'.format(key, i)
	h = md5(val).hexdigest()
	if h.startswith('000000'):
		print(i)
		break
	# print(i)
