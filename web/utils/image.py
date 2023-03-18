from cv2 import imread, imwrite
import os

def pngToJpg(image_path):
    """
    将png图片转换为jpg，其他格式不变，同时删除原jpg图片
    """
    # 获取绝对路径
    image_path = os.path.abspath(image_path)
    # 获取图片位置路径
    dir_path = os.path.abspath(os.path.join(image_path,'..'))
    # 图片全名，包括后缀
    image_full_name = image_path[len(dir_path):].strip('/')
    # 获取图片后缀
    image_name_suffix = image_path[len(dir_path):].strip('/').split('.')[-1]

    if image_name_suffix == 'png':
        # 获取图片名，不包括后缀
        image_name = image_full_name[:-len(image_name_suffix)-1]

        image = imread(image_path, 1)
        new_image_path = os.path.join(dir_path ,image_name + '.jpg')
        imwrite(new_image_path, image)
        os.remove(image_path)
        return new_image_path
    else:
        return image_path