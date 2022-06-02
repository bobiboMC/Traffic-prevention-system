# ordered info buses in csv file without description in field
import csv
import json
import time
from datetime import datetime

import pytz

import buses_request_page
import entities_to_csv_file
from old_scripts.schedule import right_time

locations = open("traffics/data/commaLocation.txt", 'r')#traffics/data/
content = locations.readlines()
# new = open("csvFile.txt", 'a')
# csv_f = csv.writer(new)
# except:
new = open("traffics/data/csvFile_1.txt", 'w')
new.write('trip_id,start_time,start_date,route_id,latitude,longitude,bearing,speed,watching_time\n')


if __name__ == '__main__':
    flag = 1
    while flag == 1:
        tz_SDN = pytz.timezone('Australia/Sydney')
        datetime_SDN = datetime.now(tz_SDN)
        if right_time(timeZone=tz_SDN, start_hour=4, end_hour=10, minutes=1,seconds=6):
            try:
                buses_request_page.run()
                entities_to_csv_file.run()
                locations = open("commaLocation.txt", 'r')
                content = locations.readlines()

                listEntities = []
                # i = 0
                for line in content:
                    listEntities = []
                    split_words = line.split(",")
                    for word in split_words:
                        if word != '\n':
                            pos = word.index(":")
                            new_word = word[pos + 1:]
                            listEntities.append(new_word)
                    if len(listEntities) == 8:
                        for part in listEntities:
                            new.write(part + ',')
                        new.write(str(datetime_SDN.strftime("%d/%m/%y %H:%M")) + '\n')
                    print(datetime_SDN.strftime('%H:%M:%S'))
                time.sleep(0.7)
                        # csv_f.writerow(listEntities+[str(datetime_SDN.strftime("%d/%m/%y %H:%M"))])
            except:
                print('expired')

        if str(datetime_SDN.strftime("H")) == '10':
            flag = 5 #to finish the loop
            locations.close()
            new.close()
