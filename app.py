from math import nan
from types import CodeType
from flask import *
app=Flask(__name__)
app.config["JSON_AS_ASCII"]=False
app.config["TEMPLATES_AUTO_RELOAD"]=True

app = Flask(__name__,static_folder="static",static_url_path="/")
app.config['SECRET_KEY'] = 'ricetia'

# import mysql.connector
import pymysql.cursors
import pymysql
# datatime
import datetime

@app.route("/")
def index():
	return render_template("index.html")
@app.route("/menu")
def menu():
	return render_template("menu.html")
@app.route("/count")
def count():
	return render_template("count.html")
@app.route("/work")
def work():
	return render_template("work.html")

@app.route("/works",methods=['POST'])
def POSTwork():
	ordercode = request.data.decode('utf-8')
	ordercode = json.loads(ordercode)
	ordercode = ordercode["ok"]

	signup = pymysql.connect(
		host='ricetia-mysql.cyb5eosysjkk.ap-northeast-1.rds.amazonaws.com',
		port=3306,
		user='admin',
		password='UUU', #記得改
		db='quickpig',
		cursorclass=pymysql.cursors.DictCursor
	)
	with signup.cursor() as cursor:
		mysqlact = "UPDATE `pick` SET `finish`='true' WHERE number = %s;"
		# mysqlact = "select * from pick where number = %s"
		cursor.execute(mysqlact,ordercode)
		signup.commit()
	signup.close()
	# return {"data":tablepick}

	return {"ok":ordercode}

@app.route("/works",methods=['GET'])
def GETwork():
	today = datetime.date.today()
	tomorrow = today + datetime.timedelta(days=1)
	today = str(today)
	tomorrow = str(tomorrow)

	signup = pymysql.connect(
		host='ricetia-mysql.cyb5eosysjkk.ap-northeast-1.rds.amazonaws.com',
		port=3306,
		user='admin',
		password='UUU', #記得改
		db='quickpig',
		cursorclass=pymysql.cursors.DictCursor
	)
	with signup.cursor() as cursor:
		mysqlact = "SELECT `number`,`code`,`finish`,`content` FROM `pick` WHERE time >= %s and time < %s and finish = 'false'"
		cursor.execute(mysqlact,(today,tomorrow))
		tablepick = cursor.fetchall()
	signup.close()
	return {"data":tablepick}

@app.route("/counts",methods=['GET'])
def GETpick():
	today = datetime.date.today()
	tomorrow = today + datetime.timedelta(days=1)
	today = str(today)
	tomorrow = str(tomorrow)

	signup = pymysql.connect(
		host='ricetia-mysql.cyb5eosysjkk.ap-northeast-1.rds.amazonaws.com',
		port=3306,
		user='admin',
		password='UUU', #記得改
		db='quickpig',
		cursorclass=pymysql.cursors.DictCursor
	)
	with signup.cursor() as cursor:
		mysqlact = "SELECT `number`,`code`,`finish` FROM `pick` WHERE time >= %s and time < %s"
		cursor.execute(mysqlact,(today,tomorrow))
		tablepick = cursor.fetchall()
	signup.close()

	return {"tablepick":tablepick}

@app.route("/table",methods=['GET'])
def GETtable():
	table = session["table_code"]
	return {"table":table}

@app.route("/table",methods=['PATCH'])
def PATCHtable():
	tabledata = request.data.decode('utf-8')
	tabledata = json.loads(tabledata)
	waiter = tabledata["waiter"]
	code = tabledata["code"]
	password = tabledata["password"]

	loginTest1 = False # 檢查參數1
	loginTest2 = False # 檢查參數2
	loginTest3 = False # 檢查參數3
	if code != "" and password != "" and waiter != "":
		loginTest1 = True
	else :
		error = {"error":True,"message": "　有項目未填寫！"}
		return error
	
	signup = pymysql.connect(
		host='ricetia-mysql.cyb5eosysjkk.ap-northeast-1.rds.amazonaws.com',
		port=3306,
		user='admin',
		password='UUU', #記得改
		db='quickpig',
		cursorclass=pymysql.cursors.DictCursor
	)
	with signup.cursor() as cursor:
		mysqlact = "SELECT `name`,`code` FROM `user` WHERE `code`=%s"
		cursor.execute(mysqlact,waiter)
		waiter_check = cursor.fetchall()
	signup.close()

	if len(waiter_check) >= 1 :
		loginTest3 = True
	if len(waiter_check) == 0 :
		error = {"error":True,"message": "　您沒有權限！"}
		return error

	signup = pymysql.connect(
		host='ricetia-mysql.cyb5eosysjkk.ap-northeast-1.rds.amazonaws.com',
		port=3306,
		user='admin',
		password='UUU', #記得改
		db='quickpig',
		cursorclass=pymysql.cursors.DictCursor
	)
	with signup.cursor() as cursor:
		mysqlact = "SELECT `code`,`password` FROM `usetable` WHERE `code`=%s"
		cursor.execute(mysqlact,code)
		code_check = cursor.fetchall()
	signup.close()

	if len(code_check) >= 1 :
		if code_check[0]["password"] == password :
			loginTest2 = True
		else :
			error = {"error":True,"message": "　密碼輸入錯誤！"}
			return error
	if len(code_check) == 0 :
		error = {"error":True,"message": "　此桌號還未註冊！"}
		return error

	if loginTest1 == True and loginTest2 == True and loginTest3 == True:
		session["table_code"] = code_check[0]["code"]
		success = {"ok":True}
		loginTest1 = False
		loginTest2 = False
		return success

	else :
		loginTest1 = False
		loginTest2 = False
		error = {"error":True,"message": "　伺服器錯誤！"}
		return error

