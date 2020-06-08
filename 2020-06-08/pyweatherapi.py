# Weather API (LONDON)
import sys, subprocess



def package(p):
    subprocess.run([sys.executable, "-m", "pip", "-q", "install", p])

package("requests")
import requests, json, pprint as pp
url = "https://samples.openweathermap.org/data/2.5/weather?q=London,uk&callback=test&appid=439d4b804bc8187953eb36d2a8c26a02"

response = requests.get(url)
response.raise_for_status()

jsonText = response.text

li = list(jsonText)

del li[:5]
del li[-1]
conStr = "".join(li)

pyVal = json.loads(conStr)
pp.pprint(pyVal)