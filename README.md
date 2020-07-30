- [Dockerhub image](https://hub.docker.com/r/scoulomb/mail-sender).

# Mail sender 

A simple generic mail sender written in python and delivered as a docker package.

Why this project?
- It support file attachment 
- it Dockerizes mail sending. In particular to be used as non-regression side container to send content of a file by email.
- It supports tls authentication. In particular it is useful when using `smtp.gmail.com` and can not use port `465`.
In that case we should use port `587` which requires to put the connection to the SMTP server into TLS mode. 

Note that if using gmail as smtp server, we need to setup less secure app access: https://myaccount.google.com/lesssecureapps

<!--
See mail-sender\basic_mail\basic_send_mail.py
--> 
## User guide

### Usage 

### Prepare 



````shell script
bash
export FROM="rene.coty@gmail.com"
export TO="cool.dev@gmail.com"
export SMTP_PWD="a-secret-pwd"
````

Replace with your own parameter

### Pull 

````shell script
docker pull scoulomb/mail-sender
````

### Help

````shell script
$ docker run scoulomb/mail-sender --help
usage: send_mail.py [-h] --sender SENDER --recipients RECIPIENTS
                    [RECIPIENTS ...] --topic TOPIC --body BODY --files FILES
                    [FILES ...] --host HOST --port PORT [--username USERNAME]
                    [--password PASSWORD]

A mail sender

optional arguments:
  -h, --help            show this help message and exit
  --sender SENDER       Mail sender
  --recipients RECIPIENTS [RECIPIENTS ...]
                        Mail recipients
  --topic TOPIC         Mail topic
  --body BODY           Mail body
  --files FILES [FILES ...]
                        Files to send as attachment
  --host HOST           server
  --port PORT           port
  --username USERNAME   Username
  --password PASSWORD   Password
````

### Run 

#### Sending attachment

````shell script
mkdir shared_folder_sample
echo "My attachment text file" > shared_folder_sample/sample.txt

docker run -v "$(pwd)/shared_folder_sample:/shared_folder_sample" scoulomb/mail-sender \
--sender $FROM \
--recipients $TO \
--topic "non reg results" \
--body "Finf attached the report" \
--files "/shared_folder_sample/sample.txt" \
--host "smtp.gmail.com" --port 587 \
--username $FROM --password $SMTP_PWD
````

## Dev guide

### Run python 

````shell script
cd mail-sender

python send_mail.py \
--sender $FROM \
--recipients $TO \
--topic "non reg results" \
--body "Finf attached the report" \
--files "shared_folder_sample/sample.txt" \
--host "smtp.gmail.com" --port 587 \
--username $FROM --password $SMTP_PWD
````

### Build and Run docker

````shell script
cd mail-sender

docker build . -t mail

docker run -v "$(pwd)/shared_folder_sample:/shared_folder_sample" mail \
--sender $FROM \
--recipients $TO \
--topic "non reg results" \
--body "Finf attached the report" \
--files "/shared_folder_sample/sample.txt" \
--host "smtp.gmail.com" --port 587 \
--username $FROM --password $SMTP_PWD
````

Note `--files` is at root here

<!--
Volume similar to: https://github.com/alpine-docker/git
-->

## Continuous delivery

Every time a change is merged in master, a docker image is built on dockerhub.
We use a dockerhub build rule.
Image is available here: https://hub.docker.com/r/scoulomb/mail-sender

## Tips
 
### Use telnet
 
when looking for SMTP server we can use telnet to test connectivity

````shell script
telnet <host> 25
````

### if name or service unknown

````shell script
sudo systemd-resolve --flush-caches
````

### Google

Google is overriding the `from` with the server user used in authentication.
As such when allowing less secure app access: it enable other user to send mail with your name.
