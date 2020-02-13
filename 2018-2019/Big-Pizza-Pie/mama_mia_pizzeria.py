# Created by Gustavo A. Diaz Galeas
#
# A sample program for an assignment for the students enrolled in the AP
# Computer Science course at Colonial High School in Orlando, Florida.
#
# Purpose: To implement a program that prints out a customers receipt upon
# order placement. A worker inputs the necessary data, it is processed, then
# all of the information will be displayed upon the screen.
#

# Initialization
pizza_base_price = 9.99
price_per_topping = 1.05
tax_rate = 0.1
prompt_welcome = "Welcome to the Big Pizza Pie Pizzeria!"

# Welcome prompts
print prompt_welcome
print

# Inputs and declaration of further variables
customer_name = raw_input('What is the name of the customer?\n')
order_number = input('What is the order number?\n')
num_toppings = input('How many toppings are on the pizza?\n')

# Calculating pricing for the subtotal and total of the pizza
subtotal = pizza_base_price + (num_toppings * price_per_topping)
tax = subtotal * tax_rate
total = subtotal + tax

#Printing the receipt
print
print
print customer_name + "          Order #" + str(order_number)
print "----------------------------"
print "Base price of pizza: $" + str(pizza_base_price)
print "Price per topping: $" + str(price_per_topping)
print "Number of toppings: "  + str(num_toppings)
print "Subtotal: $" + str(subtotal)
print "Tax: $%0.2f" % (tax)
print "Total: $%0.2f" % (total)
