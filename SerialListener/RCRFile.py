import datetime, logging, time

class File(object):
    def __init__(self, file_address='RCRSerialListener{}.dat'.format(datetime.datetime.now().strftime("%y_%m_%d_%H_%M")), header=["time", "response"]):
        self.file = open(file_address, "w")
        time.sleep(1)
        self.file.close()
        time.sleep(1)

        self.address = file_address
        self.file = open(file_address, "r+")
        self.file.write(",".join(header) + "\n")
        print("Data file: \"" + file_address + "\" has been initialized")

    def getFile(self):
        return self.file

    def store(self, info):
        self.file.write(info + "\n")

    def format_and_store(self, data):
        self.store(",".join(data))

    def getContent(self):
        self.file.seek(0,0)
        content = list()

        for line in self.file:
            content.append(str(line))

        return content

    def close(self):
        self.file.close()
        print(self.address + " has been closed.")