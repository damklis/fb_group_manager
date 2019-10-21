import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class GmailEmailSender(object):

    def __init__(self, email_owner, password, subject):

        self.email_owner = email_owner
        self.__password = password
        self.subject = subject
        self.context = ssl.create_default_context()
        self.gm = "smtp.gmail.com"
        self.server = smtplib.SMTP_SSL(
            host = self.gm,
            port = 465, 
            context=self.context
        )

    def __create_message(self, receiver_email, msg):
        """
        Returns well formatted string message.
        """
        message = MIMEMultipart()
        message["Subject"] = self.subject
        message["From"] = self.email_owner
        message["To"] = receiver_email
        text = MIMEText(msg, "plain")
        message.attach(text)

        return message.as_string()

    def __log_into_mail(self):
        """
        Logs in mail server. Excepting SMTPAuthenticationError.
        Return self or Error Class.
        """
        try:
            self.server.login(self.email_owner, self.__password)
            return GmailEmailSender
        except smtplib.SMTPAuthenticationError as err:
            print("""
                Go to this link and select -> Turn On <-
                https://www.google.com/settings/security/lesssecureapps
            """
            )
            return err
    
    def send_information(self, receiver_email, msg):
        """
        Sends email to provided reciver. 
        """
        str_message = self.__create_message(
            receiver_email, msg
        )

        logging_status = self.__log_into_mail()
        if not issubclass(logging_status, smtplib.SMTPException):
            self.server.sendmail(
                self.email_owner, receiver_email, str_message
            )

    def __str__(self):
        return f"Google emil account: {self.email_owner}."

    