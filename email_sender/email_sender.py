import os
import smtplib
from dotenv import load_dotenv, find_dotenv # environs package is another option to use here
from email.message import EmailMessage
from pathlib import Path
from string import Template

# Load environment variables from .env file
load_dotenv(find_dotenv('.env.dev')) #  replace this '.env.dev' by the environmet file name

# Access environment variables
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Read the list of contacts to send email to
contacts = []
with open(Path('contacts.txt')) as file:
	lines = file.readlines()
	# for each line we have name and email separated by a comma
	contacts = [tuple(x.split(',')) for x in lines]

# Read the HTML content 
html = Template(Path('email_content.html').read_text())


# set the Email subject and from attributes
email = EmailMessage()
email['from'] = 'Jaime Contreras'
email['subject'] = 'This is a test by aalvarez!' # static for now but then we want to ask for the subject

# for each contact in our list, send the email
for i, contact in enumerate(contacts):
	print(f'sending email to contact: {i+1} - {contact}')
	contact_name = contact[0]
	contact_email = contact[1]

	html_content = html.substitute({'name': contact_name})
	email.set_content(html_content, 'html')
	email['to'] = contact_email

	with smtplib.SMTP(host=SMTP_SERVER, port=SMTP_PORT) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
		smtp.send_message(email)
		print('email sent!')



