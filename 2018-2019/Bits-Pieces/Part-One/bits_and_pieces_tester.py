# Importing the program of the students

import sys

try:
	import bits_and_pieces
except:
	print("ERROR: Please rename your program to \"bits_and_pieces.py\"")
	sys.exit(-1)

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

# ==========================
#    Beginning of Testing
# ==========================

# Total number of test cases: 28
# is_binary() will have 4 test cases, all others will be 8
# Variables initialzied to 0 for more dynamic options
total_test = 22
total_passed = 0
total_crashed = 0

# Testing is_binary() function
prep_msg("is_binary()")

try:
	if bits_and_pieces.is_binary("1101"):
		pass_msg(test_Case_msg("1", "is_binary()"))
		total_passed += 1
	else:
		err_msg(test_Case_msg("1", "is_binary()"))
except:
	crash_msg(test_Case_msg("1", "is_binary()"))
	total_crashed += 1

try:
	if bits_and_pieces.is_binary("11000000011011100101010110"):
		pass_msg(test_Case_msg("2", "is_binary()"))
		total_passed += 1
	else:
		err_msg(test_Case_msg("2", "is_binary()"))
except:
	crash_msg(test_Case_msg("2", "is_binary()"))
	total_crashed += 1

try:
	if not bits_and_pieces.is_binary("1101100101011500111001"):
		pass_msg(test_Case_msg("3", "is_binary()"))
		total_passed += 1
	else:
		err_msg(test_Case_msg("3", "is_binary()"))
except:
	crash_msg(test_Case_msg("3", "is_binary()"))
	total_crashed += 1

try:
	if not bits_and_pieces.is_binary("123456789"):
		pass_msg(test_Case_msg("1", "is_binary()"))
		total_passed += 1
	else:
		err_msg(test_Case_msg("1", "is_binary()"))
except:
	crash_msg(test_Case_msg("1", "is_binary()"))
	total_crashed += 1

# Printing a newline
print("")

# Testing binary_to_decimal() function
prep_msg("binary_to_decimal()")

try:
	if bits_and_pieces.binary_to_decimal("100") != 4:
		err_msg(test_Case_msg("1", "binary_to_decimal()"))
	else:
		pass_msg(test_Case_msg("1", "binary_to_decimal()"))
		total_passed += 1
except:
	crash_msg(test_Case_msg("1", "binary_to_decimal()"))
	total_crashed += 1

try:
	if bits_and_pieces.binary_to_decimal("111111") != 63:
		err_msg(test_Case_msg("2", "binary_to_decimal()"))
	else:
		pass_msg(test_Case_msg("2", "binary_to_decimal()"))
		total_passed += 1
except:
	crash_msg(test_Case_msg("2", "binary_to_decimal()"))
	total_crashed += 1

try:
	if bits_and_pieces.binary_to_decimal("1000000010000000001") != 263169:
		err_msg(test_Case_msg("3", "binary_to_decimal()"))
	else:
		pass_msg(test_Case_msg("3", "binary_to_decimal()"))
		total_passed += 1
except:
	crash_msg(test_Case_msg("3", "binary_to_decimal()"))
	total_crashed += 1

try:
	if bits_and_pieces.binary_to_decimal("1100100000111100") != 51260:
		err_msg(test_Case_msg("4", "binary_to_decimal()"))
	else:
		pass_msg(test_Case_msg("4", "binary_to_decimal()"))
		total_passed += 1
except:
	crash_msg(test_Case_msg("4", "binary_to_decimal()"))
	total_crashed += 1

try:
	if bits_and_pieces.binary_to_decimal("1100100a00111100") != -1:
		err_msg(test_Case_msg("5", "binary_to_decimal()"))
	else:
		pass_msg(test_Case_msg("5", "binary_to_decimal()"))
		total_passed += 1
except:
	crash_msg(test_Case_msg("5", "binary_to_decimal()"))
	total_crashed += 1

try:
	if bits_and_pieces.binary_to_decimal("11001002000111100") != -1:
		err_msg(test_Case_msg("6", "binary_to_decimal()"))
	else:
		pass_msg(test_Case_msg("6", "binary_to_decimal()"))
		total_passed += 1
except:
	crash_msg(test_Case_msg("6", "binary_to_decimal()"))
	total_crashed += 1

# Printing a newline
print("")

# Testing decimal_to_binary() function
prep_msg("decimal_to_binary()")

