# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    if len(word) != len(anagram): return False

    word_histogram = {}

    for char in word:
        word_histogram[char] = word_histogram.get(char, 0) + 1

    anagram = list(anagram)
    unique_anagram = set(anagram)

    for char in unique_anagram:
        if anagram.count(char) != word_histogram.get(char, 0): return False

    return True

print(find_anagram("below", "elbow"))