import serial
import time
import datetime


def get_timestamp():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return st


def init_serial():
    # Init Serial
    try:
        ser = serial.Serial('/dev/ttyACM0', 115200)
    except:
        try:
            ser = serial.Serial('/dev/ttyACM1', 115200)
        except:
            print('Unable to comunicate with arduino on Serial port')
            exit(1)

    return ser
