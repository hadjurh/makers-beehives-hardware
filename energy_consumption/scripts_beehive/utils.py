import serial


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
