import requests
import socket

hostname = socket.gethostname()
beehive_id = int(hostname[-1])

# Upload data to spreadsheet
api_endpoint = 'https://script.google.com/macros/s/AKfycbw61xdBYnNVJI7AEDuUay7il1hTATextokstUNsuIy3jjE-vViu/exec'
data = {'beehive_id': beehive_id, 'serial_string': 'Just testing consumption here', 'image_link': 'image_link'}
r = requests.post(url=api_endpoint, data=data)
print('>>>> data uploaded:%s' % r.text)
