from datetime import datetime
import os
import boto3
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="Object Detection CLI")

    parser.add_argument("-of", "--original_file", type=str, help="Original image", required=True)
    parser.add_argument("-df", "--detected_file", type=str, help="Image with detection", required=True)

    return parser.parse_args()


def upload_image():
    args = parse_arguments()

    img_name = datetime.now().strftime("%Y%m%d-%H%M%S")

    s3 = boto3.client("s3")
    s3.upload_file(args.original_file, "iot-bucket-rserra", f"{img_name}.jpg")
    s3.upload_file(args.detected_file, "iot-bucket-rserra", f"{img_name}_tracked.jpg")
    print("images uploaded")
    os.remove(args.original_file)
    os.remove(args.detected_file)
    print("images removed")


if __name__ == "__main__":
    upload_image()
