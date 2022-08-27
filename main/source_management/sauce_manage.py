from pickle import FALSE


class Sauce:
    
    def __init__(self, name,  isLiquid, id):
        self.name = name    # 멤버
        self.isLiquid = isLiquid
        self.id = id
        
    def getinfo(self):
        print("이름 : " , self.name , ", 액체 여부 : ", self.isLiquid , "ID : " , self.id , end='' )
        
    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def getLiquid(self):
        return self.isLiquid
    
    def getId(self):
        return self.id
    
    
        
        
        
class sauceList :
    def __init__(self):
        self.sauce_list = []
        self.current_sauce_list = ["", "", "", "", "", "", ""]
        self.current_sauce_exist = [0,0,0,0,0,0]
        self.sauce_comp = []
        
    def addsauce(self, name, isLiquid, id):
        self.sauce_list.append(Sauce(name, isLiquid, id))
    
    def regist_current_sauce(self, Cartridge_number, num):
        if Cartridge_number < 0 or Cartridge_number > 5 :
            return
        else :
            # self.current_sauce_list[Cartridge_number] = Sauce(name, isLiquid, id)
            # temp = self.sauce_list[sauce_num]
            temp = self.sauce_list[num]
            self.current_sauce_list[Cartridge_number] = temp
            self.current_sauce_exist[Cartridge_number] = 1
            
    def save_sauceComp(self, sauceStr):
        self.sauce_comp.append(sauceStr)
        
    def delete_current_sauce(self, number):
        self.current_sauce_list[number] = ""
        self.current_sauce_exist[number] = 0
    
    def getsauceCompList(self):
        return self.sauce_comp
    
    def getsauceList(self):
        return self.sauce_list
    
    def getCurrentsauceList(self):
        return self.current_sauce_list
    
    def getCurrentsauceExist(self):
        return self.current_sauce_exist
    
    def findById(self, id):
        for i in range(len(self.getsauceList())):
            if id == self.getsauceList()[i].getId():
                return True
        return False

