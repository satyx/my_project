#A calculator that calculates two terms at a time.
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import math

entry="0"	#used storing a particular number in an expression
net_val=0       #stores the net result
opr=False       #stores if the previous entry was a operator or not
c_operation,p_operation="+","+"	#stores previous and present operator including '='
num_input=0	#stores if the entering of any number has yet been started or not.
                #Actually used for determining if - sign belongs to the expression or does it indicates a -ve number

class Calc(QWidget):	#Declaration of window and button
    def __init__(self):
        super().__init__()
        self.title = "Calculator"
        self.left = 10
        self.top = 10
        self.width = 270
        self.height = 320
        self.line = QLineEdit(self)
        self.line.move(15,15)
        self.line.setReadOnly(True)
        self.line.setAlignment(Qt.AlignRight)
        font = self.line.font()
        font.setPointSize(18)
        self.line.setFont(font)
        self.line.resize(240, 40)
        self.line.setText("0")

        self.initUI()

    def initUI(self):	#Declaration and customisation of window and button

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        num = [0,1,2,3,4,5,6,7,8,9]

        for i in range(1,10):
            num[i]=QPushButton(str(i),self)
            num[i].move(15+((i-1)%3)*50,215-((int)((i-1)/3))*50)
            num[i].resize(40,40)
            num[i].clicked.connect(self.Num)

        num[0]=QPushButton("0",self)
        num[0].move(15,265)
        num[0].resize(40,40)
        num[0].clicked.connect(self.Num)
        
        point=QPushButton(".",self)
        point.move(65,265)
        point.resize(40,40)
        point.clicked.connect(self.POINT)
        
        modulus=QPushButton("%",self)
        modulus.move(115,265)
        modulus.resize(40,40)
        modulus.clicked.connect(self.operator)
        
        plus=QPushButton("+",self)
        plus.move(165,265)
        plus.resize(40,40)
        plus.clicked.connect(self.operator)
        
        equals=QPushButton("=",self)
        equals.move(215,215)
        equals.resize(40,90)
        equals.clicked.connect(self.FINAL)

        minus=QPushButton("-",self)
        minus.move(165,215)
        minus.resize(40,40)
        minus.clicked.connect(self.operator)
        
        multiply=QPushButton("X",self)
        multiply.move(165,165)
        multiply.resize(40,40)
        multiply.clicked.connect(self.operator)
        
        divide=QPushButton("/",self)
        divide.move(165,115)
        divide.resize(40,40)
        divide.clicked.connect(self.operator)
        
        squared=QPushButton("x²",self)
        squared.move(215,115)
        squared.resize(40,40)
        squared.clicked.connect(self.SQUARED)

        root=QPushButton("x½",self)
        root.move(215,165)
        root.resize(40,40)
        root.clicked.connect(self.ROOT)
        
        ce=QPushButton("CE",self)
        ce.move(15,65)
        ce.resize(115,40)
        ce.clicked.connect(self.CE)
        
        c=QPushButton("C",self)
        c.move(140,65)
        c.resize(115,40)
        c.clicked.connect(self.C)

        self.show()


    def Num(self):	#Responsible for dealing with numeric entry
        #print("inside num")
        global entry,net_val,opr,num_input
        num_input=1;	#Indicates that input of digits has been started
        if opr==False:
            entry=str(entry)+self.sender().text()
        else:
            opr=False
            entry=str((entry)+(self.sender().text()))

        if "." not in entry and "-" not in entry:    #To convert the input into appropriated form i.e. integer or decimal
            entry=str(int(float(entry)))
            self.line.setText(entry)
        else:
            self.line.setText(entry)


    def operator(self):
        #print("inside operator")
        self.line.setText("0")
        global c_operation,p_operation,entry,num_input
        c_operation=str(self.sender().text())
        
        if c_operation=="CE":
            self.CE()
        elif c_operation=="C":
            self.C()
            self.line.setText("0")
        else:
            if num_input==0 and c_operation=="-":	#prints the - sign if it doesn't belong to expression i.e.
							#number is itself negative
                entry="-"
                c_operation="+"
                self.line.setText(entry)
                num_input=1
            else:
                temp=self.EQUALS()
                if temp=="error":			#Determines if the calculations are valid or not
                    self.display("error")
                    self.new()
                else:
                    entry="0"
                    num_input=0
                    p_operation=c_operation
            opr=True
        

    def EQUALS(self):		#Responsible for calculating the result
        #print("inside EQUAL")
        global p_operation,entry,net_val
        
        try: 			#Mostly handles mathematcal errors line division by 0
            if p_operation=="+":
                net_val=net_val+float(entry)
            elif p_operation=="-":
                net_val=net_val-float(entry)
            elif p_operation=="X":
                net_val=net_val*float(entry)
            elif p_operation=="/":
                net_val=net_val/float(entry)
            elif p_operation=="%":
                net_val=net_val%float(entry)
            
            if c_operation=="=":
                self.new()
            return net_val
        except:
            entry="0"
            return "error"


    def FINAL(self):	#prints the final result
        #print("inside FINAL")
        global p_operation,net_val,entry
        temp=self.EQUALS()
        if temp=="error":
            self.display(temp)
        else:
            self.display(net_val)

        self.new()


    def SQUARED(self):	#calculate the square
        #print("inside SQUARED")
        try:
            global entry
            temp=self.set_POINT()**2
            if temp-int(temp)==0:
                entry=str(int(temp))
            else:
                entry=str(temp)
            self.display(float(entry))
        except:
            self.display("error")
            self.new()

        
    def ROOT(self):	#Calculate the square-root
        #print("inside ROOT")
        try:
            global entry
            if float(entry)<0:
                self.display("error")
                self.new()
            else:
                temp=self.set_POINT()**(1/2.0)
                if temp-int(temp)==0:
                    entry=str(int(temp))
                else:
                    entry=str(temp)
                self.display(float(entry))
        except:
            self.display("error")
            self.new()


    def POINT(self):	#add point if user enters a decimal
        #print("inside point")
        global entry
        if "." not in entry:	#Prevents adding decimal if the number already number has a decimal
            entry=entry+"."

        self.line.setText(entry)
        
    def set_POINT(self):	#makes the number of appropriate form
        #print("inside set_point")
        global entry
        if "." in entry:
            self.line.setText(str(int(float(entry))))
        else: 
            self.line.setText(entry)
        return float(entry)


    def CE(self):		#Reset the calculator
        #print("inside CE")
        self.new()
        self.display(0.0)
        

    def new(self):		#Reinitialise global variables
        #print("inside new")
        global net_val,entry,c_operation,p_operation,opr,num_input
        net_val=0.0
        c_operation,p_operation="+","+"
        entry="0"
        opr=False
        num_input=0

        
    def display(self,val):	#Display the output
        #print("inside display")
        if val==0.0:
            self.line.setText("0")
        elif val=="error":
            self.line.setText("Illegal Operation")
        else:					#Output is customised so that it fits the screen
            range=int(math.log(abs(val),10))
            if range>=13:
                self.line.setText("Overflow")
            else:
                if abs(val-int(val))<0.000001:	#Prevents the error due to floating type like 5/2.5 may result in
						#2.00000000001
                    self.line.setText(str(int(val)))     
                else:
                    output=val*math.pow(10,13-range)
                    output=int(output)
                    output/=math.pow(10,13-range)
                    self.line.setText(str(output))
        
        
    def C(self):				#Clears the current entry
        #print("inside C")
        global entry
        entry="0"
        self.display(0.0)
            
        
def main():					#main function
    app = QApplication(sys.argv)
    main = Calc()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
  
