def buyEgg(tanggal, uang):
	telur = 2500
	perlusin = 2
	genap = 5
	ganjil = 10

	totalTelurDibeli = uang//telur
	if tanggal in [9,15,21,25,27]:
		perlusin = 3
	lusin = totalTelurDibeli//12
	totalTelurDibeli += lusin*perlusin

	if tanggal % 5 == 0:
		if tanggal % 2:
			totalTelurDibeli += ganjil
		else:
			totalTelurDibeli += genap
	return totalTelurDibeli

print(buyEgg(10,60000))