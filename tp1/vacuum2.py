
import random
import time

choices = [" ", "+", "*", "#"]

class Tile:

	def __init__(self):
		self.state = random.choice(choices)
		self.happened = 0
		self.isStained = False


class Floor:

	def __init__(self, N):
		self.size = N
		self.tiled = [Tile() for x in range(self.size)]

	def printTiled(self): 
		for x in self.tiled:
			# print(vars(x))
			print(x.state)

class Vacuum:

	def __init__(self, floor, direction, position):
		self.floor = floor
		self.direction = direction
		self.position = position

	def run(self):
		while True:
			print(self.floor.printTiled())
			# Esta condición se cumple mientras la aspiradora NO esté en los extremos.
			# Cuando llega a un extremo, sale del while y comprueba el cambio de dirección
			while self.position > 0 and self.position < self.floor.size -1:
				print('		\033[92m Tile Nº:' + str(self.position))
				tile = self.floor.tiled[self.position]
				# Si está limpio no hace nada, solo se mueve
				if tile.state == ' ' :
					print('\033[92m Its clean')
					self.move()
				# Si esta sucio llama al método limpiar y se mueve
				else:
					print('\033[91m Its dirty')
					tile.state = self.clean(tile.state)	
					self.move()
				print(tile.state)
				time.sleep(1)


			if self.position <= 0:
				self.position = 1
				self.changeDirection()
			elif self.position >= self.floor.size -1:
				self.position = self.floor.size -2
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
			print('\033[94m Moves to tile Nº:' + str(self.position))
		elif self.direction == 'l':
			self.position = self.position - 1
			print('\033[94m Moves to tile Nº:' + str(self.position))

	def changeDirection(self):
		print('\033[93m _______________')
		print('\033[93m Wall detected')
		print('\033[93m _______________')
		if self.direction == 'l':
			self.direction = 'r'
		elif self.direction == 'r':
			self.direction = 'l'


if (__name__ == "__main__"):

	size = random.randint(1,100)

	position = random.randint(0, size-1)

	floor = Floor(N=size)

	print(size)
	print(position)
	vacuum = Vacuum(floor=floor, direction='l', position=position)
	vacuum.run()

