# Initial simple version for sending email with attachment
# Based on: https://stackoverflow.com/questions/3362600/how-to-send-email-attachments
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

# Open the plain text file whose name is in textfile for reading.
with open("../shared_folder_sample/sample.txt") as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = f'The contents of '
msg['From'] = "scoulomb.mail1@gmail.com"
msg['To'] = "scoulomb.mail2@gmail.com"

# Send the message via our own SMTP server.
s = smtplib.SMTP('smtp.gmail.com', 587)
# See README. Add authentication
s.ehlo()
s.starttls()
s.login("scoulomb.mail1@gmail.com", "XXXX")

s.send_message(msg)
s.quit()
print("mail sent")