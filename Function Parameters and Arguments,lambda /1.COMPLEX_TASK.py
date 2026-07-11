## COMPLEX TASK
# Problem
Write a Python script to multiply two complex numbers given in string format. The complex numbers will be in the form of "real+imaginaryi", where 'real' and 'imaginary' are integers. Your script should return result.
Functionality Requirements:
- Parsing Complex Numbers:
- Multiplying Complex Numbers:

-- Difficulty: Medium
-- Uses : Slicing

## Solution

def parser(s):
    s = s[:-1]

    real,img = s.split("+")

    return int(real),int(img)

def multiply_complex_numbers(num1, num2):

    a,b = parser(num1)
    c,d = parser(num2)

    real_part = (a*c - b*d)
    img_part =  (a*d + b*c)
    return (f"{real_part}+{img_part}i")



