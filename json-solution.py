import json
import urllib.request

#data = '''
#[
#  { "id" : "001",
#    "x" : "2",
#    "name" : "Chuck"
#  } ,
#  { "id" : "009",
#    "x" : "7",
#    "name" : "Brent"
#  }
#]'''


url = input('Enter - ')
print('Retrieving', url)

response = urllib.request.urlopen(url)
data = response.read().decode()
info = json.loads(data)
#print(data)

info = json.loads(data)

count = 0
for item in info["comments"]:
    #print('Name', item['name'])
    #print('Id', item['id'])
    #print('Attribute', item['count'])
    count = count + item['count']
    
print('User count:', len(info["comments"]))
print(count)