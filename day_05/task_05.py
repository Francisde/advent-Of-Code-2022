file1 = open('input.txt', 'r')
Lines = file1.readlines()

configuration = [
[],
['P', 'F', 'M', 'Q', 'W', 'G', 'R', 'T'],
['H', 'F', 'R'],
['P', 'Z', 'R', 'V', 'G', 'H', 'S', 'D'],
['Q', 'H', 'P', 'B', 'F', 'W', 'G'],
['P', 'S', 'M', 'J', 'H'],
['M', 'Z', 'T', 'H', 'S', 'R', 'P', 'L'],
['P', 'T', 'H', 'N', 'M', 'L'],
['F', 'D', 'Q', 'R'],
['D', 'S', 'C', 'N', 'L', 'P', 'H']
]

count = 0
fully_contained_pair = 0
overlap_pairs = 0

# solution part 1
#for line in Lines:
#	count += 1
#	parsed_line = line.strip().split(' ')
#	moves = int(parsed_line[1])
#	from_stack = int(parsed_line[3])
#	to_stack = int(parsed_line[5])
#	print("Line{}: {}".format(count, parsed_line))
#	# perform moves
#	for i in range(moves):
#		move_object = configuration[from_stack].pop()
#		print(move_object)
#		configuration[to_stack].append(move_object)


# solution part 2		
for line in Lines:
	count += 1
	parsed_line = line.strip().split(' ')
	moves = int(parsed_line[1])
	from_stack = int(parsed_line[3])
	to_stack = int(parsed_line[5])
	print("Line{}: {}".format(count, parsed_line))
	# perform moves
	cache = []
	for i in range(moves):
		cache.append(configuration[from_stack].pop())
	for i in range(moves):	
		configuration[to_stack].append(cache.pop())


print(configuration)
result = []
result_string = ""
for i in range(len(configuration)-1):
	#result.append(configuration[i+1].pop())
	result_string += configuration[i+1].pop()
print("result:{}".format(result_string))
