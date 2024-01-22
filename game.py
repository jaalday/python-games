"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class Character:
    def  __init__(self, health, power):
        self.health = health
        self.power = power
        
    def alive(self):
       return self.health <= 0
       
    def status_check(self):
        print(self.health, self.power)
        
   
    
class Hero(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power
        
    def attack(self, goblin):
           goblin.health -= self.power
           if goblin.health <= 0: 
            print("goblin is dead")
            
    
    def print_status(self):
        print (self.health, self.power)
        
  
           
   
        
    
class Goblin(Character):
    def __init__ (self, health, power):
        self.health = health
        self.power = power
                    
    def attack(self, hero):
        hero.health -= self.power
        if hero.health <=0:
            print("you died")
        
    def print_status(self):
        print(self.health, self.power)
    
            
            
def main():
    # hero_health = 10
    # hero_power = 5
    # goblin_health = 6
    # goblin_power = 2
    
        

    # while goblin.health >0  and hero.health >0:
    while goblin.alive and hero.alive:
        print("You have %d health and %d power." % (hero.health, hero.power))
        print("The goblin has %d health and %d power." % (goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            hero.attack(goblin)
            # # Hero attacks goblin
            # goblin_health -= hero_power
            print("You do %d damage to the goblin." % hero.power)
            if goblin.health <= 0:
                print("The goblin is dead.")
                break
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)
            print("The goblin does %d damage to you." % goblin.power)
            if hero.health <= 0:
                print("You are dead.")

hero = Hero(10, 5)
goblin = Goblin(6, 2)


main()
