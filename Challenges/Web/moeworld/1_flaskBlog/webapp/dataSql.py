import pymysql
import time
import getPIN

pin = getPIN.get_pin()

class Database:
    def __init__(self, max_retries=3):
        self.max_retries = max_retries
        self.db = None

    def __enter__(self):
        self.db = self.connect_to_database()
        return self.db, self.db.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.db and self.db.open:
            self.db.close()

    def connect_to_database(self):
        retries = 0
        while retries < self.max_retries:
            try:
                db = pymysql.connect(
                    host="mysql",  # 数据库地址
                    port=3306,  # 数据库端口
                    user="root",  # 数据库用户名
                    passwd="The_P0sswOrD_Y0u_Nev3r_Kn0w",  # 数据库密码
                    database="messageboard",  # 数据库名
                    charset='utf8'
                )
                return db
            except pymysql.Error as e:
                retries += 1
                print(f"Connection attempt {retries} failed. Retrying in 5 seconds...")
                time.sleep(5)
        raise Exception("Failed to connect to the database after maximum retries.")

def canLogin(username,password):
    with Database() as (db, cursor):
        sql = 'select password from users where username=%s'
        cursor.execute(sql, username)
        res = cursor.fetchall()
        if res:
            if res[0][0] == password:
                return True
        return False

def register(id,username,password,power):
    with Database() as (db, cursor):
        sql = 'select username from users where username=%s'
        cursor.execute(sql, username)
        res = cursor.fetchall()
        if res:
            return False
        else:
            sql = 'insert into users (id,username,password,power) values (%s,%s,%s,%s)'
            cursor.execute(sql, (id,username,password,power))
            db.commit()
            return True

def changePassword(username,oldPassword,newPassword):
    with Database() as (db, cursor):
        sql = 'select password from users where username=%s'
        cursor.execute(sql, username)
        res = cursor.fetchall()
        if res:
            if oldPassword == res[0][0]:
                sql = 'update users set password=%s where username=%s'
                cursor.execute(sql, (newPassword,username))
                db.commit()
                return True
            else:
                return "wrong password"
        else:
            return "username doesn't exist."

def uploadMessage(username,message,nowtime,private):
    with Database() as (db, cursor):
        sql = 'insert into message (username,data,time,private) values (%s,%s,%s,%s)'
        cursor.execute(sql, (username,message,nowtime,private))
        db.commit()
        return True

def showMessage():
    with Database() as (db, cursor):
        sql = 'select * from message'
        cursor.execute(sql)
        res = cursor.fetchall()
        res = [tuple([str(elem).replace('128-243-397', pin) for elem in i]) for i in res]
        return res

def usersName():
    with Database() as (db, cursor):
        sql = 'select * from users'
        cursor.execute(sql)
        res = cursor.fetchall()
        return len(res)

def getPower(username):
    with Database() as (db, cursor):
        sql = 'select power from users where username=%s'
        cursor.execute(sql, username)
        res = cursor.fetchall()
        return res[0][0]

def deleteMessage(username,pubTime):
    with Database() as (db, cursor):
        sql = 'delete from message where username=%s and time=%s'
        cursor.execute(sql,(username,pubTime))
        db.commit()
        return True