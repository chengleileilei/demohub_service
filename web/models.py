# -*- coding: utf-8 -
import os,sys
from utils import subprocess_popen,pngToJpg

basedir = os.path.abspath(os.path.dirname(__file__)).replace('/web','')

def active_conda_command(conda_env):
    active_command = 'source /opt/conda/etc/profile.d/conda.sh\n'
    active_command +=  'conda activate ' +conda_env +'\n' 
    return active_command


def get_demo_abspath(classname,demoname,pyname="demo.py"):
    return os.path.join(basedir,'demohub/demohub',classname,demoname,pyname)


def run_model(classname,demoname,image_path,demoparams,conda_env):
    """ common models funs
    """
    demo_path = get_demo_abspath(classname,demoname)
    print(demo_path)
    command = active_conda_command(conda_env)
    command +=  'python ' + demo_path + ' ' + '\"' + pngToJpg(image_path) + '\"' + ' ' + demoparams  
    print(command)
    return subprocess_popen(command)


def run_watermark_embed(classname,demoname,image_path,watermark_path,demoparams,conda_env):
    demo_path = get_demo_abspath(classname,demoname,pyname='embed.py')
    command = active_conda_command(conda_env)
    command +=  'python ' + demo_path+' ' + '--img' + ' ' + '\"' + pngToJpg(image_path)  +'\"' + ' '  + '--watermark' + ' ' +'\"'+watermark_path +'\"'
    print(command)
    return subprocess_popen(command)


def run_watermark_extract(classname,demoname,image_path,demoparams,conda_env):
    demo_path = get_demo_abspath(classname,demoname,pyname='extract.py')
    command = active_conda_command(conda_env)
    command +=  'python ' + demo_path+' ' + '--img' + ' ' + '\"' + image_path  +'\"'  
    print(command)
    return subprocess_popen(command)

def run_diffusion_text2img(classname,demoname,image_path,text_path,demoparams,conda_env):
    demo_path = get_demo_abspath(classname,demoname,pyname='diffusion_text2img.py')
    command = active_conda_command(conda_env)
    command +=  'python ' + demo_path+' ' + '--img' + ' ' + '\"' + pngToJpg(image_path)  +'\"' + ' '  + '--text' + ' ' +'\"'+text_path +'\"'
    print(command)
    return subprocess_popen(command)
