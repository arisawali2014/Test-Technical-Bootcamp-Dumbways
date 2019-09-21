import random

def serialGen(count):
	seed = 'abcdefghijklmnopqrstuvwxyz1234567890'
	data = []
	for i in range(count):
		data.append('-'.join(''.join(random.choice(seed) for _ in range(4)) for _ in range(4)))
	return data

a = serialGen(500)
for i in a:
	print(i)
print('Success Generated', len(a),'serial.')