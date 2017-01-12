# -*- coding: utf-8 -*-
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise SystemExit('need parameter: debug | serv')
    else:
        from serv import Serv
        Serv(sys.argv[1]).start()
