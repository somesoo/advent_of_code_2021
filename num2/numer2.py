with open("input.txt") as numbers:
	data = numbers.read().splitlines()



for i in range(len(data)):
	data[i] = data[i].split(" ")

vertical = 0
horizontal = 0
for i in data:
    if i[0] == "forward":
        horizontal += int(i[1])
    elif i[0] == "down":
        vertical += int(i[1])
    elif i[0] == "up":
        vertical -= int(i[1])

print(horizontal * vertical)

vertical = 0
horizontal = 0
aim = 0
for i in data:
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

print(horizontal * vertical)
