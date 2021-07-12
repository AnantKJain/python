import threading 

def a():
    while True:
        print("aaaaa")
def b():
    while True:
        print("bbbbb")

def c():
    print("To check no. of threads= 'cat /proc/PID/status'")

x1 = threading.Thread( target=a)
x2 = threading.Thread( target=b)

x1.start()
x2.start()
