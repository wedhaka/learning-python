# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# or pip install beautifulsoup4 to ensure you have the latest version
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl # defaults to certificate verification and most secure protocol (now TLS)

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = input('Enter Count - ')
position = input('Enter Position - ')

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
i = 1
for tag in tags:
    if int(position) == i:
        print(tag.get('href', None))
        ihtml = urllib.request.urlopen(url, context=ctx).read()
        isoup = BeautifulSoup(html, 'html.parser')
    i = i + 1
    
    ihtml = urllib.request.urlopen(url, context=ctx).read()
    isoup = BeautifulSoup(html, 'html.parser')
    itags = isoup("a")
    y = 1
    for itag in itags: 
        if int(position) == i:
            print(tag.get('href', None))
            ihtml = urllib.request.urlopen(url, context=ctx).read()
            isoup = BeautifulSoup(html, 'html.parser')
        y = y + 1