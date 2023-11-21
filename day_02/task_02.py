file1 = open('input.txt', 'r')
Lines = file1.readlines()

winning_points= {
"A X" : 3,
"A Y" : 6,
"A Z" : 0,
"B X" : 0,
"B Y" : 3,
"B Z" : 6,
"C X" : 6,
"C Y" : 0,
"C Z" : 3
}

winning_points_2= {
"A X" : 3,
"A Y" : 4,
"A Z" : 8,
"B X" : 1,
"B Y" : 5,
"B Z" : 9,
"C X" : 2,
"C Y" : 6,
"C Z" : 7
}

save_points = {
"X" : 1,
"Y" : 2,
"Z" : 3 
}

count = 0
points = 0
total_points = 0
total_points_2 = 0

# Strips the newline character
for line in Lines:
	count += 1
	points = save_points[line.strip()[2]] + winning_points[line.strip()]
	total_points += points
	total_points_2 += winning_points_2[line.strip()]
	print("Line{}: {}, roundpoints: {}, totalpoints: {}, totalpoints_2: {}".format(count, line.strip(), points, total_points, total_points_2))
	
	
