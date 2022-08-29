import os.path
import json as j

class Sauce:
    
    def __init__(self, name,  isLiquid, id):
        self.name = name    # 멤버
        self.isLiquid = isLiquid
        self.id = id
        
    def getinfo(self):
        print("name : " , self.name , ", isLiquid : ", self.isLiquid , "id : " , self.id , end='' )
        
        
    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def getLiquid(self):
        return self.isLiquid
    
    def getId(self):
        return self.id
    
    def getJson(self):
        return {"name" : self.name, "isLiquid" : self.isLiquid, "id" : self.id}
    
        
        
class sauceList :
    
    def __init__(self):
        self.saucelist = []
        
        self.currentSauceList = {
            'messageType': 2,
            "body" : [
                "null",
                "null",
                "null",
                "null",
                "null",
                "null" 
                ],
            }
        # ["", "", "", "", "", "", ""]
        self.currentSauceExist = [0,0,0,0,0,0]
        self.sauceComp = []
    
    def path(self, id):
        return "/home/pi/project_test_python/main/assets/saucePickles/" + str(id) + ".json"
        
    def addSauce(self, name, isLiquid, id):    
        s = Sauce(name, isLiquid, id)
        jsonData = s.getJson()
        with open(self.path(id), "w", encoding='UTF-8') as sauce:
            j.dump(jsonData, sauce, ensure_ascii=False)

    def getSauce(self, id):
        with open(self.path(id), "r") as sauce:
            data = j.load(sauce)
        return data
    
    def editSauce(self, id, json):
        with open(self.path(id), "w", encoding='UTF-8') as sauce:
            j.dump(json, sauce, ensure_ascii=False) 

    def delSauce(self, id):
        if os.path.isfile(self.path(id)) and os.path.getsize(self.path(id)) > 0:
            os.remove(self.path(id))
        
    def getSauceById(self, id):
        if os.path.isfile(self.path(id)) and os.path.getsize(self.path(id)) > 0:
            print(os.path.isfile(self.path(id)) > 0)
            print(str(id) + " : 파일 존재")
            
            return self.getSauce(id)
        else:
            print(str(id) + " : 파일 없음")
            self.addSauce('null', 1, id)    
            print(str(id) + " : 파일 생성 완료")

            return self.getSauce(id)
    
    def registCurrentSauce(self, Cartridge_number, id):
        # temp = self.sauceList[num]
        
        if id != 0:
            self.currentSauceList["body"][Cartridge_number] = self.getSauceById(id)
            # self.currentSauceList["body"][Cartridge_number] = "hello"
            print("self.currentSauceList[\"body\"]" , self.currentSauceList["body"])
            print("self.currentSauceList[\"body\"][Cartridge_number]" , self.currentSauceList["body"][Cartridge_number])
            # self.currentSauceList[Cartridge_number] = id
            self.currentSauceExist[Cartridge_number] = 1
        else :
            self.currentSauceList["body"][Cartridge_number] = {
                "name" : "null", 
                "isLiquid" : "null", 
                "id" : "null"
                }
            self.currentSauceExist[Cartridge_number] = 0
            
            
            
    def saveCurrnetSourceList(self):
        with open(self.path("currentSauceList"), "w") as sauce:
            data = j.dump(self.currentSauceList, sauce)
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
            with open(self.path("currentSauceList"), "r") as fr:
                data = j.load(fr)
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

