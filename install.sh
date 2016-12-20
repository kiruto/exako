# require venv path for python 3.5.2
if [ ! -d "venv" ]; then
	echo building environment...
	virtualenv venv -p python3
	source venv/bin/activate
	pip install -r requirements.txt
fi

# Init maria database
echo Init database...
echo Please input password for mysql root user:
mysql -u root -p < install.sql
