# PyQt5 GUI Caixas de Texto

import pygame as pg
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap

class Janela(QMainWindow):
    pg.mixer.init()
    pg.mixer.music.load('55_.mp3')
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.caixa_texto_altura = QLineEdit(self)
        self.caixa_texto_largura = QLineEdit(self)
        self.imagem = QLabel(self)
        IU.inic_UI(self)

    def altura_muda(self):
        texto = self.sender().text()
        if texto.isdigit():
            texto = int(texto)
            pg.mixer.music.play()
            self.imagem.setGeometry((self.width()-self.imagem.width())//2,
                                    (self.height()-self.imagem.height())//2,
                                    self.imagem.width(), texto)

                
    def largura_muda(self):
        texto = self.sender().text()
        if texto.isdigit():
            texto = int(texto)
            pg.mixer.music.play()
            self.imagem.setGeometry((self.width()-self.imagem.width())//2,
                                    (self.height()-self.imagem.height())//2,
                                    texto, self.imagem.height())            


class IU(Janela):
    def __init__(self):
        super().__init__()

    def inic_UI(self):
        self.imagem.setPixmap(QPixmap('48_banana.jpeg'))
        self.imagem.setGeometry((self.width()-self.imagem.width())//2,
                                (self.height()-self.imagem.height())//2, 0, 0)
        self.imagem.setScaledContents(True)
        self.caixa_texto_altura.setPlaceholderText('Altura')
        self.caixa_texto_largura.setPlaceholderText('Largura')
        self.caixa_texto_altura.setGeometry(0, 0, 150, 45)
        self.caixa_texto_largura.setGeometry(150, 0, 150, 45)
        self.caixa_texto_altura.setStyleSheet('font-size: 30px')
        self.caixa_texto_largura.setStyleSheet('font-size: 30px')
        self.caixa_texto_altura.textChanged.connect(self.altura_muda)
        self.caixa_texto_largura.textChanged.connect(self.largura_muda)


def main():
    app = QApplication(sys.argv)
    janela = Janela()
    janela.show()
    sys.exit(app.exec_())

main()