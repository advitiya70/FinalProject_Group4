import pymysql
import pymysql.cursors
import requests as req
import datetime
print("Batch Process start ....\n\n")
print("Data acquisition start ....\n")
apiKey = "ada9cf8ca86c5de0a0423a4542b9e282"
Loc = {"T": (43.65, -79.38), "V": (49.24, -123.11),
       "O": (45.42, -75.69), "M": (45.50, -73.56), "C": (51.04, -114.07)}
listofrecords = []
print("Loading API credentials ...")
for i in Loc.keys():

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={Loc[i][0]}&lon={Loc[i][1]}&appid={apiKey}"
    print(
        f"prepared url : https://api.openweathermap.org/data/2.5/weather?lat={Loc[i][0]}&lon={Loc[i][1]}&appid=")
    res = req.get(url).json()
    #print(f"Sample response  : {res}")
    # exit(0)
    print("getting data....")
    listofrecords.append(
        f" {str (datetime.datetime.fromtimestamp( res['dt'] )).split (' ') [0].replace('-','')},'{res['name'].replace(' ','')}','{res['weather'][0]['description'].replace(' ','')}','{int (res['main']['temp'])-273}','{res['main']['pressure']}','{res['main']['humidity']}','{res['visibility']}'")
    print(
        f"fetched Data :{str (datetime.datetime.fromtimestamp( res['dt'] )).split (' ') [0].replace('-','')  },{res['name']},{res['weather'][0]['description']},{int (res['main']['temp'])-273},{res['main']['pressure']},{res['main']['humidity']},{res['visibility']}")

print("\nData acquisition end ....\n\n")

print("Data storage start ....\n")
Port = 3306
Endpoint = "finaldatabase.c0rw6uf5mclw.us-east-2.rds.amazonaws.com"
Username = "admin"
Pass = "Python123"
Dbname = "finaldatabase"

con = pymysql.connect(host=Endpoint,
                      user=Username,
                      password=Pass,
                      database=Dbname,
                      cursorclass=pymysql.cursors.DictCursor)
Table = "weatherTable"

clear = f"DROP TABLE IF EXISTS {Table};"
createTable = f"CREATE TABLE IF NOT EXISTS {Table} (date int, city varchar(255), description varchar(255), temperature varchar(255), pressure varchar(255), humidity varchar(255), visibility varchar(255));"
try:

    with con.cursor() as cur:

        cur.execute('SELECT VERSION()')
        version = cur.fetchone()
        print(f'Creating data base connection ...')
        print(f'Checking data base connection ...')
        print(f'Connnection successfull, database version: {version}')
        cur.execute(clear)
        print(f"Creating table if not there : {Table}")
        cur.execute(createTable)
        for c in listofrecords:
            sql = f"INSERT INTO {Table} VALUES ({c});"
            cur.execute(sql)
            print(f"Data row inserted into data base: {c}.")

    con.commit()
    with con.cursor() as cur:

        sql = f"SELECT * from {Table}"
        cur.execute(sql)

        rows = cur.fetchall()

        print(f'Table result : {rows}')
    con.commit()
finally:

    con.close()

print("\nData storage end ....\n\n")
print("Batch Process end ....")
