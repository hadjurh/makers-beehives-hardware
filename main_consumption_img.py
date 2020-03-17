"""
Routine of images capturing/resizing/aggregating as a GIF
in order to measure current consumption

1- Capture images
    a- number of images varies
    b- size of images varies

2- Resize images
    a- number of images varies
    b- size of input images varies
    c- size of output images varies

3 GIF creation
    a- number of images varies
    b- size of images varies
"""

from datetime import datetime
from beehive.src.capture_images import capture_images

prev_time = datetime.now()
line_separator = '\n--------------'

print('1a', datetime.now().__str__())
for nb_img in [1, 2, 3, 5, 7, 10, 15, 20, 30, 50]:
    path_to_img = capture_images(nb_img, resolution=(800, 600))
    print(f'capture {nb_img} images,{datetime.now() - prev_time}{line_separator}')
    prev_time = datetime.now()

print('1b - resolution parameter', datetime.now().__str__())
for resolution in [(640, 480), (800, 600), (960, 720),
                   (1024, 768), (1280, 960), (1400, 1050),
                   (1440, 1080), (1600, 1200), (1856, 1392),
                   (1920, 1440), (2048, 1536)]:
    nb_img = 20
    path_to_img = capture_images(nb_img, resolution=resolution)
    print(f'capture {nb_img} images,{datetime.now() - prev_time}{line_separator}')
    prev_time = datetime.now()


print('1b - resize parameter', datetime.now().__str__())
for resolution in [(640, 480), (800, 600), (960, 720),
                   (1024, 768), (1280, 960), (1400, 1050),
                   (1440, 1080), (1600, 1200), (1856, 1392),
                   (1920, 1440), (2048, 1536)]:
    nb_img = 20
    path_to_img = capture_images(nb_img, resize=resolution)
    print(f'capture {nb_img} images,{datetime.now() - prev_time}{line_separator}')
    prev_time = datetime.now()
