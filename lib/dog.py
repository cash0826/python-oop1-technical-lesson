# Dog model goes here

class Dog:
    def __init__(self, name, breed, age, last_checkup = None):
        self.name = name
        self.breed = breed
        self.age = age
        self.last_checkup = last_checkup
  
    def checkup(self, date):
        print(f"Checking up with {self.name} on {date}")
        self.last_checkup = date
  
    def birthday_celebration(self):
        self.age += 1
        print(f"{self.name} is turning {self.age}")
    
    def get_age(self):
        return self._age
  
    def set_age(self, value):
        if type(value) is int and 0 <= value:
            self._age = value
        else:
            print("Not a valid age")
            
    age = property(get_age, set_age)
  
fido = Dog("Fido", "Golden Retriever", 3, "05/22/2022")
clifford = Dog(
    name = "Clifford",
    age = 2,
    breed = "Big Red"
)

# print(fido.age) # 3
# fido.birthday_celebration()
# print(fido.age) # 4

# print(clifford.last_checkup) # None
# clifford.checkup("03/02/2024")
# print(clifford.last_checkup) # 03/02/2024

balto = Dog("Balto", "Husky", "Not an age")
steele = Dog("Steele", "Husky", -10)
