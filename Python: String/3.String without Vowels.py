# String without Vowels

# Problem : a program that takes in a string and prints a new string with all vowels removed. (Vowels : aeiouAEIOU)

# Solution 

#Input a string 

string = input()

#Define a vowels in a string format (eg: vowels = "aeiouAEIOU")

vowels = "aeiouAEIOU"

new_string = ""
for i in string:
    if i not in vowels:
        new_string += i

print(new_string)

# Input:
# Hello World

# Output:
# Hll Wrld
