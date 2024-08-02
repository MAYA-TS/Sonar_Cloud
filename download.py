import datetime
import cx_Oracle
import os


def doumload():

   sql="""Query to fetch data"""   
 
   conn = cx_Oracle.connect("db_username", "db_password", "db_name")
   cursor = conn.cursor()
   cursor.execute(sql)
   imagePath = "Input_folder_path"
   for i in range(1):
        i = i + 1
        records = cursor.fetchall()
        for row in records:
          
               cust_id = row[0]
               print(cust_id)
               pledge_no=row[1]
               image_blob = row[2]
               masked_image_path=os.path.join(imagePath,str(cust_id)+'='+ str(pledge_no) +".jpg")
               image_file=open(masked_image_path,'wb')

               if image_blob is not None:
                  image_file.write(image_blob.read())
               else:
                
                  print("Error: image_blob is None")
                  unavailable_folder = "Output_folder_path"
                  unavailable_image_path = os.path.join(unavailable_folder,str(cust_id)+'='+ str(pledge_no) +".jpg")
                  os.makedirs(unavailable_folder, exist_ok=True)
                  image_file.close()   
                  
                  if os.path.exists(unavailable_image_path):
                     timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                     unavailable_image_path = os.path.join(unavailable_folder,str(cust_id)+'='+ str(pledge_no) +".jpg")
                  
                  os.rename(masked_image_path, unavailable_image_path)

doumload()
