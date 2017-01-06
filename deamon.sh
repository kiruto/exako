#! /bin/sh
app_path="~/exako"

start() {
    "$app_path/venv/bin.activate"
    nohup python src/start.py &
}

stop() {
    pkill -9 python src/start.py
}
