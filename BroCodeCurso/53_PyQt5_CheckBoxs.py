# PyQt5 GUI CheckBoxs

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel
from PyQt5.QtCore import Qt

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.checkbox = QCheckBox('Qual sua comida favorita?', self)
        self.label = QLabel(self)
        IU.inic_UI(self)

    def checkbox_mudou(self, estado):
        if estado == Qt.Checked:
            self.label.setText('sushi 🍣')
        else:
            self.label.setText('pastel 🍘')

class IU(Janela):
    def __init__(self):
        super().__init__()

    def inic_UI(self):
        self.label.setGeometry(40, 40, 500, 100)
        self.label.setStyleSheet('font-size: 40px')
        self.checkbox.setGeometry(10, 10, 300, 40)
        self.checkbox.setStyleSheet('font-size: 20px; font-family: Calibri; font-weight: bold')
        self.checkbox.stateChanged.connect(self.checkbox_mudou)

def main():
    app = QApplication(sys.argv)
    janela = Janela()
    janela.show()
    sys.exit(app.exec_())

main()