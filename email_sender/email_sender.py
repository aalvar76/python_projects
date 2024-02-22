import os
import smtplib
from dotenv import load_dotenv, find_dotenv # environs package is another option to use here
from email.message import EmailMessage
from pathlib import Path

# Load environment variables from .env file
load_dotenv(find_dotenv('.env.dev')) #  replace this '.env.dev' by the environmet file name

# Access environment variables
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = os.getenv("SMTP_PORT")
email_address = os.getenv("EMAIL_ADDRESS")
email_password = os.getenv("EMAIL_PASSWORD")

# Read the list of contacts to send email to
contacts = []
with open(Path('contacts.txt')) as file:
	lines = file.readlines()
	# for each line we have name and email separated by a comma
	contacts = [tuple(x.split(',')) for x in lines]

print(contacts)