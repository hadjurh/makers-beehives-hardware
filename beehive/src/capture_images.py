import sys
from time import sleep
import datetime
import picamera


# Makersbeehive v2: without resize parameter
# Possible optimization: with resize parameter, "it is considerably more efficient
# to have the Pi’s GPU perform the resizing when capturing the image".
# https://picamera.readthedocs.io/en/release-1.13/recipes1.html#capturing-resized-images
def capture_images(nb_img=20, path_to_img='beehive/data/pi_img', resize=None):
    # Init
    camera = picamera.PiCamera()

    # Capture
    for i in range(nb_img):
        img_path = f'{path_to_img}/{datetime.datetime.now().__str__()}.jpg'
        camera.capture(img_path) if resize is None else camera.capture(img_path, resize=resize)
        print(f'>>>> image {i} captured')
        sleep(0.5)

    return path_to_img


if __name__ == '__main__':
    nb_images = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    capture_images(nb_images)
