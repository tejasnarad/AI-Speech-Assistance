import pymysql as abc
#need to change sql root and password for your pc
#need to create data base PROJECT_SPEECH

db=abc.Connect(host="localhost",user="root" ,password="" )

cursor=db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS PROJECTAI_SPEECH")
cursor.execute("USE PROJECTAI_SPEECH")
#store in database
def store(request):
    
    try:
        cursor.execute("create table info(id int(2) NOT NULL AUTO_INCREMENT PRIMARY KEY,text_info text(100))");
        if "name" in request:
            sql="INSERT INTO info (text_info) VALUES (%s)"
            cursor.execute(sql,request)
        
        if "phone" in request:
            sql="INSERT INTO info (text_info) VALUES (%s)"
            cursor.execute(sql,request)
        
        else:
            sql="INSERT INTO info (text_info) VALUES (%s)"
            cursor.execute(sql,request)

        db.commit()
    except abc.InternalError:
    

        if "name" in request:
            sql="INSERT INTO info (text_info) VALUES (%s)"
            cursor.execute(sql,request)

        if "phone" in request:
            sql="INSERT INTO info (text_info) VALUES (%s)"
            cursor.execute(sql,request)
        
        else:
            sql="INSERT INTO info (text_info) VALUES (%s)"
            cursor.execute(sql,request)

        db.commit()

#retrive info from database
def get_info(request):
    
    if "phone" in request:
        cursor.execute("select MAX(id)  from info where text_info like '%phone%'")
        myresult = cursor.fetchall()
        value=myresult[0][0]
        
        cursor.execute("select text_info from info where id=%s",value)
        result=cursor.fetchall()
        db.commit()
        return result[0][0]
        
    elif "name" in request:
        cursor.execute("select MAX(id)  from info where text_info  like '%name%'")
        myresult = cursor.fetchall()
        value=myresult[0][0]
        
        cursor.execute("select text_info from info where id=%s",value)
        result=cursor.fetchall()
        db.commit()
        return result[0][0]
    elif "text" in request:
        cursor.execute("select MAX(id)  from info where text_info not like '%name%' and text_info not like '%phone%' ")
        myresult = cursor.fetchall()
        value=myresult[0][0]
        
        cursor.execute("select text_info from info where id=%s",value)
        result=cursor.fetchall()
        db.commit()
        return result[0][0]
    else :
        return "false"
        
        
       

