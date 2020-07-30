"""
Mail sender module
"""

import argparse

from mail_sender.cli_reader import read_cli_arguments
from mail_sender.credentials import Credentials
from mail_sender.message_builder import make_message
from mail_sender.smtp_server import SMTPServer


def send_mail(smtp_server: SMTPServer, send_from, send_to, subject, text, files=None):
    assert isinstance(send_to, list)
    msg = make_message(send_from, send_to, subject, text, files)
    print(msg)
    smtp_server.send_mail(send_from, send_to, msg)


if __name__ == "__main__":
    inputs: argparse.Namespace = read_cli_arguments()
    credentials = None
    print(inputs.username)
    if inputs.username != "" and inputs.password != "":
        print("Credential provided")
        credentials = Credentials(inputs.username, inputs.password)
    with SMTPServer(inputs.host, inputs.port, credentials=credentials) as s:
        send_mail(s, inputs.sender, inputs.recipients, inputs.topic, inputs.body,
                  files=inputs.files)

    print("sent")
