import argparse
import os.path as osp

import cv2
import numpy as np

def read_image(image_path: str):
    return cv2.imread(image_path, 1)

def equalize_hist(image: np.ndarray, space='rgb'):
    if space == 'rgb':
        image = image
        (c1, c2, c3) = cv2.split(image)
        c1 = cv2.equalizeHist(c1)
        c2 = cv2.equalizeHist(c2)
        c3 = cv2.equalizeHist(c3)
        image = cv2.merge((c1, c2, c3))
    elif space == 'hsv':
        image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
        image = list(cv2.split(image))
        image[0] = cv2.equalizeHist(image[0])
        image = cv2.merge(image)
        image = cv2.cvtColor(image, cv2.COLOR_YCrCb2BGR)
    else:
        raise ValueError("expect space in [rgb, hsv]")
    return image

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
        "--space", 
        type=str,
        default="rgb",
        help="space to equalize hist, support rgb and hsv"
    )
    args = parser.parse_args()
    return args

def main():
    args = parse_arg()
    image = read_image(args.image_path)
    image = equalize_hist(image, args.space)
    output_path = osp.join(
        osp.dirname(args.image_path), 
        osp.basename(args.image_path)+'.eh.{}.jpg'.format(args.space))
    print("output_path is {}".format(output_path))
    save_image(image, output_path)

if __name__ == "__main__":
    main()