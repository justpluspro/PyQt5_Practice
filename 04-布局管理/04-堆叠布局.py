from PyQt5.QtWidgets import *


class FormA(QWidget):

    def __init__(self):
        super().__init__()
        self.btnPress = QPushButton("buttonA")

        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.btnPress)
        self.setStyleSheet('background-color: green;')


class FormB(QWidget):

    def __init__(self):
        super().__init__()
        self.btnPress = QPushButton("buttonB")

        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.btnPress)
        self.setStyleSheet('background-color: red;')


class TextEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QStackLayout')
        self.resize(700, 300)

        self.btnPress1 = QPushButton("FromA")
        self.btnPress2 = QPushButton("FromB")

        self.form1 = FormA()
        self.form2 = FormB()

        widget = w


app = QApplication([])
firstPageWidget = QWidget()
secondPageWidget = QWidget()
thirdPageWidget = QWidget()

stack_layout = QStackedLayout()
stack_layout.addWidget(firstPageWidget)
stack_layout.addWidget(secondPageWidget)
stack_layout.addWidget(thirdPageWidget)

main_layout = QVBoxLayout()
main_layout.addLayout(stack_layout)

window = QMainWindow()
window.resize(400, 300)
window.move(300, 100)
window.setWindowTitle('stackLayout')
window.setLayout(main_layout)
window.show()
app.exec_()
