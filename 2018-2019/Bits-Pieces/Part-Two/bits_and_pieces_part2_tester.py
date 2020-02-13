import sys
from random import randint

try:
	import bits_and_pieces_part2
except:
	print("***ERROR***")
	print("Please make sure your program is saved as \"bits_and_pieces_part2.py\"")
	print("and that it is in the same folder as the tester program.")
	sys.exit(-1)

# ======================
#    Global Variables
# ======================

# The index of this list corresponds to the position of the bit, with its value
# representing the value of the bit at that position
BIT = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]

# The initial_val will be used in all test cases. The test_val variable will be
# used in comparison tests, so as to not alter the value of initial_val.
# DISCLAIMER: Using randin() to generate a random value may not be the best
# possible approach when it comes to testing
initial_val = randint(0, 255)
test_val = initial_val

# =======================
#    Message Functions
# =======================

# Will let the student know which test case was failed
def err_msg(message):
	print("FAILED: " + message)

# Will let the student know which test case was passed
def pass_msg(message):
	print("PASSED: " + message)

def crash_msg(message):
	print("CRASHED: " + message)

# Returns a string. Useful so I don't end up having to type out too much
def test_Case_msg(num, func):
	return "Test case " + num + " for " + func

# Will print a message in preparation for testing of the function
def prep_msg(func):
	print("Beginning testing of the " + func + " function...")

# ============================
#    Miscellaneous Function
# ============================

def decimal_to_binary_8bit(deci):

	binary_str = ""

	for i in range(8, 0, -1):
		if ((deci >> i - 1) & 1) == 1:
			binary_str += "1"
		else:
			binary_str += "0"

	return binary_str

# ===================
#   Test Variables
# ===================

# Current test cases at 24. 8 each for 3 functions. Only function that doesn't
# have explicit test cases is the bit_status() function
total_test = 32
total_passed = 0
total_crashed = 0

# Some auxilliary variables to aid in the testing process
reps = len(BIT)
bin_str = decimal_to_binary_8bit(initial_val)

# Stating two values used in testing of the functions
print("Value of initial_val: " + str(initial_val))
print("Value of bin_str: " + bin_str)

# Printing a newline
print("")

# A warning message to let others know about the possibility of not passing
# test cases for the set_bit() and clear_bit() functions
print("***NOTE***")
print("The bit_status() function is used in the testing of the set_bit() and")
print("clear_bit() functions. If you are not completely passing the test cases")
print("for this function, then there is a good likelihood that you won't be")
print("completely passing the test cases for the set_bit() and clear_bit()")
print("functions")

# Printing a newline
print("")

# Testing bit_status() function
prep_msg("bit_status()")

for i in range(int(reps / 2)):
	try:
		if bits_and_pieces_part2.bit_status(BIT[i*2], BIT[i*2]):
			pass_msg(test_Case_msg(str(i + 1), "bit_status()"))
			total_passed += 1
		else:
			err_msg(test_Case_msg(str(i + 1), "bit_status()"))
	except:
		crash_msg(test_Case_msg(str(i + 1), "bit_status()"))
		total_crashed += 1

for i in range(int(reps / 2)):
	try:
		if not bits_and_pieces_part2.bit_status(BIT[i*2], ~BIT[i*2]):
			pass_msg(test_Case_msg(str(i + 5), "bit_status()"))
			total_passed += 1
		else:
			err_msg(test_Case_msg(str(i + 5), "bit_status()"))
	except:
		crash_msg(test_Case_msg(str(i + 5), "bit_status()"))
		total_crashed += 1

# Printing a newline
print("")

# Testing set_bit() function
prep_msg("set_bit()")

for i in range(reps):
	try:
		test_val = bits_and_pieces_part2.set_bit(initial_val, BIT[i])
		if bits_and_pieces_part2.bit_status(test_val, BIT[i]):
			pass_msg(test_Case_msg(str(i + 1), "set_bit()"))
			total_passed += 1
		else:
			err_msg(test_Case_msg(str(i + 1), "set_bit()"))
	except:
		crash_msg(test_Case_msg(str(i + 1), "set_bit()"))
		total_crashed += 1

