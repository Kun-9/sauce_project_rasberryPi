class Source:
    
    def __init__(self, name,  isLiquid):
        self.name = name    # 멤버
        # self.cartridge_number = cartridge_number
        self.isLiquid = isLiquid
        
    def getinfo(self):
        print("이름 : " , self.name , ", 액체 여부 : ", self.isLiquid , end='')
        
    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def getLiquid(self):
        return self.isLiquid
        
        
        
class SourceList :
    def __init__(self):
        self.source_list = []
        self.current_source_list = ["", "", "", "", "", "", ""]
        self.current_source_exist = [0,0,0,0,0,0]
        
    def addSource(self, name, isLiquid):
        self.source_list.append(Source(name, isLiquid))
    
    def register_current_source(self, Cartridge_number, source_num):
        if Cartridge_number < 0 or Cartridge_number > 5 :
            print("1 ~ 6까지의 번호만 입력해주세요.")
        else :
            temp = self.source_list[source_num]
            self.current_source_list[Cartridge_number] = temp
            self.current_source_exist[Cartridge_number] = 1
        
    def delet_current_source(self, number):
        self.current_source_list[number] = ""
        self.current_source_exist[number] = 0
    
    def getSourceList(self):
        return self.source_list
    
    def getCurrentSourceList(self):
        return self.current_source_list
    
    def getCurrentSourceExist(self):
        return self.current_source_exist