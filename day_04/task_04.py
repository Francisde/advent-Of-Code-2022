file1 = open('input.txt', 'r')
Lines = file1.readlines()

count = 0
fully_contained_pair = 0
overlap_pairs = 0


# Strips the newline character
for line in Lines:
	count += 1
	print("Line{}: {}".format(count, line.strip()))
	elves = line.strip().split(",")
	start1 = int(elves[0].split("-")[0])
	end1 = int(elves[0].split("-")[1])
	start2 = int(elves[1].split("-")[0])
	end2 = int(elves[1].split("-")[1])
	# elf 2 complete in 1?
	if start2 >= start1 and end2 <= end1:
		fully_contained_pair +=1
	# elf 1 complete in 2?
	elif start1 >= start2 and end1 <= end2:
		fully_contained_pair +=1
	# elf 2 partly in 1?
	if start2 >= start1 and start2 <= end1:
		overlap_pairs +=1
	# elf 1 complete in 2?
	elif start1 >= start2 and start1 <= end2:
		overlap_pairs +=1
		
print("pairs does one range fully contain the other: {}".format(fully_contained_pair))
print("pairs does one range partly contain the other: {}".format(overlap_pairs))
	
