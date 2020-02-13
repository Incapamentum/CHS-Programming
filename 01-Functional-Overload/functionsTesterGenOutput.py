# Created by Gustavo Diaz Galeas
# 2019 - 2020 AP Computer Science Principles
# Instructor: Nathan Whaley
# School: Colonial High School
# District: Orange County Public Schools, Florida

# This is a program to be used in generating output files
# for some of the tested functions in the Functional Overload
# assignment.

# These are lists to be used in generating content for the output files
# as for loops are being used to reduce the number of lines of code
dataList = ["Integer\n", "Float\n", "String\n", "Boolean\n"]
tempFList = [32, 78, 55.5, -30]
tempCList = [0.00, 25.56, 13.06, -34.44]
medianList = [13, 29, -8, 0]
milList = ["12:00 AM\n", "10:00 AM\n", "1:00 PM\n", "11:00 PM\n"]

# Will generate output files for test cases 5, 6, 7, and 8.
# These are associated with the determine_data_type() function.
def gen_data_type_output():
    for x in range(4):
        fileName = "sample_output0%d.txt" % (x + 5)

        with open(fileName, "w") as fo:
            fo.write(dataList[x])

# Will generate output files for test cases 13, 14, 15, and 16.
# These are associated with the fahrenheit_to_celcius() function.
def gen_fahrenheit_celcius_output():
    for x in range(4):
        fileName = "sample_output%d.txt" % (x + 13)

        msg = "Fahrenheit temperature: %.2f; Celcius temperature: %.2f\n" % (tempFList[x], tempCList[x])

        with open(fileName, "w") as fo:
            fo.write(msg)

# Will generate output files for test cases 17, 18, 19, and 20
def gen_median_three_output():
    for x in range(4):
        fileName = "sample_output%d.txt" % (x + 17)

        msg = "The median is: %d\n" % (medianList[x])

        with open(fileName, "w") as fo:
            fo.write(msg)

# Will generate output files for test cases 21, 22, 23, and 24
def gen_military_standard_output():
    for x in range(4):
        fileName = "sample_output%d.txt" % (x + 21)

        with open(fileName, "w") as fo:
            fo.write(milList[x])
