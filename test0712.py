# 第一題
def search(arr, target):
    result = ""
    for i in arr :
        if i == target :
            result = 0
            break
        else :
            result = -1
    return result
        
index=search([3, 4, 1, 10], 4)
print(index)
index=search([1, 5, 2, -5], 3)
print(index)

#第二題
def findMax(arr):
    result = arr[0]
    for i in arr:
        if i > result :
            result = i
        else:
            continue
    return result

result=findMax([3, 4, 1, 10])
print(result)
result=findMax([1, 5, 2, -5])
print(result)

# 第三題
def twoSum(data, target):
    for i in  range(len(data)) :
        for j in range(len(data)) :
            if data[i] + data[j] == target :
                return i,j

result=twoSum([3, 4, 1, 10], 5)
print(result)
result=twoSum([1, 5, 2, -5], 0)
print(result)

# 第四題
# def search(arr, target):
#     i = 0
#     j = len(arr)
#     k = int((i+j)/2)
#     index = arr[i]
#     end = arr[j]
#     mid = arr[k]
#     if target > mid :
#         index = arr[k+1]
    
    

search([-5, 1, 5, 8, 20], 8);
search([-5, 1, 5, 8, 20], 7);

# a = 5
# b = 2
# c = (a+b)/2
# print(int(c))

# import mysql.connector
import pymysql.cursors
import pymysql
# datatime
import datetime

# today = datetime.date.today()
# tomorrow = today + datetime.timedelta(days=1)
# today2 = today.strftime('%y%m%d')
# today = str(today)
# tomorrow = str(tomorrow)
# today2 = str(today2)

# signup = pymysql.connect(
# 	host='ricetia-mysql.cyb5eosysjkk.ap-northeast-1.rds.amazonaws.com',
# 	port=3306,
# 	user='admin',
# 	password='EMEdd2lDaZOp2UbOSLkC', #記得改
# 	db='quickpig',
# 	cursorclass=pymysql.cursors.DictCursor
# 	)
# with signup.cursor() as cursor:
#     mysqlact = "SELECT count(*) FROM `pick` WHERE time >= %s and time < %s;"
#     cursor.execute(mysqlact,(today,tomorrow))
#     result = cursor.fetchall()
# signup.close()

# res_number = result[0]["count(*)"] +1
# order_number = today2 + str(res_number)

# print(today)
# print(tomorrow)
# print(order_number)

code = "4321"

signup = pymysql.connect(
	host='ricetia-mysql.cyb5eosysjkk.ap-northeast-1.rds.amazonaws.com',
	port=3306,
	user='admin',
	password='EMEdd2lDaZOp2UbOSLkC', #記得改
	db='quickpig',
	cursorclass=pymysql.cursors.DictCursor
)
with signup.cursor() as cursor:
	mysqlact = "SELECT `id`,`name`,`code`,`password` FROM `user` WHERE `code`=%s"
	cursor.execute(mysqlact,code)
	code_check = cursor.fetchall()
signup.close()

print(code_check[0]["password"])