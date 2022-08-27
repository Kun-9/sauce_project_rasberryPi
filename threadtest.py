import time
import threading

global a
a = ''

def print_time():
    for i in range(100):
        global a
        time.sleep(1)
        print("name : %s, num : %d, input : %s " % (threading.current_thread().getName(), i, a))
 

def print_time2():
    global a
    while(1):
        a = input()
        print("name : %s, input : %s " % (threading.current_thread().getName(), a))
        time.sleep(5)



if __name__ == "__main__":
    t = threading.Thread(target=print_time)
    t2 = threading.Thread(target=print_time2)
    t.start()
    t2.start()