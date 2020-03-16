import socket
from datetime import datetime
from beehive.src.get_sensor_node_data import get_data_from_serial, init_serial
from beehive.src.capture_images import capture_images
from beehive.src.resize_img import resize_img
from beehive.src.convert_img_to_gif import convert_jpg_to_gif
from beehive.src.upload_gif_to_imgur import upload_to_imgur
from beehive.src.upload_data_to_spreadsheet import upload_to_spreadsheet
from beehive.src.git_pull import git_pull

start_time = datetime.now()

hostname = socket.gethostname()
beehive_id = int(hostname[-1])

line_separator = '\n--------------'

serial_data = get_data_from_serial(init_serial())
print(f'serial data,{datetime.now() - start_time}{line_separator}')
prev_time = datetime.now()

nb_img = 20
path_to_img = capture_images(nb_img, resolution=(800, 600))
print(f'capture {nb_img} images,{datetime.now() - prev_time}{line_separator}')
prev_time = datetime.now()

# resize_img(path_to_img)
# print(f'resize images,{datetime.now() - prev_time}{line_separator}')
# prev_time = datetime.now()

path_to_gif_file = convert_jpg_to_gif(path_to_img)
print(f'convert jpg to gif,{datetime.now() - prev_time}{line_separator}')
prev_time = datetime.now()

gif_url = upload_to_imgur(beehive_id, path_to_gif_file)
print(f'upload gif to imgur,{datetime.now() - prev_time}{line_separator}')
prev_time = datetime.now()

upload_to_spreadsheet(beehive_id, str(serial_data), gif_url)
print(f'upload data to spreadsheet,{datetime.now() - prev_time}{line_separator}')
prev_time = datetime.now()

git_pull()
print(f'git pull,{datetime.now() - prev_time}')
