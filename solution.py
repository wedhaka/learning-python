# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
    
def findPosition(domain, count, position, processed, names): 
    html = urlopen(domain, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    
    if processed == 0 : 
        print('Retrieving:', domain)
        names = names + domain.split("known_by_")[1].split(".html")[0] + " "

    # Retrieve all of the anchor tags
    tags = soup('a')
    i = 1
    for tag in tags :
        if processed == count: 
            #print(names, i)
            break
        
        if i == position : 
            print('Retrieving:', tag.get('href', None))
            names = names + tag.contents[0] + ' '
            processed = processed + 1
            findPosition(tag.get('href', None), count, position, processed, names)
            
        i = i + 1

url = input('Enter - ')
count = input('Enter Count - ')
position = input('Enter Position - ')
processed = 0
names = ''

findPosition(url, int(count), int(position), int(processed), names)