from urllib.request import urlopen

link = "https://github.com/odify"

link = urlopen(link)
source_code = link.read().decode()

print(source_code)