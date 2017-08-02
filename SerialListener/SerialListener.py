import serial, time

serial_port = serial.Serial('COM6', 9600, timeout=0)

while True:
    try:
        print(serial_port.readline())
    except serial_port.SerialTimeoutException:
        print('Data could not be read.')