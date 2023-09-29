import os
import logging
import smtplib
from email.message import EmailMessage
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

class EmailAction:
    def send_email(self, to_email):
        try:
            # Load credentials from the saved file (or perform OAuth 2.0 authentication if no credentials are found)
            creds = None
            if os.path.exists('token.json'):
                creds = Credentials.from_authorized_user_file('token.json')
            if not creds or not creds.valid:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'C:/Users/Ashwani Anand/Documents/Rasa_Projects/install_demo/client_secret_304837254295-2jk5vo8c497stbhgdd3viqmh7rmaskfc.apps.googleusercontent.com.json',
                    SCOPES,
                    redirect_uri='https://ab16-103-214-63-220.ngrok.io/webhook'
                )
                creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open('token.json', 'w') as token:
                    token.write(creds.to_json())

            # Set up the SMTP server with your Gmail details
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()

            # Use OAuth 2.0 credentials for authentication
            server.ehlo()
            server.login('ashwaniworksonml@gmail.com', None, initial_response_ok=True)

            # Compose the email message
            msg = EmailMessage()
            msg.set_content('Hi. This is a sample email sent from Rasa Bot. If you are seeing this, then have a good day.')
            msg['Subject'] = 'Rasa Chatbot Notification'
            msg['From'] = 'ashwaniworksonml@gmail.com'
            msg['To'] = to_email

            # Send the email
            server.send_message(msg)
            server.quit()
            return True
        except Exception as e:
            logging.error(f"Error: {e}")
            return False
