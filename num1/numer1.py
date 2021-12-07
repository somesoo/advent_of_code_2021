with open("input.txt") as numbers:
	data = numbers.read().splitlines()

for i in range(len(data)):
	data[i] = int(data[i])

counter = 0
for i in range(len(data)-1):
	i += 1
	if data[i] > data[i-1]:
		counter += 1

print("Wiekszych\t\t\t\t", counter)

# zadanie 2
data2 = data.copy()
for j in range(len(data)-2):
	data2[j] = (data[j] + data[j + 1] + data[j + 2])

counter2 = 0
for i in range(len(data2)-3):
	i += 1
	if data2[i] > data2[i-1]:
		counter2 += 1

print("wiekszych trójek\t\t", counter2)