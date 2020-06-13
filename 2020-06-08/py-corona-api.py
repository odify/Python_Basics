# import sys, subprocess
# try:
#     import bs4, requests
# except ImportError:
#     subprocess.run([sys.executable, "-m", "pip","-q", "install", "bs4", "requests"])
# finally:
#     import bs4, requests
    
# url = "https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Germany"
# res = requests.get(url)
# res.raise_for_status()
# soup = bs4.BeautifulSoup(res.text, features="html.parser")
# a = soup.find(string="Arrival date").next_element.get_text()
# b = soup.find(string="Confirmed cases").next_element.get_text()
# c = soup.find(string="Recovered").next_element.get_text()
# d = soup.find(string="Deaths").next_element.get_text()
# info = {"Arrival Date": a, "Confirmed Cases": b, "Recovered": c, "Deaths": d}
# for key in info:
#     length = len(f"{key}: {info[key]}")
#     print(f"{'='*length}\n{key}: {info[key]}")


#2nd:

import pandas as pd 
import numpy as n
from sklearn.metrics import r2_score as rs
import matplotlib.pyplot as p
input = input("Enter country name: ")
inp = input.title()
print(inp)
a = 20
b= 17
case = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/total_cases.csv')
death = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/total_deaths.csv')
ncase = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/new_cases.csv')
ndeath = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/new_deaths.csv')
date = case["date"].dropna().tolist()[-1]
case,wcase = [int(x) for x in case[inp].dropna().tolist()[-a:]],[int(x) for x in case["World"].dropna().tolist()[-a:]]
death,wdeath = [int(x) for x in death[inp].dropna().tolist()[-a:]],[int(x) for x in death["World"].dropna().tolist()[-a:]]
ncase,wncase = [int(x) for x in ncase[inp].dropna().tolist()[-a:]],[int(x) for x in ncase["World"].dropna().tolist()[-a:]]
ndeath,wndeath = [int(x) for x in ndeath[inp].dropna().tolist()[-a:]],[int(x) for x in ndeath["World"].dropna().tolist()[-a:]]
x = list([])
for i in range(1,len(case)+1):
 x.append(i)
