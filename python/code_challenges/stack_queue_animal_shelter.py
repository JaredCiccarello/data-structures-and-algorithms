from data_structures.queue import Queue


# shelter = AnimalShelter()
#cat = Cat()
#dog = Dog()
#The shelter is queue. cat is a node.dog is a node (just nodes that are created with a different class)

#Shelter
#(cat)(dog)(cat)(dog)(cat)(dog)


class Animal:
    def __init__(self, species, name):
       self.species = species
       self.name = name


class AnimalShelter:
  def __init__(self):
     self.dogs = Queue()
     self.cats = Queue()

# We take an animal, and then add them to individual queues
  def enqueue(self, animal):
     if animal.species == "dog":
        self.dogs.enqueue(animal)
     elif animal.species == "cat":
        self.cats.enqueue(animal)
     else:
        return "Not a dog or cat"

  def dequeue(self, pref):
     if pref == 'dog':
        return self.dogs.dequeue()
     elif pref == 'cat':
        return self.cats.dequeue()
     else:
        return None

class Dog(Animal):
  #Test2 will not pass without name equal to string
  def __init__(self, name=''):
    #super calls the parents class constructor
    super().__init__("dog", name)


class Cat(Animal):
  #Test1 will not pass without name equal to string
  def __init__(self, name=''):
    #super calls the parents class constructor
    super().__init__("cat", name)
