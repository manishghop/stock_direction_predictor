from DBConnection import DBConnection


class UserLoginCheck:

    def datacheck(self,uid,pwd):
        if uid == "" or pwd == "":
            return True
        else:
            return False
    @staticmethod
    def logincheck(uid,pwd):
        database = DBConnection.getConnection()
        cursor=database.cursor()
        print("select name from users where email='"+uid+"' and pwd='"+pwd+"' ")
        rows=cursor.execute("select name from users where email='"+uid+"' and pwd='"+pwd+"' ")

        if cursor.fetchone() is not None:
            print("login success")
            return True
        else:
            print("login fail")
            return False

        
        

#UserLoginCheck.logincheck("sajid@gmail.com","sajid")
