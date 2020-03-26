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
from time import sleep
from beehive.src.capture_images import capture_images

line_separator = '\n--------------'
resolution_4_3_list = [(640, 480), (800, 600), (960, 720),
                       (1024, 768), (1280, 960), (1400, 1050),
                       (1440, 1080), (1600, 1200), (1856, 1392),
                       (1920, 1440), (2048, 1536), (2592, 1944)]


def compare_nb_img():
    print("duration,nb_img")
    prev_time = datetime.now()
    for nb_img in [1, 2, 3, 5, 7, 10, 15, 20, 30, 50]:
        capture_images(nb_img, resolution=(800, 600))
        print(f'{datetime.now() - prev_time},{nb_img}')
        prev_time = datetime.now()


def compare_resolution_param(nb_img=20):
    print("duration,pixels")
    prev_time = datetime.now()
    for resolution in resolution_4_3_list:
        capture_images(nb_img, resolution=resolution)
        print(f'{datetime.now() - prev_time},{resolution[0] * resolution[1]}')
        prev_time = datetime.now()


def compare_resize_param(nb_img=20):
    prev_time = datetime.now()
    for resolution in resolution_4_3_list:
        capture_images(nb_img, resize=resolution)
        print(f'capture {nb_img} images,{datetime.now() - prev_time}{line_separator}')
        prev_time = datetime.now()


if __name__ == '__main__':
    '''1st analysis'''
    # print('1a', datetime.now().__str__())
    # compare_nb_img()
    # sleep(10)
    # print('1b - resolution parameter', datetime.now().__str__())
    # compare_resolution_param()
    # sleep(10)
    # print('1c - resize parameter', datetime.now().__str__())
    # compare_resize_param()

    '''2nd analysis'''
    compare_nb_img()
