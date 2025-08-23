import os
import datetime
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
    for query in results:
        hits = results[query]
        if not hits:
            continue
        content += f"\n<h2>Results for query '{query}':</h2>\n<ul>" + "\n".join(
            f"<li>{hit['displayLink']}:<a href='{hit['link']}'>{hit['title']}</a> \
            \n<p><em>{hit['snippet']}</em></p></li>" for hit in hits
        )
        content += "\n</ul>\n"
    content += "</body>\n</html>"
    if content == "<html>\n<body></body>\n</html>":
        return "No new results found."
    return content 

def send_email(content):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECIPIENT
    msg['Subject'] = f"Google News Search Results - \
        {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    msg.attach(MIMEText(content, 'html'))

    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(EMAIL_SENDER, EMAIL_PASSWORD)
    smtpObj.sendmail(EMAIL_SENDER, EMAIL_RECIPIENT, msg.as_string())
    smtpObj.quit()
