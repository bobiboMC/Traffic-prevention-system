import csv
import json
import os
from datetime import timedelta, datetime

import pandas as pd

f1=open("traffics/data/traffics_hours.json","r")#traffics/data/
traffics_hours=json.loads(f1.readline())
print(traffics_hours)
f2=open("traffics/data/times and traffics.csv","w")#traffics/data/
csv_writer=csv.writer(f2)

FMT = '%H:%M'
def closest_time(time,times):
    dt=datetime.strptime(time,FMT)
    time_between=timedelta(minutes=50)
    for five_min in times:
        dt1=datetime.strptime(five_min,FMT)
        if dt-dt1<time_between:
            time_between=dt-dt1

time=datetime.strptime("4:00",FMT)
times=[]
while time<datetime.strptime("10:00",FMT):
    times.append(time.strftime(FMT))
    time+=timedelta(minutes=5)

def get_road(trip_num, trips_roads, watching, value):
    watching_time = json.dumps(watching.split(" ")[1])
    if trip_num not in trips_roads:
        trips_roads[trip_num] = {  # "start_hour":watching_time,
            "roads": [json.dumps([value, watching_time])]}
    else:
        if trips_roads[trip_num]["roads"][
            len(trips_roads[trip_num]["roads"]) - 1][1] != watching_time \
                and trips_roads[trip_num]["roads"][
            len(trips_roads[trip_num]["roads"]) - 1][0] == value:
            if len(trips_roads[trip_num]["roads"][
                       len(trips_roads[trip_num]["roads"]) - 1]) == 2:
                trips_roads[trip_num]["roads"][
                    len(trips_roads[trip_num]["roads"]) - 1].append(watching_time)#already dumpsed
            else:
                trips_roads[trip_num]["roads"][
                    len(trips_roads[trip_num]["roads"]) - 1][2]=watching_time #already dumpsed
            #אם הכביש שונה, אז במידה שגם השעה המדויקת שונה, מוסיפים למער את השעה המדויקת, אם הכביש אחר, מוסיפים מערך חדש
        if trips_roads[trip_num]["roads"][
            len(trips_roads[trip_num]["roads"]) - 1][0] != value:
            trips_roads[trip_num]["roads"].append(json.dumps([value, watching_time]))
        trips_roads[trip_num]["end_hour"] = watching_time#already dumpsed
    # trips_roads[trip_num]['end_hour'] = watching_time

directory = r'C:\Users\Ronit.Iconics\PycharmProjects\djangoProject1\traffics\data\trips_coordinates'  # taking all what we have' no need to match every time
#

FMT = '%H:%M'


def closest_time(time, times):
    closest_ti = ""
    dt_given = datetime.strptime(time, FMT)
    time_between = timedelta(minutes=50)
    for five_min in times:
        current_five_min = datetime.strptime(five_min, FMT)
        if abs(current_five_min - dt_given) < time_between:
            time_between = dt_given - current_five_min
            closest_ti = current_five_min
    return str(datetime.strftime(closest_ti, FMT))


time = datetime.strptime("4:00", FMT)
times = []
while time < datetime.strptime("10:00", FMT):
    times.append(time.strftime(FMT))
    time += timedelta(minutes=5)

with open("traffics/data/traffics_hours.json", "r") as f:
    traffics = json.loads(f.readline())

def run():
    df2 = pd.read_csv("csvFile_1.csv", error_bad_lines=False)
    points = []
    trips_roads = {}

    f = open("roads_points3.csv", 'a', newline='')
    csv_f1 = csv.writer(f)
    # csv_f1.writerow(['road','point'])

    # csv_file.close()
    # for
    with open("roads_points3.csv") as csv_file:  # traffics/data/
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)
        print(rows)
    for filename in os.listdir(directory):
        df = pd.read_csv('trips_coordinates/' + filename, error_bad_lines=False)
        for index, instance in df.iterrows():
            if [instance['road'], str(instance['latitude']) + ',' + str(instance['longitude'])] not in rows:
                csv_f1.writerow([instance['road'], str(instance['latitude']) + ',' + str(instance['longitude'])])
    csv_file.close()

    df1 = pd.read_csv("roads_points3.csv", encoding='cp1252', error_bad_lines=False)
    for index, instance in df1.iterrows():
        # if instance['point'] not in points:
        points.append(instance['point'])
    with open("roads_points3.csv") as csv_file:  # traffics/data/
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)
        print(rows)
    for index, instance in df2.iterrows():
        # datetime.strptime(instance['watching_time'], "%d/%m/%y %H:%M") < datetime.now() + timedelta(
        #         minutes=15)].itterrows()]:
        try:
            # if datetime.strptime(instance['watching_time'], "%d/%m/%y %H:%M") < \
            #         datetime.strptime("13/09/21 04:00", "%d/%m/%y %H:%M") + timedelta(
            #     hours=2):
            point = str(instance['latitude']) + ',' + str(instance['longitude'])
            # if point in points:
            get_road(trip_num=str(instance["trip_id"]), trips_roads=trips_roads, watching=instance["watching_time"],
                     value=json.dumps(rows[points.index(point)][0]))
            print(instance["trip_id"], point, rows[points.index(point)][0])
            #     get_road(trip_num=instance['trip_id'],trips_roads=trips_roads,watching=instance['watching_time'],value="unknown")
        except:
            print(instance['watching_time'])

    f=open("traffics_and_hours_road.csv","w",newline='')
    csv_f=csv.writer(f)
    # for trip_road in trips_roads:
    #     for road in trips_roads[trip_road]['road']:
    #         csv_f.writerow([trips_roads[trip_road]['road']]+[])#traffics[closest_time(trips_roads[trip_road]['road'][1]
    #         #,times)]

    for trip in trips_roads:
        for road in trips_roads[trip]['roads']:
            if road[0] in traffics:
                try:
                    csv_f.writerow(road+[traffics[road[0]][closest_time(road[1],times)]])
                except:
                    csv_f.writerow(road+[traffics[road[0]][closest_time(
                        (datetime.strptime(road[1],FMT)+timedelta(minutes=5)).strftime(FMT), times)]])
    # trips_roads=json.dumps(trips_roads)
    # with open('trips_roads_times.json', 'w', encoding='utf-8') as g:
    #     g.write(trips_roads)
if __name__ == "__main__":
    run()

    # for index, instance in df.iterrows():
    #    try:
    #     points.append([float(instance['point'].split(',')[0]), float(instance['point'].split(',')[1])])
    #     #thats for the index of each point
    #     # point_time[[float(instance['point'].split(',')[0]), float(instance['point'].split(',')[1])]] = \
    #     #     instance['watched_time']
    #     print("point: ",instance["point"])
    #    except:
    #        print(instance['road'])
    # ("CSVs/roads_points2.csv")

# print([instance['road'], str(instance['latitude']) + ',' + str(instance['longitude'])])
# points.append([instance['latitude'],instance['longitude']])


    # print(instance['road'])

    # f.close()
    # for row in csv_reader:
    # f.close()

# print(routes[element]['startpoint']in points)
# for point in routes[element]['interpoints']:
#     if point in points:
#         if element not in trips_roads:
#             trips_roads[element] = [rows[points.index(point)][0]]
#         else:
#             if trips_roads[element][len(trips_roads[element]) - 1] != rows[points.index(point)][0]:
#                 trips_roads[element].append(rows[points.index(point)][0])