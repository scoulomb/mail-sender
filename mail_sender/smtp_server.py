import smtplib
from dataclasses import dataclass
from typing import Optional

from mail_sender.credentials import Credentials


@dataclass
class SMTPServer:
    server: str
    port: int
    credentials: Optional[Credentials]

    def __enter__(self):
        self.s = smtplib.SMTP(self.server, self.port)
        if self.credentials is not None:
            self.s.ehlo()
            self.s.starttls()
            self.s.login(self.credentials.username, self.credentials.password)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.s.close()

    def send_mail(self, send_from: str, send_to: str, message: str):
        self.s.sendmail(send_from, send_to, message)
