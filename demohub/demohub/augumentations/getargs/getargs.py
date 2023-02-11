import albumentations as A
import json

def change_type(byte):    
    if isinstance(byte,bytes):
        return str(byte,encoding="utf-8")  
    return json.JSONEncoder.default(byte)

def getFunInfo(fun_name:str):
    """获取函数参数信息"""
    f = eval(fun_name)
    argcount = f.__code__.co_argcount
    varnames = f.__code__.co_varnames
    defaults = f.__defaults__
    doc = f.__doc__
    return (argcount,varnames,defaults,doc)

def getAlbumFunInfo(fun_name:str):
    """获取albumentation模块类函数参数等信息

    输出：__init__函数的参数信息 和 Class的注释

    """
    doc = eval(fun_name).__doc__
    class_init_fun = eval(fun_name+'.__init__')
    argcount = class_init_fun.__code__.co_argcount
    varnames = class_init_fun.__code__.co_varnames
    defaults = class_init_fun.__defaults__
    return (argcount,varnames,defaults,doc)

def generateAlbumFunArgs(fun_name:str):
    argdata = {}
    arg_num, arg_names, arg_default, doc = getAlbumFunInfo(fun_name)
    # print(arg_num, arg_names, arg_default)
    argdata['args']={}

    for i in range(1,arg_num-len(arg_default)):
        argdata['args'].setdefault(arg_names[i],{"default":""})
    for i in range(arg_num-len(arg_default),arg_num):
        argdata['args'].setdefault(arg_names[i],{"default":str(arg_default[i-(arg_num-len(arg_default))])})
    argdata['doc'] = doc
        # argdata['args'][arg_names[i]] = {"default":arg_default[i-(arg_num-len(arg_default))]}
    return argdata


def main():
    res ={}
    with open('/home/user/demohub_data/demohub/demohub/demohub/augumentations/getargs/pixel_level','r') as f:
        for item in f.readlines():
            fun_name = item.replace('\n','')
            res[fun_name] = generateAlbumFunArgs('A.'+fun_name)
    json_data = json.dumps(res,indent=4)
    with open('/home/user/demohub_data/demohub/demohub/demohub/augumentations/getargs/pixel_level.json', 'w') as f:
        f.write(json_data)

def main2():
    res ={}
    with open('/home/user/demohub_data/demohub/demohub/demohub/augumentations/getargs/spatial_level','r') as f:
        for item in f.readlines():
            fun_name = item.replace('\n','')
            res[fun_name] = generateAlbumFunArgs('A.'+fun_name)
    json_data = json.dumps(res,indent=4)
    with open('/home/user/demohub_data/demohub/demohub/demohub/augumentations/getargs/spatial_level.json', 'w') as f:
        f.write(json_data)

        
if __name__ == "__main__":
    main2()


