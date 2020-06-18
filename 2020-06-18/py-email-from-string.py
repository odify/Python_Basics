import re

pattern=r"(\w+\.*\w+@\w+\.\w+)"

str="find the email addresses from this string hello everyone dielaraah@gmail.com, gddcrrrrrfcfhcdf pw.alaaanee98@gmail.com, gfdtbiyevv daaass20@gmail.com like this code  "

match=re.findall(pattern,str)

if match:
    
    print(str)
    
    print("The email address is:",match)