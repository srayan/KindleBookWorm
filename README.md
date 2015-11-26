# bookManager
Python script run daily, to deliver eBooks dumped in a folder (ex: from https://www.gutenberg.org/) to a Kindle device

Currently I am hosting this on my Azure VM, where the task scheduler will trigger execution of my script daily at 6 p.m.

Here are the key parameters you need to alter:

#Location where all eBooks will be dumped
sourceFolder = "C:/Users/srayan/OneDrive/bookManager/eBooks"
#Location where all eBooks will be archived
destinationFolder = r'C:/Users/srayan/OneDrive/eBook_archive'
#Location of trash (not currently used)
trashFolder= r'C:/Users/srayan/OneDrive/trashFolder'

#Email address whiteliested in your Amazon Kindle settings account
msg['From'] = 'myEmail@gmail.com'
#Your Kindle Email address 
msg['To'] = 'recipient@kindle.com'

BulkConvert.sh is a shell script used to perform bulk conversion of eBooks in .pdf or .epub formats into .mobi.
I am using CLI modules of Calibre (open source) for this
