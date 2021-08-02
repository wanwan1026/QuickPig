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
# time
import time
# env
import os
from dotenv import load_dotenv
load_dotenv()

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
@app.route("/pay")
def pay():
	return render_template("pay.html")


@app.route("/pays",methods=['POST'])
def POSTpay():
	tablecode = request.data.decode('utf-8')
	tablecode = json.loads(tablecode)
	tablecode = tablecode["table"]

	signup = pymysql.connect(
		host='ricetia-mysql.cyb5eosysjkk.ap-northeast-1.rds.amazonaws.com',
		port=3306,
		user='admin',
		password=os.getenv("RDS_password"),
		db='quickpig',
		cursorclass=pymysql.cursors.DictCursor
	)
	with signup.cursor() as cursor:
		mysqlact = "update `pick` set `finish`='pay' where code = %s and finish = 'true';"
		mysqlact2 = "update `pick` set `finish`='stop' where code = %s and finish = 'close';"
		mysqlact3 = "update `usetable` set `status`='false' where code = %s;"
		cursor.execute(mysqlact,tablecode)
		cursor.execute(mysqlact2,tablecode)
		cursor.execute(mysqlact3,tablecode)
		signup.commit()
	signup.close()

	return {"ok":"成功付款"}

@app.route("/pays",methods=['GET'])
def GETpay():
	tablecode = (request.args.get("tablecode",""))

	signup = pymysql.connect(
		host='ricetia-mysql.cyb5eosysjkk.ap-northeast-1.rds.amazonaws.com',
		port=3306,
		user='admin',
		password=os.getenv("RDS_password"),
		db='quickpig',
		cursorclass=pymysql.cursors.DictCursor
	)
	with signup.cursor() as cursor:
		mysqlact = "SELECT `number`,`content`,`allprice` FROM `pick` WHERE code = %s and finish = 'true';"
		cursor.execute(mysqlact,tablecode)
		tablepick = cursor.fetchall()
	signup.close()

	return {"pick":tablepick}

@app.route("/works",methods=['POST'])
def POSTwork():
	ordercode = request.data.decode('utf-8')
	ordercode = json.loads(ordercode)
	ordercode = ordercode["ok"]

	signup = pymysql.connect(
		host='ricetia-mysql.cyb5eosysjkk.ap-northeast-1.rds.amazonaws.com',
		port=3306,
		user='admin',
		password=os.getenv("RDS_password"),
		db='quickpig',
		cursorclass=pymysql.cursors.DictCursor
	)
	with signup.cursor() as cursor:
		mysqlact = "update `pick` set `finish`='true' where number = %s;"
		cursor.execute(mysqlact,ordercode)
		signup.commit()
	signup.close()

	return {"ok":ordercode}

@app.route("/works",methods=['GET'])
def GETwork():
	signup = pymysql.connect(
		host='ricetia-mysql.cyb5eosysjkk.ap-northeast-1.rds.amazonaws.com',
		port=3306,
		user='admin',
		password=os.getenv("RDS_password"),
		db='quickpig',
		cursorclass=pymysql.cursors.DictCursor
	)
	with signup.cursor() as cursor:
		mysqlact = "select `number`,`code`,`finish`,`content` from `pick` where finish = 'false' or finish = 'close'"
		cursor.execute(mysqlact)
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
		password=os.getenv("RDS_password"),
		db='quickpig',
		cursorclass=pymysql.cursors.DictCursor
	)
	with signup.cursor() as cursor:
		mysqlact = "select `number`,`code`,`finish` from `pick` where time >= %s and time < %s;"
		cursor.execute(mysqlact,(today,tomorrow))
		tablepick = cursor.fetchall()
		mysqlact2 = "SELECT * FROM `usetable`;"
		cursor.execute(mysqlact2)
		tablestatus = cursor.fetchall()
	signup.close()

	return {"tablepick":tablepick,"tablestatus":tablestatus}

@app.route("/table",methods=['GET'])
def GETtable():
	if "table_code" in session:
		tablecode = session["table_code"]

		signup = pymysql.connect(
		host='ricetia-mysql.cyb5eosysjkk.ap-northeast-1.rds.amazonaws.com',
		port=3306,
		user='admin',
		password=os.getenv("RDS_password"),
		db='quickpig',
		cursorclass=pymysql.cursors.DictCursor
		)
		with signup.cursor() as cursor:
			mysqlact = "select code,max(time) from opentable where code=%s"
			cursor.execute(mysqlact,tablecode)
			code_get = cursor.fetchall()
		signup.close()

		tabletime = str(code_get[0]["max(time)"])

		return {"tablecode":code_get[0]["code"],"time":tabletime}
	else :
		error = {"error":True,"message": "　伺服器錯誤！無法正確載入用餐資訊"}

		return error

