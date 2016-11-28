git checkout -f master
git pull origin master
pip install -r requirements.txt
./venv/bin/activate
echo http service start
# mysql.server start
/etc/init.d/mysql start
./venv/bin/python start.py
