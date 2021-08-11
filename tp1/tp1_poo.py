
import random

choices = [" ", "+", "*", "#"]

class Tile:

	def __init__(self):
		self.state = random.choice(choices)
		self.vecesQuePaso = 0


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
			while self.position >= 0 and self.position <= self.floor.size:
				print(self.position)
				tile = self.floor.tiled[self.position]
				if tile.state == ' ' :
					self.move()
				else:
					tile.state = self.clean(tile.state)	
					self.move()
				print(tile.state)

			if self.position <= 0:
				self.position = 0
				self.changeDirection()
			elif self.position >= self.floor.size:
				self.position = self.floor.size
				self.changeDirection()



	def clean(self, state):
		print('se limpió')
		if state == '+':
			return ' '
		elif state == '*':
			return '+'
		elif state == '#':
			return '#'



	def move(self):
		print('se movió')
		if self.direction == 'r':
			self.position = self.position + 1
		elif self.direction == 'l':
			self.position = self.position - 1

	def changeDirection(self):
		print('cambió de dirección')
		if self.direction == 'l':
			self.direction = 'r'
		elif self.direction == 'r':
			self.direction = 'l'		
		# if self.position == self.floor.size:
		# 	self.direction = 'l'
		# elif self.position == 0:
		# 	self.direction = 'r'


if (__name__ == "__main__"):

	floor = Floor(N=10)

	vacuum = Vacuum(floor=floor, direction='l', position=5)
	vacuum.run()

