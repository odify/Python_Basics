import sys, subprocess
try:
    import bs4, requests
except ImportError:
    subprocess.run([sys.executable, "-m", "pip","-q", "install", "bs4", "requests"])
finally:
    import bs4, requests
    
url = "https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Germany"
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, features="html.parser")
a = soup.find(string="Arrival date").next_element.get_text()
b = soup.find(string="Confirmed cases").next_element.get_text()
c = soup.find(string="Recovered").next_element.get_text()
d = soup.find(string="Deaths").next_element.get_text()
info = {"Arrival Date": a, "Confirmed Cases": b, "Recovered": c, "Deaths": d}
for key in info:
    length = len(f"{key}: {info[key]}")
    print(f"{'='*length}\n{key}: {info[key]}")