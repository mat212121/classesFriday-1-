# class Pelican:
#   #attributes 
#   def __init__(self, wings, legs, neck, eyes, beak):
#     self.wings = wings
#     self.legs = legs
#     self.neck = neck
#     self.eyes = eyes
#     self.beak = beak

#   wings = 4
#   legs = 2
#   neck = 1
#   eyes = 2
#   def fly(self,wings):
#     print(f'birds can fly with {wings} wings')

#   def canWalk(self):
#     print("birds can walk")

#   def canSwim(self):
#     print("birds can swim")

# wallie = Pelican(2,2,1,2,1)
# print(wallie.fly(2))
# print(wallie.canWalk())
class House:
  def __init__(self,color,floors):
    self.color = color
    self.floors = floors 
    def white_house(self,color,floors):
      print(f'the house has {floors} floors and is {color}')
  floors = 4
  color = 'white'
  

House = House('white',4)
print(House)