try:
	if bits_and_pieces.decimal_to_binary(5) != "101":
		err_msg(test_Case_msg("1", "decimal_to_binary()"))
	else:
		pass_msg(test_Case_msg("1", "decimal_to_binary()"))
		total_passed += 1
except:
	crash_msg(test_Case_msg("1", "decimal_to_binary()"))
	total_crashed += 1

try:
	if bits_and_pieces.decimal_to_binary(15) != "1111":
		err_msg(test_Case_msg("2", "decimal_to_binary()"))
	else:
		pass_msg(test_Case_msg("2", "decimal_to_binary()"))
		total_passed += 1
except:
	crash_msg(test_Case_msg("2", "decimal_to_binary()"))
	total_crashed += 1

try:
	if bits_and_pieces.decimal_to_binary(21) != "10101":
		err_msg(test_Case_msg("3", "decimal_to_binary()"))
	else:
		pass_msg(test_Case_msg("3", "decimal_to_binary()"))
		total_passed += 1
except:
	crash_msg(test_Case_msg("3", "decimal_to_binary()"))
	total_crashed += 1

try:
	if bits_and_pieces.decimal_to_binary(77) != "1001101":
		err_msg(test_Case_msg("4", "decimal_to_binary()"))
	else:
		pass_msg(test_Case_msg("4", "decimal_to_binary()"))
		total_passed += 1
except:
	crash_msg(test_Case_msg("4", "decimal_to_binary()"))
	total_crashed += 1

try:
	if bits_and_pieces.decimal_to_binary(1011) != "1111110011":
		err_msg(test_Case_msg("5", "decimal_to_binary()"))
	else:
		pass_msg(test_Case_msg("5", "decimal_to_binary()"))
		total_passed += 1
except:
	crash_msg(test_Case_msg("5", "decimal_to_binary()"))
	total_crashed += 1

try:
	if bits_and_pieces.decimal_to_binary(2048) != "100000000000":
		err_msg(test_Case_msg("6", "decimal_to_binary()"))
	else:
		pass_msg(test_Case_msg("6", "decimal_to_binary()"))
		total_passed += 1
except:
	crash_msg(test_Case_msg("6", "decimal_to_binary()"))
	total_crashed += 1

# Printing a newline
print("")

# Testing bitwise_add() function
prep_msg("bitwise_add()")

try:
	if bits_and_pieces.bitwise_add("1", "0") != "1":
		err_msg(test_Case_msg("1", "bitwise_add()"))
	else:
		pass_msg(test_Case_msg("1", "bitwise_add()"))
		total_passed += 1
except:
	crash_msg(test_Case_msg("1", "bitwise_add()"))
	total_crashed += 1

try:
	if bits_and_pieces.bitwise_add("100", "1") != "101":
		err_msg(test_Case_msg("2", "bitwise_add()"))
	else:
		pass_msg(test_Case_msg("2", "bitwise_add()"))
		total_passed += 1
except:
	crash_msg(test_Case_msg("2", "bitwise_add()"))
	total_crashed += 1

try:
	if bits_and_pieces.bitwise_add("111", "111") != "1110":
		err_msg(test_Case_msg("3", "bitwise_add()"))
	else:
		pass_msg(test_Case_msg("3", "bitwise_add()"))
		total_passed += 1
except:
	crash_msg(test_Case_msg("3", "bitwise_add()"))
	total_crashed += 1

try:
	if bits_and_pieces.bitwise_add("1010", "1010") != "10100":
		err_msg(test_Case_msg("4", "bitwise_add()"))
	else:
		pass_msg(test_Case_msg("4", "bitwise_add()"))
		total_passed += 1
except:
	crash_msg(test_Case_msg("4", "bitwise_add()"))
	total_crashed += 1

try:
	if bits_and_pieces.bitwise_add("1000000000", "10000010001") != "11000010001":
		err_msg(test_Case_msg("5", "bitwise_add()"))
	else:
		pass_msg(test_Case_msg("5", "bitwise_add()"))
		total_passed += 1
except:
	crash_msg(test_Case_msg("5", "bitwise_add()"))
	total_crashed += 1

try:
	if bits_and_pieces.bitwise_add("1000000000", "10002010001") != "Error":
		err_msg(test_Case_msg("5", "bitwise_add()"))
	else:
		pass_msg(test_Case_msg("5", "bitwise_add()"))
		total_passed += 1
except:
	crash_msg(test_Case_msg("5", "bitwise_add()"))
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
