# Given a list of numbers and a number k, return whether any two numbers from the list add up to k
# Example: Given  and k of 17, return true since 10 + 7 is 17

def pairSumToK(nums, k):
	compliments = set()
	for num in nums:
		if num in compliments:
			return True
		compliments.add(k - num)
	return False

ex_nums_true = [10, 15, 3, 7]
ex_nums_false = [10, 15, 3, 8]
ex_k = 17

print(pairSumToK(ex_nums_true, ex_k))
print(pairSumToK(ex_nums_false, ex_k))
