import tkinter
from turtle import width
import source_class
import serial
import time
from tkinter import *

def raise_frame(frame):
    frame.tkraise()
    
def sendBtn():
    sendStr = ""
    cnt = 0
    # 카트리지 번호
    for i in range(6) :
        if int(sourceNum[i].get()) > 0 :
            sendStr += str(i+1) + " " 
            cnt += 1
    print(sendStr)
    sendStr += ","
    
    # 무게
    for i in range(6) :
        if int(sourceNum[i].get()) > 0 :
            sendStr += str(sourceNum[i].get()) + " "
    print(sendStr)
    sendStr += ","
    
    # 액체 여부
    for i in range(6) :
        if int(sourceNum[i].get()) > 0 :
            tmp = sc.getCurrentSourceList()[i].getLiquid()
            sendStr += str(tmp) + " "
    print(sendStr)
    
    sendStr = str(cnt) + "," + sendStr
    
    sr.write(sendStr.encode())
    


sr = serial.Serial('/dev/ttyUSB1', 9600, timeout = 1)
msg = "2,5 6 4 5 6 0,10 35 20 34 28 0,1 1 0 1 1 0"

root = Tk()


# 타이틀
# root.title('Print Source')

# 창 크기
root.geometry('265x210+200+200')

# 창 크기 변경 불가
root.resizable(False, False)

# 메인 창
mainPage = Frame(root)
mainPage.grid(row=0, column=0, sticky='news')
 
# 세팅 창
settingPage = Frame(root)
settingPage.grid(row=0, column=0, sticky='news')

# 소스 추가 창
addSourcePage = Frame(root)
addSourcePage.grid(row=0, column=0, sticky='news')

# 카트리지 등록 창
registPage = Frame(root)
registPage.grid(row=0, column=0, sticky='news')

    
    # print(sourceNum.get())
    # sr.write(msg.encode())


sc = source_class.SourceList()

# sc.addSource("쯔유", 1)
# sc.addSource("간장", 1)
# sc.addSource("고추장", 1)
# sc.addSource("물엿", 1)
# sc.addSource("케찹", 1)
# sc.addSource("물", 1)
# sc.addSource("굴소스", 1)
# sc.addSource("고춧가루", 0)


# sc.register_current_source(3,0)
# sc.register_current_source(1,1)
# sc.register_current_source(5,5)



# listbox = Listbox(root, selectmode='single', height=5)

cartname = ['null','null','null','null','null','null']




for a in range(6):
    if sc.getCurrentSourceExist()[a] == 1 :
        cartname[a] = sc.getCurrentSourceList()[a].getName()
    else :
        cartname[a] = 'x' 


# 버튼

slabel = []
sourceNum = []
Button(mainPage, text='출력', command = sendBtn).grid(row = 3, column = 0, columnspan=12, padx = 2, pady = 10, sticky='news')
Button(mainPage, text='장착 소스 변경', command=lambda:raise_frame(settingPage)).grid(row = 4, column = 0, columnspan=12, padx = 3, pady = 3, sticky='news')

# listbox.pack()
slabel.append(Label(mainPage, text = "카트리지 번호"))
slabel.append(Label(mainPage, text = cartname[0], width=4, height=2))
slabel.append(Label(mainPage, text = cartname[1], width=4, height=2))
slabel.append(Label(mainPage, text = cartname[2], width=4, height=2))
slabel.append(Label(mainPage, text = cartname[3], width=4, height=2))
slabel.append(Label(mainPage, text = cartname[4], width=4, height=2))
slabel.append(Label(mainPage, text = cartname[5], width=4, height=2))
slabel[0].grid(row = 0, column = 0, columnspan=12, padx = 3, pady = 10, sticky='news')
slabel[1].grid(row = 1, column = 0, sticky=N+E+W+S ,columnspan=2, padx = 3, pady = 3)
slabel[2].grid(row = 1, column = 2, sticky=N+E+W+S ,columnspan=2, padx = 3, pady = 3)
slabel[3].grid(row = 1, column = 4, sticky=N+E+W+S ,columnspan=2, padx = 3, pady = 3)
slabel[4].grid(row = 1, column = 6, sticky=N+E+W+S ,columnspan=2, padx = 3, pady = 3)
slabel[5].grid(row = 1, column = 8, sticky=N+E+W+S ,columnspan=2, padx = 3, pady = 3)
slabel[6].grid(row = 1, column = 10, sticky=N+E+W+S ,columnspan=2, padx = 3, pady = 3)

