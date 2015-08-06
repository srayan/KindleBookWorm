##################################################################
#Prerequisite: Python 2.7, Valid GMail account whitelisted on Amazon
#The compiled bytecode should be saved in the same directory
#where the eBooks (.mobi) are being saved

#IMPORTANT - Since all books are getting appended into one email
#So make sure the total number of books in the dumps folder < 25MiB
#Files with the same name will be over-written into the archive

#@Author: srayanguhathakurta@yahoo.com|www.srayanguhathakurta.tk
##################################################################



#!/usr/bin/python
import sys, os, shutil, time, fnmatch
import distutils.dir_util
import distutils.util
from os.path import join, getsize

# Import smtplib for the actual sending function
import smtplib
import base64

# For guessing MIME type
import mimetypes

# Import the email modules we'll need
import email
import email.mime.application


#Email all files in C:\Users\srayan\Dropbox\Apps\gutenberg to mavewrick@amazon.com

#Location where all eBooks will be dumped
sourceFolder = "C:/Users/srayan/OneDrive/bookManager/eBooks"
#Location where all eBooks will be archived
destinationFolder = r'C:/Users/srayan/OneDrive/eBook_archive'
#Location of trash
trashFolder= r'C:/Users/srayan/OneDrive/trashFolder'

# Create a text/plain message
msg=email.mime.Multipart.MIMEMultipart()
#msg['Subject'] = '
msg['From'] = 'myEmail@gmail.com'
msg['To'] = 'recipient@kindle.com'
  
# The main body is just another attachment
# body = email.mime.Text.MIMEText("""Email message body (if any) goes here!""")
# msg.attach(body)


#To check if the directory is empty.
#If directory is empty program exits and no email/file copy operations are carried out
if os.listdir(sourceFolder) ==[]:
   print "No file for email today"
else:
    
   #filename is a list(array) which holds the name of all the .mobi books present in the directory
   #To check for the existence of .mobi files. If file exists, send as email, else not
   filename = [file for file in os.listdir(sourceFolder) if file.endswith(".mobi")]
   for iFiles in filename:
      print (iFiles)		
      #Need to store the entire path name of the file--If files dumped at other location, then append entire source to iFiles
      #Using for debugging
      currentFile = os.path.join(sourceFolder,iFiles)
      print "The current location of the file is " +(currentFile)
      fp=open(currentFile,'rb')
      att = email.mime.application.MIMEApplication(fp.read(),_subtype="mobi")
      fp.close()
      att.add_header('Content-Disposition','attachment',filename=iFiles)
      msg.attach(att)
      
   #Mail trigger module
   server = smtplib.SMTP('smtp.gmail.com:587')
   server.starttls()
   server.login('myEmail@gmail.com','password')
   server.sendmail('myEmail@gmail.com',['recipient@kindle.com'], msg.as_string())
   server.quit()
   print "Email successfully sent!"


   #Copying files for archiving
   if not os.path.exists(destinationFolder): os.makedirs(destinationFolder)
   distutils.dir_util.copy_tree(sourceFolder, destinationFolder)
   #shutil.rmtree(sourceFolder)
   #shutil.move(sourceFolder, trashFolder)

   #Cleaning the dump directory after archiving 
   trashName=[file for file in os.listdir(sourceFolder) if file.endswith(".mobi")]
   for trashFiles in trashName:
   	os.remove(os.path.join(sourceFolder, trashFiles))


   print "Files copied successfully"
   osName=distutils.util.get_platform()
   print (osName)


   #Check for os.walk and fnmatch.filter
   #Try to archive files into a dateNamed directory
