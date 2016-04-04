import pymysql

conn = pymysql.connect(user='root', passwd='root',
                 host='localhost', db='zjctest')
cur = conn.cursor()
cur.execute("SELECT * FROM LAGOU")
for r in cur:
      print("row_number:" , (cur.rownumber) )
      print("id:"+str(r[0])+"name:"+str(r[1])+"age:"+str(r[2]))
cur.close()
conn.close()