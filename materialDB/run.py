#!flask/bin/python
from app import app
from getIp import getIp
import os
os.system("service mysql restart")
app.run(debug = False,host=getIp(),port=5001)

