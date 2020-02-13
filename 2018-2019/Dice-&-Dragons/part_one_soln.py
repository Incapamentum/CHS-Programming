from random import randint

# Recall that every class definition will always begin with the "class" keyword.
# This lets Python know that any keyword beginning with "Car" will be a custom
# data type that the programmer created. To create an object using this custom
# data type, it will work much like a function, i.e. Car(make, model, year, transmission)
class Car:

	# This part is not always entirely required, but it is always nice to have,
	# especially if you wish for others to use your class. This is known as a
	# documentation string (often shortened to simply docstring) and if one is
	# decided to be included in a class definition, ensure that it is descriptive
	# enough for anyone to know what the data type will accomplish and how it
	# can be used as well
	"""Contains information regarding vehicles such as their make, model, year
	and transmission.\n
	The make, model, and transmission are entered as strings. The year is entered
	as an integer."""

	# This is a special function found within the Car class. These kinds of special
	# functions are denoted by the double underscore characters ('_') on both sides
	# of the name of the function. The reason why these functions are considered
	# special is because you do not have to explicitly call them (in other words,
	# you can simply do the following call: Car(make, model, year, transmission)
	# versus Car.__init__(make, model, year, transmission). Python knows what to
	# do with these special functions)
	def __init__(self, make, model, year, transmission):
		self.make = make
		self.model = model
		self.year = year
		self.transmission = transmission

	# This is another special function that returns the information contained within
	# a created object as a string. Remember, you do not have to explicitly call
	# the function itself (i.e. print(Car.__str__())). You can just simply do
	# print(Car), and the information will be printed out!
	def __str__(self):
		return "Make: %s, Model: %s, Year: %d, Transmission: %s" % (self.make, self.model, self.year, self.transmission)

	# Note that this is NOT a special function. This is just a regular function.
	# So, for this function you will have to explicitly call the function, i.e.
	# Cars.gears(4)
	def gears(self, num_gears):
		if self.transmission == "M":
			self.num_gears = num_gears
		else:
			self.num_gears = 0

# Here are some examples to demonstrate what was discussed here:

# This is to obtain the docstring
print(Car.__doc__)

# Printing a newline
print()

# Creating a car object
fave_car = Car("DeLorean", "DMC-12", 1981, "M")

# Printing out the information of the car
print(fave_car)

# Printing a newline
print()

# Will call the gears() function to set the number of gears to the car if it is
# a manual
fave_car.gears(7)

# Creating a list of four cars. Note that I do not have to create individual variable
# names for each vehicle as a list is an ordered sequence of elements. As an
# alternative, a dictionary can be used to assign each vehicle a unique key.
car_list = [Car("Ford", "Mustang", 2019, "A"), Car("Mazda", "3", 2015, "M"), Car("Chevrolet", "Camaro", 1968, "M"), Car("Dodge", "Charger", 1997, "M")]

# Using a for loop to print out all of the information of the vehicles
for cars in car_list:
	print(cars)

# Printing a newline
print()

class Student:

	"""To store information regarding students in a high school.\n
	Information required is the student's ID, their grade level, their expected
	graduation year, and their GPA as well."""

	def __init__(self, stu_ID, grade, grad_year, GPA):
		self.stu_ID = stu_ID
		self.grade = grade
		self.grad_year = grad_year
		self.GPA = GPA

	def __str__(self):
		return "Student ID: %d, Student Grade: %d, Expected Graduation: %d, GPA: %.1f" % (self.stu_ID, self.grade, self.grad_year, self.GPA)

# Created a list filled with the information of three students. To create UNIQUE
# key:value pairings, a dictionary may be used.
student_list = [Student(12345, 10, 2019, 3.5), Student(19839, 9, 2020, 3.0), Student(29178, 10, 2019, 4.0)]

# Using a for loop to print out the information of the students contained in the
# list
for student in student_list:
	print(student)

# Printing a newline
print()

class Die:

	"""A simple class definition that contains the number of sides of a die. Also
	includes a roll() function that returns a random integer from 1 to the number
	of sides of the die."""

	def __init__(self, sides):
		self.sides = sides

	def roll(self):
		return randint(1, self.sides)

# Creating a 6-sided die
d6 = Die(6)

# First, an empty list will be created. Then, in the following for loop, it will
# be populated with 6 0's
dice_rolls = []

for i in range(6):
	dice_rolls.append(0)

# Will begin rolling the d6 and keep track of the value it rolled on using the
# list. Recall that the indexing of a list always begins from 0 even though it is
# the very first cell it appears in. Thus, if the d6 were to roll a 1, to correctly
# keep track of the number of 1's are rolled, a 1 must be subtracted in the indexing
# to ensure the correct value will be entered. In addition, this will also avoid
# the more serious issue of a segmentation fault where we are overstepping the
# bounds in memory for the list. So, if a 6 were rolled, the index will be 6,
# even though the max index of our list is 5. Thus, subtracting a 1 will ensure
# that no segfaults occur.
for i in range(10):
	dice_rolls[d6.roll() - 1] += 1

# Printing the contents of the list, demonstrating the number of rolls done
print("Contents of the list: " + str(dice_rolls))

# Clearing out the list
for i in range(len(dice_rolls)):
	dice_rolls[i] = 0

# Printing a newline
print()

# Below is some additional code to really show that the above process works and
# no tom-follery is happening
for i in range(10):
	roll = d6.roll()
	print("Value rolled: " + str(roll))
	dice_rolls[roll - 1] += 1

print("\nContents of the list: " + str(dice_rolls))
