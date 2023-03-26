import numpy as np
import cv2
from PIL import Image
# from Method.LSB import LSB_embed
# from Method.DCT import DCT_embed
from SVD.SVD import SVD_embed
# from Method.DWT import DWT_embed
import argparse,os
__method = {
    # 'LSB': LSB_embed,
    # 'DCT': DCT_embed,
    # 'DWT': DWT_embed,
    # 'DFT': DFT_embed,
    'SVD': SVD_embed,
}

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--img', type = str,default=os.path.abspath("../image.jpg"))
    parser.add_argument('--form', type = str, default = "img")
    parser.add_argument('--watermark', type = str, default=os.path.abspath("../watermark.png"))
    parser.add_argument('--method', type = str, default = "SVD")
    args = parser.parse_args()
    img = cv2.imread(args.img)
    if args.form == 'img':
        watermark = cv2.imread(args.watermark)
    elif args.form == 'text':
        watermark = args.watermark
    else:
        print('Watermark no such form')
        # raise ValueError("Watermark no such form")
    
    if args.method not in __method.keys() :
         raise ValueError("no such method")
    marked_img = __method[args.method](img, watermark, args.form)

    output_path = os.path.join(
        os.path.dirname(args.img),
        os.path.basename(args.img)+'embeded.{}.png'.format(args.method))
    cv2.imwrite(output_path,marked_img)
    print(os.path.abspath(output_path))