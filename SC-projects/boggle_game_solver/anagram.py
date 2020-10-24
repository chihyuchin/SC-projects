"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
DICT = []
NEW_DICT = []
PLAYLIST = []


def main():
    while True:
        print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
        query = input('Find anagram for: ')
        query = query.lower()
        if query == "-1":
            break
        else:
            read_dictionary(query)
            find_anagrams(query)


def read_dictionary(query):
    global DICT
    with open('dictionary.txt', 'r') as f:
        for line in f:
            new_line = line.strip()
            if len(query) == len(new_line):
                DICT.append(new_line)


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    global PLAYLIST
    find_anagrams_helper(s, '', [])
    print(str(len(PLAYLIST)) + ' anagrams: ' + str(PLAYLIST))
    PLAYLIST = []


def find_anagrams_helper(s, string, index):
    if len(string) == len(s):
        if string in DICT and string not in PLAYLIST:
            print('Searching... ')
            print('Found: ' + string)
            PLAYLIST.append(string)
    else:
        for i in range(len(s)):
            if i not in index:
                string += s[i]
                index.append(i)
                if has_prefix(string) is True:
                    find_anagrams_helper(s, string, index)
                    index.pop()
                    string = string[:(len(string) - 1)]
                else:
                    index.pop()
                    string = string[:(len(string) - 1)]


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    for line in DICT:
        if line.startswith(sub_s):
            return True


if __name__ == '__main__':
    main()
