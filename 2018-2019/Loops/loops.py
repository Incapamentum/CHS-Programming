# Created by Gustavo A. Diaz Galeas
#
# A programming assignment for the students enrolled in the AP CSP course
# at Colonial High School in Orlando, Florida.
#
# Purpose: To test the knowledge of students in the usage of for and while
# loops. Firstly, an infinite loop condition must be implemented using a while
# loop. Secondly, students are required to implement an iterative approach
# in finding the first 5 powers (i.e. first, second, third, etc) of a user
# inputted number. Thirdly, the program MUST keep a running count of the number
# of times a user inputs a number, exiting upon a certain condition.
#

# Initialization of counter that keeps track of number of times a user has
# entered something, not counting the exit condition
counter = 0

# Infinite loop condition
while 1:
	n = input('Please enter a positive, non-zero number (enter -1 to exit): ')

	# Condition to break out of the program
	if n == -1:
		print "The user has entered " + str(counter) + " numbers!"
		print ""
		dummy_input = raw_input('Press enter to end the program.')
		break

	# Increment counter to keep track of number of times the user has entered
	# something
	counter = counter + 1

	# Condition to check for invalid inputs
	if n <= 1:
		print "Invalid input!"
		print ""
		continue

	# Range -> 1, 2, 3, 4, 5
	for x in range(1, 6):
		power = n**x
		print power

	# Printing a newline.
	print ""
