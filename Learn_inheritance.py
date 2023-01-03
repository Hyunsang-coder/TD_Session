
class Weapon:
    def __init__(self):
        self.damage = 10
        self.range = 50
        self.type = "Default Weapon"
    
    def fire(self):
        print ("탕탕탕!")
    
    def reload(self):
        print("장전이 완료되었습니다")
    
    def show_stats(self):
        print(f"Type: {self.type}, Damage: {self.damage}, Range: {self.range}")
        
'''    
class M416(Weapon):
    def __init__(self):
        super().__init__()
        
        #데이터 변경
        self.type = "M416"
        self.damage = 30
        self.range = 100
    
    #method override    
    #def reload(self):
    #    print("M416 장전 완료!")
'''

'''

'''      
        
print("-----------------------------------------------------------------------")
#인스턴스 생성
default_weapon = Weapon()

#함수 호출
default_weapon.show_stats()
default_weapon.fire()
default_weapon.reload()
print("-----------------------------------------------------------------------")


'''
#M416으로 동일하게 실행
m416 = M416()
m416.show_stats()
m416.fire()
m416.reload()
print("-----------------------------------------------------------------------")
'''
   
'''
#Handgun으로 동일하게 실행
handgun = Handgun()
handgun.show_stats()
handgun.fire()
handgun.reload()
'''    
    
    