@app.route("/user",methods=['PATCH'])
def PATCHuser():
	userdata = request.data.decode('utf-8')
	userdata = json.loads(userdata)
	code = userdata["code"]
	password = userdata["password"]

	loginTest1 = False # 檢查參數1
	loginTest2 = False # 檢查參數2
	if code != "" and password != "" :
		loginTest1 = True
	else :
		error = {"error":True,"message": "　有項目未填寫！"}
		return error
	
	signup = pymysql.connect(
		host='ricetia-mysql.cyb5eosysjkk.ap-northeast-1.rds.amazonaws.com',
		port=3306,
		user='admin',
		password='UUU', #記得改
		db='quickpig',
		cursorclass=pymysql.cursors.DictCursor
	)
	with signup.cursor() as cursor:
		mysqlact = "SELECT `id`,`name`,`code`,`password` FROM `user` WHERE `code`=%s"
		cursor.execute(mysqlact,code)
		code_check = cursor.fetchall()
	signup.close()

	if len(code_check) >= 1 :
		if code_check[0]["password"] == password :
			loginTest2 = True
		else :
			error = {"error":True,"message": "　密碼輸入錯誤！"}
			return error
	if len(code_check) == 0 :
		error = {"error":True,"message": "　此編號還未註冊！"}
		return error

	if loginTest1 == True and loginTest2 == True :
		session["login_id"] = code_check[0]["id"]
		session["login_name"] = code_check[0]["name"]
		session["login_code"] = code_check[0]["code"]
		success = {"ok":True}
		loginTest1 = False
		loginTest2 = False
		session["logout"] = False
		return success

	else :
		loginTest1 = False
		loginTest2 = False
		error = {"error":True,"message": "　伺服器錯誤！"}
		return error

@app.route("/menus",methods=['GET'])
def GETmenus():
	menuclass = (request.args.get("class",""))

	signup = pymysql.connect(
		host='ricetia-mysql.cyb5eosysjkk.ap-northeast-1.rds.amazonaws.com',
		port=3306,
		user='admin',
		password='UUU', #記得改
		db='quickpig',
		cursorclass=pymysql.cursors.DictCursor
	)
	with signup.cursor() as cursor:
		mysqlact = "SELECT `name`,`price`,`image`,`code` FROM `menu` WHERE class=%s"
		cursor.execute(mysqlact,menuclass)
		result = cursor.fetchall()
	signup.close()

	return {"data":result}

@app.route("/menus",methods=['POST'])
def POSTmenus():
	orderData = request.data.decode('utf-8')
	orderData = json.loads(orderData)

	today = datetime.date.today()
	tomorrow = today + datetime.timedelta(days=1)
	today2 = today.strftime('%y%m%d')
	today = str(today)
	tomorrow = str(tomorrow)
	today2 = str(today2)
	signup = pymysql.connect(
		host='ricetia-mysql.cyb5eosysjkk.ap-northeast-1.rds.amazonaws.com',
		port=3306,
		user='admin',
		password='UUU', #記得改
		db='quickpig',
		cursorclass=pymysql.cursors.DictCursor
		)
	with signup.cursor() as cursor:
		mysqlact = "SELECT count(*) FROM `pick` WHERE time >= %s and time < %s;"
		cursor.execute(mysqlact,(today,tomorrow))
		result = cursor.fetchall()
	signup.close()
	res_number = result[0]["count(*)"] +1
	order_number = today2 + str(res_number)

	orderData_order = orderData["order"]
	orderData_order = str(orderData_order)
	orderData_subtotal = orderData["subtotal"]
	orderData_table = orderData["table"]
	finish = "false"

	signup = pymysql.connect(
			host='ricetia-mysql.cyb5eosysjkk.ap-northeast-1.rds.amazonaws.com',
			port=3306,
			user='admin',
			password='UUU', #記得改
			db='quickpig',
			cursorclass=pymysql.cursors.DictCursor
			)
	with signup.cursor() as cursor:
		mysqlact = "INSERT INTO pick (number,content,allprice,code,finish) VALUES (%s,%s,%s,%s,%s)"
		cursor.execute(mysqlact,(order_number,orderData_order,orderData_subtotal,orderData_table,finish))
		signup.commit()
	signup.close()

	return {"ok":True}


app.run(port=3000)
# app.run(host="0.0.0.0",port=3000)