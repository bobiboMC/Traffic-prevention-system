import os
import pandas as pd
# import requests
import csv
import math

from traffics.data.old_scripts.schedule import try_except_next, read_routing_point_api_data

keys = ["JFF6W4ZnqWnNSJarr8RsiTP4GeqCkJND", "fN1GFcLNR2Jd0oYxrQrhpqOTpeGAq9YM",
        "CwMysQRumeK8JZ9JG9WVdGIaixZY5ohR",
        "19TxtGiVQdQhRqPlVGhc2fzVI3WB3AUc"]
f = open('CSVs/roads_points.csv', 'w', encoding="utf-8", newline='')  # traffics/data/
g = open("CSVs/roads_length_capacity.csv", 'a', encoding='utf-8', newline='')

csv_f1 = csv.writer(f)
csv_f2 = csv.writer(g)
directory = r'C:\Users\Ronit.Iconics\PycharmProjects\djangoProject1\traffics\data\trips_coordinates'  # taking all what we have' no need to match every time
def if_then_write():
    if instance['road'] not in roads['points'] or (
            instance['road'] in roads['points'] and instance['point']
            not in roads['points'][instance['road']]):  #
        for point in data['routes'][0]['legs'][0]['points']:
            csv_f1.writerow([instance['road'], str(point['latitude']) + "," + str(point['longitude'])])
        print("  ", instance['road'])
    length = data['routes'][0]['legs'][0]['summary']['lengthInMeters']
    if instance['road'] not in roads['lengths']:
        capac = int(length / 1.95)
        csv_f2.writerow([instance['road'], length, capac])
        print(length, instance['road'])

if __name__ == '__main__':

    df2 = pd.read_csv("traffics/data/trips google maps.csv", error_bad_lines=False)
    df = pd.read_csv("traffics/data/free_busy_very_busy.csv", error_bad_lines=False)
    roads = {'lengths': {}, 'points': {}}
    df3=pd.read_csv("traffics/data/old_csv's/edges.csv", error_bad_lines=False)

    for index, instance in df3.iterrows():
        if instance['road'] in []:
            orig = instance['origin'].replace(" ", "")
            des = instance['destination'].replace(" ", "")
            print(instance['road'])

            # path = "https://api.tomtom.com/routing/1/calculateRoute/" + orig + ":" + des + "/json?&key=CwMysQRumeK8JZ9JG9WVdGIaixZY5ohR"
            response = try_except_next(array=keys,params=[orig,des],i=0,func=read_routing_point_api_data)
            coords1 = []
            for point in response.json()['routes'][0]['legs'][0]['points']:
                value=str(point['latitude']) + "," + str(point['longitude'])
                csv_f1.writerow([instance['road'],value])
                if instance['road'] not in roads['points']:
                            roads['points'][instance['road']] = []
                roads['points'][instance['road']].append(value)
    points = []
    for index, instance in df2.iterrows():
        points.append(str(instance['latitude']) + "," + str(instance['longitude']))
        if index % 2 == 1:
            print(instance['road'])
            data = try_except_next(array=keys, params=points, func=read_routing_point_api_data, i=0)
            try:
                if_then_write()
            except:
                print(instance['road'])
            points = []

    for index,instance in df.iterrows():
        for i in range(1, 9):
            indexes = 'point' + str(i), 'point' + str(i + 1)
            try:
                if math.isnan(instance[indexes[0]]) or math.isnan(
                        instance[indexes[1]]):  # if the cell got a value it goes to the except
                    break
            except:
                points = [instance[indexes[0]], instance[indexes[1]]]
                data = try_except_next(array=keys, params=points, func=read_routing_point_api_data, i=0)
                try:
                    if_then_write()
                except:
                    print(instance['road'])
# df1=pd.read_csv('CSVs/roads_points2.csv',error_bad_lines=False)
# roads=[]
# for index,instance in df1.iterrows():
#     if instance['road'] not in roads:
#         roads.append([instance['road']])
# os.rename(directory + "/" + filename, directory + "/" + filename.replace('.txt', '.csv'))


    # for elem_file in (
    # [["CSVs/roads_length_capacity.csv", 'lengths', 'utf-8'], ['CSVs/roads_points2.csv', 'points', 'cp1252']]):  #
    #     df3 = pd.read_csv(elem_file[0], error_bad_lines=False, encoding=elem_file[2])
    #
    #     for index, instance in df3.iterrows():
    #         if instance['road'] not in roads[elem_file[1]]:
    #             roads[elem_file[1]][instance['road']] = []
    #         roads[elem_file[1]][instance['road']].append(instance[elem_file[1].replace('s', '')])
    #     print(elem_file[1], ':', roads[elem_file[1]])


    # for filename in os.listdir(directory):
    #     df = pd.read_csv('trips_coordinates/' + filename, error_bad_lines=False)
    #     for index, instance in df.iterrows():
    #         # if instance['road'] not in roads:
    #         csv_f1.writerow([instance['road'], str(instance['latitude']) + ',' + str(instance['longitude'])])