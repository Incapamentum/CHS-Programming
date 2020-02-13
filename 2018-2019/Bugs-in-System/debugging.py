# Created by Gustavo A. Diaz Galeas
#
# A programming assignment for the students enrolled in the AP CSP course at
# Colonial High School in Orlando, Florida
#
# Purpose: To aid the students in the development of debugging and critical
# thinking skills, aimed to cover recognizing programming errors that arise
# due to syntax errors and other unintended consequences.
#
# ===========
#    NOTES
# ===========
# Lines that have the following:
#			print ""
# are there to print out a newline. This is just to avoid having everything so
# cramped up and allows for readability for when the program is executed.
#
# The usage of the
#		\n
# command is interpreted by Python to be an instruction to include a newline
# at that particular position of the string.
#

# Introductory prompts
print "Welcome to th- "
print "Oh no! There appears to be a bug in the system!!"
print "Please help us out!"

print ""

# Line asking for the name of the user
user_input = input('Please enter your name: ')

print ""

# This for loop will print out 5 random numbers between 1 and 20
for x in range(0,5):
if (x != 5):
print "The random number is: " str(random.randint(1, 20))
else:
print "The random number is: " + random.randint(1, 20)

print ""

# Given a user input, will go through some math operators
num = input('Please enter an integer: ')
num_add = num + 1
num_sub = num - 1
num_mult = 2 * num
num_div = num / 5
print "num_add: %d\nnum_sub: %d\nnum_mult: $d\nnum_div: %d" % (num_add, num_sub, num_mult, num_div)

print ""

num1 = 1
num2 = 2
num3 = 3
print "num1: %d\nnum2: %d\nnum3: %d" % (num1, num2, num3, num4)

print ""

# While loop that should loop only ONCE.
while i == 0:
	print "We are in loop %d!" % (i + 1)

print ""

print "Congrats! You've helped us in debugging this program!"

print ""

# Dummy variable to avoid having the program automatically exit after it is done
# running outside of the IDLE environemnt
dummy_input = raw_input('Press enter to exit the program.')
