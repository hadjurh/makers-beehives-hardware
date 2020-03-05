import requests


def upload_to_spreadsheet(beehive_id, serial_string='No Data', image_link='No Link'):
    api_endpoint = 'https://script.google.com/macros/s/AKfycbw61xdBYnNVJI7AEDuUay7il1hTATextokstUNsuIy3jjE-vViu/exec'
    data = {'beehive_id': beehive_id, 'serial_string': serial_string, 'image_link': image_link}
    r = requests.post(url=api_endpoint, data=data)
    print(f'>>>> data uploaded: {r.text}')


if __name__ == '__main__':
    import socket
    hostname = socket.gethostname()
    beehive_id = int(hostname[-1])

    upload_to_spreadsheet(beehive_id)
