import serial, time, logging, datetime

#serial_port = serial.Serial('COM6', 9600, timeout=0)

header = ["time", "response"]
start = time.time()
data_file_string = 'RCRSerialListener{}.dat'.format(datetime.datetime.now().strftime("%y_%m_%d_%H_%M"))
data_file = open(data_file_string, "w")
print("Data file initialized.")

def store(info):
    data_file = open(data_file_string, "w")
    data_file.write(info + "\n")
    data_file.close()

def format_and_store(data):
    print(data)
    store(",".join(data))

format_and_store(header)

try:
#       response = serial_port.readline()
    response = "test"
    run_time = time.time() - start
    format_and_store([run_time, response])
    print("Stored:",run_time,response)
except KeyboardInterrupt:
    print("File closed.")
#    except serial_port.SerialTimeoutException:
#        print('Data could not be read.')

data_file.close()
