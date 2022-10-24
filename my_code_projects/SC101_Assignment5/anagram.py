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

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """
    ####################
    #                  #
    #       TODO:      #
    #                  #
    ####################
    print(f'Welcome to stanCode "Anagram Generator" (or {EXIT} to quit)')
    s = input('Find anagrams for: ')
    start = time.time()
    while True:
        if s != EXIT:
            find_anagrams(s)
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end - start} seconds.')
            s = input('Find anagrams for: ')
        else:
            break


def read_dictionary():
    lst = []
    with open(FILE, 'r') as f:
        for word in f:
            ans = ''
            for ch in word:
                if ch != '\n':
                    ans += ch
            lst.append(ans)
        return lst


def find_anagrams(s):
    """
    :param s: The string being input by user.
    :return: List of words which include param 's'.
    """
    answer = []
    lst1 = []
    lst2 = []
    for i in range(len(s)):
        lst1.append(i)
    find_anagrams_helper(s, '', len(s), answer, lst1, lst2)
    print(f'{len(answer)} anagrams: {answer}')


def find_anagrams_helper(s, current_s, ans_len, answer, lst1, lst2):
    if len(current_s) == ans_len:
        dic = read_dictionary()
        for word in dic:
            if current_s == word:
                if word not in answer:
                    print(f'Found: {word}')
                    print('Searching...')
                    answer.append(word)
    else:
        for i in lst1:
            if i in lst2:
                pass
            else:
                # Choose
                lst2.append(i)
                current_s += s[i]
                if has_prefix(current_s) is True:
                    # Explore
                    find_anagrams_helper(s, current_s, ans_len, answer, lst1, lst2)
                # Un-choose
                ans = ''
                for j in range(len(current_s)-1):
                    ans += current_s[j]
                current_s = ans
                lst2.pop()


def has_prefix(sub_s):
    """
    :param sub_s: Current sub string of word.
    :return: True or False
    """
    lst = read_dictionary()
    for word in lst:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
