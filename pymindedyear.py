import datetime



def leap_year(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    else:
        return False

try:
    year_orig = int(input("For which year do you want to re-use an old calender? "))
except(ValueError):
    print("Please enter a year.")
    exit()
print(year_orig)

fristdayofyear_orig = datetime.date(year_orig,1,1).strftime("%A")
leapyear_orig = leap_year(year_orig)
year_test = year_orig

search = True

while (search):
    year_test -= 1 
    if (fristdayofyear_orig == datetime.date(year_test,1,1).strftime("%A")):
        if (leapyear_orig == leap_year(year_test)):
            search = False


print ("The calender of "+str(year_test)+" can be used.")