# Printing a newline
print("")

# Testing clear_bit() function
prep_msg("clear_bit()")

for i in range(reps):
	try:
		test_val = bits_and_pieces_part2.clear_bit(initial_val, BIT[i])
		if not bits_and_pieces_part2.bit_status(test_val, BIT[i]):
			pass_msg(test_Case_msg(str(i + 1), "clear_bit()"))
			total_passed += 1
		else:
			err_msg(test_Case_msg(str(i + 1), "clear_bit()"))
	except:
		crash_msg(test_Case_msg(str(i + 1), "clear_bit()"))
		total_crashed += 1

# Printing a newline
print("")

# Testing clear_bit() function
prep_msg("extract_bit()")

for i in range(reps):
	try:
		weight = int(bin_str[reps - (i + 1)]) * (2**i)
		if bits_and_pieces_part2.extract_bit(initial_val, BIT[i]) != weight:
			err_msg(test_Case_msg(str(i + 1), "extract_bit()"))
		else:
			pass_msg(test_Case_msg(str(i + 1), "extract_bit()"))
			total_passed += 1
	except:
		crash_msg(test_Case_msg(str(i + 1), "extract_bit()"))
		total_crashed += 1

# Printing a newline
print("")

# =====================
#    Testing Summary
# =====================

print("Total number of test cases: " + str(total_test))
print("Total passed: " + str(total_passed))
print("Total failed: " + str(total_test - total_passed - total_crashed))
print("Total crashed: " + str(total_crashed))

if total_passed == total_test:
	print("")
	print("")
	print("              ,)))))))),,,")
	print("            ,(((((((((((((((,")
	print("            )\\`\\)))))))))))))),")
	print("     *--===///`_    ```(((((((((")
	print("           \\\\\\ b\\  \\    ``)))))))")
	print("            ))\\    |     ((((((((               ,,,,")
	print("           (   \\   |`.    ))))))))       ____ ,)))))),")
	print("                \\, /  )  ((((((((-.___.-\"    `\"(((((((")
	print("                 `\"  /    )))))))               \\`)))))")
	print("                    /    ((((``                  \\(((((")
	print("              _____|      `))         /          |)))))")
	print("             /     \\                 |          / (((((")
	print("            /  --.__)      /        _\\         /   )))))")
	print("           /  /    /     /'`\"~----~`  `.       \\   ((((")
	print("          /  /    /     /`              `-._    `-. `)))")
	print("         /_ (    /    /`                    `-._   \\ ((")
	print("        /__|`   /   /`                        `\\`-. \\ ')")
	print("               /  /`                            `\\ \\ \\")
	print("              /  /                                \\ \\ \\")
	print("             /_ (                                 /_()_(")
	print("            /__|`                                /__/__|")
	print("")
	print("                             Legendary.")
	print("")
	print("                10/10 would run this program again.")
	print("")
	print("  CONGRATULATIONS! You appear to be passing all required test cases!")
	print("  Note that these test cases are in no way comprehensive. Your program")
	print("  may not provide the correct output for certain fringe cases, so please")
	print("  be aware of this fact, and it is encouraged to thoroughly test your")
	print("  program for such possibilities!")
	print("")
else:
	print("")
	print("")
	print("                           .")
	print("                          \":\"")
	print("                        ___:____     |\"\\/\"|")
	print("                      ,'        `.    \\  /")
	print("                      |  o        \\___/  |")
	print("                    ~^~^~^~^~^~^~^~^~^~^~^~^~")
	print("")
	print("                           (fail whale)")
	print("")
	print("Note: The fail whale is friendly and adorable! He is not here to")
	print("      demoralize you, but rather, to bring you comfort and joy")
	print("      in your time of need. \"Keep plugging away,\" he says! \"You")
	print("      can do this!\"")
	print("")
