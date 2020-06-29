# import datetime
# x= datetime.datetime.now()
# print(x)

import datetime

x= datetime.datetime(2020, 5, 7)

# day
# print(x.strftime("%d")) | print(x.strftime("%A")) | print(x.strftime("%a"))

# month
# print(x.strftime("%B")) | print(x.strftime("%b")) | print(x.strftime("%m"))

# # year
# print(x.strftime("%Y")) | print(x.strftime("%y"))

#microsec
# print(x.strftime("%f"))

# easiest
print(x.strftime("%c"))