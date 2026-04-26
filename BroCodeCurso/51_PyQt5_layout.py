# PyQt5 GUI Layout

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        IU.inic_IU(self)

class IU(Janela):
    def __init__(self):
        super().__init__()

    def inic_IU(self):
        widget_central = QWidget()
        self.setCentralWidget(widget_central)

        label1 = QLabel('1')
        label2 = QLabel('2')
        label3 = QLabel('3')
        label4 = QLabel('4')
        label5 = QLabel('5')

        label1.setStyleSheet('background-color: #ff0000')
        label2.setStyleSheet('background-color: #ff0080')
        label3.setStyleSheet('background-color: #ff00ff')
        label4.setStyleSheet('background-color: #8000ff')
        label5.setStyleSheet('background-color: #0000ff')

        layout = QGridLayout()

        layout.addWidget(label1, 0, 0)
        layout.addWidget(label2, 0, 1)
        layout.addWidget(label3, 0, 2)
        layout.addWidget(label4, 1, 0)
        layout.addWidget(label5, 1, 1)

        widget_central.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    janela = Janela()
    janela.show()
    sys.exit(app.exec_())

main()