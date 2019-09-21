from functools import reduce
OPERATION_DICT = {
	'SUM': lambda digits, digitarray: reduce(lambda x, y:x+y,[int(digits[i]) for i in digitarray]),
	'MUL': lambda digits, digitarray: reduce(lambda x, y:x*y,[int(digits[i]) for i in digitarray]),
	'SUB': lambda digits, digitarray: reduce(lambda x, y:x-y,[int(digits[i]) for i in digitarray]),
	'DIV': lambda digits, digitarray: reduce(lambda x, y:x/y,[int(digits[i]) for i in digitarray])
}

def mrClints(operation, N, digitarray):
	global OPERATION_DICT
	digits = []
	for x in range(N+1):
		digits.append(str(x))
	digits = ''.join(digits)
	return OPERATION_DICT[operation](digits,digitarray)

print(mrClints('SUM',20,[11,13,15]))