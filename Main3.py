import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QMessageBox, qApp
from PyQt5.QtGui import QPixmap, QIcon

class MyWindow(QWidget):
    def __init__(self, xpos=0, ypos=0):
        super(MyWindow, self).__init__()
        self.initGUI(xpos, ypos)
        self.setWindowIcon(QIcon("FBicon.png"))



    def initGUI(self, xpos, ypos):
        self.setGeometry(0, 0, 400, 600)
        self.setWindowTitle("Timeline")

        styleSheet = open("style.css")
        qApp.setStyleSheet(styleSheet.read())
        styleSheet.close()



        self.button1 = QPushButton(self)
        self.button1.setText("Like!")
        self.button1.clicked.connect(self.Like)
        self.button1.setObjectName("Like")

        self.button2 = QPushButton(self)
        self.button2.setText("Comment")
        self.button2.clicked.connect(self.Comment)
        self.button2.setObjectName("Comment")

        self.button3 = QPushButton(self)
        self.button3.setText("Share")
        self.button3.clicked.connect(self.Share)
        self.button3.setObjectName("Share")

        self.button4 = QPushButton(self)
        self.button4.setText("Like!")
        self.button4.clicked.connect(self.Like)
        self.button4.setObjectName("Like")


        self.button5 = QPushButton(self)
        self.button5.setText("Comment")
        self.button5.clicked.connect(self.Comment)
        self.button5.setObjectName("Comment")

        self.button6 = QPushButton(self)
        self.button6.setText("Share")
        self.button6.clicked.connect(self.Share)
        self.button6.setObjectName("Share")



        self.button7 = QPushButton(self)
        self.button7.setText("Like!")
        self.button7.clicked.connect(self.Like)
        self.button7.setObjectName("Like")


        self.button8 = QPushButton(self)
        self.button8.setText("Comment")
        self.button8.clicked.connect(self.Comment)
        self.button8.setObjectName("Comment")

        self.button9 = QPushButton(self)
        self.button9.setText("Share")
        self.button9.clicked.connect(self.Share)
        self.button9.setObjectName("Share")


        self.button10 = QPushButton(self)
        self.button10.setText("Like!")
        self.button10.clicked.connect(self.FBLike)
        self.button10.setObjectName("Like")


        self.button11 = QPushButton(self)
        self.button11.setText("Comment")
        self.button11.clicked.connect(self.FBComment)
        self.button11.setObjectName("Comment")

        self.button12 = QPushButton(self)
        self.button12.setText("Share")
        self.button12.clicked.connect(self.Share)
        self.button12.setObjectName("Share")


        self.button13 = QPushButton(self)
        self.button13.setText("Like!")
        self.button13.clicked.connect(self.Like)
        self.button13.setObjectName("Like")


        self.button14 = QPushButton(self)
        self.button14.setText("Comment")
        self.button14.clicked.connect(self.Comment)
        self.button14.setObjectName("Comment")

        self.button15 = QPushButton(self)
        self.button15.setText("Share")
        self.button15.clicked.connect(self.Share)
        self.button15.setObjectName("Share")

        self.button16 = QPushButton(self)
        self.button16.setText("Flag")
        self.button16.clicked.connect(self.Flag)
        self.button16.setObjectName("Flag")

        self.button17 = QPushButton(self)
        self.button17.setText("Flag")
        self.button17.clicked.connect(self.Flag)
        self.button17.setObjectName("Flag")

        self.button18 = QPushButton(self)
        self.button18.setText("Flag")
        self.button18.clicked.connect(self.Flag)
        self.button18.setObjectName("Flag")

        self.button19 = QPushButton(self)
        self.button19.setText("Flag")
        self.button19.clicked.connect(self.FBFlag)
        self.button19.setObjectName("Flag")

        self.button20 = QPushButton(self)
        self.button20.setText("Flag")
        self.button20.clicked.connect(self.Flag)
        self.button20.setObjectName("Flag")


        self.text1 = QLineEdit(self)
        self.text1.setEnabled(False)
        self.text1.setMinimumSize(300,50)
        self.text1.setText("News: Python renamed to Snake")


        self.text2 = QLineEdit(self)
        self.text2.setEnabled(False)
        self.text2.setMinimumSize(300,50)
        self.text2.setText("Confirmed: Half-Life 3!")


        self.text3 = QLineEdit(self)
        self.text3.setEnabled(False)
        self.text3.setMinimumSize(300,50)
        self.text3.setText("Trump: Even Fake News are Fake!")

        self.text4 = QLineEdit(self)
        self.text4.setEnabled(False)
        self.text4.setMinimumSize(300,50)
        self.text4.setText("Data security: Facebook is number 1!")

        self.text5 = QLineEdit(self)
        self.text5.setEnabled(False)
        self.text5.setMinimumSize(300,50)
        self.text5.setText("#Pizzagate - Hillary abuses children!")

        self.text1.move(20, 30)
        self.text2.move(20, 130)
        self.text3.move(20, 230)
        self.text4.move(20, 330)
        self.text5.move(20, 430)


        self.button1.move(20, 85)
        self.button2.move(95, 85)
        self.button3.move(170, 85)
        self.button4.move(20, 185)
        self.button5.move(95, 185)
        self.button6.move(170, 185)
        self.button7.move(20, 285)
        self.button8.move(95, 285)
        self.button9.move(170, 285)
        self.button10.move(20, 385)
        self.button11.move(95, 385)
        self.button12.move(170, 385)
        self.button13.move(20, 485)
        self.button14.move(95, 485)
        self.button15.move(170, 485)
        self.button16.move(325, 40)
        self.button17.move(325, 140)
        self.button18.move(325, 240)
        self.button19.move(325, 340)
        self.button20.move(325,440)


        self.move(xpos, ypos)
        self.show()



    def Like(self):
        QMessageBox.about(self, "Hello", "You just Liked this post!")

    def Comment(self):
        QMessageBox.about(self, "Hello", "You just commented on this post!")

    def Share(self):
        QMessageBox.about(self, "Hello", "You just shared this post with your friends!")

    def FBComment(self):
        QMessageBox.about(self, "Hello", "No need to do that, Jon. We already know everything about you and your opinions!")

    def FBLike(self):
        QMessageBox.about(self, "Hello", "You just Liked this post! But we can never get enough of your Likes - please hit that button again, lad!")

    def FBFlag(self):
        QMessageBox.about(self, "Hello", "Oops something went wrong, please try again later! P.S. Praise Lord ZuckerB!")

    def Flag(self):
          QMessageBox.about(self, "Hello", "You just flagged this post - a staff member will shortly initiate further examinations!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywin1 = MyWindow(360, 0)
    sys.exit(app.exec_())
