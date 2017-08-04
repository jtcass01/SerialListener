import datetime

from Serial import Serial
from RCRFile import File

class Analytics():
    """Sample rate analysis"""
    def sr_test(data_file):
        content = data_file.getContent()
        proper_content = list()
        frequency_count = 0
        ceiling = 1
        total_count=0
        average_frequency=float(0)
        frequency_list = list()

        print("content", content)

        print("typeof", type(content))

        for sample in list(content):
            print("sample", sample)
            print("type(sample)", type(sample))
            sample = sample.split(",")
            if sample[0] == "time":
                """Header found : )"""
                pass
            else:
                time = float(sample[0])
                response = str(sample[1])
                proper_content.append([time,response])
                total_count += 1
                if time > ceiling:
                    frequency_list.append([str(ceiling-1), str(ceiling), str(frequency_count)])
                    ceiling += 1
                    if time > ceiling:
                        frequency_count = 0
                    else:
                        frequency_count = 1
                else:
                    frequency_count += 1

        frequency_file = File(file_address='FrequencyFinder{}.dat'.format(datetime.datetime.now().strftime("%y_%m_%d_%H_%M")), header=["start", "stop", "count"])
        for frequency_sample in frequency_list:
            frequency_file.format_and_store(frequency_sample)
        frequency_file.close()

        print("Average frequency: ", total_count / (len(frequency_list)-2))