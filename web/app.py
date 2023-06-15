# encoding:utf8
from init import initJsonData,find_subdir,find_subfile,exist_file
# from models import models.run_model 
import models
from flask import Response, Flask, request,jsonify,render_template
import os,random,string
import json
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix

import utils

current_path = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_path)

app = Flask(__name__,static_folder=current_path+'/dist/static',template_folder=current_path)

CORS(app, resources=r'/*')

# 解决jsonify中文显示为ascii码的问题
app.config["JSON_AS_ASCII"] = False


# 获取相对路径对应特定参考系的绝对路径
def getAbsPath( relative_path, reference_path):
    count = relative_path.count("../")
    relative_path = relative_path.replace('../','')
    reference_path_list = reference_path.split("/")
    for v in reference_path_list:
        if v=='':
            reference_path_list.remove(v)
    reference_path_list= reference_path_list[:len(reference_path_list)-count]
    reference_path = ''
    for s in reference_path_list:
        reference_path += "/" + s
    return reference_path+'/'+relative_path.replace("./","")

@app.route("/", methods=['post', 'get'])
def getIndexe():
    return render_template('dist/index.html') 

@app.route("/absimage", methods=['post', 'get'])
def getAbsImage():
    path = request.args.get('path')
    resp = Response(open(path, 'rb'), mimetype="image/jpeg")
    return resp

@app.route("/image", methods=['post', 'get'])
def getImage():
    path = request.args.get('path')
    # print(path)
    path = current_path + "/images/" + path
    # path = os.path.abspath(path)
    resp = Response(open(path, 'rb'), mimetype="image/jpeg")
    return resp


@app.route("/data",methods=['post','get'])
def getData():
    # print(current_path+'/mockData.json')
    result = json.load(open(current_path+'/mockData.json','r',encoding='utf-8'))
    t = {}
    path = root_dir+'/demohub/demohub'
    type_dirs = find_subdir(path)
    for type_dir in type_dirs:
        # print(type_dir.path)
        # print(exist_file(type_dir.path,"setting.json"))
        if (exist_file(type_dir.path,"setting.json")):
            s = json.load(open(type_dir.path+'/setting.json','r',encoding='utf-8'))
            t[type_dir.name] =s
            t[type_dir.name]["models"] = {}
            model_dirs = find_subdir(type_dir.path)
            for model_dir in model_dirs:
                if (exist_file(model_dir.path,"setting.json")):
                    model_json = json.load(open(model_dir.path+'/setting.json','r',encoding='utf-8'))
                    image_path = getAbsPath(model_json["input_image_name"], model_dir.path)
                    model_json["input_image_name"] = image_path
                    image_path = getAbsPath(model_json["output_image_name"], model_dir.path)
                    model_json["output_image_name"] = image_path
                    # print(image_path)
                    for i in range(len(model_json["show_images"])):
                        model_json["show_images"][i] = getAbsPath(model_json["show_images"][i], model_dir.path)
                    # 水印模型的watermark_images路径
                    if "watermark_images" in model_json:
                        for i in range(len(model_json["watermark_images"])):
                            model_json["watermark_images"][i] = getAbsPath(model_json["watermark_images"][i], model_dir.path)
                    t[type_dir.name]["models"][model_dir.name] = model_json
    # print(type(t),t)
    t = utils.sort_dict_by_priority(t)
    result["model_type"] = t
    return Response(json.dumps(result), mimetype='application/json')
    # return jsonify(result)

#  http://127.0.0.1:5000/like?type=classification&&model=alexnet
@app.route("/like",methods=['post','get'])
def like():
    model_type = request.args.get("type")
    model_name = request.args.get("model")
    model_dir = root_dir+'/demohub/demohub/'+ model_type+'/'+model_name+'/setting.json'
    s = json.load(open(model_dir,'r',encoding='utf-8'))
    s["likes"] += 1
    with open(model_dir, 'w',encoding='utf-8') as write_f:
        write_f.write(json.dumps(s, indent=4, ensure_ascii=False))
    return jsonify(s["likes"])

@app.route("/dislike",methods=['post','get'])
def dislike():
    model_type = request.args.get("type")
    model_name = request.args.get("model")
    model_dir = root_dir+'/demohub/demohub/'+ model_type+'/'+model_name+'/setting.json'
    s = json.load(open(model_dir,'r',encoding='utf-8'))
    if s["likes"] > 0:
        s["likes"] -= 1
        with open(model_dir, 'w',encoding='utf-8') as write_f:
            write_f.write(json.dumps(s, indent=4, ensure_ascii=False))
        return jsonify(s["likes"])
    else:
        return jsonify(s["likes"])


