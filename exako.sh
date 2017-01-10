#! /bin/sh

start() {
    venv/bin.activate
    nohup python src/exako.py serv &
}

stop() {
    kill -9 $(ps -ef | grep '[e]xako.py serv' | awk '{print $2}')
}

restart() {
    stop
    start
}