trax = x[:b]
trac = case[:b]
tx = x[b:]
tc = case[b:]
trad = death[:b]
td = death[b:]
tranc = ncase[:b]
tnc = ncase[b:]
trand = ndeath[:b]
tnd = ndeath[b:]
trawc = wcase[:b]
twc = wcase[b:]
trawd = wdeath[:b]
twd = wdeath[b:]
trawnc = wncase[:b]
twnc = wncase[b:]
trawnd = wndeath[:b]
twnd = wndeath[b:]
modelc = n.poly1d(n.polyfit(trax,trac,3))
conc = rs(tc,modelc(tx))
modeld = n.poly1d(n.polyfit(trax,trad,3))
cond = rs(td,modeld(tx))
modelnc = n.poly1d(n.polyfit(trax,tranc,3))
connc = rs(tnc,modelnc(tx))
modelnd = n.poly1d(n.polyfit(trax,trand,3))
connd = rs(tnd,modelnd(tx))
modelwc = n.poly1d(n.polyfit(trax,trawc,3))
conwc = rs(twc,modelwc(tx))
modelwd = n.poly1d(n.polyfit(trax,trawd,3))
conwd = rs(twd,modelwd(tx))
modelwnc = n.poly1d(n.polyfit(trax,trawnc,3))
conwnc = rs(twnc,modelwnc(tx))
modelwnd = n.poly1d(n.polyfit(trax,trawnd,3))
conwnd = rs(twnd,modelwnd(tx))
mc = n.poly1d(n.polyfit(x,case,3))
cc = rs(case,mc(x))
md = n.poly1d(n.polyfit(x,death,3))
cd = rs(death,md(x))
mnc = n.poly1d(n.polyfit(x,ncase,3))
cnc = rs(ncase,mnc(x))
mnd = n.poly1d(n.polyfit(x,ndeath,3))
cnd = rs(ndeath,mnd(x))
mwc = n.poly1d(n.polyfit(x,wcase,3))
cwc = rs(wcase,mwc(x))
mwd = n.poly1d(n.polyfit(x,wdeath,3))
cwd = rs(wdeath,mwd(x))
mwnc = n.poly1d(n.polyfit(x,wncase,3))
cwnc = rs(wncase,mwnc(x))
mwnd = n.poly1d(n.polyfit(x,wndeath,3))
cwnd = rs(wndeath,mwnd(x))
print("last updated on %s \n---------------------------------\nIn %s on %s\n\nTotal cases: %d \nTodal deaths: %d \nNew cases: %d \nNew deaths: %d \n------------------------------\nPrediction for next day\n\nTotal cases: %d with %.1f%% confidence \nTotal deaths: %d with %.1f%% conf..\nNew cases: %d with %.1f%% con..\nNew deaths: %d with %.1f%% con..\n\n prediction by model type 2\n\nTotal cases: %d with %.1f%% con..\nTotal deaths: %d with %.1f%% con..\nNew cases: %d with %.1f%% con..\nNew deaths: %d with %.1f%% con..\n------------------------------------------------\n----------------------------------------------------\nfor world on %s\n\nTC: %d \nTD: %d \nNC: %d \nND: %d \n\n Prediction for world on next day\n\nTC: %d  vth %.1f%% con..\nTD: %d  vth %.1f%% con..\nNC: %d  vth %.1f%% con..\nTD: %d  vth %.1f%% con..\n\nSecond model..\n\nTC: %d  vth %.1f%% con..\nTD: %d  vth %.1f%% con..\nNC: %d  vth %.1f%% con..\nND: %d  vth %.1f%% con..\n\n Not sure about correctness of datasets. & The prediction value may differ coz this is not a thing of prediction. \n\n ©SR - 19/4/20"%(date,inp,date,case[-1],death[-1],ncase[-1],ndeath[-1],round(modelc(len(x)+1)),conc*100,round(modeld(len(x)+1)),cond*100,round(modelnc(len(x)+1)),connc*100,round(modelnd(len(x)+1)),connd*100,round(mc(len(x)+1)),cc*100,round(md(len(x)+1)),cd*100,round(mnc(len(x)+1)),cnc*100,round(mnd(len(x)+1)),cnd*100,date,wcase[-1],wdeath[-1],wncase[-1],wndeath[-1],round(modelwc(len(x)+1)),conwc*100,round(modelwd(len(x)+1)),conwd*100,round(modelwnc(len(x)+1)),conwnc*100,round(modelwnd(len(x)+1)),conwnd*100,round(mwc(len(x)+1)),cwc*100,round(mwd(len(x)+1)),cwd*100,round(mwnc(len(x)+1)),cwnc*100,round(mwnd(len(x)+1)),cwnd*100))
#graph not supported on sl
#--graph for input
g = n.linspace(1,len(x)+1,200)
p.scatter(x, case)
p.scatter(x,death)
p.scatter(x,ncase)
p.scatter(x,ndeath)
p.plot(g, mc(g),label='cases in '+inp)
p.plot(g,md(g),label='deaths in '+inp)
p.plot(g, mnc(g),label='new cases in '+inp)
p.plot(g, mnd(g),label='new deaths in '+inp)
p.xlabel('days')
p.ylabel('no. of cases & death')
p.title('ML predicts covid-19 v1.1')
#uncommnt
#graph for worldwide
#p.scatter(x, wcase)
#p.scatter(x,wdeath)
#p.scatter(x,wncase)
#p.scatter(x,wndeath)
#p.plot(g, mwc(g),label='world cases')
#p.plot(g,mwd(g),label='world deaths')
#p.plot(g, mwnc(g),label='world new cases')
#p.plot(g, mwnd(g),label='world new deaths')
p.legend()
p.show()

#END