import datetime
import cx_Oracle
import os


def doumload():

   sql="""select 
       e.cust_id,
       a.pledge_no,
       a.item_photo,
       c.loan_no,
       c.item_id,
       c.item_count,
       c.act_wt,
       c.net_wt,
       c.stone_wt,
       d.item_name,
       trunc(e.created_date) created_date
  from dms.pledgeitem_photo_new@uatr_backup2 a
  left outer join mana0809.pledge_master@uatr_backup2 b
    on a.pledge_no = b.pledge_no
  left outer join mana0809.gold_dtl@uatr_backup2 c
    on a.pledge_no = c.loan_no
  left outer join mana0809.item_master@uatr_backup2 d
    on c.item_id = d.item_id
  left outer join mana0809.customer@uatr_backup2 e
    on b.cust_id = e.cust_id
 where trunc(e.created_date) = trunc(sysdate) - 2"""   
 
   conn = cx_Oracle.connect("kpmg", "Asd$1234", "HISTDB1")
   cursor = conn.cursor()
   cursor.execute(sql)
   imagePath = "C:\\Users\\398504\\CRF\\crf23\\Gold_photo_verification_122016\\downloaded_images\\"
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
                  unavailable_folder = "C:\\Users\\398504\\CRF\\crf23\\Gold_photo_verification_122016\\unavailable\\"
                  unavailable_image_path = os.path.join(unavailable_folder,str(cust_id)+'='+ str(pledge_no) +".jpg")
                  os.makedirs(unavailable_folder, exist_ok=True)
                  image_file.close()   
                  
                  if os.path.exists(unavailable_image_path):
                     timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                     unavailable_image_path = os.path.join(unavailable_folder,str(cust_id)+'='+ str(pledge_no) +".jpg")
                  
                  os.rename(masked_image_path, unavailable_image_path)

doumload()
