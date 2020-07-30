FROM python:3.8

WORKDIR /working_dir

RUN mkdir -p /.local && chmod g+rw /.local && chmod g+rw /working_dir
USER 100002

COPY *.py ./
COPY mail_sender mail_sender

ENTRYPOINT ["python", "send_mail.py"]
