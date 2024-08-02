Fake KYC Report

CRFID : 122016
User Department : Audit

AIM : 
Need a new report for gold photo verification of customers, 
including both new pledge and repledge . The KYC should be verified by AI technology and Fake gold photo 
leads shall be provided including the black screen photos, faded images,coins, blank screen photos other than gold.

download.py
---------------
    Database Connection and Data Retrieval:
        The script establishes a connection to an Oracle database using the cx_Oracle library.
        It then executes a SQL query to retrieve records from the database.

    Image Processing:
        The script processes the retrieved image data to determine the image type using the get_ext function.
        It saves the images to the local file system based on their type, and in the case of TIFF images, 
	it converts them to JPEG format using OpenCV.

    Error Handling:
        The script includes error handling for image processing and conversion, such as handling exceptions 
	when saving or converting images.

    Cleanup:
        The script closes the database cursor and connection after processing the records.

code.py
-------

    Image Processing and Classification:
        The main function process_images processes images from a specified folder, extracts text using the 
	extract_text function, and then classifies the images based on the presence of blur ,blank and coin images. 
	It moves the images to fake folder based on the classification results.


insert.py,insert_null.py
------------------------------------------
inserting the images from the corresponding folders to the database.

mail.py
-------
mail automation to send the fake gold photo verification data.


