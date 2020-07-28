def get_min_max(ints):
	"""
	Return a tuple(min, max) out of list of unsorted integers.

	Args:
		ints(list): list of integers containing one or more integers
	"""
	if len(ints) > 0:
		min_number = ints[0]
		max_number = ints[0]
		for int in ints[1:] :
			if min_number > int:
				min_number = int
			if max_number < int:
				max_number = int
		return (min_number,max_number)
	return None
	pass

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [0 for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 0) == get_min_max(l)) else "Fail")

l = [2 for i in range(0, 10)]  # a list containing 0 - 9
l[5]=5
random.shuffle(l)

print ("Pass" if ((2, 5) == get_min_max(l)) else "Fail")