# PyQt5 GUI Introdução

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Introdução') # Nome da Janela
        self.setWindowIcon(QIcon('48_banana.jpeg')) # Ícone da Janela
        self.setGeometry(700, 300, 500, 500) # Posição e Tamanho da Janela

def main():
    app = QApplication(sys.argv)
    janela = Janela()
    janela.show()
    sys.exit(app.exec_())

main()