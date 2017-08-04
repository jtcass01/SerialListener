import serial, time
from RCRFile import File

class Serial(object):
    def __init__(self, port_address):
        self.port_address = port_address
        self.serial_port = serial.Serial(port_address, 9600, timeout=0.1)

        """listen()
        Description: Opens the serial port for listening. Ctrl-C ends listen
        Parameters: data_file, start_time"""
    def listen_and_log(self, data_file, start_time=time.time()):
        try:
            while True:
                response = str(self.serial_port.readline())
                run_time = str(time.time() - start_time)
                try:
                    data_file.format_and_store([run_time, response])
                finally:
                    print("Stored:",run_time,response)
        except KeyboardInterrupt:
            print("Please interrupt again.")
            pass