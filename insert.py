import os
import cx_Oracle
import datetime
import os
import shutil
import zipfile
from datetime import datetime, timedelta


connection1 = cx_Oracle.connect("kpmg", "Asd$1234", "HISTDB1")
cursor = connection1.cursor()

path_images="C:\\Users\\398504\\CRF\\crf23\\Gold_photo_verification_122016\\fake\\"
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
            connection = cx_Oracle.connect("kpmg", "Asd$1234", "HISTDB1")
            cursor = connection.cursor()


            cursor.execute("INSERT INTO tbl_fake_gold_verification(PLEDGE_NO,CREATED_DT, STATUS,cust_id) VALUES (:pledge_no,TO_DATE(:1, 'DD-MM-YYYY'), :status,:cust_id)",
                        (pledge_no,current_date,status,CUST_ID))
            cursor.close()
            print(pledge_no, "inserted")
            count = count+1
            print(count)
          
            connection.commit() 



connection1.commit()
connection1.close() 