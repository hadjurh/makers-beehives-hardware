from subprocess import call


# https://imagemagick.org/script/mogrify.php
def resize_img(path_to_img='beehive/data/pi_img'):
    call(['mogrify', '-resize', '800x600', f'{path_to_img}/*.jpg'])
    print('>>>> images resized')


if __name__ == '__main__':
    resize_img()