#  http://127.0.0.1:5000/views?type=classification&&model=alexnet
@app.route("/pageviews",methods=['post','get'])
def pageviews():
    model_type = request.args.get("type")
    model_name = request.args.get("model")
    model_dir = root_dir+'/demohub/demohub/'+ model_type+'/'+model_name+'/setting.json'
    s = json.load(open(model_dir,'r',encoding='utf-8'))
    s["pageviews"] += 1
    with open(model_dir, 'w',encoding='utf-8') as write_f:
        write_f.write(json.dumps(s, indent=4, ensure_ascii=False))
    return jsonify(s["pageviews"])


@app.route('/markdown',methods=['GET','POST'])
def markdown():
    model_type = request.args.get("type")
    model_name = request.args.get("model")
    if (model_name != None and model_name != ''):
        model_dir = root_dir+'/demohub/demohub/'+ model_type+'/'+model_name +'/'
    else:
        model_dir = root_dir+'/demohub/demohub/' + model_type +'/'

    markdown_name_cn = "introduction_cn.md"
    markdown_name_en = "introduction_en.md"

    with open(model_dir+markdown_name_cn,'r',encoding='utf-8') as f:
        md_cn = f.read()
    with open(model_dir+markdown_name_en,'r',encoding='utf-8') as f:
        md_en = f.read()
    res = {'en':md_en,'cn':md_cn}
    return jsonify(res)

@app.route('/upload',methods=['GET','POST'])
def uploadimage():
    #生成随机字符串，防止图片名字重复
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    #获取图片文件 name = upload
    img = request.files.get('image')
    #定义一个图片存放的位置 存放在static下面
    path = current_path+"/source_images/"
    #图片名称 给图片重命名 为了图片名称的唯一性
    imgName = ran_str+img.filename.replace(" ","_")
    #图片path和名称组成图片的保存路径
    file_path = path+imgName
    #保存图片
    img.save(file_path)
    #这个是图片的访问路径，需返回前端（可有可无）
    return file_path 

@app.route('/submit',methods=['GET','POST'])
def submit():
    p = request.json
    classname = p['classname']
    demoname = p['demoname']
    demoparams = p['args']
    image_path = p["local_image_url"]
    conda_env = p['conda_env']
    # print("收到的原始参数：",demoparams)
    demoparams_str = ''
    for (arg_name,arg_value) in demoparams.items():
        demoparams_str += '--' +arg_name + ' \"' + str(arg_value) + '\" ' 
    demoparams_str.replace("(","\(").replace(")","\)")  # inux5.0之后，bash命令参数不能带有括号，需要转译
    # conda_env = p["conda_env"]
    # print(demoparams_str)
    res = models.run_model(classname,demoname,image_path,demoparams_str,conda_env)
    # print("kkkkres:",res)
    res = jsonify(res)
    return res

@app.route('/verification.html',methods=['GET','POST'])
def verfi():
    return render_template('dist/verification.html') 

@app.route('/watermark/embed',methods=['GET','POST'])
def embed():
    p = request.json
    classname = p['classname']
    demoname = p['demoname']
    demoparams = p['args']
    image_path = p["local_image_url"]
    watermark_path = p['local_watermark_url']
    conda_env = p['conda_env']
    print(p)
    res = models.run_watermark_embed(classname,demoname,image_path,watermark_path,demoparams,conda_env)
    print(res)
    return jsonify(res)

    
@app.route('/watermark/extract',methods=['GET','POST'])
def extract():
    p = request.json
    classname = p['classname']
    demoname = p['demoname']
    demoparams = p['args']
    image_path = p["local_image_url"]
    conda_env = p['conda_env']
    print(p)
    res = models.run_watermark_extract(classname,demoname,image_path,demoparams,conda_env)
    print(res)
    return jsonify(res)

if __name__ == "__main__":
    # 初始化json数据（补充点赞，浏览，默认样例图片数据）
    initJsonData()
    # 在unix环境下，小于1024的端口不能被普通用户绑定
    # ssl_keys = ('cert/demohub.bjtu.edu.cn.pem', 'cert/demohub.bjtu.edu.cn.key')
    ssl_keys = ('cert/aliyun/9380646_demohub.bjtu.edu.cn.pem', 'cert/aliyun/9380646_demohub.bjtu.edu.cn.key')

    # app.run(debug='True',host='0.0.0.0', port=80)

    app.run(debug='True',host='0.0.0.0', port=443,ssl_context=ssl_keys)
    # app.wsgi_app = ProxyFix(app.wsgi_app)
    # app.run(ssl_context=ssl_keys)   