@app.route("/table",methods=['POST'])
def POSTtable():
	tablecode = request.data.decode('utf-8')
	tablecode = json.loads(tablecode)
	tablecode = tablecode["timeout"]

	signup = pymysql.connect(
		host='ricetia-mysql.cyb5eosysjkk.ap-northeast-1.rds.amazonaws.com',
		port=3306,
		user='admin',
		password=os.getenv("RDS_password"),
		db='quickpig',
		cursorclass=pymysql.cursors.DictCursor
	)
	with signup.cursor() as cursor:
		mysqlact = "update `usetable` set `status`='close' where code = %s;"
		mysqlact2 = "update pick set finish = 'close' where code = %s and finish = 'false';"
		cursor.execute(mysqlact,tablecode)
		cursor.execute(mysqlact2,tablecode)
		signup.commit()
	signup.close()

	del session["table_code"]

	return {"ok":tablecode}

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

	# test1
	if code != "" and password != "" and waiter != "":
		loginTest1 = True
	else :
		error = {"error":True,"message": "　有項目未填寫！"}
		return error
	
	# test3
	signup = pymysql.connect(
		host='ricetia-mysql.cyb5eosysjkk.ap-northeast-1.rds.amazonaws.com',
		port=3306,
		user='admin',
		password=os.getenv("RDS_password"),
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

	# test2
	signup = pymysql.connect(
		host='ricetia-mysql.cyb5eosysjkk.ap-northeast-1.rds.amazonaws.com',
		port=3306,
		user='admin',
		password=os.getenv("RDS_password"),
		db='quickpig',
		cursorclass=pymysql.cursors.DictCursor
	)
	with signup.cursor() as cursor:
		mysqlact = "SELECT `code`,`password`,`status` FROM `usetable` WHERE `code`=%s"
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

	# finial check
	if loginTest1 == True and loginTest2 == True and loginTest3 == True:
		if code_check[0]["status"] == "false" :
			opentime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

			signup = pymysql.connect(
			host='ricetia-mysql.cyb5eosysjkk.ap-northeast-1.rds.amazonaws.com',
			port=3306,
			user='admin',
			password=os.getenv("RDS_password"),
			db='quickpig',
			cursorclass=pymysql.cursors.DictCursor
			)
			with signup.cursor() as cursor:
				mysqlact = "update `usetable` set `status`='true' where code = %s;"
				cursor.execute(mysqlact,code_check[0]["code"])
				mysqlact2 = "insert into opentable (code,time) values (%s,%s);"
				cursor.execute(mysqlact2,(code_check[0]["code"],opentime))
				signup.commit()
			signup.close()

			session["table_code"] = code_check[0]["code"]
			success = {"ok":True}
			loginTest1 = False
			loginTest2 = False
			loginTest3 = False

			return success
		if code_check[0]["status"] == "true" :
			session["table_code"] = code_check[0]["code"]
			success = {"ok":True}
			loginTest1 = False
			loginTest2 = False
			loginTest3 = False

			return success
		if code_check[0]["status"] == "close" :
			error = {"error":True,"message": "　錯誤，前位尚未買單！"}
			
			return error
	else :
		loginTest1 = False
		loginTest2 = False
		loginTest3 = False
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

	# test1 
	if code != "" and password != "" :
		loginTest1 = True
	else :
		error = {"error":True,"message": "　有項目未填寫！"}
		return error
	
	# test2
	signup = pymysql.connect(
		host='ricetia-mysql.cyb5eosysjkk.ap-northeast-1.rds.amazonaws.com',
		port=3306,
		user='admin',
		password=os.getenv("RDS_password"),
		db='quickpig',
		cursorclass=pymysql.cursors.DictCursor
	)
	with signup.cursor() as cursor:
		mysqlact = "select `id`,`name`,`code`,`password` from `user` where `code`=%s"
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

	# finial check
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
		password=os.getenv("RDS_password"),
		db='quickpig',
		cursorclass=pymysql.cursors.DictCursor
	)
	with signup.cursor() as cursor:
		mysqlact = "select `name`,`price`,`image`,`code` from `menu` where class=%s"
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
		password=os.getenv("RDS_password"),
		db='quickpig',
		cursorclass=pymysql.cursors.DictCursor
		)
	with signup.cursor() as cursor:
		mysqlact = "select count(*) from `pick` where time >= %s and time < %s;"
		cursor.execute(mysqlact,(today,tomorrow))
		result = cursor.fetchall()
	signup.close()

	res_number = result[0]["count(*)"] +1
	order_number = today2 + str(res_number)

	orderData_order = orderData["order"]
	orderData_subtotal = orderData["subtotal"]
	orderData_table = orderData["table"]
	finish = "false"
	picktime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

	signup = pymysql.connect(
			host='ricetia-mysql.cyb5eosysjkk.ap-northeast-1.rds.amazonaws.com',
			port=3306,
			user='admin',
			password=os.getenv("RDS_password"),
			db='quickpig',
			cursorclass=pymysql.cursors.DictCursor
			)
	with signup.cursor() as cursor:
		mysqlact = "insert into pick (number,content,allprice,code,finish,time) values (%s,%s,%s,%s,%s,%s)"
		cursor.execute(mysqlact,(order_number,orderData_order,orderData_subtotal,orderData_table,finish,picktime))
		signup.commit()
	signup.close()

	return {"ok":True}


app.run(port=3000)
# app.run(host="0.0.0.0",port=3000)