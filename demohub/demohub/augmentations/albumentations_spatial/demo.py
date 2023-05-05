import albumentations as A
import cv2
import numpy as np
import argparse
import os.path as osp


def read_image(image_path: str):
    return cv2.imread(image_path, 1)

def parse_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "image_path", 
        type=str,
        help="path to input image *.jpg"
    )
    parser.add_argument(
        "--funName", 
        # default="Blur",
        type=str,
    )
    parser.add_argument(
        "--funArgs", 
        type=str,
    )

    args = parser.parse_args()
    return args

def save_image(image: np.ndarray, output_path: str):
    cv2.imwrite(output_path, image)

def main():
    args = parse_arg()
    image = read_image(args.image_path)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    fun_comm = "A."+args.funName + '( ' + args.funArgs +' )'
    # print("***fun_comm:::",fun_comm)


    transform = A.Compose([
        eval(fun_comm)
    ])

    transformed = transform(image=image)

    transformed_image = transformed["image"]

    output_path = osp.join(
        osp.dirname(args.image_path), 
        osp.basename(args.image_path)+'.albumentations.{}.jpg'.format(args.funName).replace(' ',''))
    save_image(transformed_image,output_path)
    print("output_path is {}".format(output_path))


if __name__ == "__main__":
    main()



# image = cv2.imread("demo.jpg")
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# transformed = transform(image=image)

# transformed_image = transformed["image"]

# save_image(transformed_image,'demoout.jpg')
