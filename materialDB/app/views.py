# -*-coding=utf-8 -*-

from flask import render_template,request,url_for,redirect
from app import app
from getData import getDataMysql
from getImg import simple
from getIp import getIp

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/extends')
def extends():
 
    user = { 'nickname': 'Miguel' } # fake user
    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'wang jun' },
            'body': 'welcome to material physics!'
        },
        {
            'author': { 'nickname': 'haidong chen' },
            'body': 'welcome, this is created by me!'
        },
	{
            'author': { 'nickname': 'david' },
            'body': 'hello!'
        }
	
    ]
    return render_template("extends.html",
        title = 'Home',
        user = user,
        posts = posts)

@app.route("/showTerminal")
def showTerminal():
	return render_template("terminal.html",ip=getIp())

def success(someText,result,imgSrc):
	return '<h2>your request is:</h2></br>%s</br><h2>result is:</h2></br></br> %s<br>your image is:<br> <img src=%s>'%(someText,result,imgSrc)

def image():
	return simple()

@app.route('/reply',methods=['POST','GET'])
def reply():
	if request.method=='POST':
		youAsk=request.form['name']
		return render_template("reply.html",
		yourRequest=youAsk,
		result=getDataMysql(youAsk),
		imageResult=image() )

		#return success(youAsk,getDataMysql(youAsk),"static/figure.png")  
		#redirect(url_for('success',someText=userName,result=getDataMysql()))
	else:
		youAsk=request.args.get("name")
		return "error while handling %s"%youAsk
		#return success(youAsk,getDataMysql(youAsk),"static/figure.png")
		#return redirect(url_for('success',someText=userName,result=getDataMysql()))

