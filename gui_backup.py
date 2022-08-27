import tkinter
import socket
from source_management import source_class
import serial
import time
from tkinter import *
from tkinter import messagebox
import threading
# from socketClass import serverModule


class GUI :
    def __init__(self):
        self.sc = source_class.SourceList()
    
    def startGui(self):
        
        # msg = "2,5 6 4 5 6 0,10 35 20 34 28 0,1 1 0 1 1 0"
        
        root = Tk()

        # 타이틀
        root.title('Print Source')
        # root.overrideredirect(True)
        # 창 크기
        root.geometry('848x480+0-30')

        # 창 크기 변경 불가
        root.resizable(False, False)

        # 메인 창
        self.mainPage = Frame(root, relief = 'solid', bd = 1)
        self.mainPage.grid(row=0, column=0, sticky='news')

        # 배열 창
        self.arrPage = Frame(self.mainPage, relief = 'solid', bd = 1)
        self.arrPage.pack(side = 'top')


        # 서브 창
        self.subPage = Frame(self.mainPage, relief = 'solid', bd = 1)
        self.subPage.pack(side = 'left')
        Button(self.subPage, text='top').pack(side = 'top')
        Button(self.subPage, text='left').pack(side = 'left')


        # Button(self.subPage, text='center').pack(left)
        Button(self.subPage, text='right').pack(side = 'right')
        Button(self.subPage, text='bottom').pack(side = 'bottom')
        
        # 세팅 창
        self.settingPage = Frame(root)
        self.settingPage.grid(row=0, column=0, sticky='news')

        # 소스 추가 창
        self.addSourcePage = Frame(root)
        self.addSourcePage.grid(row=0, column=0, sticky='news')

        # 카트리지 등록 창
        self.registPage = Frame(root)
        self.registPage.grid(row=0, column=0, sticky='news')

        # 소스 조합 저장 창
        self.sourceCompPage = Frame(root)
        self.sourceCompPage.grid(row=0, column=0, sticky='news')

        # 소스 조합 목록 창
        self.compListPage = Frame(root)
        self.compListPage.grid(row=0, column=0, sticky='news')


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
            if self.sc.getCurrentSourceExist()[a] == 1 :
                cartname[a] = self.sc.getCurrentSourceList()[a].getName()
            else :
                cartname[a] = 'x' 


        # 메인 페이지
        slabel = []
        self.sourceNum = []


        slabel.append(Label(self.arrPage, text = "카트리지"))
        slabel[0].grid(row = 0, column = 0, columnspan=12, padx = 3, pady = 40, sticky='news')

        for i in range(6) :
            slabel.append(Label(self.arrPage, text = cartname[i], width=12, height=1))    
            slabel[i+1].grid(row = 1, column = 2*i, sticky=N+E+W+S ,columnspan=2, padx = 15, pady = 1)
            self.sourceNum.append(Entry(self.arrPage, width=12,justify='center'))
            self.sourceNum[i].insert(0, '0')
            self.sourceNum[i].grid(row = 2, column = 2*i, sticky=N+E+W+S ,columnspan=2, padx = 15, pady = 3)

        
        Button(self.arrPage, text='출력', command = self.sendBtn, height=10).grid(row = 3, column = 0 ,columnspan=2, padx = 0, pady = 0, sticky='news')
        Button(self.arrPage, text='현재 조합 저장', command = lambda:self.raise_frame(self.sourceCompPage)).grid(row = 4, column = 0, columnspan=2, padx = 0, pady = 0, sticky='news')
        Button(self.arrPage, text='저장 조합 보기', command = lambda:self.raise_frame(self.compListPage)).grid(row = 4, column = 2, columnspan=2, padx = 0, pady = 0, sticky='news')
        Button(self.arrPage, text='장착 소스 변경', command = lambda:self.raise_frame(self.settingPage)).grid(row = 5, column = 0, columnspan=2, padx = 0, pady = 0, sticky='news')
        Button(self.arrPage, text='닫기', command=lambda:root.destroy(), width='7').grid(row = 6, column = 0, columnspan=2, padx = 0, pady = 0, sticky='news')
        
        
        global gloStr
        # 세팅 페이지
        Label(self.settingPage, text=gloStr).pack(pady='3',side = 'top')
        self.listbox = Listbox(self.settingPage, selectmode='single', height=5)
        self.listbox.pack(pady='2', side='top')


        Button(self.settingPage, text='카트리지에 등록', command=lambda:self.raise_frame(self.registPage)).pack(padx='20',pady='5')
        Button(self.settingPage, text='소스 추가', command=lambda:self.raise_frame(self.addSourcePage)).pack(pady = '7',side='left', padx = '2')
        
        Button(self.settingPage, text='선택 삭제', command=self.deleteSource).pack(pady = '7',side = 'left', padx = '2')
        Button(self.settingPage, text='돌아가기', command=lambda:self.raise_frame(self.mainPage)).pack(side='left', padx = '2')
        Button(self.settingPage, text='ref', command=self.refresh_name).pack(side='left', padx = '2')


        # 카트리지 등록 페이지
        Label(self.registPage, text = '위치 (1 ~ 6)', width = 13, height = 3).grid(row = 1, column = 0, sticky='news')

        self.CartNum = Entry(self.registPage, width=3)
        self.CartNum.grid(row = 1, column= 1, pady=15)

        Button(self.registPage, text='등록', width = 26, command=self.registCartridge).grid(row = 3, column = 0, sticky='news', columnspan=2, padx='15', pady='10')
        Button(self.registPage, text='취소', width = 26, command=lambda:self.raise_frame(self.settingPage)).grid(row = 4, column = 0, sticky='news', columnspan=2, padx='15')


        # 소스 추가 페이지
        self.CheckVariety_1 = IntVar()

        Label(self.addSourcePage, text = '명칭', width = 13, height = 3).grid(row = 1, column = 0, sticky='news')
        Label(self.addSourcePage, text = '액체', width = 13, height = 3).grid(row = 2, column = 0, sticky='news')
        self.sourceName = Entry(self.addSourcePage, width=14)
        self.sourceName.grid(row = 1, column= 1 ,padx=10, pady=15)
        self.Liquid_check = Checkbutton(self.addSourcePage, variable=self.CheckVariety_1, )
        self.Liquid_check.grid(row = 2, column = 1, sticky='news', padx=10, pady=3)

        Button(self.addSourcePage, text='추가', width = 26, command=self.addSource).grid(row = 3, column = 0, sticky='news', columnspan=2, padx='15', pady='10')
        Button(self.addSourcePage, text='취소', width = 26, command=lambda:self.raise_frame(self.settingPage)).grid(row = 4, column = 0, sticky='news', columnspan=2, padx='15')


        # 소스 조합 추가 페이지
        Label(self.sourceCompPage, text = '소스 조합 등록', width = 13, height = 3).grid(row = 0, column = 0, columnspan = 12, sticky='news', pady='2')

        Label(self.sourceCompPage, text = '명칭', width = 13, height = 3).grid(row = 1, column = 0, sticky='news')

        self.compName = Entry(self.sourceCompPage, width=14)
        self.compName.grid(row = 1, column= 1 ,padx=10, pady=15)

        Button(self.sourceCompPage, text='추가', width = 26, command=self.saveSourceComp).grid(row = 3, column = 0, sticky='news', columnspan=2, padx='15', pady='10')
        Button(self.sourceCompPage, text='취소', width = 26, command=lambda:self.raise_frame(self.mainPage)).grid(row = 4, column = 0, sticky='news', columnspan=2, padx='15')

        # 소스 조합 목록 조회 페이지

        Label(self.compListPage, text='소스 조합 목록').pack(pady='12')
        self.compListbox = Listbox(self.compListPage, selectmode='single', height=5)
        self.compListbox.pack(pady='2')



        Button(self.compListPage, text='조합 출력', command=self.applyComp, width='7').pack(pady = '7',side='left', padx = '2')
        Button(self.compListPage, text='선택 삭제', command=self.deleteComp, width='7').pack(pady = '7',side = 'left', padx = '2')
        Button(self.compListPage, text='취소', command=lambda:self.raise_frame(self.mainPage), width='7').pack(side='left', padx = '2')


        self.raise_frame(self.mainPage)
        # root.wm_attributes("-topmost", 1)
        root.mainloop()

    def refresh_name(self) :
        global gloStr
        print('실행')
        print(gloStr)
        self.listbox.insert(END, gloStr)
        self.listbox.insert(END, 'hello')
        print('실행 종료')

    
    def raise_frame(self, frame):
        frame.tkraise()
    
    def sendBtn(self):
        sendStr = ""
        cnt = 0
        # 카트리지 번호
        for i in range(6) :
            if int(self.sourceNum[i].get()) > 0 :
                sendStr += str(i+1) + " " 
                cnt += 1
        print(sendStr)
        sendStr += ","
        
        # 무게
        for i in range(6) :
            if int(self.sourceNum[i].get()) > 0 :
                sendStr += str(self.sourceNum[i].get()) + " "
        print(sendStr)
        sendStr += ","
        
        # 액체 여부
        for i in range(6) :
            if int(self.sourceNum[i].get()) > 0 :
                tmp = self.sc.getCurrentSourceList()[i].getLiquid()
                sendStr += str(tmp) + " "
        print(sendStr)
        
        sendStr = str(cnt) + "," + sendStr
        
        self.serialArdu.write(sendStr.encode())
        
    def registCartridge(self):
        try :
            num = self.listbox.curselection()[0]
            self.sc.register_current_source(int(self.CartNum.get())-1,num)
            name = self.sc.getSourceList()[num].getName()
            self.slabel[int(self.CartNum.get())].config(text = name)   
            messagebox.showinfo(title="알림", message="소스가 등록되었습니다.")
            self.CartNum.delete(0,END)
            self.raise_frame(self.settingPage)
        except :
            messagebox.showinfo(title="알림", message="소스를 선택하세요.")
            self.CartNum.delete(0,END)
            self.raise_frame(self.settingPage)
        
        
    def addSource(self):
        name = self.sourceName.get()
        self.listbox.insert(END, name)

        self.sc.addSource(name, self.CheckVariety_1.get())
        tkinter.messagebox.showinfo(title="알림", message="소스가 추가되었습니다.")
        
        
        self.sc.getSourceList()[-1].getinfo()
        
        self.sourceName.delete(0,END)
        self.Liquid_check.deselect()
        self.raise_frame(self.settingPage)

    def deleteComp(self) :
        num = self.compListbox.curselection()[0]
        self.compListbox.delete(num)
        self.sc.getSourceCompList().pop(num)

    def applyComp(self) :
        num = self.compListbox.curselection()[0]
        sendStr = self.sc.getSourceCompList()[num]
        self.serialArdu.write(sendStr.encode())

    def saveSourceComp(self):
        sendStr = ""
        cnt = 0
        name = self.compName.get()
        
        # 카트리지 번호
        for i in range(6) :
            if int(self.sourceNum[i].get()) > 0 :
                sendStr += str(i+1) + " " 
                cnt += 1
        print(sendStr)
        sendStr += ","
        
        # 무게
        for i in range(6) :
            if int(self.sourceNum[i].get()) > 0 :
                sendStr += str(self.sourceNum[i].get()) + " "
        print(sendStr)
        sendStr += ","
        
        # 액체 여부
        for i in range(6) :
            if int(self.sourceNum[i].get()) > 0 :
                tmp = self.sc.getCurrentSourceList()[i].getLiquid()
                sendStr += str(tmp) + " "
        print(sendStr)
        
        sendStr = str(cnt) + "," + sendStr
        self.sc.save_SourceComp(sendStr)
            
        self.compListbox.insert(END, name)
        messagebox.showinfo(title="알림", message="조합이 저장되었습니다.")
        self.raise_frame(self.mainPage)


    def deleteSource(self) :
        num = self.listbox.curselection()[0]
        self.sc.getSourceList().pop(num)
        self.listbox.delete(num)
        

    def quit(self):
        self.root.destroy()


def start_Gui():
    gui = GUI()
    gui.startGui()
    
    
GuiThread = threading.Thread(target=start_Gui)

GuiThread.start()    
