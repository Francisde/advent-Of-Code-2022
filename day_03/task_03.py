file1 = open('input.txt', 'r')
Lines = file1.readlines()

count = 0
points = 0
total_points = 0
batch_points = 0
group = []

# Strips the newline character
for line in Lines:
	count += 1
	group.append(line)
	length = len(line.strip())
	border = int((length)/2)
	part1 = line[0:border]
	part2 = line.strip()[border:]
	same_character = ''
	for character in part1:
		if character in part2:
			print(character)
			if character.islower():
				print(ord(character)-96)
				total_points += (ord(character)-96)
			else:
				print(ord(character)-38)
				total_points += (ord(character)-38)
			break
	print("Line{}: {}, len: {}, part1: {}, part2: {}".format(count, line.strip(),length, part1, part2))
	if len(group) == 3:
		for character in group[0]:
			if character in group[1] and character in group[2]:
				if character.islower():
					print(ord(character)-96)
					batch_points += (ord(character)-96)
				else:
					print(ord(character)-38)
					batch_points += (ord(character)-38)
				group = []
				break

print("total_points: {}".format(total_points))
print("batch_points: {}".format(batch_points))
