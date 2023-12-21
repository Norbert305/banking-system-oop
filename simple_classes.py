



class User() :
    def __init__(self,name,age,gender):
        # Holds details about the user
        self.name = name
        self.age = age
        self.gender = gender
    
user1 = User("Bob", 50, "Male")
John = User("John", 21, "Male")


   

print(user1.name)
print(user1.age)
print(user1.gender)
print(f"My name is {John.name} and I am {John.age} years old.")


class Pizza():
    def __init__(self,toppings,size):
        self.toppings = toppings
        self.size = size
        
user2 = Pizza("Peperoni", "medium")

print(user2.toppings)
print(user2.size)




class Colors():
    def __init__(self,color):
        self.color = color

red = Colors("red")
green = Colors("green")
blue = Colors("blue")        
    

print(f"My favorite color is {red.color}")


        
        
        
        
    
        
        
        
        
