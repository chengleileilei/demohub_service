#！/bin/bash
source /opt/conda/etc/profile.d/conda.sh
conda activate web_flask

# gunicorn --certfile=./cert/aliyun/9380646_demohub.bjtu.edu.cn.pem --keyfile=./cert/aliyun/9380646_demohub.bjtu.edu.cn.key -w 5 -b 0.0.0.0:443 app:app

nohup gunicorn --certfile=./cert/aliyun/9380646_demohub.bjtu.edu.cn.pem --keyfile=./cert/aliyun/9380646_demohub.bjtu.edu.cn.key -w 5 -b 0.0.0.0:443 app:app > /root/demohub/web/run.log 2>&1 &



# 停止服务命令
# pstree -ap|grep gunicorn
# 然后杀掉主程序