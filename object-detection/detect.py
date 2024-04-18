import shutil

import torch
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="Object Detection CLI")

    parser.add_argument("filename", type=str, help="Image file to analyze")

    return parser.parse_args()


if __name__ == "__main__":

    args = parse_arguments()

    # Model
    model = torch.hub.load("ultralytics/yolov5", "yolov5s")

    # Images
    img = args.filename

    # Inference
    results = model(img)

    # Results
    objects = [v[-1] for v in results.pandas().xyxy[0].values.tolist()]
    if "cat" in objects:
        print("Schiuma trovato! - 1")
    else:
        print("Schiuma non c'è! - 1")

    results.save(save_dir="runs/detect/exp")

    shutil.move("/home/app/runs/detect/exp/output.jpg", "/home/app/output/output_detect.jpg")
