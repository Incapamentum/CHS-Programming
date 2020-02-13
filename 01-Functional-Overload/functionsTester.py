# Created by Gustavo Diaz Galeas
# 2019 - 2020 AP Computer Science Principles
# Instructor: Nathan Whaley
# School: Colonial High School
# District: Orange County Public Schools, Florida

# Importing the sys and os module. Also importing two specific functions found
# in the random and contextlib modules
import sys
import os
from contextlib import redirect_stdout
from random import randint

# Attempting to import the functionsTesterGenOutput.py program
try:
	import functionsTesterGenOutput
except:
	print("***ERROR***")
	print("Please make sure the functionsTesterGenOutput.py file is")
	print("in the same folder as the functionsTester.py file.")
	sys.exit(-1)

# Attempting to import the student's program
try:
	import functions
except:
	print("***ERROR***")
	print("Please make sure your program is saved as \"functions.py\"")
	print("and that it is in the same folder as the functionsTester.py file.")
	sys.exit(-1)

# =======================
#    Message Functions
# =======================

# Will let the student know which test case was failed
def fail_msg(msg):
	print(msg + "FAILED!")

# Will let the student know which test case was a mismatch
def mismatch_msg(msg):
	print(msg + "OUTPUT MISMATCH!")

# Will let the student know which test case was passed
def pass_msg(msg):
	print(msg + "PASSED!")

def crash_msg(msg):
	print(msg + "CRASHED!")

# Returns a string. Useful so I don't end up having to type out too much
def test_Case_msg(num):
	return "Test case #%d . . . " % (num)

# Returns a string stating what test value was used for the results.txt file
def return_test_value(num, val="NONE"):
	return "Test Value used for Test case #%d . . . %s\n" % (num, val)

# ====================
#    Test Variables
# ====================

# Total number of test cases: 32 test cases
total_test = 32
total_passed = 0
total_crashed = 0
test_case = 1

# Lists to help in testing due to use of for loops
testList = [14, 2.13, "String", True]
tempList = [32, 78, 55.5, -30]
medianList = [[5, 13, 20], [29, 54, 1], [-6, -9, -8], [-55, 0, 98]]
milList = [0, 10, 13, 23]

# Creating a new file that will summarize results of testing by stating what
# test variables were used exactly, to better aid the students.
fResults = open("results.txt", "w")

fResults.write("=============\n")
fResults.write("   RESULTS   \n")
fResults.write("=============\n\n")

# ============================
#    Directory Housekeeping
# ============================

# Obtaining the current working directory (referred to
# as the main current working directory), then creating
# path names for a sample_output and output directory
rootPath = os.getcwd()
samplePath = os.path.join(rootPath, "sample_output")
outputPath = os.path.join(rootPath, "output")

# Checking to see for the existence of a sample_output or
# output directory
if not os.path.exists(samplePath):
	os.makedirs(samplePath)
if not os.path.exists(outputPath):
	os.makedirs(outputPath)

# Changing the working directory to /sample_output
os.chdir(samplePath)

# Generating sample_output#.txt files into the /sample_output
# directory
functionsTesterGenOutput.gen_data_type_output()
functionsTesterGenOutput.gen_fahrenheit_celcius_output()
functionsTesterGenOutput.gen_median_three_output()
functionsTesterGenOutput.gen_military_standard_output()

# Changing the working directory back to root
os.chdir(rootPath)

# Testing return_five() function (Test Case 1)
try:
	if functions.return_five() != 5:
		fail_msg(test_Case_msg(test_case))
	else:
		pass_msg(test_Case_msg(test_case))
		total_passed += 1
except:
	crash_msg(test_Case_msg(test_case))
	total_crashed += 1

fResults.write(return_test_value(test_case))
test_case += 1

# Testing return_pi() function (Test Case 2)
try:
	if functions.return_pi() != 3.14:
		fail_msg(test_Case_msg(test_case))
	else:
		pass_msg(test_Case_msg(test_case))
		total_passed += 1
except:
	crash_msg(test_Case_msg(test_case))
	total_crashed += 1

fResults.write(return_test_value(test_case))
test_case += 1

# Testing return_hello() function (Test Case 3)
try:
	if functions.return_hello() != "Hello":
		fail_msg(test_Case_msg(test_case))
	else:
		pass_msg(test_Case_msg(test_case))
		total_passed += 1
except:
	crash_msg(test_Case_msg(test_case))
	total_crashed += 1

fResults.write(return_test_value(test_case))
test_case += 1

# Testing return_True() function (Test Case 4)
try:
	if functions.return_True() != True:
		fail_msg(test_Case_msg(test_case))
	else:
		pass_msg(test_Case_msg(test_case))
		total_passed += 1
except:
	crash_msg(test_Case_msg(test_case))
	total_crashed += 1

fResults.write(return_test_value(test_case))
test_case += 1

# Including a newline to results.txt
fResults.write('\n')

