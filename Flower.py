#Taylor Vonville 10/22/2023

#defines the class as Flower
class Flower:

#Utilizes the constructor method apply the name function for each flower without modifying the flower objects.
    def __init__(self, name):
        self.name = name

#Defines a method named grow within the Flower class that will use the print function when assigned to an object. 
    def grow(self):
        print("The " +self.name + " is growing.")

#Defines a method named blow within the Flower class that will use the print function when assigned to an object. 
    def bloom(self):
        print("The " + self.name + " is blooming.")

#Creates that objects that will be instantied within the Flower class. The 3 different objects are Flower1(named Rose), Flower2(named Daisy), and Flower3(named Tulip). The .grow and .bloom dot operators assign an attribute to each object. 
def main():
    flower1 = Flower("Rose")
    flower1.grow()
    flower1.bloom()
    flower2 = Flower("Daisy")
    flower2.grow()
    flower2.bloom()
    flower3 = Flower("Tulip")
    flower3.grow()
    flower3.bloom()

if __name__ == "__main__":
  main()