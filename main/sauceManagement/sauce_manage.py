import pickle as p
import os.path
import json as j

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
        self.saucelist = []
        self.currentSauceList = [0,0,0,0,0,0] 
        # ["", "", "", "", "", "", ""]
        self.currentSauceExist = [0,0,0,0,0,0]
        self.sauceComp = []
    
    def path(self, id):
        return "/home/pi/project_test_python/main/assets/saucePickles/" + str(id) + ".pickle"
        
    def addSauce(self, name, isLiquid, id):    
        with open(self.path(id), "wb") as sauce:
            data = p.dump(Sauce(name, isLiquid, id), sauce)
        return data    
    
    def getSauce(self, id):
        with open(self.path(id), "rb") as sauce:
            data = p.load(sauce)
        return data  

    def delSauce(self, id):
        if os.path.isfile(self.path(id)) and os.path.getsize(self.path(id)) > 0:
            os.remove(self.path(id))
        
    def getSauceById(self, id):
        if os.path.isfile(self.path(id)) and os.path.getsize(self.path(id)) > 0:
            print(os.path.isfile(self.path(id)) > 0)
            print(id + " : 파일 존재")
            
            return self.getSauce(id)
        else:
            print(id + " : 파일 없음")
            self.addSauce('null', 1, id)    
            print(id + " : 파일 생성 완료")

            return self.getSauce(id)
    
    def registCurrentSauce(self, Cartridge_number, id):
        if Cartridge_number < 0 or Cartridge_number > 5 :
            return
        else :
            # temp = self.sauceList[num]
            self.currentSauceList[Cartridge_number] = id
            self.currentSauceExist[Cartridge_number] = 1
            
    def saveCurrnetSourceList(self):
        with open(self.path("currentSauceList"), "wb") as sauce:
            data = p.dump(self.currentSauceList, sauce)
        return data
            
    def saveSauceComp(self, sauceStr):
        self.sauceCompList.append(sauceStr)
        
    def deleteCurrentSauce(self, number):
        self.currentSauceList[number] = ""
        self.currentSauceExist[number] = 0
    
    def getsauceCompList(self):
        return self.sauceCompList
    
    def getsauceList(self):
        return self.sauceList
    
    def getCurrentsauceList(self):
        if os.path.isfile(self.path("currentSauceList")) and os.path.getsize(self.path("currentSauceList")) > 0:
            with open(self.path("currentSauceList"), "rb") as fr:
                data = p.load(fr)
            return data
        else :
            return 

    
    def getCurrentsauceExist(self):
        return self.currentSauceExist
    
    def findById(self, id):
        for i in range(len(self.getsauceList())):
            if id == self.getsauceList()[i].getId():
                return True
        return False

