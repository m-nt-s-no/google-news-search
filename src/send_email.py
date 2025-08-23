import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT")

def format_email_body(results):
    content = "<html>\n<body>"
    for query, items in results.items():
        if not items:
            continue
        content += f"\n<h2>Results for query '{query}':</h2>\n<ul>" + "\n".join(
                f"<li>{item['displayLink']}:<a href='{item['link']}'>{item['title']}</a>\n<p><em>{item['snippet']}</em></p></li>" for item in items
            )
    content += "\n</ul>\n</body>\n</html>"
    if content == "<html>\n<body>\n</ul>\n</body>\n</html>":
        return "No new results found."
    return content 

def send_email(content):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(EMAIL_SENDER, EMAIL_PASSWORD)
    smtpObj.sendmail(EMAIL_SENDER, EMAIL_RECIPIENT, content)
    smtpObj.quit()

"""
TO-DO: 
Where do I add MIME module?
TEST both functions
"""
