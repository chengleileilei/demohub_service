# coding=utf-8

import os
import json
current_path = os.path.dirname(__file__)
root_dir = os.path.dirname(current_path)

default_data = {
    "likes": 0,
    "pageviews": 0,
    "input_image_name": "../../../../web/images/default.png",
    "output_image_name": "../../../../web/images/default.png",
    "author": "DemoHub",
    "show_images": [
        "../../../../web/images/demo.jpg",
        "../../../../web/images/airplane.jpg",
        "../../../../web/images/bird.jpg",
        "../../../../web/images/cat.jpg",
        "../../../../web/images/chair.jpg",
        "../../../../web/images/deer.jpg"
    ]
}
default_markdown = {
    "en": "## No description information is available for this model",
    "cn": "## 此模型暂无说明信息"
}
# reset_data={
#         "show_images": [
#         "../../../../web/images/demo.jpg",
#         "../../../../web/images/airplane.jpg",
#         "../../../../web/images/bird.jpg",
#         "../../../../web/images/cat.jpg",
#         "../../../../web/images/chair.jpg",
#         "../../../../web/images/deer.jpg"
#     ]
# }


def find_subdir(path):
    sub_dirs = []
    for item in os.scandir(path):
        if item.is_dir():
            sub_dirs.append(item)
    return sub_dirs


def find_subfile(path):
    sub_files = []
    for item in os.scandir(path):
        if item.is_dir():
            sub_files.append(item)
    return sub_files

# 目录是否存在某个file


def exist_file(path, filename):
    for item in os.scandir(path):
        # print(item.name)
        if item.is_file() and item.name == filename:
            return True
    return False


def initJsonData():
    # 初始化json数据（补充点赞，浏览量，默认样例图片数据）
    path = root_dir+'/demohub/demohub'
    type_dirs = find_subdir(path)
    for type_dir in type_dirs:
        if (exist_file(type_dir.path, "setting.json")):
            model_dirs = find_subdir(type_dir.path)
            for model_dir in model_dirs:
                if (exist_file(model_dir.path, "setting.json")):
                    # 初始化info markdown文档
                    if(not exist_file(model_dir.path, "introduction_cn.md")):
                        with open(os.path.join(model_dir.path, "introduction_cn.md"),'w') as f:
                            f.write(default_markdown["cn"])
                    if(not exist_file(model_dir.path, "introduction_en.md")):
                        with open(os.path.join(model_dir.path, "introduction_en.md"),'w') as f:
                            f.write(default_markdown["en"])
                    # with open(os.path.join(model_dir.path, "introduction_cn.md"),'w') as f:
                    #     f.write(default_markdown["cn"])
                    # with open(os.path.join(model_dir.path, "introduction_en.md"),'w') as f:
                    #     f.write(default_markdown["en"])


                    model_json = json.load(
                        open(model_dir.path+'/setting.json', 'r', encoding='utf-8'))
                    for key in default_data:
                        if not (key in model_json):
                            model_json[key] = default_data[key]
                    # # 重置参数
                    # for key in reset_data:
                    #     model_json[key] = default_data[key]
                    # 设置默认conda环境为类名+模型名
                    if "conda_env" not in model_json:
                        model_json["conda_env"] = "demohub." + model_dir.name
                    # 设置默认name
                    if "name" not in model_json:
                        model_json["name"] = {
                            "en": model_dir.name,
                            "cn": model_dir.name
                        }
                    # 存在参数则设置参数默认值
                    # if "args" in model_json:
                    #     for arg_name, arg_data in model_json["args"].items():
                    #         if (("default" not in arg_data) or (arg_data["default"] == "")):
                    #             arg_data["default"] = arg_data["values"][0]
                    with open(model_dir.path+'/setting.json', 'w', encoding='utf-8') as write_f:
                        write_f.write(json.dumps(
                            model_json, indent=4, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    initJsonData()
    # print(default_markdown)
