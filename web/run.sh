source /opt/conda/etc/profile.d/conda.sh
conda activate web_flask
nohup python /root/demohub/web/app.py > /root/demohub/web/run.log 2>&1 &