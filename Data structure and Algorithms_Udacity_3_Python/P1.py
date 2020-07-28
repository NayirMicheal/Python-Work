def sqrt(number):
	"""
	Calculate the floored square root of a number

	Args:
		number(int): Number to find the floored squared root
	Returns:
		int: Floored Square Root
	"""

	end = number 
	start = 1
          
    # e decides the accuracy level 
	e = 0.000001
	while(end - start > e):   
		end = (end + start)/2
		start = number / end   
	return int(end) 
	pass

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print (sqrt(37))