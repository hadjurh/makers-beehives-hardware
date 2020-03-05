import serial
import json
import datetime


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


def get_data_from_serial(ser):
    while True:
        ser.flush()
        serial_string = ser.readline()
        print('>>>> incoming serial_string: %s' % serial_string)
        print(datetime.datetime.now().__str__()[:-7])

        try:
            # Check if incoming data is parsable
            serial_data = json.loads(serial_string)
            print('>>>> parsed serial_data: %s' % serial_data)

            break

        except ValueError as e:
            print('>>>> SOMETHING WENT WRONG', str(e))
            print('An exception of type {} occured'.format(type(e).__name__))

    return serial


if __name__ == '__main__':
    ser = init_serial()
    print(get_data_from_serial(ser))
