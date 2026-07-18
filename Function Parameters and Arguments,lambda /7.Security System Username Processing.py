#join the username with a prefix "user_"

# use = strip,lower,count,cancatenation,f string
# difficulty : medium

# problem = he program should remove any leading or trailing spaces, convert the username to lowercase, and count the occurrences of a particular character within the username.

# solution


username = input()
char_to_count = input()

username = username.strip()
username = username.lower()

char_count = username.count(char_to_count)

final_username = "user_" + username

print(f"Processed Username: {final_username}")
print (f"Number of times {char_to_count} appears in the username {char_count}")
