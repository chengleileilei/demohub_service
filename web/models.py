# -*- coding: utf-8 -
import os,sys
from utils import subprocess_popen,pngToJpg
import subprocess

basedir = os.path.abspath(os.path.dirname(__file__)).replace('/web','')

def generate_command(env,demo_dir,image_dir,demoparams):
    command = 'source /opt/conda/etc/profile.d/conda.sh\n'
    command +=  'conda activate ' +env +'\n'  # 'conda activate ' + env + '\n'
    command +=  'python ' + demo_dir + ' ' + '\"' + image_dir + '\"' + ' ' + demoparams  
    return command

def run_model(classname,demoname,image_dir,demoparams,conda_env):
    env = conda_env
    demo_dir = basedir + '/demohub/demohub/' + classname + '/' + demoname + '/demo.py'
    command = generate_command(env,demo_dir,pngToJpg(image_dir),demoparams)
    print(command)
    res_arr = subprocess_popen(command)
    print('res_arr:',res_arr)
    # return [res_arr[-1]]
    return res_arr
