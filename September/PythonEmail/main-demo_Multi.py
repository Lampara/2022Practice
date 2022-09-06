
import smtplib
import imghdr
from email.message import EmailMessage


EMAIL_ADDRESS = 'LuisMRomanTest77@gmail.com'
#following is password gotten from acocunt apppasswords, found in google account in security,just past in ''
EMAIL_PASSWORD = ''

contacts = ['LuisMRomanTest77@gmail.com', ]

msg = EmailMessage()
msg['Subject'] = 'Check out this cool new game?'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts
msg.set_content('Image Attached!')

files = ['AmongUs.jpeg'] #can also use pdf files, should read it on its own

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        #know issue with imghdr, just marked it as JPEG
        #for this demo using imghdr but it doesn't work
        file_type = imghdr.what(f.name)
        #file_type = 'JPEG'
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    #smtp.login(email, password)
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)