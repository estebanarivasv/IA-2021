import random
import time

choices = [" ", "+", "*", "#"]


class Tile:

    def __init__(self):
        self.state = random.choice(choices)


class Floor:

    def __init__(self, N):
        self.size = N
        self.tiles = [Tile() for x in range(self.size)]

    def printTiles(self):
        states = []
        for x in self.tiles:
            states.append(x.state)
        print(states)


class Vacuum:

    def __init__(self, floor, direction, position):
        self.floor = floor
        self.direction = direction
        self.position = position

    def run(self):
        while True:
            print(self.floor.printTiles())
            # This condition is met as long as the vacuum is NOT at the ends.
            # Esta condición se cumple mientras la aspiradora NO esté en los extremos.
            # Cuando llega a un extremo, sale del while y comprueba el cambio de dirección.
            # When it reaches an extreme, it exits the while and checks for the change of direction.
            while 0 <= self.position <= self.floor.size - 1:
                print('		\033[92m Tile Nº:' + str(self.position + 1))
                tile = self.floor.tiles[self.position]
                # Si está limpio no hace nada, solo se mueve
                # If it's clean it doesn't do anything, it just moves
                if tile.state == ' ':
                    print('\033[92m Its clean')
                    self.move()
                # Si esta sucio llama al método limpiar y se mueve
                # If it is dirty, it calls the clean method and moves
                else:
                    print('\033[91m Its dirty')
                    tile.state = self.clean(tile.state)
                    self.move()
                print(tile.state)
                time.sleep(1)

            if self.position <= -1:
                # Cuando se salga del extremo izquierdo, que lo vuelva a posicionar en la posicion 0
                # When it comes off the left end, reposition it to position 0
                self.position = 0
                self.changeDirection()
            elif self.position >= self.floor.size:
                # Cuando se salga del extremo derecho, que lo vuelva a posicionar en la última posicion
                # When it comes off the far right, let it reposition it in the last position
                self.position = self.floor.size - 1
                self.changeDirection()
            time.sleep(1)
            print(' ')
            print('\033[1m \033[92m -----------------')
            print('\033[1m \033[92m Restart')
            print('\033[1m \033[92m -----------------')
            print(' ')

    def clean(self, state):
        print('Cleaning')
        if state == '+':
            return ' '
        elif state == '*':
            return '+'
        elif state == '#':
            return '#'

    def move(self):
        if self.direction == 'r':
            self.position = self.position + 1
            print('\033[94m Moves to tile Nº:' + str(self.position + 1))
        elif self.direction == 'l':
            self.position = self.position - 1
            print('\033[94m Moves to tile Nº:' + str(self.position + 1))

    def changeDirection(self):
        print('\033[93m _______________')
        print('\033[93m Wall detected')
        print('\033[93m _______________')
        if self.direction == 'l':
            self.direction = 'r'
        elif self.direction == 'r':
            self.direction = 'l'


if (__name__ == "__main__"):
    size = random.randint(1, 100)

    position = random.randint(0, size - 1)

    floor = Floor(N=size)

    print("Floor size: ", size)
    print("Initial position: ", position)

    vacuum = Vacuum(floor=floor, direction='l', position=position)
    vacuum.run()
