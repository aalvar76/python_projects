# Email Sender Script

This is a Python script for sending emails with HTML content to a list of email addresses read from a file.

## Features

- Send HTML content via email to multiple recipients.
- Read email addresses from a file.
- Customizable subject line and sender email address.

## Requirements

- Python 3.x
- `smtplib` library for sending emails
- `email.message` module for creating email messages
- A configured email account that supports SMTP

## Usage

1. Clone this repository:
2. Navigate into the project directory:

    ```bash
    cd email_sender
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Prepare your email content in HTML format and save it as `email_content.html` in the project directory.

5. Create a file named `recipients.txt` containing the list of email addresses, with each address on a new line.

6. Open the `.env` file and update the following variables with your email configuration:
    - `SMTP_SERVER`: Your SMTP server address
    - `SMTP_PORT`: Port number (usually 587 for TLS)
    - `EMAIL_ADDRESS`: Your sender email address
    - `EMAIL_PASSWORD`: Your email password

7. Run the script:

    ```bash
    python email_sender.py
    ```

8. Follow the prompts to enter the subject line for your email.

## Example

Suppose you have the following HTML content saved as `email_content.html`:

```html
<html>
<head></head>
<body>
    <h1>Hello!</h1>
    <p>This is a test email sent via Python.</p>
</body>
</html>
