import pyimgur
import json
import datetime


# https://github.com/Damgaard/PyImgur#uploading-an-image
def upload_to_imgur(beehive_id, imgur_cred_path='imgur_credits.json', path_to_file='beehive/data/gif/capture.gif'):
    with open(imgur_cred_path) as imgur_credits_file:
        imgur_credits = json.load(imgur_credits_file)

    imgur = pyimgur.Imgur(imgur_credits['imgurClientID'])
    image_title = 'MakersBeehive ' + str(beehive_id) + ' | ' + datetime.datetime.now().__str__()[:-7]
    uploaded_image = imgur.upload_image(path_to_file, title=image_title)
    image_link = uploaded_image.link
    print(f'>>>> image/gif uploaded at {image_link}')

    return image_link


if __name__ == '__main__':
    import socket
    hostname = socket.gethostname()
    beehive_id = int(hostname[-1])

    upload_to_imgur(beehive_id)
