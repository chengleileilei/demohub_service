from .shell import *
from .image import *
__all__ = ['subprocess_popen','choose_gpu','pngToJpg','sort_dict_by_priority','center_crop_multiple64']

def sort_dict_by_priority(input_dict):
    return dict(sorted(input_dict.items(), key=lambda x: x[1]['priority']))


# d = {"b":{"1":2,"2":2,"priority":2},"a":{"1":2,"2":2,"priority":1}}
# print(sort_dict_by_priority(d))