# ordered info buses in csv file
from old_scripts.schedule import datetime_SDN
def run():
    FILENAME = 'Pt_locations' + str(datetime_SDN.strftime("%d_%m_%y")) + '.txt'
    locations = open(FILENAME, 'r')

    new = open("traffics/data/commaLocation.txt", 'w')
    content = locations.readlines()
    # countClosed=0
    # countOpen=0
    listEntities = []
    for line in content:
        if 'entity' in line:
            for item in listEntities:
                newstr = item.replace("\n", "")
                newstr = newstr.replace(" ", "")
                new.write(newstr + ',')
            new.write('\n')
            listEntities = []
        if 'trip_id' in line:
            listEntities.append(line)
        elif 'start_time' in line:
            listEntities.append(line)
        elif 'start_date' in line:
            listEntities.append(line)
        elif 'route_id' in line:
            listEntities.append(line)
        elif 'latitude' in line:
            listEntities.append(line)
        elif 'longitude' in line:
            listEntities.append(line)
        elif 'bearing' in line:
            listEntities.append(line)
        elif 'speed' in line:
            listEntities.append(line)

    locations.close()
    new.close()


