class Character:
    def  __init__(self, name, health, swat):
        self.name = name
        self.health = health
        self.swat = swat
    def alive(self):
       return self.health <= 0
       
    def status_check(self):
        print(self.health, self.swat)
        
    def alive(self):
       return self.health <= 0
   
    def power_up(self):
        self.health += 1 
        self.swat += 1
        
    def damage(self):
        self.health - 1
        
    def status_check(self):
        print(self.health, self.swat)
        
    def mouse(self):
        result = ('''            
        ( )___( )~~~~~~~~
         /o   O /         }   \ 
        /_ = )        {   }___/
            C--C------{   )       
                   
              ''')
        print(result)
        
    def attack(self, other_cat):
        other_cat -= self.swat
        if other_cat.health <=0:
            print("they died")
            
    def status_check(self):
        print(self.health, self.swat)
    
        
        
class Cat_1(Character):
    def __init__(self, name, health, swat):
        self.name = name
        self.health = health
        self.swat = swat
        
   
            
    def goon_pic(goonpic):
        result = ('''
                 (\______/)
                 ( .\  /. )
                  \ = ^ =/  ( )
                  [------]  ( (
                  (      )   \ \
                 /        \   ) )
                (          ) / /
                 -=-U---U-=-
              ''')
        print(result)
    def status_check(self):
        print(self.health, self.swat)
         
class Cat_2(Character):
    def __init__(self, name, health, swat):
        self.name = name
        self.health = health
        self.swat = swat
        
    def attack(self, cat_1):
        cat_1.health -= self.swat
        if cat_2.health <=0:
            print("you died")
            
    def tsuki_pic(tsukipic):
         print(''' 
                 (\______/)
                 (  n   n )
                  \ = w =/  ( )
                  [------]  ( (
                  (      )   \ \
                 /        \   ) )
                (          ) / /
                 -=-U---U-=-
       ''')
         
        
    def status_check(self):
        print(self.health, self.power)
            
class Cat_3(Character):
    def __init__(self, name, health, swat):
        self.name = name
        self.health = health
        self.swat = swat
        
    def attack(self, cat_1):
        cat_1.health -= self.swat
        if cat_3.health <=0:
            print("you died")
            
    def stray_pic(straypic):
        result = ('''
                  n______/)
                 (  o   < )
                  \ = ^ =/  
                  [------]  
                  (      )    ( )
                 /        \   ) )
                (          ) / /
                 -=-U---U-=-
            
        ''')
        print(result)
    def status_check(self):
        print(self.health, self.power)
        
        
cat_1 = Cat_1("Goon", 10, 3)
cat_2 = Cat_2("Tsuki", 10, 2)
cat_3 = Cat_3("Stray cat", 10, 4) 


     
def main():
    
    
        print("There are 3 cats in the house, Goon, Tsuki, and a Stray cat")
        print(" ")
        print("**************(=^.^=)*****************")
        print("--------------------------------------")
        print(" ")
        print("Press 1 to choose Goon ")
        print("Press 2 to choose Tsuki ")
        print("Press 3 to choose the Stray cat ")
        print("--------------------------------------")
        print(">>>>")
        while cat_1.alive and cat_2.alive and cat_3.alive:
            user_input = int(input())
            if user_input == 1:
                
                print(" you chose Goon and have %d health and %d swat power" % (cat_1.health, cat_1.swat))
                print(cat_1.goon_pic())
            elif user_input == 2:
                print("you chose Tsuki and have %d health and %d swat power" % (cat_2.health, cat_2.swat))
                print(cat_2.tsuki_pic())
            elif user_input == 3:
                print("you chose the Stray cat, you have %d health and %d swat power" % (cat_3.health, cat_3.swat))
                print(cat_3.stray_pic())
            else: 
                print("invalid response")
                
            break
        while cat_1.alive and cat_2.alive and cat_3.alive:
            print("")
            print("**************(=^.^=)*****************")
            print("--------------------------------------")
            print("you encounter a glass on the coffe table, what do you choose to do?")
            print("1 knock it over ")
            print("2 drink out of it ")
            print("3 ignore the glass ")
            print("--------------------------------------")
            print(">>>>")
            user_input = int(input())
            if user_input == 1:
                print("Good choice, you earned a power up +1")
                cat_1.power_up
                print(cat_1.power_up)
                
                # print("Goons health is "(cat_1.health))
                # print("Tsukis health is "(cat_2.health))
                # print("Strays health is "(cat_3.health))
                
            elif user_input == 2:
                print("good choice, but its not water so you take some damage -1")
                # Character.damage(self)
            elif user_input == 3:
                print("you ignore the glass")
            else:
                print("invalid")
                break
            break
        
        while cat_1.alive and cat_2.alive and cat_3.alive :
            
            print("You find a mouse in your house thats eating your food")
            print("What would you like to do?")
            print("**************(=^.^=)*****************")
            print("--------------------------------------")
            print(cat_1.mouse())
            
            print("1 play with the mouse")
            print("2 absolutely wreck that mouse, and hide the body in my owners shoes")
            print("3 ignore that mouse and walk away")
            print("---------------------------------------")
            print(">>>>")
            user_input = int(input())
            
            if user_input == 1:
                print("oh no the mouse ran away")
                   
            elif user_input == 2:
                print("excellent choice, you earned another power up")
                    # Character.power_up(self)
                print(Character.power_up)
                print(Character.status_check)
                    
            elif user_input == 3:
                print("you got better things to do anyway")
                
            else:
                print("invalid")
                break
            break
        
    
 
    
cat_1 = Cat_1("Goon", 10, 3)
cat_2 = Cat_2("Tsuki", 10, 2)
cat_3 = Cat_3("Stray cat", 10, 4)

main()