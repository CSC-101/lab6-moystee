import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp

# Part 1
def compare_title(book1: data.Book, book2: data.Book) -> bool:
    return book1 < book2
def selection_sort_books(books: list[data.Book]) -> None:
    for i in range(len(books)):
        min_index = i
        for j in range(i + 1, len(books)):
            if compare_title(books[j], books[min_index]):
                min_index = j
        if min_index != i:
            temp = books[i]
            books[i] = books[min_index]
            books[min_index] = temp
#Purpose: Alphabetize the inputted list
# Part 2
def swap_case(letters: str) -> str:
    result = []
    for letter in letters:
        if letter.islower():
            result.append(letter.upper())
        elif letter.isupper():
            result.append(letter.lower())
        else:
            result.append(letter)
    return ''.join(result)
#Purpose: Swaps lowercased letters to uppercase and vis versa
# Part 3
def str_translate(string: str, old: str, new: str) -> str:
        result = ""
        for str in string:
            if str == old:
                result += new
            else:
                result += str
        return result
#Purpose: Replace a letter in a string with another letter
# Part 4
def histogram(input_str: str) -> dict:
    word_count = {}
    word = ""
    for str in input_str:
        if str == ' ':
            if word:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
                word = ""
        else:
            word += str
    if word:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
        return word_count
#Purpose: Keep track of the number of times each word appears in the string with a dictionary.