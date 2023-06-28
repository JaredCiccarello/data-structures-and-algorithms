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
     self.queue = Queue()
    #  self.dogs = Queue()
    #  self.cats = Queue()

  #   #super calls the parents class constructor
  #   super().__init__("dog")
# Dog and cat is an object, not need two queue. TOO EASY

# We take an animal, and then add them to individual queue
  def enqueue(self, animal):
     self.queue.enqueue(animal)


  def dequeue(self, pref):
     if pref != "dog" and pref != "cat":
        return None
     else:
        while self.queue.front:
           if self.queue.front.value.species==pref:
              return self.queue.dequeue()
           else:
              self.queue.enqueue(self.queue.dequeue())
        return None

    #  if pref == 'dog':
    #     return self.dogs.dequeue()
    #  elif pref == 'cat':
    #     return self.cats.dequeue()
    #  else:
    #     return None


class Dog:
  def __init__(self):
      self.species = "dog"

class Cat:
  def __init__(self):
   self.species = "cat"
