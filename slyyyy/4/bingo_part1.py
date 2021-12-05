import os, sys


class BingoBoard:
	idCounter = 0

	def __init__(self, size_x, size_y):
		self.id = BingoBoard.idCounter
		BingoBoard.idCounter += 1

		self.x = size_x
		self.y = size_y

		self.data = []
		self.marks = []

		self.columnCount = [0]*size_x
		self.rowCount = [0]*size_y

		for i in range(size_y):
			self.data.append([0]*size_x)
			self.marks.append([False]*size_x)

	def initNumbers(self, numbers):
		for y in range(self.y):
			for x in range(self.x):
				self.data[y][x] = numbers[y*self.x + x]

	def getId(self):
		return self.id

	def getNumber(self, x, y):
		return self.data[y][x]

	def setNumber(self, x, y, value):
		self.data[y][x] = value

	def markNumber(self, x, y):
		self.marks[y][x] = True
		self.columnCount[x] += 1
		self.rowCount[y] += 1

	def findNumberCoords(self, value):
		for y in range(self.y):
			for x in range(self.x):
				if(self.data[y][x] == value):
					return (x, y)
		return None

	def findAndMarkAndCheckWin(self, value):
		coords = self.findNumberCoords(value)
		if(coords == None): return False

		self.markNumber(coords[0], coords[1])
		return self.checkWinCondition()

	def checkWinCondition(self):
		for i in self.columnCount:
			if i == self.y: return True;
		for i in self.rowCount:
			if i == self.x: return True;
		return False

	def calculateFinalScore(self, factor):
		summ = 0
		for y in range(self.y):
			for x in range(self.x):
				if(self.marks[y][x] == False):
					summ += int(self.data[y][x])

		return summ*factor


	# TODO: REMOVE
	def printBoard(self):
		for y in range(self.y):
			line = ""
			for x in range(self.x):
				line += self.data[y][x]
				if(len(self.data[y][x]) == 1): line += "  | "
				else:  line += " | "
			print(line[:-3])

	def printBoardMarked(self):
		for y in range(self.y):
			line = ""
			for x in range(self.x):
				if(self.marks[y][x] == True):
					line += self.data[y][x] 
					if(len(self.data[y][x]) == 1): line += "  | "
					else:  line += " | "
				else:
					line += "   | "
			print(line[:-3])


def readInput():
	with open("input.txt", 'r') as file:
		lines = file.readlines()
		
		numbers = lines.pop(0).split(',')
		boards = []

		b = None
		b_numbers = []
		for l in lines:
			if(l == "\n"):
				if(b != None):
					b.initNumbers(b_numbers)
					boards.append(b)
					b_numbers = []
				b = BingoBoard(5,5)
			else:
				b_numbers += l.split()

		return { "numbers" : numbers, "boards" : boards}

def main():
	f_input = readInput()

	for number in f_input["numbers"]:
		for b in f_input["boards"]:
			win = b.findAndMarkAndCheckWin(number)
			if(win == True):
				#b.printBoard()
				#print()
				#b.printBoardMarked()
				print("WINNNER!!! - Board No. \"" + str(b.getId()) + "\"")
				print("Winning Number: " + number)
				print("Final Score: " + str(b.calculateFinalScore(int(number))))
				return


if __name__ == "__main__":
	sys.exit(main())