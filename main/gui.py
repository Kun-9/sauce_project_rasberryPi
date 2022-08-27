import tkinter
from source_management import source_class
import serial
import time
from tkinter import *
from tkinter import messagebox

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
    
def registCartridge():
    try :
        num = listbox.curselection()[0]
        sc.register_current_source(int(CartNum.get())-1,num)
        name = sc.getSourceList()[num].getName()
        slabel[int(CartNum.get())].config(text = name)   
        messagebox.showinfo(title="알림", message="소스가 등록되었습니다.")
        CartNum.delete(0,END)
        raise_frame(settingPage)
    except :
        messagebox.showinfo(title="알림", message="소스를 선택하세요.")
        CartNum.delete(0,END)
        raise_frame(settingPage)
    
    
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

def deleteComp() :
    num = compListbox.curselection()[0]
    compListbox.delete(num)
    sc.getSourceCompList().pop(num)

def applyComp() :
    num = compListbox.curselection()[0]
    sendStr = sc.getSourceCompList()[num]
    sr.write(sendStr.encode())

def saveSourceComp():
    sendStr = ""
    cnt = 0
    name = compName.get()
    
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
    sc.save_SourceComp(sendStr)
        
    compListbox.insert(END, name)
    messagebox.showinfo(title="알림", message="조합이 저장되었습니다.")
    raise_frame(mainPage)


def deleteSource() :
    num = listbox.curselection()[0]
    sc.getSourceList().pop(num)
    listbox.delete(num)
    

def quit(self):
    self.root.destroy()
    
sr = serial.Serial('/dev/ttyUSB0', 9600, timeout = 1)
# msg = "2,5 6 4 5 6 0,10 35 20 34 28 0,1 1 0 1 1 0"
sc = source_class.SourceList()

root = Tk()

# 타이틀
root.title('Print Source')
# root.overrideredirect(True)
# 창 크기
root.geometry('848x480+0-30')

# 창 크기 변경 불가
root.resizable(False, False)

# 메인 창
mainPage = Frame(root)
# mainPage.pack()
mainPage.grid(row=0, column=0, sticky='news')

# topPage = Frame(mainPage, relief = 'solid', bd = 1)
# Button(topPage, text= 'hello').pack()
 
# 세팅 창
settingPage = Frame(root)
settingPage.grid(row=0, column=0, sticky='news')

# 소스 추가 창
addSourcePage = Frame(root)
addSourcePage.grid(row=0, column=0, sticky='news')

# 카트리지 등록 창
registPage = Frame(root)
registPage.grid(row=0, column=0, sticky='news')

# 소스 조합 저장 창
sourceCompPage = Frame(root)
sourceCompPage.grid(row=0, column=0, sticky='news')

# 소스 조합 목록 창
compListPage = Frame(root)
compListPage.grid(row=0, column=0, sticky='news')


# sc.addSource("쯔유", 1)
# sc.addSource("간장", 1)
# sc.addSource("고추장", 1)
# sc.addSource("물엿", 1)
# sc.addSource("케찹", 1)
# sc.addSource("물", 1)
# sc.addSource("굴소스", 1)
# sc.addSource("고춧가루", 0)


cartname = ['null','null','null','null','null','null']

for a in range(6):
    if sc.getCurrentSourceExist()[a] == 1 :
        cartname[a] = sc.getCurrentSourceList()[a].getName()
    else :
        cartname[a] = 'x' 


# 메인 페이지
slabel = []
sourceNum = []

slabel.append(Label(mainPage, text = "카트리지"))
slabel[0].grid(row = 0, column = 0, columnspan=12, padx = 3, pady = 40, sticky='news')

for i in range(6) :
    slabel.append(Label(mainPage, text = cartname[i], width=12, height=1))    
    slabel[i+1].grid(row = 1, column = 2*i, sticky=N+E+W+S ,columnspan=2, padx = 15, pady = 1)
    sourceNum.append(Entry(mainPage, width=12,justify='center'))
    sourceNum[i].insert(0, '0')
    sourceNum[i].grid(row = 2, column = 2*i, sticky=N+E+W+S ,columnspan=2, padx = 15, pady = 3)

Button(mainPage, text='출력', command = sendBtn, height=10).grid(row = 3, column = 0 ,columnspan=2, padx = 0, pady = 0, sticky='news')
Button(mainPage, text='현재 조합 저장', command = lambda:raise_frame(sourceCompPage)).grid(row = 4, column = 0, columnspan=2, padx = 0, pady = 0, sticky='news')
Button(mainPage, text='저장 조합 보기', command = lambda:raise_frame(compListPage)).grid(row = 4, column = 2, columnspan=2, padx = 0, pady = 0, sticky='news')
Button(mainPage, text='장착 소스 변경', command = lambda:raise_frame(settingPage)).grid(row = 5, column = 0, columnspan=2, padx = 0, pady = 0, sticky='news')
Button(mainPage, text='닫기', command=lambda:root.destroy(), width='7').grid(row = 6, column = 0, columnspan=2, padx = 0, pady = 0, sticky='news')


# 세팅 페이지
Label(settingPage, text='settingPage').pack(pady='3',side = 'top')
listbox = Listbox(settingPage, selectmode='single', height=5)
listbox.pack(pady='2', side='top')


Button(settingPage, text='카트리지에 등록', command=lambda:raise_frame(registPage)).pack(padx='20',pady='5')
Button(settingPage, text='소스 추가', command=lambda:raise_frame(addSourcePage)).pack(pady = '7',side='left', padx = '2')
Button(settingPage, text='선택 삭제', command=deleteSource).pack(pady = '7',side = 'left', padx = '2')
Button(settingPage, text='돌아가기', command=lambda:raise_frame(mainPage)).pack(side='left', padx = '2')


# 카트리지 등록 페이지
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

Button(addSourcePage, text='추가', width = 26, command=addSource).grid(row = 3, column = 0, sticky='news', columnspan=2, padx='15', pady='10')
Button(addSourcePage, text='취소', width = 26, command=lambda:raise_frame(settingPage)).grid(row = 4, column = 0, sticky='news', columnspan=2, padx='15')


# 소스 조합 추가 페이지
Label(sourceCompPage, text = '소스 조합 등록', width = 13, height = 3).grid(row = 0, column = 0, columnspan = 12, sticky='news', pady='2')

Label(sourceCompPage, text = '명칭', width = 13, height = 3).grid(row = 1, column = 0, sticky='news')

compName = Entry(sourceCompPage, width=14)
compName.grid(row = 1, column= 1 ,padx=10, pady=15)

Button(sourceCompPage, text='추가', width = 26, command=saveSourceComp).grid(row = 3, column = 0, sticky='news', columnspan=2, padx='15', pady='10')
Button(sourceCompPage, text='취소', width = 26, command=lambda:raise_frame(mainPage)).grid(row = 4, column = 0, sticky='news', columnspan=2, padx='15')

# 소스 조합 목록 조회 페이지

Label(compListPage, text='소스 조합 목록').pack(pady='12')
compListbox = Listbox(compListPage, selectmode='single', height=5)
compListbox.pack(pady='2')



Button(compListPage, text='조합 출력', command=applyComp, width='7').pack(pady = '7',side='left', padx = '2')
Button(compListPage, text='선택 삭제', command=deleteComp, width='7').pack(pady = '7',side = 'left', padx = '2')
Button(compListPage, text='취소', command=lambda:raise_frame(mainPage), width='7').pack(side='left', padx = '2')


raise_frame(mainPage)
# root.wm_attributes("-topmost", 1)
root.mainloop()


