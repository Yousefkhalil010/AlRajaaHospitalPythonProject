import mysql.connector
try:
    db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="14678Naseem",
    database='hospital',
    auth_plugin="mysql_native_password"
    )
except:
    print("Cannot connect to the server")
else:
    mycursor=db.cursor()
    mycursor.execute("CREATE TABLE patient (ID int PRIMARY KEY AUTO_INCREMENT, PatientName varchar(255), Age int, Address varchar(255), Mobile int, HireDate varchar(255))");
    db.commit()
    print("Table Created Suceessfully")




