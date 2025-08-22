import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT")

test_string = 'This is a test email.\nLet me know if you got it.\nThanks.'
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(EMAIL_SENDER, EMAIL_PASSWORD)
smtpObj.sendmail(EMAIL_SENDER, EMAIL_RECIPIENT, test_string)
smtpObj.quit()