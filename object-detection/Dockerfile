FROM python:3.12

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install ffmpeg libsm6 libxext6  -y

RUN mkdir /home/app
WORKDIR /home/app

RUN git clone https://github.com/ultralytics/yolov5
RUN pip install -r yolov5/requirements.txt

COPY detect.py /home/app
