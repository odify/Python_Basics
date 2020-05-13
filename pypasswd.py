
# import random 
# s="abcdefghijklmnopqrstuvwxyz\1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_-+{}[]/;'.," 
# passwordlen = 16 
# password  = "".join(random.sample(s,passwordlen))
# print(password)


char = ['!', '@', '#', '$', '%', '&', '*']
n = 0

password = input("")

num = [int(i) for i in password if i.isdigit()]
if len(password) >=7 and len(num) >= 2:
    for i in password:
        for j in char:
            if i == j:
                n += 1
            else:
                continue 
    if n >= 2:

        print("Strong")
    else:

        print("Weak")
else:

#     print("Weak")
# IMCOMPLETE