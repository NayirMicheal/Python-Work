def mergeSort(arr): 
	if len(arr) >1: 
		mid = len(arr)//2 # Finding the mid of the array 
		L = arr[:mid] # Dividing the array elements  
		R = arr[mid:] # into 2 halves 
  
		mergeSort(L) # Sorting the first half 
		mergeSort(R) # Sorting the second half 
  
		i = j = k = 0
			
		# Copy data to temp arrays L[] and R[] 
		while i < len(L) and j < len(R): 
			if L[i] < R[j]: 
				arr[k] = L[i] 
				i+= 1
			else: 
				arr[k] = R[j] 
				j+= 1
			k+= 1
			
		# Checking if any element was left 
		while i < len(L): 
			arr[k] = L[i] 
			i+= 1
			k+= 1
			
		while j < len(R): 
			arr[k] = R[j] 
			j+= 1
			k+= 1
def rearrange_digits(input_list):
	"""
	Rearrange Array Elements so as to form two number such that their sum is maximum.

	Args:
		input_list(list): Input List
	Returns:
		(int),(int): Two maximum sums
	"""
	if len(input_list) == 0:
		return [0,0]
	mergeSort(input_list)
	print(input_list)
	first_num =1
	first=0
	second=0
	max_num = 0
	co_st = 10
	co_se = 10
	while len(input_list):
		max_num=input_list[-1]
		if first_num:
			first = first*co_st + max_num
			first_num =0
		elif first_num == 0:
			second = second *co_se+ max_num
			first_num =1
		input_list.pop(-1)
	print(first)
	print(second)
	return[first,second]
	pass

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")
		
test_function([[1, 2, 3, 4, 5], [542, 31]])

test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

test_function([[2, 3, 4, 5, 6], [642, 53]])



