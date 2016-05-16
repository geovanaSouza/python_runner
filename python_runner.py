import time, threading

def foo():
    print(time.ctime())
    threading.Timer(3, foo).start()

if __name__ == "__main__":
    print('Ctrl+C to stop......')
    print('')
    foo()
