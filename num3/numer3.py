with open("input.txt") as numbers:
	data = numbers.readlines()


def first():
	odp = ""
	pdo = ""
	zero = 0
	one = 0
	for i in range(len(data[0])-1):
		for j in data:
			if j[i] == '0':
				zero += 1
			else:
				one += 1
		if zero > one:
			odp += '0'
			pdo += '1'
		else:
			odp += '1'
			pdo += '0'
		zero = 0
		one = 0
	print(pdo, odp)
	# first task
	print(int(odp, 2), '*', int(pdo, 2), '=', int(odp, 2) * int(pdo, 2))


def second():
	oxygen = data.copy()

	zeroo = 0
	onee = 0
	for a in range(8):
		for j in range(len(oxygen)):
			if oxygen[j][a] == '0':
				zeroo += 1
			else:
				onee += 1

		i = 0
		while i < len(oxygen):
			if zeroo > onee:
				if oxygen[i][a] == '1':
					del oxygen[i]
				else:
					i += 1
			elif onee > zeroo:
				if oxygen[i][a] == '0':
					del oxygen[i]
				else:
					i += 1
			elif onee == zeroo:
				if oxygen[i][a] == '0':
					del oxygen[i]
				else:
					i += 1
	print(oxygen)
	print(len(oxygen))


def co2():
	co2 = data.copy()
	ze = 0
	je = 0
	for f in range(12):
		for j in range(len(co2)):
			if co2[j][f] == '0':
				ze += 1
			else:
				je += 1
		i = 0
		while i < len(co2):
			if ze < je:
				if co2[i][f] == '1':
					del co2[i]
				else:
					i += 1
			elif je < ze:
				if co2[i][f] == '0':
					del co2[i]
				else:
					i += 1
			elif je == ze:
				if co2[i][f] == '1':
					del co2[i]
				else:
					i += 1
		print("zero", zeroo, "one", onee)
		ze = 0
		je = 0

		print(co2)
		print(len(co2))
print(int("011000111111", 2), " * ", int("101011000100", 2), " = ", int("011000111111", 2) * int("101011000100", 2))

