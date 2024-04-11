import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from utils.config import Config


class Email:
    def __init__(self):
        config = Config()
        self.to_email, self.from_email, self.password, self.smtp_name = (
            config.cfg["email"]["to_email"],
            config.cfg["email"]["from_email"],
            config.cfg["email"]["password"],
            config.cfg["email"]["smtp_name"],
        )

        self.server = smtplib.SMTP(self.smtp_name)
        self.server.starttls()
        self.server.login(self.from_email, self.password)

    # def __del__(self):
    #     self.server.quit()

    def send_email(self, content, subject="Security Alert"):
        message = MIMEMultipart()
        message["From"] = self.from_email
        message["To"] = self.to_email
        message["Subject"] = subject
        # Add in the message body
        message_body = str(content)
        message.attach(MIMEText(message_body, "plain"))
        self.server.sendmail(self.from_email, self.to_email, message.as_string())


if __name__ == "__main__":
    email = Email()
    email.send_email("test form VisonGuard")