# Testing the determine_data_type() function (Test Cases 5, 6, 7, and 8)
for x in range(4):
	try:
		# os.path.join(outputPath, outputFile)
		# os.path.join(samplePath, sample_outputFile)
		outputFile = os.path.join(outputPath, "output0%d.txt" % (x + 5))
		sample_outputFile = os.path.join(samplePath, "sample_output0%d.txt" % (x + 5))
		with open(outputFile, "w") as fp:
			with redirect_stdout(fp):
				functions.determine_data_type(testList[x])

		with open(sample_outputFile, "r") as fBase:
			stringBase = fBase.read()
		
		with open(outputFile, "r") as fTest:
			stringTest = fTest.read()

		if stringBase != stringTest:
			mismatch_msg(test_Case_msg(test_case))
		else:
			pass_msg(test_Case_msg(test_case))
			total_passed += 1
	except:
		crash_msg(test_Case_msg(test_case))
		total_crashed += 1

	fResults.write(return_test_value(test_case, testList[x]))
	test_case += 1

# Including a newline to results.txt
fResults.write('\n')

# Testing the powTen() function (Test Cases 9 and 10)
# powNum will be a random integer of interval [0, 10],
# and will be passed as an argument to the powTen() function.
# testNum will be the correct value of the powTen() function
# based on the value of powNum. For example, if powNum = 3,
# then testNum = 1000.
for x in range(2):
	try:
		powNum = randint(0, 10)
		testNum = 0

		if powNum == 0:
			testNum = 1
		elif powNum == 1:
			testNum = 10
		else:
			testNum = 10
			for x in range(powNum - 1):
				testNum *= 10

		if functions.powTen(powNum) != testNum:
			fail_msg(test_Case_msg(test_case))
		else:
			pass_msg(test_Case_msg(test_case))
			total_passed += 1
	except:
		crash_msg(test_Case_msg(test_case))
		total_crashed += 1

	fResults.write(return_test_value(test_case, powNum))
	test_case += 1

# Including a newline to results.txt
fResults.write('\n')

# Testing the cubed() function (Test Cases 11 and 12)
# baseNum will be a random integer of interval [0, 10],
# and will be passed as an argument to the cubed() function.
# testNum will be the correct value of the cubed() function
# based on the value of baseNum. For example, if baseNum = 3,
# then testNum = 8.
for x in range(2):
	try:
		baseNum = randint(0, 10)

		if baseNum == 0:
			testNum = 0
		elif baseNum == 1:
			testNum = 1
		else:
			testNum = baseNum
			for x in range(2):
				testNum *= baseNum

		if functions.cubed(baseNum) != testNum:
			fail_msg(test_Case_msg(test_case))
		else:
			pass_msg(test_Case_msg(test_case))
			total_passed += 1
	except:
		crash_msg(test_Case_msg(test_case))
		total_crashed += 1

	fResults.write(return_test_value(test_case, baseNum))
	test_case += 1

# Including a newline to results.txt
fResults.write('\n')

# Testing the fahrenheit_to_celcius() function (Test Cases 13, 14, 15, and 16)
for x in range(4):
	try:
		outputFile = os.path.join(outputPath, "output0%d.txt" % (x + 5))
		sample_outputFile = os.path.join(samplePath, "sample_output%d.txt" % (x + 13))
		with open(outputFile, "w") as fp:
			with redirect_stdout(fp):
				functions.fahrenheit_to_celcius(tempList[x])

		with open(sample_outputFile, "r") as fBase:
			stringBase = fBase.read()
		
		with open(outputFile, "r") as fTest:
			stringTest = fTest.read()

		if stringBase != stringTest:
			mismatch_msg(test_Case_msg(test_case))
		else:
			pass_msg(test_Case_msg(test_case))
			total_passed += 1
	except:
		crash_msg(test_Case_msg(test_case))
		total_crashed += 1

	fResults.write(return_test_value(test_case, tempList[x]))
	test_case += 1

# Including a newline to results.txt
fResults.write('\n')

# Testing the print_median_of_three() function (Test Cases 17, 18, 19, and 20)
for x in range(4):
	try:
		outputFile = os.path.join(outputPath, "output0%d.txt" % (x + 5))
		sample_outputFile = os.path.join(samplePath, "sample_output%d.txt" % (x + 17))
		testNumbers = medianList[x]
		with open(outputFile, "w") as fp:
			with redirect_stdout(fp):
				functions.print_median_of_three(testNumbers[0], testNumbers[1], testNumbers[2])
		
		with open(sample_outputFile, "r") as fBase:
			stringBase = fBase.read()
		
		with open(outputFile, "r") as fTest:
			stringTest = fTest.read()

		if stringBase != stringTest:
			mismatch_msg(test_Case_msg(test_case))
		else:
			pass_msg(test_Case_msg(test_case))
			total_passed += 1

	except:
		crash_msg(test_Case_msg(test_case))
		total_crashed += 1

	fResults.write(return_test_value(test_case, testNumbers))
	test_case += 1

