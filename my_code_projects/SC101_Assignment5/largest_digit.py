"""
File: largest_digit.py
Name: Jason
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: The integer to be checked.
	:return: The largest number in the integer.
	"""
	largest = 0
	return find_largest_digit_helper(n, largest)


def find_largest_digit_helper(n, largest):
	if n < 0:
		n = -n
	if int(n) <= 0:
		return largest
	else:
		x = n / 10
		n = (x - int(x)) * 10
		if n > largest:
			largest = n
			return int(find_largest_digit_helper(x, largest))
		else:
			return int(find_largest_digit_helper(x, largest))


if __name__ == '__main__':
	main()
