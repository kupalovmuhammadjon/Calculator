from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from os import *


class mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        
        #rotate counter
        self.count = 0
        
        self.setWindowTitle("Calculator")
        self.setMinimumSize(345, 600)
        self.setMaximumSize(345, 600)
        self.setStyleSheet("background-color: black;")
        self.setFont(QFont("montserrat-bold;", 20))

        rotatebtn = QPushButton(self)
        rotatebtn.setGeometry(15, 15, 70, 30)
        rotatebtn.setFont(QFont("montserrat-bold", 12, weight = 60))
        rotatebtn.setText("rotate")
        rotatebtn.setStyleSheet("background-color: #A5A5A5;")
        rotatebtn.clicked.connect(lambda : rotate(self))
        
        userInput = QLabel(self)
        userInput.setStyleSheet("color: #FEFBF1;")
        userInput.setFont(QFont("montserrat-bold", 20))
        userInput.setGeometry(15, 100, 350, 50)


        acButton = QPushButton(self)
        acButton.setGeometry(15, 170, 70, 70)
        acButton.setFont(QFont("montserrat-bold", 16, weight = 65))
        acButton.setText("AC")
        acButton.setStyleSheet("border-radius: 35;"
                            "background-color: #A5A5A5;")
        acButton.clicked.connect(lambda : ac(self))

        plmin = QPushButton(self)
        plmin.setGeometry(95, 170, 70, 70)
        plmin.setFont(QFont("montserrat-bold", 15, weight = 60))
        plmin.setText("+/-")
        plmin.setStyleSheet("border-radius: 35;"
                            "background-color: #A5A5A5;")
        plmin.clicked.connect(lambda : plusminus(self))

        pbtn = QPushButton(self)
        pbtn.setGeometry(175, 170, 70, 70)
        pbtn.setFont(QFont("montserrat-bold", 15, weight = 60))
        pbtn.setText("%")
        pbtn.setStyleSheet("border-radius: 35;"
                            "background-color: #A5A5A5;")
        pbtn.clicked.connect(lambda : percent(self))

        dvbtn = QPushButton(self)
        dvbtn.setGeometry(255, 170, 70, 70)
        dvbtn.setFont(QFont("montserrat-bold", 15, weight = 60))
        dvbtn.setText("÷")
        dvbtn.setStyleSheet("border-radius: 35;"
                            "background-color: #FF9F0A;"
                            "color: #FCFFF8")
        dvbtn.clicked.connect(lambda : devide(self))
        
        btn7 = QPushButton(self)
        btn7.setGeometry(15, 255, 70, 70)
        btn7.setFont(QFont("montserrat-bold", 15, weight = 60))
        btn7.setText("7")
        btn7.setStyleSheet("border-radius: 35;"
                               "background-color: #333333;"
                               "color: #FCFFF8")
        btn7.clicked.connect(lambda: seven(self))

        btn8 = QPushButton(self)
        btn8.setGeometry(95, 255, 70, 70)
        btn8.setFont(QFont("montserrat-bold", 15, weight = 60))
        btn8.setText("8")
        btn8.setStyleSheet("border-radius: 35;"
                            "background-color: #333333;"
                            "color: #FCFFF8")
        btn8.clicked.connect(lambda : eight(self))

        btn9 = QPushButton(self)
        btn9.setGeometry(175, 255, 70, 70)
        btn9.setFont(QFont("montserrat-bold", 15, weight = 60))
        btn9.setText("9")
        btn9.setStyleSheet("border-radius: 35;"
                            "background-color: #333333;"
                            "color: #FCFFF8")
        btn9.clicked.connect(lambda : nine(self))

        multiplybtn = QPushButton(self)
        multiplybtn.setGeometry(255, 255, 70, 70)
        multiplybtn.setFont(QFont("montserrat-bold", 15, weight = 60))
        multiplybtn.setText("×")
        multiplybtn.setStyleSheet("border-radius: 35;"
                            "background-color: #FF9F0A;"
                            "color: #FCFFF8")
        multiplybtn.clicked.connect(lambda : multiply(self))
        
        btn4 = QPushButton(self)
        btn4.setGeometry(15, 340, 70, 70)
        btn4.setFont(QFont("montserrat-bold", 16))
        btn4.setText("4")
        btn4.setStyleSheet("border-radius: 35;"
                               "background-color: #333333;"
                               "color: #FCFFF8")
        btn4.clicked.connect(lambda : four(self))

        btn5 = QPushButton(self)
        btn5.setGeometry(95, 340, 70, 70)
        btn5.setFont(QFont("montserrat-bold", 16))
        btn5.setText("5")
        btn5.setStyleSheet("border-radius: 35;"
                            "background-color: #333333;"
                            "color: #FCFFF8")
        btn5.clicked.connect(lambda : five(self))

        btn6 = QPushButton(self)
        btn6.setGeometry(175, 340, 70, 70)
        btn6.setFont(QFont("montserrat-bold", 16))
        btn6.setText("6")
        btn6.setStyleSheet("border-radius: 35;"
                            "background-color: #333333;"
                            "color: #FCFFF8")
        btn6.clicked.connect(lambda : six(self))

        minusbtn = QPushButton(self)
        minusbtn.setGeometry(255, 340, 70, 70)
        minusbtn.setFont(QFont("montserrat-bold", 16))
        minusbtn.setText("-")
        minusbtn.setStyleSheet("border-radius: 35;"
                            "background-color: #FF9F0A;"
                            "color: #FCFFF8")
        minusbtn.clicked.connect(lambda : minus(self))
        
        btn1 = QPushButton(self)
        btn1.setGeometry(15, 425, 70, 70)
        btn1.setFont(QFont("montserrat-bold", 16))
        btn1.setText("1")
        btn1.setStyleSheet("border-radius: 35;"
                               "background-color: #333333;"
                               "color: #FCFFF8")
        btn1.clicked.connect(lambda : one(self))

        btn2 = QPushButton(self)
        btn2.setGeometry(95, 425, 70, 70)
        btn2.setFont(QFont("montserrat-bold", 16))
        btn2.setText("2")
        btn2.setStyleSheet("border-radius: 35;"
                            "background-color: #333333;"
                            "color: #FCFFF8")
        btn2.clicked.connect(lambda : two(self))

        btn3 = QPushButton(self)
        btn3.setGeometry(175, 425, 70, 70)
        btn3.setFont(QFont("montserrat-bold", 16))
        btn3.setText("3")
        btn3.setStyleSheet("border-radius: 35;"
                            "background-color: #333333;"
                            "color: #FCFFF8")
        btn3.clicked.connect(lambda : three(self))

        plusbtn = QPushButton(self)
        plusbtn.setGeometry(255, 425, 70, 70)
        plusbtn.setFont(QFont("montserrat-bold", 16))
        plusbtn.setText("+")
        plusbtn.setStyleSheet("border-radius: 35;"
                            "background-color: #FF9F0A;"
                            "color: #FCFFF8")
        plusbtn.clicked.connect(lambda : plus(self))
        
        btn0 = QPushButton(self)
        btn0.setGeometry(15, 510, 155, 70)
        btn0.setFont(QFont("montserrat-bold", 16))
        btn0.setText("0")
        btn0.setStyleSheet("border-radius: 35;"
                            "background-color: #333333;"
                            "color: #FCFFF8")
        btn0.clicked.connect(lambda : zero(self))

        dotbtn = QPushButton(self)
        dotbtn.setGeometry(180, 510, 70, 70)
        dotbtn.setFont(QFont("montserrat-bold", 16))
        dotbtn.setText(".")
        dotbtn.setStyleSheet("border-radius: 35;"
                            "background-color: #333333;"
                            "color: #FCFFF8")
        dotbtn.clicked.connect(lambda : dot(self))

        equalbtn = QPushButton(self)
        equalbtn.setGeometry(255, 510, 70, 70)
        equalbtn.setFont(QFont("montserrat-bold", 16))
        equalbtn.setText("=")
        equalbtn.setStyleSheet("border-radius: 35;"
                            "background-color: #FF9F0A;"
                            "color: #FCFFF8")
        equalbtn.clicked.connect(lambda : calculate(self))
        
        openbtn = QPushButton(self)
        openbtn.setGeometry(345, 170, 70, 70)
        openbtn.setFont(QFont("montserrat-bold", 16))
        openbtn.setText("(")
        openbtn.setStyleSheet("border-radius: 35;"
                            "background-color: #FF9F0A;"
                            "color: #FCFFF8")
        openbtn.clicked.connect(lambda : open())
        
        closebtn = QPushButton(self)
        closebtn.setGeometry(425, 170, 70, 70)
        closebtn.setFont(QFont("montserrat-bold", 16))
        closebtn.setText(")")
        closebtn.setStyleSheet("border-radius: 35;"
                            "background-color: #FF9F0A;"
                            "color: #FCFFF8")
        closebtn.clicked.connect(lambda : close())
        
        
        def rotate(self):
            if self.count % 2 == 0:	
                self.setMinimumSize(675, 600)
                self.setMaximumSize(675, 600)
            else:	
                self.setMinimumSize(345, 600)
                self.setMaximumSize(345, 600)
            self.count += 1
            
        def ac(self):
            userInput.setText("")
        
        def plusminus(self):
            try:
                userInput.setText(str(-1 * int(userInput.text())))
            except:
                if userInput.text == "0.0" or userInput.text == "0":
                    userInput.setText("0")
                
                else:  
                    userInput.setText(str(-1 * float(userInput.text())))
            
        def percent(self):
            if userInput.text() == "0":
                return 0
            
            try:
                userInput.setText(str(int(userInput.text())/100))
            except:
                userInput.setText(str(float(userInput.text())/100))
            
        def devide(self):
            if not userInput.text()[-1].isdigit():
                userInput.setText(userInput.text()[:-1] + "÷")
            else:
                userInput.setText(userInput.text() + "÷")
            
        def multiply(self):
            if not userInput.text()[-1].isdigit():
                userInput.setText(userInput.text()[:-1] + "*")
            else:
                userInput.setText(userInput.text() + "*")

        def minus(self):
            if not userInput.text()[-1].isdigit():
                userInput.setText(userInput.text()[:-1] + "-")
            else:
                userInput.setText(userInput.text() + "-")
            
        def plus(self):
            if not userInput.text()[-1].isdigit():
                userInput.setText(userInput.text()[:-1] + "+")
            else:
                userInput.setText(userInput.text() + "+")
            
        def dot(self):
            
            inp =userInput.text()
            
            if "+" in inp:
                inp.split("+")
                
            elif "-" in inp:
                inp.split("-")
                
            elif "*" in inp:
                inp.split("*")
                
            elif "÷" in inp:
                inp.split("÷")
            
            if "." in inp[-1]:
                return 0
            
            if not inp[-1].isdigit():
                return 0
            else:
                userInput.setText(userInput.text() + ".")
            
        def calculate(self):
            try:
                userInput.setText(str(eval(userInput.text())))
            except:
                m = QMessageBox(self)
                m.critical(self, "Xatolik", "")
                
            
        def zero(self):
            userInput.setText(userInput.text() + "0")
            
        def one(self):
            userInput.setText(userInput.text() + "1")
        
        def two(self):
            userInput.setText(userInput.text() + "2")
        
        def three(self):
            userInput.setText(userInput.text() + "3")
            
        def four(self):
            userInput.setText(userInput.text() + "4")
            
        def five(self):
            userInput.setText(userInput.text() + "5")
            
        def six(self):
            userInput.setText(userInput.text() + "6")
            
        def seven(self):
            userInput.setText(userInput.text() + "7")
        
        def eight(self):
            userInput.setText(userInput.text() + "8")
        
        def nine(self):
            userInput.setText(userInput.text() + "9")
        
        def open():
            userInput.setText(userInput.text() + "(")
        
        def close():
            userInput.setText(userInput.text() + ")")
            
            
        
        
        self.show()


app = QApplication([])
win = mainwindow()
app.exec_()
