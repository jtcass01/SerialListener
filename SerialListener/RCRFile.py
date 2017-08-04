import datetime, logging

class File(object):
    def __init__(self, file_address='RCRSerialListener{}.dat'.format(datetime.datetime.now().strftime("%y_%m_%d_%H_%M")), header=["time", "response"]):
        self.file = open(file_address, "w")
        self.file.write(",".join(header) + "\n")
        print("Data file " + file_address + " has been initialized")

    def getFile(self):
        return self.file

    def store(self, info):
        self.file.write(info + "\n")

    def format_and_store(self, data):
        self.store(",".join(data))

    def close():
        self.file.close()