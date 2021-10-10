import MySQLdb
conn=MySQLdb.connect(host="remotemysql.com",user="uGu9fJVTjJ",passwd="xcZ7oQJir0",db="uGu9fJVTjJ")
cur=conn.cursor()
cur.execute("Create Table User_Info (Email varchar(50) NOT NULL UNIQUE,First_Name varchar(30) NOT NULL,Last_Name varchar(30) NOT NULL,User_no int, PRIMARY KEY(Email))")
cur.execute("Create Table Login_Info (Username varchar(30) NOT NULL UNIQUE,Password varchar(30) NOT NULL,SQ1 varchar(50) NOT NULL,SQ1_Ans varchar(20) NOT NULL,SQ2 varchar(50) NOT NULL,SQ2_Ans varchar(20) NOT NULL,Email varchar(50) NOT NULL UNIQUE,PRIMARY KEY (Username), FOREIGN KEY (Email) REFERENCES User_Info(Email))")
cur.execute("CREATE TABLE Chat_Exists (person int,chats_with int,time int, Check (person<chats_with))")
conn.close()
