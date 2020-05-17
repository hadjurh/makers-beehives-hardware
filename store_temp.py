from subprocess import call
from time import time, sleep
import sys

if __name__ == '__main__':
	while True:
		sys.stdout = open('room_temp.out', 'a')
		call(['vcgencmd', 'measure_temp'], stdout=sys.stdout)
		print(str(time()))
		print('')			
		sleep(0.5)