sourceNum.append(Entry(mainPage, width=4))
sourceNum.append(Entry(mainPage, width=4))
sourceNum.append(Entry(mainPage, width=4))
sourceNum.append(Entry(mainPage, width=4))
sourceNum.append(Entry(mainPage, width=4))
sourceNum.append(Entry(mainPage, width=4))
sourceNum[0].grid(row = 2, column = 0, sticky=N+E+W+S ,columnspan=2, padx = 3, pady = 3)
sourceNum[1].grid(row = 2, column = 2, sticky=N+E+W+S ,columnspan=2, padx = 3, pady = 3)
sourceNum[2].grid(row = 2, column = 4, sticky=N+E+W+S ,columnspan=2, padx = 3, pady = 3)
sourceNum[3].grid(row = 2, column = 6, sticky=N+E+W+S ,columnspan=2, padx = 3, pady = 3)
sourceNum[4].grid(row = 2, column = 8, sticky=N+E+W+S ,columnspan=2, padx = 3, pady = 3)
sourceNum[5].grid(row = 2, column = 10, sticky=N+E+W+S ,columnspan=2, padx = 3, pady = 3)

# tField = textinput(root)
# tField.pack(fmt, v1, v2, ...)



# 세팅 페이지
Label(settingPage, text='settingPage').pack(pady='5')
listbox = Listbox(settingPage, selectmode='single', height=5)
listbox.pack(pady='5')



Button(settingPage, text='카트리지에 등록', command=lambda:raise_frame(registPage)).pack()
Button(settingPage, text='소스 추가', command=lambda:raise_frame(addSourcePage)).pack(side='left',padx='32')
Button(settingPage, text='돌아가기', command=lambda:raise_frame(mainPage)).pack(side='left')




# 카트리지 등록 페이지

def registCartridge():
    try :
        num = listbox.curselection()[0]
        sc.register_current_source(int(CartNum.get())-1,num)
        name = sc.getSourceList()[num].getName()
        slabel[int(CartNum.get())].config(text = name)   
        tkinter.messagebox.showinfo(title="알림", message="소스가 등록되었습니다.")
        CartNum.delete(0,END)
        raise_frame(settingPage)
    except :
        tkinter.messagebox.showinfo(title="알림", message="소스를 선택하세요.")
        CartNum.delete(0,END)
        raise_frame(settingPage)
    
        
    
        
    
    
    
Label(registPage, text = '위치 (1 ~ 6)', width = 13, height = 3).grid(row = 1, column = 0, sticky='news')

CartNum = Entry(registPage, width=3)
CartNum.grid(row = 1, column= 1, pady=15)

Button(registPage, text='등록', width = 26, command=registCartridge).grid(row = 3, column = 0, sticky='news', columnspan=2, padx='15', pady='10')
Button(registPage, text='취소', width = 26, command=lambda:raise_frame(settingPage)).grid(row = 4, column = 0, sticky='news', columnspan=2, padx='15')





# 소스 추가 페이지
CheckVariety_1 = IntVar()

Label(addSourcePage, text = '명칭', width = 13, height = 3).grid(row = 1, column = 0, sticky='news')
Label(addSourcePage, text = '액체', width = 13, height = 3).grid(row = 2, column = 0, sticky='news')
sourceName = Entry(addSourcePage, width=14)
sourceName.grid(row = 1, column= 1 ,padx=10, pady=15)
Liquid_check = Checkbutton(addSourcePage, variable=CheckVariety_1, )
Liquid_check.grid(row = 2, column = 1, sticky='news', padx=10, pady=3)


def addSource():
    name = sourceName.get()
    listbox.insert(END, name)

    sc.addSource(name, CheckVariety_1.get())
    tkinter.messagebox.showinfo(title="알림", message="소스가 추가되었습니다.")
    
    
    sc.getSourceList()[-1].getinfo()
    print()
    
    sourceName.delete(0,END)
    Liquid_check.deselect()
    raise_frame(settingPage)

Button(addSourcePage, text='추가', width = 26, command=addSource).grid(row = 3, column = 0, sticky='news', columnspan=2, padx='15', pady='10')
Button(addSourcePage, text='취소', width = 26, command=lambda:raise_frame(settingPage)).grid(row = 4, column = 0, sticky='news', columnspan=2, padx='15')


raise_frame(mainPage)
root.mainloop()


