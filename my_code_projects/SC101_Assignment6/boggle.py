"""
File: boggle.py
Name: Jason
----------------------------------------
TODO: Find matched words in the 4*4 input table.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'




def main():
	"""
	TODO: Find matched words in the 4*4 input table.
	"""
	####################
	#                  #
	#       TODO:      #
	#                  #
	####################
	lst = get_grid()
	if len(lst) == 4:
		start = time.time()
		dic = read_dictionary()
		count = []
		for i in range(4):
			for j in range(4):
				word = lst[i][j]
				cur_list = [(i, j)]
				find_word(lst, i, j, word, cur_list, [], dic, count)
				cur_list.clear()
		print("There are", len(count), "words in total.")
		end = time.time()
		print('----------------------------------')
		print(f'The speed of your boggle algorithm: {end - start} seconds.')


def get_grid():
	lst1 = []
	for i in range(4):
		letters = input(str(i + 1) + " row of letters: ")
		if len(letters) != 7:
			print('Illegal input.')
			break
		else:
			lst2 = []
			for j in range(4):
				lst2 += letters[(2 * j)].lower()
			lst1.append(lst2)
	return lst1


def find_word(lst, m, n, word, cur_list, word_list, dic, count):
	if word in dic and len(word) > 3 and word not in word_list:
		print('Found: ', word)
		word_list.append(word)
		count.append(1)
	if has_prefix(word) is True:
		for i in range(-1, 2):
			for j in range(-1, 2):
				if 4 > m+i >= 0 and 4 > n+j >= 0 and (m+i, n+j) not in cur_list:
					word += lst[m+i][n+j]
					cur_list.append((m+i, n+j))
					find_word(lst, m+i, n+j, word, cur_list, word_list, dic, count)
					cur_list.pop()
					word = word[:-1]


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dictionary = []
	with open(FILE, "r") as f:
		for words in f:
			dictionary += words.split()
		return dictionary


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	lst = read_dictionary()
	for word in lst:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
