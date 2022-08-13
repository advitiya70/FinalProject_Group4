import pymysql
import pymysql.cursors


def getreport(v=True):
    rows = None
    print("accessing DataBase start ....\n")
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

    try:

        with con.cursor() as cur:
            print("fetching data from database..")
            sql = f"SELECT * from {Table}"
            cur.execute(sql)

            rows = cur.fetchall()

            print(f'Table result : {rows}')

        con.commit()
    finally:

        con.close()
    if (v):
        li = [[k[i] for i in k.keys()] for k in rows]
        # print(li)
        return li
    return rows


#
# getreport()
