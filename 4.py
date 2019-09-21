def drawLine(nama):
	for ind,i in enumerate(range(len(nama))):
		if ind == 0:
			print(''*(i),nama[i])
		else:
			print(' '*(i),nama[i])

drawLine('DumbWays')