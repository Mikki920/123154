
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
