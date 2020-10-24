"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""

NUM = 0

def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	n = abs(n)
	find_largest_digit_helper(n, 0)
	return NUM


def find_largest_digit_helper(n, ans):
	global NUM
	if n <= 0:
		NUM = ans
		pass
	else:
		x = n // 10
		y = n - x * 10
		if ans <= y:
			ans = y
		find_largest_digit_helper(n // 10, ans)


if __name__ == '__main__':
	main()
