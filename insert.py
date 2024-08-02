import os
import cx_Oracle
import datetime
import os
import shutil
import zipfile
from datetime import datetime, timedelta


connection1 = cx_Oracle.connect("db_username", "db_pwd", "db_name")
cursor = connection1.cursor()

path_images="Folder_path"
count=0
for filename in os.listdir(path_images):
        if filename.endswith('.JPEG') or filename.endswith('.jpg'):
            CUST_ID = filename.split('=')[0]
            print(CUST_ID ," ")
            pledge=filename.split("=")[1]
            pledge_no=pledge.split(".")[0]
            current_date1 = datetime.now() - timedelta(days=1)
            current_date = datetime.strftime(current_date1, '%d-%m-%Y')

            status = 1
            connection = cx_Oracle.connect("db_username", "db_pwd", "db_name")
            cursor = connection.cursor()


            cursor.execute("Query for insertion",
                        (pledge_no,current_date,status,CUST_ID))
            cursor.close()
            print(pledge_no, "inserted")
            count = count+1
            print(count)
          
            connection.commit() 



connection1.commit()
connection1.close() 
