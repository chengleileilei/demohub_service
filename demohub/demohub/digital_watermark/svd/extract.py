import numpy as np
import cv2
from PIL import Image
# from Method.LSB import LSB_extract
# from Method.DCT import DCT_extract
from SVD.SVD import SVD_extract
# from Method.DWT import DWT_extract
import argparse,os
__method = {
    # 'LSB': LSB_extract,
    # 'DCT': DCT_extract,
    # 'DWT': DWT_extract,
    # 'DFT': DFT_extract,
    'SVD': SVD_extract,
}

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--img', type = str,default = os.path.abspath("marked_img.png"))
    parser.add_argument('--form', type = str, default = "img")
    parser.add_argument('--method', type = str, default = "SVD")
    args = parser.parse_args()
    args.img = args.img.replace("&t","")
    img = cv2.imread(args.img)
    form = args.form
    if args.method not in __method.keys():
         raise ValueError("no such method")
    extracted_watermark = __method[args.method](img, form)
    output_path = os.path.join(
        os.path.dirname(args.img),
        os.path.basename(args.img)+'.extractmark.{}.png'.format(args.method))
    if form == 'img':
        cv2.imwrite(output_path,extracted_watermark)
        print(output_path)
    else:
        print("value = ", extracted_watermark)
    
    