# Created by Jon Bell (with help from Gustavo Diaz Galleas)
# 2019 - 2020 AP Computer Science Principles
# Instructor: Nathan Whaley
# School: Colonial High School
# District: Orange County Public Schools, Florida

import random
# For various mispellings
try:
    import Binomial_Coefficient as test
except ExplicitException:
    try:
        import BinomialCoefficient as test
    except ExplicitException:
        try:
            import binomialCoefficient as test
        except ExplicitException:
            try:
                import binomialcoefficient as test
            except ExplicitException:
                print (("Error: Missing or Misnamed file. Please rename "
                        "as Binomial_Coefficient.py and try again!"))
                sys.exit(-1)

# =======================
#    Message Functions
# =======================

print(("Starting tester! May take some time "
         "(~30 seconds at MOST depending on your implementation)\n\n"), flush = True)

# ==================== #
#    Test Variables    #
# ==================== #

amtPassed = 0
amtToPass = 10

# randomly 10 numbers for N and K inputs, each
testN = [random.randint(1, 27) for i in range(10)]
testK = [random.randint(0, 27) for i in range(10)]
t = lambda n, k: 1 if k == 0 or k == n else t(n-1, k) + t(n-1, k-1)

# test cases
for i in range(10):
    # ensures that n >= k >= 0
    if testN[i] > testK[i]:
        tempN = testN[i]
        tempK = testK[i]
    else:
        tempN = testK[i]
        tempK = testN[i]

    print("Case %d: n = %d, k = %d" % (i+1, tempN, tempK))

    try:
        yourVal = test.Binomial_Coefficient(tempN, tempK)
        realVal = t(tempN, tempK)
        if yourVal == realVal:
            amtPassed += 1
            isEq = "=="
            mismatch = ""
        else:
            isEq = "!="
            mismatch = "(Output mismatch!)"

        print("   Your result: %d" % yourVal)
        print("\t\t\t    %s Expected Result: %d %s\n" % (isEq, realVal, mismatch))

    except NameError:
        print(("ERROR: Function not found! "
                "Make sure your function is spelled as: Binomial_Coefficient\n"))

    except e:
        print("ERROR: Program Crashed!\n")


if amtPassed == amtToPass:
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
