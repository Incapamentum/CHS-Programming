# Created by Gustavo A. Diaz Galeas
#
# A programming assignment for the students enrolled in the AP CSP course
# at Colonial High School in Orlando, Florida.
#
# Purpose: To further develop critical thinking skills in the creation of
# Python programs based on constraints and an end-result. Will test concepts
# already previously covered (loops), and provide new content to aid in the
# reinforcement of newly introduced data structures: lists and dictionaries
#

# Creating an inventory of items for the store using a dictionary data structure
inventory = {'milk': 2.99, 'bread': 3.00, 'egg': 0.09, 'chicken': 5.05, 'shrimp': 8.99, 'sirloin steak': 13.85}

# Creating an inventory list that contains all of the keys associated with the
# dictionary inventory
inventory_list = inventory.keys()

# Creating an empty list to be populated by user input
shopping_list = []

# Creating a total to keep a running total going
total = 0

# Welcome prompts
print "Welcome to Barg'n Shop!\n"
print "Here is our current inventory of items available to our shoppers: "

# Will print the items within the dictionary
for k, v in inventory.iteritems():
	print str(k) + ": " + "$%.2f" % (v)

# Will populate the empty shopping list. Also contains conditional satements to
# check what the shopper would like to do.
while 1:
	shopper_input = raw_input('\nWhat would you like to buy? (Type \'exit\' to checkout / Type \'cart\' to peak at your cart) ')

	if (shopper_input == 'exit'):
		break
	elif (shopper_input == 'cart'):
		print "Here is your cart: " + str(shopping_list)
		continue
	elif (not inventory.has_key(shopper_input)):
		print "Sorry! Seems we do not have that item in stock."
		continue
	else:
		shopping_list.append(shopper_input)
		print "The " + shopper_input + " was successfully added to your cart!"

# Prompt to determine if the shopper has placed anything in their cart or not.
if (len(shopping_list) == 0):
	print "\nThanks for dropping by!"
else:
	print "\nCalculating your total!"

	for x in range(len(shopping_list)):
		total += inventory[shopping_list[x]]

	print "Your total is: " + str(total) + "!"
	print "Thank you for shopping with us!"

	print ""

	dummy_input = raw_input('Please press enter to exit.')
