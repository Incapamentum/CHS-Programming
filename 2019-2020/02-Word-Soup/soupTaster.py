# Format of the tester program was created by
# Gustavo Diaz Galeas, but much of the functionality
# was adapted to be used for the Word Soup assignment,
# which was done by Jonathan Bell.
# 2019 - 2020 AP Computer Science Principles
# Instructor: Nathan Whaley
# School: Colonial High School
# District: Orange County Public Schools, Florida

# Importing a variety of different modules and specific
# functions
import logging
import sys
import os
from os import path
from contextlib import redirect_stdout
from random import randint
from io import StringIO

# Attempting to import the student's program
try:
	import wordsoup as test
except:
	logging.error("Exception occured", exc_info=True)
	sys.exit(-1)

# Checks if testcases are in the correct directory
for i in range(1, 8):
	name = "TestCases/testcase" + str(i) + ".txt"
	if not path.exists(name):
		print("ERROR: TestCases not found. Please ensure the TestCases folder is in the same")
		print("       folder as wordsoup.py and that it has all 7 testcases")
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

# Creates a list with the string literals that should be printed out
ans = [None] * 7
ans[0] = """'a' : ['a']
'c' : ['case']
'i' : ['is']
't' : ['test', 'this']\n"""

ans[1] = """'a' : ['alligator']
'b' : ['bird']
'c' : ['crocodile']
'd' : ['deer']
'e' : ['eagle']
'f' : ['flamingo']
'g' : ['gazelle']
't' : ['turtle']
'z' : ['zebra', 'zoo']\n"""

ans[2] = """'a' : ['apple']
's' : ['salad', 'salamander', 'sam', 'sanguine', 'select', 'set', 'shazam', 'son', 'state', 'status', 'stop', 'sun']\n"""

ans[3] = """'c' : ['computer']
's' : ['science']\n"""

ans[4] = """'b' : ['brown']
'd' : ['dog']
'f' : ['fox']
'j' : ['jumps']
'l' : ['lazy']
'o' : ['over']
'q' : ['quick']
't' : ['the']\n"""

ans[5] = """'a' : ['alabama']
'b' : ['barony']
'c' : ['computers']
'd' : ['decimation']
'e' : ['egress']
'f' : ['foreign']
'g' : ['gregarious']
'h' : ['hondouras']
'i' : ['italy']
'j' : ['jumanji ']
'k' : ['kilobyte']
'l' : ['limousine']
'm' : ['meme', 'mundane']
'n' : ['namibia ']
'o' : ['overpowered']
'p' : ['protest']
'q' : ['qwerty']
'r' : ['rangers']
's' : ['supercalifragilisticexpialidocious']
't' : ['titanic']
'u' : ['ubuntu']
'v' : ['verizon']
'w' : ['windows']
'x' : ['xylography']
'y' : ['youtube']
'z' : ['zeal']\n"""

ans[6] = "'k' : ['kalmah', 'keelerakh', 'keetongu', 'kohrak', 'kreka', 'kriika', 'kurahk']\n"

# stores original stdout
origstdout = sys.stdout

# counter vars
total_passed = 0
total_test = 7

for i in range(1, 8):
	# redirects stdout and stores output as a string
	checker = StringIO()
	sys.stdout = checker
	# open each testcase (no need for try/except as existence was confirmed earlier)
	name = "TestCases/testcase" + str(i) + ".txt"
	fp = open(name, 'r')

	# runs the program and notes if it crashes
	# Note: can expand this to check each individual function
	#       if you are reading this, it means i didnt do the above,
	#       either out of forgetfullness or laziness, oops
	try:
		myList = test.Create_List(fp)
		myDict = test.Create_Dict(myList)
		test.Fancy_Print(myDict)
	except:
		sys.stdout = origstdout
		crash_msg(test_Case_msg(i))
		continue

	# restores stdout in order to print to console
	sys.stdout = origstdout
	
	# checks if program had the correct output
	if (checker.getvalue() == ans[i - 1]):
		total_passed += 1
		pass_msg(test_Case_msg(i))
	else:
		mismatch_msg(test_Case_msg(i))
	
# restores print output to console
sys.stdout = origstdout

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
