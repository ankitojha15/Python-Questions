</> Markdown

# Define a function to reverse a string

- uses = slicing
- difficulty = easy

## Solution


def reverse_string(str1):

    # Return the reversed string using slicing with a step of -1

    return str1[::-1]

# Take user input for the name
string = input()

# Call the reverse_string function to reverse the name
reversed_str = reverse_string(string)

# Print the reversed name using an f-string for formatted output    
print(f"Your name reversed is: {reversed_str}")
