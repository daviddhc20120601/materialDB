import pandas as pd
import numpy as np
import mysql.connector

def getDataMysql(yourQuery):

	###connect to mysql
	from sqlalchemy import create_engine
	engine=create_engine("mysql+mysqldb://root:toor@localhost:3306/materialDB",echo=False)
	try:
		s=pd.read_sql(yourQuery,engine)
		print s
	except:
		return 'there is an error'
	return s.to_html()

