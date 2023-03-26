# 总结杀掉绑定443端口的gunicorn应用命令就是
# kill $(lsof -i:443|awk '{if(NR==2)print $2}')

# pstree -ap|grep gunicorn
# 然后杀掉主程序