# Created by Gustavo A. Diaz Galeas

def is_binary(string):

	for s in string:
		if s != '0' and s != '1':
			return False

	return True

def binary_to_decimal(binary_string):

	if not is_binary(binary_string):
		return -1

	length = len(binary_string)
	dec = 0

	for i in range(0, length):
		dec = dec * 2 + int(binary_string[i])

	return dec

def decimal_to_binary(deci):
	unsorted_list = []
	binary_string = ""
	working_num = deci

	while working_num != 0:
		bit = working_num % 2
		unsorted_list.append(bit)
		working_num = int(working_num / 2)

	length = len(unsorted_list)

	for i in range(0, length):
		binary_string += str(unsorted_list[length - (i + 1)])

	return binary_string

def bitwise_add(binary_string1, binary_string2):

	if (not is_binary(binary_string1)) or (not is_binary(binary_string2)):
		return "Error"

	dec1 = binary_to_decimal(binary_string1)
	dec2 = binary_to_decimal(binary_string2)

	result_dec = dec1 + dec2

	return decimal_to_binary(result_dec)
