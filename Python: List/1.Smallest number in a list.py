# Smallest number in a list
# Problem : Write a program to get the smallest number from a list.

# Difficulty : easy

-- Vaious ways to solve this...

# Solution

#from functools import reduce

list1 =  list(map(int,input().strip().split()))
#Write your code here

#samllest_number = reduce(min,list1)
#print(f"Smallest element is: {samllest_number}")

#samllest_number = min(list1)
#print(samllest_number)

smallest_number = list1[0]
for i in list1:
    if i < smallest_number:
        smallest_number = i
    
print(f"Smallest element is: {smallest_number}")
