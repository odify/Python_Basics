import re

pattern = r"@"

mail = input("Enter a valid email: ")

if re.search(pattern, mail):
    print(mail)
else:
    print("Incorrect Email!")