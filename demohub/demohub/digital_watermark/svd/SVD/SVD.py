import cv2
from .blind_watermark import WaterMark
from .LSB import LSBSteg
import numpy as np

def embed_shape(image, h, w):
    steg = LSBSteg(image) 
    binw = steg.binary_value(w, 16) #Width coded on to byte so width up to 65536
    binh = steg.binary_value(h, 16)
    steg.put_binary_value(binw) #Put width
    steg.put_binary_value(binh) #Put height
    return steg.image

def extract_shape(image, form):
    steg = LSBSteg(image) 
    width = int(steg.read_bits(16),2) #Read 16bits and convert it in int
    height = int(steg.read_bits(16),2)
    if form == 'img':
        return np.array([height, width])
    else:
        return height

def SVD_embed(image, watermark, form = "img"):
    if form == 'text':
        form = 'str'
    bwm = WaterMark(password_wm=1, password_img=1)
    bwm.read_img(img = image)
    bwm.read_wm(wm_content=watermark, mode=form)
    img_encoded = bwm.embed()
    len_wm = len(bwm.wm_bit)
    if form == 'img':
        h, w, _= watermark.shape
    else:
        h, w = len_wm, 0
    img_encoded = embed_shape(img_encoded, h, w)
    return img_encoded

def SVD_extract(marked_img,  form = "img"):
    if form == 'text':
        form = 'str'
    bwm1 = WaterMark(password_wm=1, password_img=1)
    wm_shape = extract_shape(marked_img, form)
    watermark = bwm1.extract(embed_img= marked_img, wm_shape=wm_shape,  mode=form)
    return watermark
