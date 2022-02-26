import config
import smtplib, ssl

class Mail():
    def __init__(self):
        context = ssl.create_default_context()
        self.mail_server = smtplib.SMTP_SSL(config.MAIL_HOST, config.MAIL_PORT, context=context)
        self.mail_server.ehlo()
        self.mail_server.login(config.MAIL_SENDER, config.MAIL_PASSWORD)
    
    def send_mail(self, receiver, subject, message):
        email_body = """\
From: %s
To: %s
Subject: %s

%s
""" % (config.MAIL_SENDER, receiver, subject, message)
        try:
            self.mail_server.sendmail(config.MAIL_SENDER, receiver, email_body)
            self.mail_server.close()
            return True
        except Exception as e:
            print(e)
            self.mail_server.close()
            return False