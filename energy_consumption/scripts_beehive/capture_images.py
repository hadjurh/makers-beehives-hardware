import sys
from time import sleep
import picamera

nb_img = int(sys.argv[1])

# PiCamera
try:
    camera = picamera.PiCamera()
except:
    print('Unable to start camera')
    exit(1)

for i in range(nb_img):
    img_title = str(i) + '.jpg'
    # Capture image
    camera.capture(img_title)
    print('>>>> image %d captured' % i)

    sleep(0.5)