# Including a newline to results.txt
fResults.write('\n')

# Testing the print_military_to_standard() function (Test Cases 21, 22, 23, and 24)
for x in range(4):
	try:
		outputFile = os.path.join(outputPath, "output0%d.txt" % (x + 5))
		sample_outputFile = os.path.join(samplePath, "sample_output%d.txt" % (x + 21))
		with open(outputFile, "w") as fp:
			with redirect_stdout(fp):
				functions.print_military_to_standard(milList[x])
		
		with open(sample_outputFile, "r") as fBase:
			stringBase = fBase.read()
		
		with open(outputFile, "r") as fTest:
			stringTest = fTest.read()

		if stringBase != stringTest:
			mismatch_msg(test_Case_msg(test_case))
		else:
			pass_msg(test_Case_msg(test_case))
			total_passed += 1
	except:
		crash_msg(test_Case_msg(test_case))
		total_crashed += 1

	fResults.write(return_test_value(test_case, milList[x]))
	test_case += 1

# Including a newline to results.txt
fResults.write('\n')

# Testing the get_ordinal_day() function (Test Cases 25, 26, 27, and 28)
try:
	if functions.get_ordinal_day(1, 24) != 24:
		fail_msg(test_Case_msg(test_case))
	else:
		pass_msg(test_Case_msg(test_case))
		total_passed += 1
except:
	crash_msg(test_Case_msg(test_case))
	total_crashed += 1

fResults.write(return_test_value(test_case, (1, 24)))
test_case += 1

try:
	if functions.get_ordinal_day(5, 21) != 141:
		fail_msg(test_Case_msg(test_case))
	else:
		pass_msg(test_Case_msg(test_case))
		total_passed += 1
except:
	crash_msg(test_Case_msg(test_case))
	total_crashed += 1

fResults.write(return_test_value(test_case, (5, 21)))
test_case += 1

try:
	if functions.get_ordinal_day(7, 1) != 182:
		fail_msg(test_Case_msg(test_case))
	else:
		pass_msg(test_Case_msg(test_case))
		total_passed += 1
except:
	crash_msg(test_Case_msg(test_case))
	total_crashed += 1

fResults.write(return_test_value(test_case, (7, 1)))
test_case += 1

try:
	if functions.get_ordinal_day(12, 31) != 365:
		fail_msg(test_Case_msg(test_case))
	else:
		pass_msg(test_Case_msg(test_case))
		total_passed += 1
except:
	crash_msg(test_Case_msg(test_case))
	total_crashed += 1

fResults.write(return_test_value(test_case, (12, 31)))
test_case += 1

# Including a newline to results.txt
fResults.write('\n')

# Testing the ordinal_day_error_checking() function (Test Cases 29, 30, 31, and 32)
try:
	if functions.ordinal_day_error_checking(13, 1) != -1:
		fail_msg(test_Case_msg(test_case))
	else:
		pass_msg(test_Case_msg(test_case))
		total_passed += 1
except:
	crash_msg(test_Case_msg(test_case))
	total_crashed += 1

fResults.write(return_test_value(test_case, (13, 1)))
test_case += 1

try:
	if functions.ordinal_day_error_checking(3, 32) != -1:
		fail_msg(test_Case_msg(test_case))
	else:
		pass_msg(test_Case_msg(test_case))
		total_passed += 1
except:
	crash_msg(test_Case_msg(test_case))
	total_crashed += 1

fResults.write(return_test_value(test_case, (3, 32)))
test_case += 1

try:
	if functions.ordinal_day_error_checking(2, 29) != -1:
		fail_msg(test_Case_msg(test_case))
	else:
		pass_msg(test_Case_msg(test_case))
		total_passed += 1
except:
	crash_msg(test_Case_msg(test_case))
	total_crashed += 1

fResults.write(return_test_value(test_case, (2, 29)))
test_case += 1

try:
	if functions.ordinal_day_error_checking(6, 31) != -1:
		fail_msg(test_Case_msg(test_case))
	else:
		pass_msg(test_Case_msg(test_case))
		total_passed += 1
except:
	crash_msg(test_Case_msg(test_case))
	total_crashed += 1

fResults.write(return_test_value(test_case, (6, 31)))
test_case += 1

# Printing a newline
print()

# Including a newline to results.txt
fResults.write('\n')

# =====================
#    Testing Summary
# =====================

print("Total number of test cases: " + str(total_test))
print("Total passed: " + str(total_passed))
print("Total failed: " + str(total_test - total_passed - total_crashed))
print("Total crashed: " + str(total_crashed))

fResults.write("Total number of test cases: %d\n" % (total_test))
fResults.write("Total passed: %d\n" % (total_passed))
fResults.write("Total failed: %d\n" % (total_test - total_passed - total_crashed))
fResults.write("Total crashed: %d\n" % (total_crashed))

# Closing the fResults file object
fResults.close()

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
