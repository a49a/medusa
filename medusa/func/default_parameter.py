from datetime import datetime
from time import sleep


def log(msg, when=datetime.now()):
    print(msg, when)


log("f")
sleep(0.5)
log("b")
