"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
DICT = []
ALL = []
TOTAL_LIST = []
PLAYLIST = []
EXIT = -1


def main():
	while True:
		row_1_1 = input('1 row of letters: ')
		if not check(row_1_1):
			print('Illegal input')
			break
		row_2_1 = input('2 row of letters: ')
		if not check(row_2_1):
			print('Illegal input')
			break
		row_3_1 = input('3 row of letters: ')
		if not check(row_3_1):
			print('Illegal input')
			break
		row_4_1 = input('4 row of letters: ')
		if not check(row_4_1):
			print('Illegal input')
			break
		total(row_1_1, row_2_1, row_3_1, row_4_1)
		read_dictionary()
		boggle(TOTAL_LIST)
		break


def boggle(lst):
	global PLAYLIST
	for i in range(4):
		for j in range(4):
			boggle_helper(lst, '', [(i, j)], i, j)
	print('There are ' + str(len(PLAYLIST)) + ' words in total')
	PLAYLIST = []


def boggle_helper(s, string, index, r, c):
	if string in DICT and string not in PLAYLIST and len(string) >= 4:
		print('Found: ' + string)
		PLAYLIST.append(string)
	else:
		for i in range(-1, 2):
			for j in range(-1, 2):
				new_r = r + i
				new_c = c + j
				if 0 <= new_r < 4:
					if 0 <= new_c < 4:
						if [new_r, new_c] not in index:
							string += s[new_r][new_c]
							index.append([new_r, new_c])
							if has_prefix(string):
								boggle_helper(s, string, index, new_r, new_c)
							index.pop()
							string = string[:(len(string) - 1)]


def check(row):
	if len(row) != 7:
		return False
	for i in range(len(row)):
		if i % 2 == 1:
			if row[i] != ' ':
				return False
	return True


def total(r1, r2, r3, r4):
	global ALL, TOTAL_LIST
	r1 = r1.lower()
	r2 = r2.lower()
	r3 = r3.lower()
	r4 = r4.lower()
	ALL.append(r1)
	ALL.append(r2)
	ALL.append(r3)
	ALL.append(r4)
	for line in ALL:
		if line != ' ':
			line = line.split()
			TOTAL_LIST.append(line)
	return TOTAL_LIST


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global DICT
	with open('dictionary.txt', 'r') as f:
		for line in f:
			new_line = line.strip()
			DICT.append(new_line)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for line in DICT:
		if line.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()