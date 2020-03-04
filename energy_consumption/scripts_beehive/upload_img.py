import pyimgur
import json
import socket
import time
import datetime

hostname = socket.gethostname()
beehive_id = int(hostname[-1])

# Imgur
image_link = ""
IMGUR_CLIENT_ID = ""
with open('imgur_credits.json') as imgur_credits_file:
    imgur_credits = json.load(imgur_credits_file)
    imgur_client_id = imgur_credits['imgurClientID']

ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

imgur = pyimgur.Imgur(imgur_client_id)
image_title = 'MakersBeehive ' + str(beehive_id) + ' | ' + timestamp
uploaded_image = imgur.upload_image('capture.gif', title=image_title)
image_link = uploaded_image.link
print('>>>> image uploaded at %s' % image_link)
