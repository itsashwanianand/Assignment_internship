from actions import EmailAction

def main():
    # Replace with a valid recipient email address
    email_address = "aubnmaiml@gmail.com"

    # Create an instance of EmailAction
    email_action = EmailAction()

    # Call the send_email function and check the result
    result = email_action.send_email(email_address)

    if result:
        print("Email sent successfully!")
    else:
        print("Failed to send email.")

if __name__ == "__main__":
    main()
