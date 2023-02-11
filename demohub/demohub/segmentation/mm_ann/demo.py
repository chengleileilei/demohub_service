from mmseg.apis import inference_segmentor, init_segmentor
from mmseg.apis import show_result_pyplot
import os 
import argparse
import numpy as np 


root_dir = os.path.dirname(os.path.abspath(__file__))
class_dir = os.path.abspath(os.path.join(root_dir, ".."))
# /root/demohub/demohub/demohub/segmentation'

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
    res_image_name = 'ann_' + image_name
    
    out_file = os.path.join(image_dir,res_image_name)

    config_file = class_dir+'/mmsegmentation/configs/ann/ann_r50-d8_512x1024_40k_cityscapes.py'
    # 从 model zoo 下载 checkpoint 并放在 `checkpoints/` 文件下
    # 网址为: http://download.openmmlab.com/mmsegmentation/v2.0/faster_rcnn/faster_rcnn_r50_fpn_1x_coco/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth
    checkpoint_file = class_dir+'/mmsegmentation/checkpoints/ann_r50-d8_512x1024_40k_cityscapes_20200605_095211-049fc292.pth'
    device = 'cuda:'+str(choose_gpu())
    # 初始化检测器
    model = init_segmentor(config_file, checkpoint_file, device=device)
    # 推理演示图像
    result = inference_segmentor(model, image_path)
    # print('result:',result)
    show_result_pyplot(model, image_path,result,  out_file = out_file)
    print(out_file)

if __name__ == "__main__":
    # print( '***',class_dir)

    main()