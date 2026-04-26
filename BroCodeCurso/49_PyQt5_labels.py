# PyQt5 GUI Labels

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        label = QLabel('Label', self)
        label.setFont(QFont('Calibri',30))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet('color: #38232a;' # cor da letra
                            'background-color: #c28498;' # cor do fundo
                            'font-weight: bold;' # negrito
                            'font-style: italic;' # itálico
                            'text-decoration: underline') # sublinado
        label.setAlignment(Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)
    janela = Janela()
    janela.show()
    sys.exit(app.exec_())

main()