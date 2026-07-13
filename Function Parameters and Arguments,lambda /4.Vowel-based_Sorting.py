## Vowel-based Sorting

# Problem

## You have a list of words, and you want to sort them based on the number of vowels in each word. 
## Create a Python lambda function custom_sort that takes a list of words as an argument and sorts the words in ascending order of the number of vowels in each word using a lambda function.

#  Input : python java cpp c-sharp scala
# Output : ['cpp', 'python', 'c-sharp', 'java', 'scala']

# Difficulty : Hard
# Use :  lambda and sorted()

# solution

custom_sort = lambda words: sorted (
    words, key = lambda word: sum(1 for char in word if char in 'aeiou')
)
