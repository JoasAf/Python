# PyQt5 GUI imagens

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        imagem = QLabel(self)
        imagem.setPixmap(QPixmap('48_banana.jpeg'))
        imagem.setGeometry((self.width()-250)//2,
                           (self.height()-250)//2, 250, 250)
        imagem.setScaledContents(True)

def main():
    app = QApplication(sys.argv)
    janela = Janela()
    janela.show()
    sys.exit(app.exec_())

main()