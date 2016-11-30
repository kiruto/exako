git checkout -f master
git pull origin master
venv/bin/activate
pip install -r requirements.txt
echo http service start
# run nginx
# run redis
# run sentry
# mysql.server start
/etc/init.d/mysql start
nohup venv/bin/python start.py &
