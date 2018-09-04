#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from random import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,QMessageBox)
from PyQt5.QtGui import QPainter, QColor, QFont,QIcon


arr=[[0,0,0,0,0,0,0,0] for i in range(10)]
state=1
safe_tile=68


class Example(QWidget):

	def __init__(self):
		super().__init__()
		self.initUI()


	def initUI(self):
		self.setGeometry(300, 0, 170, 230)
		self.setWindowTitle('M-sweeper')
		self.btn=[[QPushButton('', self),QPushButton('', self),QPushButton('', self),QPushButton('', self),QPushButton('', self),QPushButton('', self),QPushButton('', self),QPushButton('', self)] for i in range(10)]

		pos=[[(),(),(),(),(),(),(),()] for i in range(10)]

		self.btn[0][0].clicked.connect(lambda:self.buttonClicked(self.btn,0,0,1))	#Connecting buttons and action
		self.btn[0][1].clicked.connect(lambda:self.buttonClicked(self.btn,0,1,1))
		self.btn[0][2].clicked.connect(lambda:self.buttonClicked(self.btn,0,2,1))
		self.btn[0][3].clicked.connect(lambda:self.buttonClicked(self.btn,0,3,1))
		self.btn[0][4].clicked.connect(lambda:self.buttonClicked(self.btn,0,4,1))
		self.btn[0][5].clicked.connect(lambda:self.buttonClicked(self.btn,0,5,1))
		self.btn[0][6].clicked.connect(lambda:self.buttonClicked(self.btn,0,6,1))
		self.btn[0][7].clicked.connect(lambda:self.buttonClicked(self.btn,0,7,1))

		self.btn[1][0].clicked.connect(lambda:self.buttonClicked(self.btn,1,0,1))
		self.btn[1][1].clicked.connect(lambda:self.buttonClicked(self.btn,1,1,1))
		self.btn[1][2].clicked.connect(lambda:self.buttonClicked(self.btn,1,2,1))
		self.btn[1][3].clicked.connect(lambda:self.buttonClicked(self.btn,1,3,1))
		self.btn[1][4].clicked.connect(lambda:self.buttonClicked(self.btn,1,4,1))
		self.btn[1][5].clicked.connect(lambda:self.buttonClicked(self.btn,1,5,1))
		self.btn[1][6].clicked.connect(lambda:self.buttonClicked(self.btn,1,6,1))
		self.btn[1][7].clicked.connect(lambda:self.buttonClicked(self.btn,1,7,1))

		self.btn[2][0].clicked.connect(lambda:self.buttonClicked(self.btn,2,0,1))
		self.btn[2][1].clicked.connect(lambda:self.buttonClicked(self.btn,2,1,1))
		self.btn[2][2].clicked.connect(lambda:self.buttonClicked(self.btn,2,2,1))
		self.btn[2][3].clicked.connect(lambda:self.buttonClicked(self.btn,2,3,1))
		self.btn[2][4].clicked.connect(lambda:self.buttonClicked(self.btn,2,4,1))
		self.btn[2][5].clicked.connect(lambda:self.buttonClicked(self.btn,2,5,1))
		self.btn[2][6].clicked.connect(lambda:self.buttonClicked(self.btn,2,6,1))
		self.btn[2][7].clicked.connect(lambda:self.buttonClicked(self.btn,2,7,1))

		self.btn[3][0].clicked.connect(lambda:self.buttonClicked(self.btn,3,0,1))
		self.btn[3][1].clicked.connect(lambda:self.buttonClicked(self.btn,3,1,1))
		self.btn[3][2].clicked.connect(lambda:self.buttonClicked(self.btn,3,2,1))
		self.btn[3][3].clicked.connect(lambda:self.buttonClicked(self.btn,3,3,1))
		self.btn[3][4].clicked.connect(lambda:self.buttonClicked(self.btn,3,4,1))
		self.btn[3][5].clicked.connect(lambda:self.buttonClicked(self.btn,3,5,1))
		self.btn[3][6].clicked.connect(lambda:self.buttonClicked(self.btn,3,6,1))
		self.btn[3][7].clicked.connect(lambda:self.buttonClicked(self.btn,3,7,1))

		self.btn[4][0].clicked.connect(lambda:self.buttonClicked(self.btn,4,0,1))
		self.btn[4][1].clicked.connect(lambda:self.buttonClicked(self.btn,4,1,1))
		self.btn[4][2].clicked.connect(lambda:self.buttonClicked(self.btn,4,2,1))
		self.btn[4][3].clicked.connect(lambda:self.buttonClicked(self.btn,4,3,1))
		self.btn[4][4].clicked.connect(lambda:self.buttonClicked(self.btn,4,4,1))
		self.btn[4][5].clicked.connect(lambda:self.buttonClicked(self.btn,4,5,1))
		self.btn[4][6].clicked.connect(lambda:self.buttonClicked(self.btn,4,6,1))
		self.btn[4][7].clicked.connect(lambda:self.buttonClicked(self.btn,4,7,1))

		self.btn[5][0].clicked.connect(lambda:self.buttonClicked(self.btn,5,0,1))
		self.btn[5][1].clicked.connect(lambda:self.buttonClicked(self.btn,5,1,1))
		self.btn[5][2].clicked.connect(lambda:self.buttonClicked(self.btn,5,2,1))
		self.btn[5][3].clicked.connect(lambda:self.buttonClicked(self.btn,5,3,1))
		self.btn[5][4].clicked.connect(lambda:self.buttonClicked(self.btn,5,4,1))
		self.btn[5][5].clicked.connect(lambda:self.buttonClicked(self.btn,5,5,1))
		self.btn[5][6].clicked.connect(lambda:self.buttonClicked(self.btn,5,6,1))
		self.btn[5][7].clicked.connect(lambda:self.buttonClicked(self.btn,5,7,1))

		self.btn[6][0].clicked.connect(lambda:self.buttonClicked(self.btn,6,0,1))
		self.btn[6][1].clicked.connect(lambda:self.buttonClicked(self.btn,6,1,1))
		self.btn[6][2].clicked.connect(lambda:self.buttonClicked(self.btn,6,2,1))
		self.btn[6][3].clicked.connect(lambda:self.buttonClicked(self.btn,6,3,1))
		self.btn[6][4].clicked.connect(lambda:self.buttonClicked(self.btn,6,4,1))
		self.btn[6][5].clicked.connect(lambda:self.buttonClicked(self.btn,6,5,1))
		self.btn[6][6].clicked.connect(lambda:self.buttonClicked(self.btn,6,6,1))
		self.btn[6][7].clicked.connect(lambda:self.buttonClicked(self.btn,6,7,1))

		self.btn[7][0].clicked.connect(lambda:self.buttonClicked(self.btn,7,0,1))
		self.btn[7][1].clicked.connect(lambda:self.buttonClicked(self.btn,7,1,1))
		self.btn[7][2].clicked.connect(lambda:self.buttonClicked(self.btn,7,2,1))
		self.btn[7][3].clicked.connect(lambda:self.buttonClicked(self.btn,7,3,1))
		self.btn[7][4].clicked.connect(lambda:self.buttonClicked(self.btn,7,4,1))
		self.btn[7][5].clicked.connect(lambda:self.buttonClicked(self.btn,7,5,1))
		self.btn[7][6].clicked.connect(lambda:self.buttonClicked(self.btn,7,6,1))
		self.btn[7][7].clicked.connect(lambda:self.buttonClicked(self.btn,7,7,1))

		self.btn[8][0].clicked.connect(lambda:self.buttonClicked(self.btn,8,0,1))
		self.btn[8][1].clicked.connect(lambda:self.buttonClicked(self.btn,8,1,1))
		self.btn[8][2].clicked.connect(lambda:self.buttonClicked(self.btn,8,2,1))
		self.btn[8][3].clicked.connect(lambda:self.buttonClicked(self.btn,8,3,1))
		self.btn[8][4].clicked.connect(lambda:self.buttonClicked(self.btn,8,4,1))
		self.btn[8][5].clicked.connect(lambda:self.buttonClicked(self.btn,8,5,1))
		self.btn[8][6].clicked.connect(lambda:self.buttonClicked(self.btn,8,6,1))
		self.btn[8][7].clicked.connect(lambda:self.buttonClicked(self.btn,8,7,1))

		self.btn[9][0].clicked.connect(lambda:self.buttonClicked(self.btn,9,0,1))
		self.btn[9][1].clicked.connect(lambda:self.buttonClicked(self.btn,9,1,1))
		self.btn[9][2].clicked.connect(lambda:self.buttonClicked(self.btn,9,2,1))
		self.btn[9][3].clicked.connect(lambda:self.buttonClicked(self.btn,9,3,1))
		self.btn[9][4].clicked.connect(lambda:self.buttonClicked(self.btn,9,4,1))
		self.btn[9][5].clicked.connect(lambda:self.buttonClicked(self.btn,9,5,1))
		self.btn[9][6].clicked.connect(lambda:self.buttonClicked(self.btn,9,6,1))
		self.btn[9][7].clicked.connect(lambda:self.buttonClicked(self.btn,9,7,1))

		for i in range(10):						#positioning and resizing buttons
			for j in range(8):		
				self.btn[i][j].resize(20,20)
				self.btn[i][j].move(5+20*j,5+20*i)

		reset=QPushButton('Reset', self)
		reset.resize(80,20)
		reset.move(5,210)
		reset.clicked.connect(lambda:self.restart(self.btn))

		quit=QPushButton('Exit', self)
		quit.clicked.connect(QApplication.instance().quit)
		quit.resize(80,20)
		quit.move(85,210)

		self.show()

	
	def buttonClicked(self,btn,x,y,firstclick):			#action of buttons
		global safe_tile,state,arr
		s=self.sender()
		color = btn[x][y].palette().button().color().name()

		if str(color)=='#ffff00':				#Checking if the button is already clicked
			return
		if state==0:
			return
		if x<0 or y<0 or x>9 or y>7:				#Checking if the button exists or not
			return

		elif arr[x][y]==-1:
			if firstclick==0:				#Checking if the X button is clicked by user 
				return
			state=0
			for i in range(10):
				for j in range(8):
					if arr[i][j]==-1:
						btn[i][j].setText('X')
						btn[i][j].setStyleSheet("background-color: red")
			self.result(-1)
			return

		elif arr[x][y]!=0:					#Button with 1 or more adjacent X
			btn[x][y].setText(str(arr[x][y]))
			btn[x][y].setStyleSheet("background-color: yellow")
			safe_tile-=1
			if safe_tile<=0:
				self.result(1)
			return
		else:							#Buttons with no adjacent X
			safe_tile-=1
			btn[x][y].setStyleSheet("background-color: yellow")
			for i in range(-1,2):
				for j in range(-1,2):
					if i==0 and j==0:
						continue
					if x+i>=0 and x+i<10 and y+j>=0 and y+j<8:
						self.buttonClicked(btn,x+i,y+j,0)
			if safe_tile<=0:
				self.result(1)


	def closeEvent(self, event):
		reply = QMessageBox.question(self, 'Message',
		"Are you sure to quit?", QMessageBox.Yes | 
		QMessageBox.No, QMessageBox.No)

		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()


	def result(self,res):				#Declares the result
		global state
		state=0
		if res==1:
			reply = QMessageBox.question(self, 'Victory!',
			"Congratulations, You Won!! Want to play Again?", QMessageBox.Yes | 
			QMessageBox.No, QMessageBox.No)
		else:
			reply = QMessageBox.question(self, 'Oops!',
			"Sorry,You Lost!! Want to play Again?", QMessageBox.Yes | 
			QMessageBox.No, QMessageBox.No)

		if reply == QMessageBox.Yes:
			self.restart(self.btn)
		

	def restart(self,btn):				#Reset the board to initial position
		global arr,state,safe_tile
		safe_tile=68
		state=1
		arr=[[0,0,0,0,0,0,0,0] for i in range(10)]

		for z in range(4):
			count=0
			while(count<3):
				x=randint(5*(z//2),4+5*(z//2))
				y=randint(4*(z%2),3+4*(z%2))
				if arr[x][y]==-1:
					continue

				count+=1
				arr[x][y]=-1
				for i in range(-1,2):
					for j in range(-1,2):
						if i==0 and j==0:
							arr[x][y]=-1
							continue
						if x+i>=0 and x+i<=9 and y+j>=0 and y+j<=7:
							if arr[x+i][y+j]==-1:
								continue
							arr[x+i][y+j]+=1
		for i in range(10):
			for j in range(8):
				btn[i][j].setText('')
				btn[i][j].setStyleSheet("background-color: white")


if __name__ == '__main__':
	count=0
	arr=[[0,0,0,0,0,0,0,0] for i in range(10)]

	for z in range(4):
		count=0
		while(count<3):
			x=randint(5*(z//2),4+5*(z//2))
			y=randint(4*(z%2),3+4*(z%2))
			if arr[x][y]==-1:
				continue

			count+=1
			arr[x][y]=-1
			for i in range(-1,2):
				for j in range(-1,2):
					if i==0 and j==0:
						arr[x][y]=-1
						continue
					if x+i>=0 and x+i<=9 and y+j>=0 and y+j<=7:
						if arr[x+i][y+j]==-1:
							continue
						arr[x+i][y+j]+=1

	app = QApplication(sys.argv)
	ex=Example()		
	sys.exit(app.exec_())
