from subprocess import call


# Doc: https://imagemagick.org/Usage/anim_basics/
def convert_jpg_to_gif(path_to_img='beehive/data/pi_img', path_to_gif='beehive/data/gif', gif_name='capture.gif'):
    path_to_gif_file = f'{path_to_gif}/{gif_name}'
    call(['convert', '-delay', '25', '-loop', '0', f'{path_to_img}/*.jpg', path_to_gif_file])
    print('>>>> gif created')
    return path_to_gif_file


if __name__ == '__main__':
    convert_jpg_to_gif()
