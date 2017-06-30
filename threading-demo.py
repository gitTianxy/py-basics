# coding=utf-8
from time import sleep
import threading
from datetime import datetime


def music(name, dur):
    print 'START listen music'
    start = datetime.now()
    while True:
        if (datetime.now() - start).seconds > dur:
            print 'STOP listen music'
            break
        print 'listen', name
        sleep(1)


def movie(name, dur):
    print 'START watch movie '
    start = datetime.now()
    while True:
        if (datetime.now() - start).seconds > dur:
            print 'STOP watch movie'
            break
        print 'watch', name
        sleep(1)


threads = []
mutex = threading.Lock()

if __name__ == '__main__':
    print 'main thread START'
    # init
    t1 = threading.Thread(target=music, args=('kevin-music', 5,))
    threads.append(t1)
    t2 = threading.Thread(target=movie, args=('kevin-movie', 10,))
    threads.append(t2)
    # start threads
    for t in threads:
        t.start()
    # main-thread wait
    for t in threads:
        t.join()
    # finish
    print 'main thread FINISH'
