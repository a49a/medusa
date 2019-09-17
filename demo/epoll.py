import logging
import socket, select

ADDRESS = 'localhost'
PORT = 8080

logger = logging.getLogger("server")

def initLog():
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler("network-server.log")
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

if __name__ == "__main__":
    initLog()

    try:
        listen_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as msg:
        logger.error("create socket failed")
    try:
        epoll_fd = select.epoll()
    except select.error as msg:
        logger.error(msg)