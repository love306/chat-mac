lines = []

with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip().split(' '))
		#print()
for line in lines:
	time = []
	name = []
	time.append(line[0][:5])
	name.append(line[0][5:])
	print(time)
	print(name)