import random
import time

choices = [" ", "+", "*", "#"]


class Tile:

	def __init__(self):
		self.state = random.choice(choices)
		self.clean_happened = 0
		self.is_stained = False


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
		self.direction = direction
		self.position = position
		self.num_tiles = floor.size
		self.movements = 0
		self.cleaned_tiles = 0

	def run(self):
		print("Number of tiles: ", self.num_tiles)

		while self.cleaned_tiles < self.num_tiles:

			# Esta condición se cumple mientras la aspiradora NO esté en los extremos.
			# Cuando llega a un extremo, sale del while y comprueba el cambio de dirección.

			while 0 <= self.position <= self.floor.size - 1:
				self.floor.print_tiles()
				self.print_position()

				self.movements += 1
				print("Movement No: ", self.movements)

				print('\n\033[92mTile Nº:' + str(self.position + 1))
				tile = self.floor.tiles[self.position]
				print("Initial tile state: ", tile.state)

				# Si está limpio no hace nada, solo se mueve
				if tile.state == ' ' or (tile.is_stained is True and tile.clean_happened > 3):
					self.cleaned_tiles += 1
					print('Cleaned tiles: ', self.cleaned_tiles, '/', self.num_tiles)
					print('\033[92mIts clean')
					if tile.is_stained is True:
						print("Times that the tile has been cleaned: ", tile.clean_happened)

					self.move()
				# Si esta sucio llama al método limpiar y se mueve
				else:
					print('\033[91mIts dirty')
					tile = self.clean(tile)
					self.move()
				print("New tile state: '", tile.state, "'")
				time.sleep(1)

			if self.position <= -1:
				# Cuando se salga del extremo izquierdo, que lo vuelva a posicionar en la posicion 0
				self.position = 0
				self.change_direction()
			elif self.position >= self.floor.size:
				# Cuando se salga del extremo derecho, que lo vuelva a posicionar en la última posicion
				self.position = self.floor.size - 1
				self.change_direction()
			time.sleep(1)

			print(' ')
			print('\033[1m \033[92m -----------------')
			print('\033[1m \033[92m Restart')
			print('\033[1m \033[92m -----------------')
			print(' ')

		print("Final state: ", self.floor.print_tiles())

	def print_position(self):
		position = []
		for x in self.floor.tiles:
			position.append(x.clean_happened)
		position[self.position] = "V"
		print("Vacuum position and times cleaned: ", position)

	def clean(self, tile):
		print('Cleaning')
		# El entorno se modifica pero la aspiradora realmente no reconoce los tipos de suciedad
		if tile.state == '+':
			tile.state = ' '
		elif tile.state == '*':
			tile.state = '+'
		elif tile.state == '#':
			tile.state = '#'
		tile.clean_happened += 1

		# Si la baldosa sigue sucia, y ya fue limpiada, se marca como manchada.
		if tile.state == '#' and tile.clean_happened < 4:
			tile.is_stained = True

		return tile

	def move(self):
		if self.direction == 'r':
			self.position = self.position + 1
			print('\033[94mMoves to tile Nº:' + str(self.position + 1))
		elif self.direction == 'l':
			self.position = self.position - 1
			print('\033[94mMoves to tile Nº:' + str(self.position + 1))

	def change_direction(self):
		print('\033[93m _______________')
		print('\033[93m Wall detected')
		print('\033[93m _______________')
		if self.direction == 'l':
			self.direction = 'r'
		elif self.direction == 'r':
			self.direction = 'l'


if __name__ == "__main__":
	size = random.randint(1, 100)

	position = random.randint(0, size - 1)

	floor = Floor(N=10)

	print("Floor size: ", size)
	print("Initial position: ", position)

	vacuum = Vacuum(floor=floor, direction='l', position=5)
	vacuum.run()
