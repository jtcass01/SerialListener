from Serial import Serial
from RCRFile import File

#Don't forget to update the serial port location!!
serial_port = Serial('COM8')

header = ["time", "response"]

data_file = File(header=header)

serial_port.listen_and_log(data_file)

data_file.close()