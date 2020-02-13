import random

def is_int(data):
	if type(data) is int:
		return True

	return False

def is_even(n):
	if (n % 2) == 0:
		return True

	return False

def string_contains_char(str, ch):
	for c in str:
		if c == ch:
			return True

	return False

def find_distance_traveled(time, rate):
	return time * rate

def fahrenheit_to_celsius(f):
	return (f - 32) * (5.0/9.0)

def string_travel_data(dist, time, rate):
	if dist == 0:
		# print("Distance traveled: %.2f feet" % (time * rate))
		return "Distance traveled: %.2f feet" % (time * rate)

	if time == 0:
		# print("Time spent traveling: %.2f minutes" % (dist / rate))
		return "Time spent traveling: %.2f minutes" % (dist / rate)

	if rate == 0:
		# print("Rate traveled: %.2f feet per minute" % (dist / time))
		return "Rate traveled: %.2f feet per minute" % (dist / time)

# Specify that absolute value function CANNOT be used for this one
def find_floor_distance(eleOne, eleTwo):
	if eleOne == 0 or eleTwo == 0:
		return -1

	if eleOne == eleTwo:
		return 0

	dist = eleOne - eleTwo

	if dist < 0:
		dist *= -1

	return dist

def find_inclusive_sum(start, end):
	sum = 0

	if start == end:
		return start
	elif start > end:
		return -1

	for x in range(start, end + 1):
		sum += x

	return sum
