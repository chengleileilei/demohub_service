# -*- coding: utf-8 -
import os,sys
from utils import subprocess_popen,pngToJpg
# import subprocess

basedir = os.path.abspath(os.path.dirname(__file__)).replace('/web','')

def generate_command(conda_env,demo_path,image_path,demoparams):
    command = 'source /opt/conda/etc/profile.d/conda.sh\n'
    command +=  'conda activate ' +conda_env +'\n'  # 'conda activate ' + env + '\n'
    command +=  'python ' + demo_path + ' ' + '\"' + image_path + '\"' + ' ' + demoparams  
    return command

def run_model(classname,demoname,image_path,demoparams,conda_env):
    """ common models funs
    """
    demo_path = basedir + '/demohub/demohub/' + classname + '/' + demoname + '/demo.py'
    command = generate_command(conda_env,demo_path,pngToJpg(image_path),demoparams)
    print(command)
    res_arr = subprocess_popen(command)
    print('res_arr:',res_arr)
    return res_arr

def generate_watermark_embed_command(conda_env,demo_path,image_path,watermark_path,demoparams = ''):
    command = 'source /opt/conda/etc/profile.d/conda.sh\n'
    command +=  'conda activate ' +conda_env +'\n'  # 'conda activate ' + env + '\n'
    command +=  'python ' + demo_path+' ' + '--img' + ' ' + '\"' + image_path  +'\"' + ' '  + '--watermark' + ' ' +'\"'+watermark_path +'\"' # + ' ' + demoparams  
    return command

def run_watermark_embed(classname,demoname,image_path,watermark_path,demoparams,conda_env):
    """ water mark embed
    """
    demo_path = basedir + '/demohub/demohub/' + classname + '/' + demoname + '/embed.py'
    command = generate_watermark_embed_command(conda_env,demo_path,pngToJpg(image_path),watermark_path,demoparams)
    print(command)
    res_arr = subprocess_popen(command)
    print('res_arr:',res_arr)
    # return [res_arr[-1]]
    return res_arr

def generate_watermark_extract_command(conda_env,demo_path,image_path,watermark_path,demoparams = ''):
    command = 'source /opt/conda/etc/profile.d/conda.sh\n'
    command +=  'conda activate ' +conda_env +'\n'  # 'conda activate ' + env + '\n'
    command +=  'python ' + demo_path+' ' + '--img' + ' ' + '\"' + image_path  +'\"' # + ' ' + demoparams  
    return command

def run_watermark_extract(classname,demoname,image_path,demoparams,conda_env):
    """ water mark embed
    """
    demo_path = basedir + '/demohub/demohub/' + classname + '/' + demoname + '/extract.py'
    command = generate_watermark_extract_command(conda_env,demo_path,image_path,demoparams)
    print(command)
    res_arr = subprocess_popen(command)
    print('res_arr:',res_arr)
    # return [res_arr[-1]]
    return res_arr
