
from DBConnection import DBConnection

class Signup:

	@staticmethod
	def store(name, email, ph, pwd):
		
		database = DBConnection.getConnection()
		cursor=database.cursor()
		query = "insert into USERS values('"+email+"','"+name+"','"+pwd+"','"+ph+"')"		
		cursor.execute(query)
		print(database.commit())
		print ("Records created successfully");
		database.close()
	@staticmethod
	def datacheck(name, email, contact, pwd):
		if name == "" or email == "" or contact == "" or  pwd == "":
			return False
		else:
			return True


