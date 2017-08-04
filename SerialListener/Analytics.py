from Serial import Serial
from RCRFile import File

class Analytics():
    """Sample rate analysis"""
    def sr_test(data_file):
        content = data_file.getContent()
        proper_content = list()

        print("content", content)

        for sample in list(content):
            print("sample", sample)
            sample = sample.split(",")
            if sample[0] == "time":
                """Header found : )"""
                pass
            else:
                time = int(sample[0])
                response = str(sample[1])
                proper_content.append([time,response])

        for sample in proper_content:
            print(sample)