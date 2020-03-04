import requests

# Upload data to spreadsheet
api_endpoint = 'https://script.google.com/macros/s/AKfycbw61xdBYnNVJI7AEDuUay7il1hTATextokstUNsuIy3jjE-vViu/exec'
data = {'beehive_id': 'BEEHIVE_ID', 'serial_string': 'Just testing consumption here', 'image_link': 'image_link'}
r = requests.post(url=api_endpoint, data=data)
print('>>>> data uploaded:%s' % r.text)
