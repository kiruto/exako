git checkout -f master
git pull origin master
venv/bin/activate
pip install -r requirements.txt
echo http service start
# mysql.server start
/etc/init.d/mysql start
nohup venv/bin/python start.py &
