
import smtplib

EMAIL_ADDRESS = 'LuisMRomanTest77@gmail.com'
#following is password gotten from acocunt apppasswords, found in google account in security,just past in ''
EMAIL_PASSWORD = ''
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    #smtp.login(email, password)
    smtp.login(EMAIL_ADDRESS, EMAIL_ADDRESS)

    subject = 'Grab dinner this weekend?'
    body = 'How about dinner at 6pm this Saturday?'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, 'LuisMRomanTest77@gmail.com', msg)