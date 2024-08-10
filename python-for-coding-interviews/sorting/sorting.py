# Sort Ascending
from typing import List


def sort_words(words: List[str]) -> List[str]:
    words.sort()
    return words

def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort()
    return numbers

def sort_decimals(numbers: List[float]) -> List[float]:
    numbers.sort()
    return numbers
    



# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))


# Sort Descending
def sort_words(words: List[str]) -> List[str]:
    words.sort(reverse=True)
    return words

def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(reverse=True)
    return numbers


def sort_decimals(numbers: List[float]) -> List[float]:
    numbers.sort(reverse=True)
    return numbers




# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))

# Sort Custom
def get_word_length(word: str) -> int:
    return len(word)

def get_abs_value(number: int) -> int: 
    return abs(number)


def sort_words(words: List[str]) -> List[str]:
    words.sort(key=get_word_length, reverse=True)
    return words 
    


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=get_abs_value)
    return numbers

# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))

# Sort Lambda
def sort_words(words: List[str]) -> List[str]:
    words.sort(
        key=lambda word: len(word),
        reverse=True
    )
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(
        key= lambda number: abs(number),
        reverse=False
    )
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))

# Sorted Copy
def sort_words(words: List[str]) -> List[str]:
    return sorted(words)


def sort_numbers(numbers: List[int]) -> List[int]:
    return sorted(numbers, key=abs, reverse=True)


# do not modify below this line
original_words = ["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]

print(original_words)
print(sort_words(original_words))

original_numbers = [1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]

print(original_numbers)
print(sort_numbers(original_numbers))

