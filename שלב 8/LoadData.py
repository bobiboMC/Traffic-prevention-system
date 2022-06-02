import pyodbc as sql
import pandas as pd
cs="""Driver={SQL Server};Server=RONIT\SQLEXPRESS;Database=test;"""
# sql.connect("Data Source=.\\SQLExpress;Database=test;Trusted_Connection=true;MultipleActiveResultSets=True;")
if __name__=="__main__":
 # print(sql.drivers())
 conn=sql.connect(cs)
 cur=conn.cursor()
 # cur.execute("INSERT INTO [test].[dbo].[Games] VALUES('real madrid','liverpool')")
 cur.execute("""CREATE TABLE [test].[dbo].[occupancy](
   road      VARCHAR(43) NOT NULL PRIMARY KEY
  ,hour      VARCHAR(43) NOT NULL
  ,cars_counted  VARCHAR(43) NOT NULL
  ,very_busy INTEGER  NOT NULL
  ,busy      INTEGER  NOT NULL
  ,free      INTEGER  NOT NULL);""")
 cur.commit()
 df=pd.read_csv("traffics/data/traffic_viewed.csv",error_bad_lines=False)
 for index,instance in df.iterrows():
     cur.execute("""INSERT INTO [test].[dbo].[occupancy](road,very_busy,busy,free) VALUES """)
 # cur.execute("UPDATE [test].[dbo].[Games] SET id=6 WHERE id=10")

 rows=cur
 for row in rows:
     print(row)