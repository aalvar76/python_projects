import os
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file
load_dotenv(find_dotenv('.env.dev')) #  replace this '.env.dev' by the environmet file name

# Access environment variables
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = os.getenv("SMTP_PORT")
email_address = os.getenv("EMAIL_ADDRESS")
email_password = os.getenv("EMAIL_PASSWORD")

# Print and check values from env file

print(smtp_server)
print(smtp_port)
print(email_address)
print(email_password)