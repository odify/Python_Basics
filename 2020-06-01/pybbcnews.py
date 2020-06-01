# LATEST BBC NEWS CHECKER

import urllib.request as RE
import xml.etree.ElementTree as ET

url = 'http://feeds.bbci.co.uk/news/rss.xml?edition=de#'
data = RE.urlopen (url).read()
tree = ET.fromstring(data)

print ('This are the latest News at the BBC:\n')

for i in tree.iter('item'):
    print ('{}\n{}\n'.format(i.find('title').text, i.find('description').text))

#END