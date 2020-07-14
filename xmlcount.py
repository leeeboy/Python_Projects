import urllib.request, urllib.error, urllib.parse
import ssl
import xml.etree.ElementTree as ET

url = input('Enter location:')
uh=urllib.request.urlopen(url)
data=uh.read()
tree=ET.fromstring(data)
counts=tree.findall('.//count')
total=0
for count in counts:
    value=count.text
    total=total+int(value)
print('Sum:',total)
