# Created by Gustavo Diaz Galeas

# Given an "unknown" number num, it will set the bit of that number, potentially
# altering its value if that bit has been set or not.
# As an example, consider the following, "unknown" 8-bit number: XXXX XXXX
# As the value of the number is unknown, so too are the bits. When it comes to
# setting a bit, the fortunate thing is that it doesn't matter whether or not
# the value of the number is known because a bit in the number will be set to a
# 1, regardless of the previous value of the bit.
#
# Consider the following table for the bitwise or operation:
# +---------------+
# | a | b | a | b |
# | 0 | 0 |   0   |
# | 0 | 1 |   1   |
# | 1 | 0 |   1   |
# | 1 | 1 |   1   |
# +---------------+
#
# Note how the output is always 1 if there is a 1 as an input. This relationship,
# taking into consideration unknown bits X, can be described by the following
# two expressions:
# X | 0 = X
# X | 1 = 1
#
# In setting a bit from an n-bit number, just use bitwise or! To clarify and
# demonstrate, consider setting BIT4 from an unknown 8-bit number:
#
#   XXXX XXXX  <------- This is the unknown 8-bit number
# | 0001 0000  <------- Setting BIT4 into the unknown 8-bit number
# -----------
#   XXX1 XXXX  <------- The resulting value for the unknown 8-bit number, using
#						the expressions discussed above.
#
# Below is a function that accomplishes this concept of setting a bit given a
# possibly unknown number.
def set_bit(num, bit):
	return num | bit

# Given an "unknown" number num, it will clear the bit of that number, possibly
# altering its value if that bit has been set or not.
# Using the above "unknown" 8-bit number of XXXX XXXX:
# When it comes to clearing a bit, the forunate thing is that it doesn't matter
# whetehr or not the value of the number is known because a bit in the number
# will be cleared to a 0, regardless of the previous value of the bit.
#
# Consider the following table for the bitwise and operation:
# +---------------+
# | a | b | a & b |
# | 0 | 0 |   0   |
# | 0 | 1 |   0   |
# | 1 | 0 |   0   |
# | 1 | 1 |   1   |
# +---------------+
#
# Note how, regardless if there is a 1 present as an input or not, if there is a
# 0 as an input, the output will always be 0. This relationship, taking into
# consideration unknown bits X, can be described by the following two
# expressions:
# X & 1 = X
# X & 0 = 0
#
# In clearing a bit from an n-bit number, the bit to be cleared must first be
# negated so that the bit in question becomes 0, but all other bits are 1 in the
# bit value so as to not affect the value of the other bits in the unknown
# number. To clarify, consider clearing BIT2 from an unknown 8-bit number:
#
#     XXXX XXXX   <-------- this is the unknown number
# & ~(0000 0100)  <-------- this is BIT2.
#
#   XXXX XXXX
# & 1111 1011     <-------- this is ~BIT2 (the inverse of BIT2).
# -----------
#   XXXX X0XX     <-------- the expressions discussed above were used to express
#							the new value of an unknown number.
#
# Below is the function that clears a specified bit from a number, which may
# possibly be unknown.
def clear_bit(num, bit):
	return num & (~bit)

# In the extraction of a bit, it is a similar thought process as in clearing a
# bit. The only exception to this is that the bit will be extracted to determine
# what its value is from the passed number, disregarding all other bits. Below
# is an example of this being done, extracting BIT5 of an unknown number:
#
#   XXXX XXXX
# & 0010 0000
# -----------
#   00X0 0000    <----- extracted bit from an unknown number.
def extract_bit(num, bit):
	return num & bit

# This is very similar to the extract_bit() function, with the exception that
# this will return a Boolean value by doing a logical comparison to the bit.
# It returns True if the extracted bit is 1, False otherwise.
def bit_status(num, bit):
	return (num & bit) == bit
