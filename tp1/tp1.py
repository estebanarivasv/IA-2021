import random

def create_enviroment():
	choices = [" ", "+", "*", "#"]
	size = random.randint(1,100)
	line = [random.choice(choices) for x in range(size)]
	position = random.randint(0, size-1)
	print(f"LINE {line}\n POSITION {position}\n LONGITUD {len(line)} \n")
	return position, line

def agente_uno(line:list,position:int):

if __name__ == '__main__':
	position, line = create_enviroment()