import csv
import pandas as pd

df=pd.read_csv("full_data_roads.csv",error_bad_lines=False)
# df1=pd.read_csv("count_cars_in_range.csv",error_bad_lines=False)
if __name__=="__main__":
    # rows,rows1=[],[]
    # count_cars=open("count_cars_in_range.csv") # traffics/data/
    # csv_reader = csv.reader(count_cars)
    # rows = list(csv_reader)

    count_cars, full_data = open("count_cars_in_range.csv"), open("full_data_roads.csv")  # traffics/data/
    csv_reader,csv_reader1 = csv.reader(count_cars),csv.reader(full_data)
    count_cars_rows, full_data_rows = list(csv_reader), list(csv_reader1)
    full_data_rows.remove(full_data_rows[0])
    count_cars_rows.remove(count_cars_rows[0])
    roads=[]
    new_file=[]
    for index,instance in df.iterrows():
        roads.append(instance['road'])
    # print(rows1)
    # print("\nrows:\n", rows)
    # print("\nroads:\n",roads)
    for row in count_cars_rows:
        if row[1] in roads:
            traffic=float(row[2])/float(full_data_rows[roads.index(row[1])][5])
            print(float(row[2]),float(full_data_rows[roads.index(row[1])][5]))
            new_file.append([row[0],row[2]] + full_data_rows[roads.index(row[1])][2:]+[traffic])#road name not duplicate, and without indexes
            print(row + full_data_rows[roads.index(row[1])])
    # print(new_file)
    f=open('traffics/data/traffic_viewed.csv','w',newline='')#traffics/data/
    csv_r=csv.writer(f)
    csv_r.writerow(['hour','cars_counted','road','cars_free','cars_busy','cars_very_busy','speed_free','speed_busy','speed_very_busy','traffic'])
    csv_r.writerows(new_file)