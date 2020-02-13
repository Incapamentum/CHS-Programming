# Importing the program of the students and the random module
import functions, random

# Will let the student know which test case was failed
def err_msg(message):
	print("FAILED: " + message)

# Will let the student know which test case was passed
def pass_msg(message):
	print("PASSED: " + message)

# Returns a string. Useful so I don't end up having to type out too much
def test_Case_msg(num, func):
	return "Test case " + num + " for " + func

# Will print a message in preparation for testing of the function
def prep_msg(func):
	print("Beginning testing of the " + func + " function...")

# Total number of test cases per function: 4
# Total number of functions: 8
# Total number of test cases: 32 test cases
total_test = 32
total_passed = 0

# Testing is_int() function
prep_msg("is_int()")

if functions.is_int(1):
	pass_msg(test_Case_msg("1", "is_int()"))
	total_passed += 1
else:
	err_msg(test_Case_msg("1", "is_int()"))

if not functions.is_int(3.14):
	pass_msg(test_Case_msg("2", "is_int()"))
	total_passed += 1
else:
	err_msg(test_Case_msg("2", "is_int()"))

if not functions.is_int("Hello!"):
	pass_msg(test_Case_msg("3", "is_int()"))
	total_passed += 1
else:
	err_msg(test_Case_msg("3", "is_int()"))

if not functions.is_int(True):
	pass_msg(test_Case_msg("4", "is_int()"))
	total_passed += 1
else:
	err_msg(test_Case_msg("4", "is_int()"))

# Printing a newline
print("")

# Testing is_even() function
prep_msg("is_even()")

if functions.is_even(90):
	pass_msg(test_Case_msg("1", "is_even()"))
	total_passed += 1
else:
	err_msg(test_Case_msg("1", "is_even()"))

if not functions.is_even(17999079):
	pass_msg(test_Case_msg("2", "is_even()"))
	total_passed += 1
else:
	err_msg(test_Case_msg("2", "is_even()"))

if not functions.is_even(3.14):
	pass_msg(test_Case_msg("3", "is_even()"))
	total_passed += 1
else:
	err_msg(test_Case_msg("3", "is_even()"))

if functions.is_even(0):
	pass_msg(test_Case_msg("4", "is_even()"))
	total_passed += 1
else:
	err_msg(test_Case_msg("4", "is_even()"))

# Printing a newline
print("")

# Testing string_contains_char() function
prep_msg("string_contains_char()")

if functions.string_contains_char("hello there", ' '):
	pass_msg(test_Case_msg("1", "string_contains_char()"))
	total_passed += 1
else:
	err_msg(test_Case_msg("1", "string_contains_char()"))

if functions.string_contains_char("Mount Everest", 'v'):
	pass_msg(test_Case_msg("2", "string_contains_char()"))
	total_passed += 1
else:
	err_msg(test_Case_msg("2", "string_contains_char()"))

if not functions.string_contains_char("poop emoji", 'z'):
	pass_msg(test_Case_msg("3", "string_contains_char()"))
	total_passed += 1
else:
	err_msg(test_Case_msg("3", "string_contains_char()"))

if not functions.string_contains_char("newcomer", ' '):
	pass_msg(test_Case_msg("4", "string_contains_char()"))
	total_passed += 1
else:
	err_msg(test_Case_msg("4", "string_contains_char()"))

# Printing a newline
print("")

# Testing find_distance_traveled() function
prep_msg("find_distance_traveled()")

if functions.find_distance_traveled(60, 5280) != 316800:
	err_msg(test_Case_msg("1", "find_distance_traveled()"))
else:
	pass_msg(test_Case_msg("1", "find_distance_traveled()"))
	total_passed += 1

if functions.find_distance_traveled(10, 500) != 5000:
	err_msg(test_Case_msg("2", "find_distance_traveled()"))
else:
	pass_msg(test_Case_msg("2", "find_distance_traveled()"))
	total_passed += 1

if functions.find_distance_traveled(5, 10) != 50:
	err_msg(test_Case_msg("3", "find_distance_traveled()"))
else:
	pass_msg(test_Case_msg("3", "find_distance_traveled()"))
	total_passed += 1

if functions.find_distance_traveled(0, 1) != 0:
	err_msg(test_Case_msg("4", "find_distance_traveled()"))
