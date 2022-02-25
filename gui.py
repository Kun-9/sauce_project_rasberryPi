from turtle import textinput
import serial
import time
from tkinter import *

sr = serial.Serial('/dev/ttyUSB1', 9600, timeout = 1)
msg = "2,5 6 4 5 6 0,10 35 20 34 28 0,1 1 0 1 1 0"

root = Tk()

# 타이틀
root.title('Print Source')

# 창 크기
root.geometry('640x480+200+200')

# 창 크기 변경 불가
root.resizable(False, False)

def sendStr():
    print(sourceNum.get())
    # sr.write(msg.encode())

btn1 = Button(root, width=10, height=3, text = 'Button1', command = sendStr)
btn1.pack()

sourceNum = Entry(root, width=1)
sourceNum.pack()

listbox = Listbox(root, selectmode='single', height=5)

listbox.pack


# tField = textinput(root)
# tField.pack(fmt, v1, v2, ...)





root.mainloop()

