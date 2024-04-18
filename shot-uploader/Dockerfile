FROM python:3.12

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN mkdir /home/app
WORKDIR /home/app

COPY upload.py /home/app/upload.py