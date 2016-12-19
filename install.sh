# require venv path for python 3.5.2
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt

# Init maria database
echo Please input password for mysql root user:
mysql -u user -p < install.sql