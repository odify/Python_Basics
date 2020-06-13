from datetime import date
#import tyz, json
import calendar
from string import *
from urllib.request import urlopen
from html.parser import HTMLParser
import sys
import codecs
sys.stdout = codecs.getwriter('utf_16')(sys.stdout.buffer, 'strict')


# print-out func
def _output(zodiac, sign, daily):
    print("i am : {}".format(zodiac))
    print("My symbol : {}".format(sign),'\n')
    print(sign*10,'\n')
    print(daily)
    
def out_2(zodiac, sign):
    print("i am :",zodiac)
    print("My symbol :",sign)
    print("\n")
    print(sign*20)


class MyHTMLParser(HTMLParser): 
    def __init__(self):
        super().__init__()
        self.p=False
        self.pbuf=[]
    def handle_starttag(self, tag, attrs): 
        if(tag=="p"):
            self.p=True
            self.pbuf=[]
    def handle_endtag(self, tag): 
        if(tag=="p"):
            self.p=False
            print("".join(self.pbuf),flush=1)
    def handle_data(self, data): 
        if(self.p):
            data=data.replace("\\n","\n")
            data=data.replace("\\","")
            self.pbuf.append(data)


parser = MyHTMLParser()

def z_txt(sybm_):
    lin = urlopen("https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign="+sybm_).read()
    lin = str(lin)
    parser.feed(lin)

def zodiac_sign(day, month):
    global z_sign
    if month == z_sign[0]:
        if day < 20:
           print(out_2(z_month[0], symb[0]))
           _output(z_month[0], symb[0], z_txt('10'))
        else:
            print(out_2(z_month[1], symb[1]))
            _output(z_month[1], symb[1], z_txt('11'))
    elif month == z_sign[1]:
        if day < 19 :
            print(out_2(z_month[1], symb[1]))
            _output(z_month[1], symb[1], z_txt('11'))
        else:
            print(out_2(z_month[2], symb[2]))
            _output(z_month[2], symb[2], z_txt('12'))
    elif month == z_sign[2]:
        if day < 21:
            print(out_2(z_month[2], symb[2]))
            _output(z_month[2], symb[2], z_txt('12'))
        else:
            print(out_2(z_month[3], symb[3]))
            _output(z_month[3], symb[3], z_txt('1'))
    elif month == z_sign[3]:
        if day < 20:
            print(out_2(z_month[3], symb[3]))
            _output(z_month[3], symb[3], z_txt('1'))
        else:
            print(out_2(z_month[4], symb[4]))
            _output(z_month[4], symb[4], z_txt('2'))
    elif month == z_sign[4]:
        if day < 21:
            print(out_2(z_month[4], symb[4]))
            _output(z_month[4], symb[4], z_txt('2'))
        else:
            print(out_2(z_month[5], symb[5]))
            _output(z_month[5], symb[5], z_txt('3'))
    elif month == z_sign[5]:
        if day < 21:
            print(out_2(z_month[5], symb[5]))
            _output(z_month[5], symb[5], z_txt('3'))
        else:
            print(out_2(z_month[6], symb[6]))
            _output(z_month[6], symb[6], z_txt('4'))
    elif month == z_sign[6]:
        if day < 23:
            print(out_2(z_month[6], symb[6]))
            _output(z_month[6], symb[6], z_txt('4'))
        else:
            print(out_2(z_month[7], symb[7]))
            _output(z_month[7], symb[7], z_txt('5'))
    elif month == z_sign[7]:
        if day < 23:
            print(out_2(z_month[7], symb[7]))
            _output(z_month[7], symb[7], z_txt('5'))
        else:
            print(out_2(z_month[8], symb[8]))
            _output(z_month[8], symb[8], z_txt('6'))
    elif month == z_sign[8]:
        if day < 23:
            print(out_2(z_month[8], symb[8]))
            _output(z_month[8], symb[8], z_txt('6'))
        else:
            print(out_2(z_month[9], symb[9]))
            _output(z_month[9], symb[9], z_txt('7'))
    elif month == z_sign[9]:
        if day < 23:
            print(out_2(z_month[9], symb[9]))
            _output(z_month[9], symb[9], z_txt('7'))
        else:
            print(out_2(z_month[10], symb[10]))
            _output(z_month[10], symb[10], z_txt('8'))
    elif month == z_sign[10]:
        if day < 22:
            print(out_2(z_month[10], symb[10]))
            _output(z_month[10], symb[10], z_txt('8'))
        else:
            print(out_2(z_month[11], symb[11]))
            _output(z_month[11], symb[11], z_txt('9'))
    elif month == z_sign[11]:
        if day < 22:
            print(out_2(z_month[11], symb[11]))
            _output(z_month[11], symb[11], z_txt('9'))
        else:
            print(out_2(z_month[0], symb[0]))
            _output(z_month[0], symb[0], z_txt('10'))

# zodiac list = 12 changed z_month
z_month = ["capricon", "aquarius", "pisces", "aries", 
            "taurus", "gemini", "cancer", "leo", "virgio", 
            "libra", "scorpio", "sagittarius"] 
#z_month now z_sign cos of mistake
z_sign = [
    "january", "february", "march", "april", "may",
    "june", "july", "august", "september", "october",
    "november", "december" #wwwwwwwwwwwwwwwww
]


symb = [
    "♑",  "♒",  "♓",    "♈",    "♉",     "♊",     "♋",       
    "♌",  "♍",   "♎",   "♏",    "♐",      "🌞"
    
    ]
birthday = int(input()) #enter your birthday
#
#if birthday.isalpha() == True:
#   raise Exception "Birthday must be a integer"
birth_month = input().lower() # march, april, december

try:
    print(symb[12]*15,"\n")
    zodiac_sign(birthday, birth_month)
except:
    "Input error, please try again"
finally:
    print("\n"*2)