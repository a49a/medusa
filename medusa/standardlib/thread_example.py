import threading
import queue
import time

thread_lock = threading.Lock()

# 队列最大尺寸问题
MAX_SIZE = 4
mq = queue.Queue(MAX_SIZE)



def foo(x):
    print(x)


class Producer(threading.Thread):

    def __init__(self, mq):
        self.mq = mq
        super().__init__()

    def run(self):

        i = 0
        while True:
            self.mq.put(i)
            i += 1
            print("生产: ", self.mq.qsize())


class Consumer(threading.Thread):
    def __init__(self, mq):
        self.mq = mq
        super().__init__()

    def run(self):
        while True:
            msg = self.mq.get()
            print(msg)
            print("消费: ", self.mq.qsize())


p = Producer(mq)
c = Consumer(mq)
p.setDaemon(True)
c.setDaemon(True)
p.start()
c.start()
# timeout
p.join(1)
c.join(1)