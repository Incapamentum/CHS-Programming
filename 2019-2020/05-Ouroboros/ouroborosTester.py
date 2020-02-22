# Created by Gustavo Diaz Galeas
# 2019 - 2020 AP Computer Science Principles
# Instructor: Nathan Whaley
# School: Colonial High School
# District: Orange County Public Schools, Florida

import logging
import sys
from random import randint

# Importing a bunch of specific objects from
# the following modules
try:
    from node import Node
except:
    print("***ERROR***")
    print("Please make sure the node.py file is", end=' ')
    print("in the same folder as the following files:")
    print("\touroboros.py\n\touroborosTester.py")
    sys.exit(-1)

try:
    from ouroboros import insert_and_link
    from ouroboros import remove_and_link
    from ouroboros import count_nodes
except:
    print("***ERROR***")
    print("Please make sure your program is saved as \"ouroboros.py\",", end=' ')
    print("and that it is in the same folder as the ouroborosTester.py program.")
    print("\n***NOTE***")
    print("If ANY of the required functions are NOT defined, the tester program", end=' ')
    print("will automatically exit to avoid having it crash.")
    print("This also includes if the functions are not named correctly.")
    print()
    logging.error("Exception occured", exc_info=True)
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

# ========================
#    Helper Function(s)
# ========================

# =======================
#    TESTING VARIABLES
# =======================

total_test = 9
total_passed = 0
test_case = 1

fib = [1, 1]

val1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
val2 = [1, 1, 2, 3, 5]
val3 = []

# =============
#    TESTING
# =============

# Creating a basic Ouroboros structure of size 10
n1 = Node(0)
n2 = Node(1, n1)
n1.next = n2

# Test Case #1
try:
    for i in range(2, 10):
        insert_and_link(n1, i)

    head = n1
    count = 0

    for i in range(10):
        if (head.data == val1[i]):
            head = head.next
            count += 1
        else:
            fail_msg(test_Case_msg(test_case))
            break

    if (count == 10):
        pass_msg(test_Case_msg(test_case))
        total_passed += 1

except:
    crash_msg(test_Case_msg(test_case))

test_case += 1

# Test Case #2
try:
    if (count_nodes(n1) != 10):
        fail_msg(test_Case_msg(test_case))
    else:
        pass_msg(test_Case_msg(test_case))
        total_passed += 1
except:
    crash_msg(test_Case_msg(test_case))

test_case += 1

# Test Case #3
try:
    count = 0

    for i in range(3):
        if (remove_and_link(n1) == (9 - i)):
            count += 1
        else:
            fail_msg(test_Case_msg(test_case))
            break

    if (count == 3):
        pass_msg(test_Case_msg(test_case))
        total_passed += 1

except:
    crash_msg(test_Case_msg(test_case))

test_case += 1

# Destroying the Ouroboros structure through the
# garbace collector
n2.next = None
n1 = None

# Creating a basic Ouroboros structure of size 5
n1 = Node(1)
n2 = Node(1, n1)
n1.next = n2

# Test Case #4
try:
    for i in range(2, 5):
        temp = fib[0] + fib[1]
        insert_and_link(n1, temp)
        fib[0] = fib[1]
        fib[1] = temp

    head = n1
    count = 0

    for i in range(5):
        if (head.data == val2[i]):
            head = head.next
            count += 1
        else:
            break
    
    if (count == 5):
        pass_msg(test_Case_msg(test_case))
        total_passed += 1
    else:
        fail_msg(test_Case_msg(test_case))
except:
    crash_msg(test_Case_msg(test_case))

test_case += 1

# Test Case #5
try:
    if ((remove_and_link(n1) == 5) and remove_and_link(n1) == 3):
        pass_msg(test_Case_msg(test_case))
        total_passed += 1
    else:
        fail_msg(test_Case_msg(test_case))    
except:
    crash_msg(test_Case_msg(test_case))

test_case += 1

# Test Case #6
try:
    if (count_nodes(n1) != 3):
        fail_msg(test_Case_msg(test_case))
    else:
        pass_msg(test_Case_msg(test_case))
        total_passed += 1
except:
    crash_msg(test_Case_msg(test_case))

test_case += 1

# Destroying the Ouroboros structure through the
# garbace collector
n2.next = None
n1 = None

# Creating a basic Ouroboros structure of undeterminate
# length
rand = randint(0, 200)
n1 = Node(rand)
val3.append(rand)

rand = randint(0, 200)
n2 = Node(rand, n1)
val3.append(rand)

n1.next = n2

size = 2
j = randint(11, 19)

# Test Case #7
try:
    for i in range(j):
        rand = randint(0, 200)
        val3.append(rand)
        insert_and_link(n1, rand)
        size += 1

    head = n1
    count = 0

    for i in range(size):
        if (head.data == val3[i]):
            head = head.next
            count += 1
        else:
            break

    if (count == size):
        pass_msg(test_Case_msg(test_case))
        total_passed += 1
    else:
        fail_msg(test_Case_msg(test_case))
except:
    crash_msg(test_Case_msg(test_case))

test_case += 1

# Test Case #8
try:
    if (count_nodes(n1) != size):
        fail_msg(test_Case_msg(test_case))
    else:
        pass_msg(test_Case_msg(test_case))
        total_passed += 1
except:
    crash_msg(test_Case_msg(test_case))

test_case += 1

# Test Case #9
try:
    j = randint(5, 10)
    count = 0

    for i in range(j):
        if (remove_and_link(n1) == val3[size - (1 + i)]):
            count += 1
        else:
            break

    if (count == j):
        pass_msg(test_Case_msg(test_case))
        total_passed += 1
    else:
        fail_msg(test_Case_msg(test_case))
            
except:
    crash_msg(test_Case_msg(test_case))

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