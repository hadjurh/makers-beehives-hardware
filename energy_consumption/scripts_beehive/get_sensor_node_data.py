import serial
import json
import time
import datetime

# Init Serial
try:
    ser = serial.Serial('/dev/ttyACM0', 115200)
except:
    try:
        ser = serial.Serial('/dev/ttyACM1', 115200)
    except:
        print('Unable to comunicate with arduino on Serial port')
        exit(1)

while True:
    ser.flush()
    serial_string = ser.readline()
    print('>>>> incoming serial_string: %s' % serial_string)

    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print("[%s]" % timestamp)

    try:
        # Check if incoming data is parsable
        serial_data = json.loads(serial_string)
        print('>>>> parsed serial_data: %s' % serial_data)

        break

    except Exception as e:
        print('>>>> SOMETHING WENT WRONG', str(e))
        print('An exception of type {} occured'.format(type(e).__name__))

        # Shutdown if error is not due to incomplete JSON parsing
        if e.__class__ != ValueError:
            exit(1)
