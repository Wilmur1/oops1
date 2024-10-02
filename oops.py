class dog:
    def __init__(self,name,age,gender,breed):
      self.name = name
      self.age = age
      self.gender = gender
      self.breed = breed
    def bark(self):
       print("woof")
       

object = dog("buddy",3,"male","golden labrador")

print(object.name)
print(object.age)
object1 = dog("molly",7,"female","german shepoard")
print(object1.name)
object.bark()