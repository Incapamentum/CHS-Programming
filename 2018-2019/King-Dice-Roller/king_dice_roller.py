# Created by Gustavo A. Diaz Galeas
#
# A programming assignment for the students enrolled in the AP CSP course
# at Colonial High School in Orlando, Florida
#
# Purpose: To test the knowledge of students in the usage of a wide scope of
# programming topics that include, but are not limited to: loops, break and
# continue statements, assignment operators, logic operators, conditional
# statements, and the use of the import statement to import a module into
# their programs.
#

# Importing the random module
import random

# A welcome prompt for friendliness
print "Welcome to King Dice Roller!"
print "The rules of the game are simple! There are two, 6-sided dice!"
print "Both dice will be rolled, and you must guess their sum!"
print "Keep in mind, there are only three opportunities to guess!"
print ""

# Initialization of all variables ot be used
n = 0
dice_one = random.randint(1, 6)
dice_two = random.randint(1, 6)
dice_sum = dice_one + dice_two

# Will loop three times
while (n < 3):
	guess = input('Please enter a guess: ')

	if guess > 12 or guess < 2:
		print "Out of bounds! Please try again!"
		print "Attempts left: %d" % (3 - n)
		print ""
		continue

	# Condition if guess is less than dice_sum
	if guess < dice_sum:
		n += 1
		print "Too low! Try again!"
		print "Attempts left: %d" % (3 - n)
		print ""
		continue

	# Condition if guess is greater than dice_sum
	elif guess > dice_sum:
		n += 1
		print "Too high! Try again!"
		print "Attempts left: %d" % (3 - n)
		print ""
		continue

	# Condition if guess is the correct guess
	elif guess == dice_sum:
		print "Congratulations! You've guessed it correctly!"
		break

if n == 3:
	print "The sum was: %d" % (dice_sum)

print ""
print "Thanks for playing!"
print ""

dummy_input = raw_input('Press enter to exit the program.')
