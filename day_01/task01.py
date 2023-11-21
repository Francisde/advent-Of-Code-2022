

file1 = open('data.txt', 'r')
Lines = file1.readlines()
 
count = 0
calories_count = 0
max_calories = 0
calories_set = []
# Strips the newline character
for line in Lines:
	count += 1
	print("Line{}: {}, number:{}".format(count, line.strip(), line.strip().isnumeric()))
	if line.strip().isnumeric():
		calories_count = calories_count + int(line.strip())
		print("total: {}".format(calories_count))
	else:
		if max_calories < calories_count:
			max_calories = calories_count
		calories_set.append(calories_count)
		calories_count = 0

print(calories_set)
calories_set.sort(reverse=True)
print(calories_set)

max_three_cal = calories_set[0] + calories_set[1] + calories_set[2]		
print("max calories:{}, max_three: {}".format(max_calories, max_three_cal))
		
