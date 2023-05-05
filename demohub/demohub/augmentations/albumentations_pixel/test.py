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
    image_path = "/home/user/demohub_data/demohub/web/images/cat.jpg"
    image = read_image(image_path)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # fun_comm = "A."+funName + '( ' + funArgs +' )'
    # print("***fun_comm:::",fun_comm)


    transform = A.Compose([
        A.ToGray(always_apply=False, p=0),

        # A.RandomCrop(width=256, height=256),
        # A.HorizontalFlip(p=0.1),
        # A.RandomBrightnessContrast(p=0.5),
    ]) 
    transformed = transform(image=image)

    transformed_image = transformed["image"]

    transform = A.Compose([
        A.ToGray(always_apply=False, p=1),

        # A.RandomCrop(width=256, height=256),
        # A.HorizontalFlip(p=0.1),
        # A.RandomBrightnessContrast(p=0.5),
    ])
    transformed = transform(image=image)

    transformed_image = transformed["image"]
    # output_path = osp.join(
    #     osp.dirname(image_path), 
    #     osp.basename(image_path)+'.albumentations.{}.jpg'.format(funName))
    # save_image(transformed_image,output_path)
    print("output_path is {}".format(1))


if __name__ == "__main__":
    main()



# image = cv2.imread("demo.jpg")
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# transformed = transform(image=image)

# transformed_image = transformed["image"]

# save_image(transformed_image,'demoout.jpg')
