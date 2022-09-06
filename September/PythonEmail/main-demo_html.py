
import smtplib
import imghdr
from email.message import EmailMessage


EMAIL_ADDRESS = 'LuisMRomanTest77@gmail.com'
#following is password gotten from acocunt apppasswords, found in google account in security,just past in ''
EMAIL_PASSWORD = 'eqvkugetcuottgud'

contacts = ['LuisMRomanTest77@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Check out this cool new game?'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts
msg.set_content('This is a plain text email!')

msg.add_alternative("""\
<!DOCTYPE html>
<thml>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</thml>
""", subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    #smtp.login(email, password)
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)