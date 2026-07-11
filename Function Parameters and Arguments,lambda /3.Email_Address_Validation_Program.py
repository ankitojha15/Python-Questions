</> Markdown

# Email Address Validation Program

## problem

-- checking if the email is valid or not

-- difficulty : Medium

## solution

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
