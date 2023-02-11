import torch
import os 
import argparse

root_path = os.path.abspath(os.path.dirname(__file__))



def parse_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "image_path", 
        type=str,
        help="path to input image *.jpg"

    )
    args = parser.parse_args()
    return args

def main():
    args = parse_arg()
    image_path = args.image_path


    # Model
    model = torch.hub.load(root_path+'/yolov5', 'custom', path=root_path+'/yolov5s.pt',source='local')  # or yolov5n - yolov5x6, custom

    # Images
    # img = 'airplane.jpg'  # or file, Path, PIL, OpenCV, numpy, list


    # Inference
    # image_path = root_path+"/dog.jpeg"
    results = model(image_path)


    results.save(save_dir=root_path+"/results")  # or .show(), .save(), .crop(), .pandas(), etc.

    print(root_path+"/results/"+image_path.split('/')[-1].split('.')[0] +'.jpg')

if __name__ == "__main__":
    main()