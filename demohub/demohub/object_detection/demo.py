# Copyright (c) OpenMMLab. All rights reserved.
import os
os.sys.path.append('/data/demohub/demohub')
import os.path as osp
from argparse import ArgumentParser

import torch
from mmdet.apis import (async_inference_detector, inference_detector,
                        init_detector)

from demohub.utils import structure_file_path, download_url, Range, FileTypes


MODEL_ZOO = {
    'CascadeRCNN': {
        'config': '/data/demohub/demohub/demohub/object_detection/mmdetection-master/configs/cascade_rcnn/cascade_mask_rcnn_x101_64x4d_fpn_mstrain_3x_coco.py',
        'ckpt': {
            'url': 'https://download.openmmlab.com/mmdetection/v2.0/cascade_rcnn/cascade_mask_rcnn_x101_64x4d_fpn_mstrain_3x_coco/cascade_mask_rcnn_x101_64x4d_fpn_mstrain_3x_coco_20210719_210311-d3e64ba0.pth',
            'filename': 'cascade_mask_rcnn_x101_64x4d_fpn_mstrain_3x_coco_20210719_210311-d3e64ba0.pth',
        }
    }
}


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        'img', 
        type=str,
        choices=[FileTypes('jpg', 'png', 'jpeg')],
        help='image to be processed')
    parser.add_argument(
        '--model',
        type=str,
        default='CascadeRCNN',
        choices=MODEL_ZOO.keys(), 
        help=f'model type to be used')
    parser.add_argument(
        '--score-thr', 
        type=float, 
        default=0.5, 
        choices=[Range(0, 1)],
        help='bbox score larger than score-thr will be displayed, ' 
             'score-thr accept float in range(0, 1)')
    args = parser.parse_args()
    return args


def show_result_pyplot(model,
                       img,
                       out_file,
                       result,
                       score_thr=0.5,
                       title='result',
                       wait_time=0,
                       palette=None):
    """Visualize the detection results on the image.

    Args:
        model (nn.Module): The loaded detector.
        img (str or np.ndarray): Image filename or loaded image.
        result (tuple[list] or list): The detection result, can be either
            (bbox, segm) or just bbox.
        score_thr (float): The threshold to visualize the bboxes and masks.
        title (str): Title of the pyplot figure.
        wait_time (float): Value of waitKey param.
                Default: 0.
    """
    if hasattr(model, 'module'):
        model = model.module
    model.show_result(
        img,
        result,
        score_thr=score_thr,
        show=True,
        wait_time=wait_time,
        win_name=title,
        bbox_color=palette,
        text_color=(200, 200, 200),
        mask_color=palette,
        out_file=out_file)


def detect(
    model_name: str,
    config: str,
    checkpoint: str,
    img: str,
    device: str='cuda:0',
    score_thr: float=0.5,
):
    model = init_detector(config, checkpoint, device=device)
    result = inference_detector(model, img)
    dirname, filename, suffix = structure_file_path(img)
    out_file = osp.join(dirname, f'{filename}.{model_name.lower()}.{suffix}')
    show_result_pyplot(
        model,
        img,
        out_file,
        result,
        score_thr=score_thr)

    return out_file


def main(args):
    assert args.model in MODEL_ZOO.keys(), \
        f'expect parameter model in {MODEL_ZOO.keys()} but get {args.model}'
    config = MODEL_ZOO[args.model]['config']
    url = MODEL_ZOO[args.model]['ckpt']['url']
    filename = MODEL_ZOO[args.model]['ckpt']['filename']
    ckpt = download_url(
        url, 
        osp.expanduser('~/.cache/demohub'), 
        filename)
    out_file = detect(
        args.model,
        config,
        ckpt,
        args.img,
        torch.device('cpu'),
    )
    print(out_file)

if __name__ == '__main__':
    args = parse_args()
    main(args)
