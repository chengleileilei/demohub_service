import argparse
import os.path as osp

import cv2
import numpy as np

def read_image(image_path: str):
    return cv2.imread(image_path, 1)

def canny(image: np.ndarray,threshold1=100,threshold2=200):
    edges = cv2.Canny(image,threshold1,threshold2)
    return edges

def save_image(image: np.ndarray, output_path: str):
    cv2.imwrite(output_path, image)

def parse_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "image_path", 
        type=str,
        help="path to input image *.jpg"
    )
    parser.add_argument(
        "--threshold1", 
        type=str,
        default="100",
        help="threshold1"
    )
    parser.add_argument(
        "--threshold2", 
        type=str,
        default="200",
        help="threshold2"
    )
    args = parser.parse_args()
    return args

def main():
    args = parse_arg()
    image = read_image(args.image_path)
    image = canny(image,int(args.threshold1),int(args.threshold2))
    output_path = osp.join(
        osp.dirname(args.image_path), 
        osp.basename(args.image_path)+'.canny.jpg')
    print("output_path is {}".format(output_path))
    save_image(image, output_path)

if __name__ == "__main__":
    main()