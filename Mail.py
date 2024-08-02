import xlsxwriter
import os
import pandas as pd
import cx_Oracle
import openpyxl
from pandas import ExcelWriter
from openpyxl import Workbook
from email.message import EmailMessage
from email.utils import make_msgid
import mimetypes
from tableau_api_lib import TableauServerConnection
from tableau_api_lib.utils import querying
from tableau_api_lib.utils.common import flatten_dict_column
import pandas as pd
import xlrd
from pandas import ExcelWriter
from openpyxl import load_workbook
from openpyxl.styles import PatternFill,Font
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment
from openpyxl.styles import Border, Side
import smtplib
import datetime
import time
# import schedule
import time


conn = cx_Oracle.connect("db_username", "db_password", "db_name")
tableau_server_config = {
                'my_env': {
                        'server': 'tableau_url',
                        'api_version': "3.17",
                        'username': 'tableau_user_name',
                        'password': 'tableau_password',
                        'site_name': 'Default',
                        'site_url': ''
                }
        }
conn = TableauServerConnection(tableau_server_config, env='my_env',ssl_verify=False)
conn.sign_in()
site_views_df = querying.get_views_dataframe(conn)
site_views_detailed_df = flatten_dict_column(site_views_df, keys=['name', 'id'], col_name='workbook')
site_views_detailed_df.tail(60)
relevant_views_df = site_views_detailed_df[site_views_detailed_df['workbook_name'] == 'Workbook Name']
print(relevant_views_df)



fzm_data='fzm_workbook_id'
view_img = conn.query_view_image(view_id=fzm_data)
print(view_img)
with open(r"path_to_image","wb") as f:
   
    f.write(view_img.content)
print("Third section completed................")
conn = cx_Oracle.connect("db_username", "db_pwd", "db_name")
print("Oracle database connected")
print("Tableau server connected")

        


df1=pd.read_sql("""Query to Fetch data
#---------------------------------------------------------------------


print("Query section completed...........")



if not df1.empty:
    writer=pd.ExcelWriter("path_to_excel",engine="openpyxl")
    df1.to_excel(writer, sheet_name="Gold_verification_report", index=False)


    print("saved as excel")
    writer.save()
    print("Excel downloading section completed............")


    workbook = openpyxl.load_workbook('path_to_excel')
    print("wb open")
    sheet_names = workbook.sheetnames
    heading_color =  'E2BCB7'    #'73BCC5'#'8080ff'  # Red color
    # body_color = 'F6E5F5'  # Green color
    border_style = Border(
        left=Side(border_style='thin'),
        right=Side(border_style='thin'),
        top=Side(border_style='thin'),
        bottom=Side(border_style='thin'))


    for sheet_name in sheet_names:
        sheet = workbook[sheet_name]
        header_font = Font(color="000000", bold=True)
        header_fill = PatternFill(start_color='E2BCB7', end_color='E2BCB7', fill_type='solid')
        for cell in sheet[1]:
            cell.fill = header_fill
            cell.font = header_font
                
        for column in sheet.columns:
            non_empty_values = [cell.value for cell in column if cell.value]
            if non_empty_values:
                max_length = max(len(str(value)) for value in non_empty_values)
                column_letter = get_column_letter(column[0].column)
                adjusted_width = (max_length + 2) * 1.2  # Adjust the width as desired
                sheet.column_dimensions[column_letter].width = adjusted_width
        for row in sheet.rows:
            max_height = max(str(cell.value).count('\n') + 1 for cell in row if cell.value)
            row_number = row[0].row
            adjusted_height = max_height * 17 # Adjust the height as desired
            sheet.row_dimensions[row_number].height = adjusted_height
        for row in sheet.iter_rows():
            for cell in row:
                cell.alignment = Alignment(horizontal='center', vertical='center')
        for row in sheet.iter_rows():
            for cell in row:
                cell.border = border_style
    workbook.save('path_to_excel')
    print("done")
   
    workbook = openpyxl.load_workbook(r"path_to_excel")
    worksheet = workbook["Gold_verification_report"]

    # if worksheet.max_row == 0:
    s = smtplib.SMTP(host='smtp.office365.com', port=587)
    s.starttls()
    # print("aaa")
  
    s.login('mail_id_username','mail_id_pwd')
    
    print("Login the mail address")
    msg = EmailMessage()
    print("Ready for mailing")

    msg['Subject'] = 'Subject'

    msg['From']='From mail ID'

    with open(r"path_to_excel", 'rb') as ra:
        attachment = ra.read()
    msg.add_related(attachment, maintype='application', subtype='xlsx', filename='Gold verification report.xlsx')
    image_cid = make_msgid(domain='mandala.com')
    msg.add_alternative("""\
    <html>
        <body>
            <p>Dear Sir,<br><p/>      
            <p>Please find the attachment. </p>
                        <p>
                        <p>
            <P>  <img src="cid:{image_cid}">
                        </>      
            <p>
            <p> 
            <p>
                Thanks & Regards,<br>
                Team IoT <br>
                R & D New age technology <br>
                ( This is an autogenerated mail )
            </p>
        </body>
    </html>
    """.format(image_cid=image_cid[1:-1]),subtype='html')    



    with open(r"path_to_image", 'rb') as img:
        maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')
        msg.get_payload()[1].add_related(img.read(),
                                            maintype=maintype,
                                            subtype=subtype,
                                            cid=image_cid)


    s.send_message(msg)
    s.quit()
    print("Mail send")
    print("final section completed sucessfully.............")
    print("Image removed")
else:
    print("                                                                     ")
    print("                                                                     ")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!NO DATA IN DB TABLE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        