else:
	pass_msg(test_Case_msg("4", "find_distance_traveled()"))
	total_passed += 1

# Printing a newline
print("")

# Testing fahrenheit_to_celsius() function
prep_msg("fahrenheit_to_celsius()")

# Will run through four iterations to test different temperature numbers
for x in range(0, 4):
	tempF = random.randint(-500, 500)
	tempC = (tempF - 32) * (5.0/9.0)

	if functions.fahrenheit_to_celsius(tempF) != tempC:
		err_msg(test_Case_msg(str(x), "fahrenheit_to_celsius()"))
	else:
		pass_msg(test_Case_msg(str(x), "fahrenheit_to_celsius()"))
		total_passed += 1

# Printing a newline
print("")

# Testing string_travel_data() function
prep_msg("string_travel_data()")

if functions.string_travel_data(0.0, 4.0, 5.0) != "Distance traveled: 20.00 feet":
	err_msg(test_Case_msg("1", "string_travel_data()"))
else:
	pass_msg(test_Case_msg("1", "string_travel_data()"))
	total_passed += 1

if functions.string_travel_data(5.0, 0.0, 4.0) != "Time spent traveling: 1.25 minutes":
	err_msg(test_Case_msg("2", "string_travel_data()"))
else:
	pass_msg(test_Case_msg("2", "string_travel_data()"))
	total_passed += 1

if functions.string_travel_data(5.0, 4.0, 0.0) != "Rate traveled: 1.25 feet per minute":
	err_msg(test_Case_msg("3", "string_travel_data()"))
else:
	pass_msg(test_Case_msg("3", "string_travel_data()"))
	total_passed += 1

if functions.string_travel_data(80.0, 0.0, 15.0) != "Time spent traveling: 5.33 minutes":
	err_msg(test_Case_msg("4", "string_travel_data()"))
else:
	pass_msg(test_Case_msg("4", "string_travel_data()"))
	total_passed += 1

# Printing a newline
print("")

# Testing find_floor_distance() function
prep_msg("find_floor_distance()")

if functions.find_floor_distance(0, 3) != -1:
	err_msg(test_Case_msg("1", "find_floor_distance()"))
else:
	pass_msg(test_Case_msg("1", "find_floor_distance()"))
	total_passed += 1

if functions.find_floor_distance(3, 3) != 0:
	err_msg(test_Case_msg("2", "find_floor_distance()"))
else:
	pass_msg(test_Case_msg("2", "find_floor_distance()"))
	total_passed += 1

if functions.find_floor_distance(13, 3) != 10:
	err_msg(test_Case_msg("3", "find_floor_distance()"))
else:
	pass_msg(test_Case_msg("3", "find_floor_distance()"))
	total_passed += 1

if functions.find_floor_distance(3, 13) != 10:
	err_msg(test_Case_msg("1", "find_floor_distance()"))
else:
	pass_msg(test_Case_msg("1", "find_floor_distance()"))
	total_passed += 1

# Printing a newline
print("")

# Testing find_inclusive_sum() function
prep_msg("find_inclusive_sum()")

if functions.find_inclusive_sum(3, 15) != 117:
	err_msg(test_Case_msg("1", "find_inclusive_sum()"))
else:
	pass_msg(test_Case_msg("1", "find_inclusive_sum()"))
	total_passed += 1

if functions.find_inclusive_sum(15, 19) != 85:
	err_msg(test_Case_msg("2", "find_inclusive_sum()"))
else:
	pass_msg(test_Case_msg("2", "find_inclusive_sum()"))
	total_passed += 1

if functions.find_inclusive_sum(15, 15) != 15:
	err_msg(test_Case_msg("3", "find_inclusive_sum()"))
else:
	pass_msg(test_Case_msg("3", "find_inclusive_sum()"))
	total_passed += 1

if functions.find_inclusive_sum(3, 0) != -1:
	err_msg(test_Case_msg("4", "find_inclusive_sum()"))
else:
	pass_msg(test_Case_msg("4", "find_inclusive_sum()"))
	total_passed += 1

# Printing a newline
print("")

# Testing summary
print("Total number of test cases: " + str(total_test))
print("Total passed: " + str(total_passed))
print("Total failed: " + str(total_test - total_passed))
