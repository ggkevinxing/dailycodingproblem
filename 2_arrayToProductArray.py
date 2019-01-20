# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# Example: Given input  [1, 2, 3, 4, 5], the output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

def arrayToProductArray(arr):
	product = 1
	for num in arr:
		product *= num
	res = []
	for num in arr:
		res.append(product / num)
	return res

# Follow-up: What if we couldn't use division?

def arrayToProductArray_noDivision(arr):
	if len(arr) < 2:
		return []	# can't possibly return an array in which every integer is a product of every other values in the array if there are no other values
	
	# build an array to build upon and store all the products so we don't repeat operations
	result = [1] * len(arr)
	wipProduct = 1
	
	# find the product of all the integers that come before arr[i]
	for i in xrange(len(arr)):
		result[i] = wipProduct
		wipProduct *= arr[i]
	
	wipProduct = 1
	
	# find the product of all the integers that come after arr[i], building on our products from before to build a complete result array
	for i in xrange(len(arr) - 1, -1, -1):
		result[i] *= wipProduct
		wipProduct *= arr[i]
	return result
