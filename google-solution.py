import urllib.request
import urllib.parse
import json
import ssl
#from openlocationcode import openlocationcode as olc


serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')

    if len(address) < 1:
        break

    # Build URL
    parms = {}
    parms['q'] = address.strip()

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)

    try:
        request = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0'}
        )

        response = urllib.request.urlopen(request, context=ctx)

        data = response.read().decode()

    except Exception as e:
        print("Error retrieving data:", e)
        break

    print('Retrieved', len(data), 'characters')

    # Parse JSON
    try:
        js = json.loads(data)
    except json.JSONDecodeError:
        print("==== JSON Decode Error ====")
        print(data)
        break

    # Check results
    if 'features' not in js:
        print('==== Download error ====')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        break

    # Extract information
    properties = js['features'][0]['properties']

    lat = properties['lat']
    lon = properties['lon']
    location = properties['formatted']
    plus_code = properties['plus_code']
    


    print('Latitude:', lat)
    print('Longitude:', lon)
    print('Location:', location)
    print("plus Code:", plus_code)