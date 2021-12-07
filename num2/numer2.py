with open("input.txt") as numbers:
	data = numbers.read().splitlines()

data2 = []

for i in range(len(data)):
	data2.append(data[i].split(" "))

vertical = 0
horizontal = 0
aim = 0

for i in data2:
	if i[0] == "forward":
		if aim == 0:
			horizontal += int(i[1])
		else:
			horizontal += int(i[1])
			vertical += (aim * int(i[1]))
	elif i[0] == "down":
		aim += int(i[1])
	else:
		aim -= int(i[1])


print(horizontal, vertical)
print(horizontal * vertical)
