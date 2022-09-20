import mysql.connector

def DataUpdate(Name,Number,Email,Description):
	mydb = mysql.connector.connect(
	  host="127.0.0.1",
	  user="root",
	  password="Password@123",
	  database="rasa",
	  port=3306,
	  auth_plugin='mysql_native_password'
	)
	
	mycursor = mydb.cursor()
	
	sql="insert into customers(name,number,email,description) values('"+Name+"','"+Number+"','"+Email+"','"+Description+"')"
	
	mycursor.execute(sql)
	
	mydb.commit()
	
	print(mycursor.rowcount, "record inserted")
	
if __name__=="__main__":
	DataUpdate("ABCD","897654321","abcd@email.com","I have a project for classification")
