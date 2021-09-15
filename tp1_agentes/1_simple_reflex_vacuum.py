import random
import time

CHOICES = [" ", "+", "*", "#"]


class Tile:

    def __init__(self):
        self.state = random.choice(CHOICES)


class Floor:

    def __init__(self, N):
        self.size = N
        self.tiles = [Tile() for x in range(self.size)]

    def print_tiles(self):
        states = []
        for x in self.tiles:
            states.append(x.state)
        print("\n\033[1m\033[33mActual floor state: ", states)


class Vacuum:

    def __init__(self, floor, direction, position):
        self.floor = floor
        self.direction = direction  # l - left, r - right
        self.position = position  # The vacuum starts in this position
        self.wall_detected = False

    def run(self):
        while True:
            self.floor.print_tiles()
            # This condition is met as long as the vacuum is NOT at the ends.
            # Esta condición se cumple mientras la aspiradora NO esté en los extremos.

            # Cuando llega a un extremo, sale del while y comprueba el cambio de dirección.
            # When it reaches an extreme, it exits the while and checks for the change of direction.

            try:

                # Si no fijamos al valor posicion como solamente positivo, la aspiradora comienza
                # a leer la lista de baldosas de manera negativa, es decir, comienza a limpiar desde
                # la otra punta del piso. No es que la aspiradora sepa donde esta posicionada.

                if self.position < 0:
                    raise IndexError

                tile = self.floor.tiles[self.position]
                print('\n\033[92mTile Nº:' + str(self.position + 1))
                print("\tTile state: '", tile.state, "'")

                if tile.state == ' ':
                    # Si la baldosa está limpia no hace nada, solo se mueve
                    # If it's clean it doesn't do anything, it just moves
                    print("\033[92m\tIt's clean")
                    self.move()
                else:
                    # Si la baldosa está sucia, la aspiradora llama al método limpiar y se mueve
                    # If it is dirty, it calls the clean method and moves
                    print("\033[91m\tIt's dirty")
                    tile.state = self.clean(tile.state)
                    self.move()
                time.sleep(1)

            except IndexError:
                print('\033[93m _______________')
                print('\033[93m Wall detected')
                print('\033[93m _______________')

                self.change_direction()

            time.sleep(1)

    def clean(self, state):
        print('\033[1m\033[33m\tCleaning...')
        if state == '+':
            return ' '
        elif state == '*':
            return '+'
        elif state == '#':
            return '#'

    def move(self):
        if self.direction == 'r':
            self.position = self.position + 1
            print('\033[94mMoves to tile Nº: ' + str(self.position + 1))
        elif self.direction == 'l':
            self.position = self.position - 1
            print('\033[94mMoves to tile Nº: ' + str(self.position + 1))

    def change_direction(self):
        if self.direction == 'l':
            self.direction = 'r'
            self.position += 1
        elif self.direction == 'r':
            self.direction = 'l'
            self.position -= 1


if __name__ == "__main__":
    size = random.randint(1, 100)

    position = random.randint(0, size - 1)

    floor = Floor(N=size)

    print("Floor size: ", size)
    print("Initial position: ", position)

    vacuum = Vacuum(floor=floor, direction='l', position=position)
    vacuum.run()
