import os


def git_pull():
    os.system('cd /home/bee/makers-beehives-hardware-current-measures && git pull')


if __name__ == '__main__':
    git_pull()
