from mmdet.apis import init_detector, inference_detector
from mmdet.apis import show_result_pyplot
import os 
import cv2
import argparse
import numpy as np 

root_dir = os.path.dirname(os.path.abspath(__file__))
class_dir = os.path.abspath(os.path.join(root_dir, ".."))

import sys
utils_path = os.path.abspath(os.path.join(root_dir,'../'*4))
utils_path = os.path.join(utils_path,'web')
sys.path.append(utils_path)
from utils import choose_gpu

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
    image_dir = os.path.abspath(os.path.dirname(image_path))

    image_name = image_path.split('/')[-1]
    res_image_name = 'faster_rcnn_' + image_name
    
    out_file = os.path.join(image_dir,res_image_name)

    config_file = class_dir+'/mmdetection/configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'
    # 从 model zoo 下载 checkpoint 并放在 `checkpoints/` 文件下
    # 网址为: http://download.openmmlab.com/mmdetection/v2.0/faster_rcnn/faster_rcnn_r50_fpn_1x_coco/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth
    checkpoint_file = class_dir+'/mmdetection/checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'
    device = 'cuda:'+str(choose_gpu())
    # 初始化检测器
    model = init_detector(config_file, checkpoint_file, device=device)
    # 推理演示图像
    result = inference_detector(model, image_path)
    # print('result:',result)
    show_result_pyplot(model, image_path,result, score_thr=0.8, out_file = out_file)
    print(out_file)

    # cv2.imwrite("{}/{}.jpg".format(out_dir, 122), img)
if __name__ == "__main__":
    main()
