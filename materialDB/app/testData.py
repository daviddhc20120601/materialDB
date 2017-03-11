import pandas as pd
import numpy as np
import mysql.connector
import getData
import matplotlib.pyplot as plt
###connect to mysql
from sqlalchemy import create_engine
engine=create_engine("mysql+mysqldb://root:toor@localhost/materialDB",echo=False)
#connect=engine.connect()

#engine=mysql.connector.connect(user="root",password="toor",host="127.0.0.1",port="3306",database="materialDB")

s=pd.DataFrame({"name":["chenhaidong","xuchangong"]*10,"id":[i*200+1 for i in range(20)]})
#print s

s.to_sql(name="test",con=engine,if_exists="replace",index=False)

s=pd.read_sql("select * from test",engine)

ax=s.plot()
fig=ax.get_figure()
plt.show()
fig.savefig("figure.png")
print s.to_html()

print "==================="
 
print getData.getDataMysql("select * from test")
