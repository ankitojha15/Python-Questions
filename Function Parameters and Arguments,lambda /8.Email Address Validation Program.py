# Email Address Validation Program

# problem : (It should contain the "@" symbol and be positioned between characters (not at the start or end).
#               There should be exactly one "@" symbol present.
#               The email address must end with either ".com" or ".in".)

# use : count,endswith,startswith,strip
# difficulty : medium

# solution 

email = input().strip()

check = (
    email.count("@") == 1
    and email.endswith((".com",".in"))
    and not email.startswith("@")
    and not email.endswith("@")
)

if check:
    print("Valid")
else:
    print("Invalid")
