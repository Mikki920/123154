ЗАВДАННЯ 1
#class Animal:
    #def __init__(self, species):
        #self.species = species

    #def make_sound(self):
        #print("Some generic animal sound")

#class Machine:
    #def __init__(self, brand):
        #self.brand = brand

    #def start(self):
        #print("The machine is starting")

#class RobotAnimal(Animal, Machine):
    #def __init__(self, species, brand, model):

        #Animal.__init__(self, species)
        #Machine.__init__(self, brand)
        #self.model = model

    #def make_sound(self):
        #print("Beep boop, I'm a robot animal")

    #def move(self):
        #print("The robot animal is moving")


#robot_dog = RobotAnimal(species="Dog", brand="TechCorp", model="Rover")
#robot_dog.make_sound()
#robot_dog.start()
#robot_dog.move()

ЗАВДАННЯ 2
import random


class Shiftrator:
    def __init__(self, number):
        self.number = number
        self._encrypt()

    def _encrypt(self):

        operation = random.choice(['+', '-', '*', '/'])


        operand = random.uniform(1, 10)


        if operation == '+':
            self.number += operand
        elif operation == '-':
            self.number -= operand
        elif operation == '*':
            self.number *= operand
        elif operation == '/':

            if operand != 0:
                self.number /= operand

    def __str__(self):
        return str(self.number)



if __name__ == "__main__":

    my_shiftrator = Shiftrator(5)


    print("Зашифрованное число:", my_shiftrator)
