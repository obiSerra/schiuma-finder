# schiuma-finder

I have a very lazy cat named Schiuma who spends most of his time sleeping in a basket on my desk.

To check on him when I'm not at home (and to ply a bit with some cool tech), I decided to build a small device that can detect his presence.


## Hardware

- Raspberry Pi 4 with 64-bit Raspberry Pi OS
- Trust Trino USB Webcam

## Software

All the software runs on Docker containers using Docker Compose.

1. A `linuxserver/ffmpeg` docker uses the webcam to capture an image
2. A custom docker (`object-detection`) with `yolov5` detects the presence of the cat (and any other object)
3. Another custom docker (`shot-uploader`) uploads the image to `S3` using `boto3` and remove the local files

## Other

The `Raspberry Pi` has `AWS Greengrass` installed with `AWS System Manager` to manage everything remotely.

## Next steps

- integration with telegram bot
- deploy the whole thing on `AWS Greengrass`

Talking about over-engineering! 😅
