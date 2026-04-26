# PyQt5 GUI Botões

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.botao = QPushButton('Botão', self)
        IU.inic_IU(self)

    def ao_clicar(self):
        self.botao.setText('Clicado')
        self.botao.setDisabled(True)

class IU(Janela):
    def __init__(self):
        super().__init__()
    
    def inic_IU(self):
        self.botao.setGeometry((self.width()-120)//2,
                               (self.width()-70)//2, 120, 70)
        self.botao.setStyleSheet('font-size: 20px;'
                                 'font-weight: bold;')
                                 #'color: #280a40;'
                                 #'background-color: #b487d6')
        self.botao.clicked.connect(self.ao_clicar)

def main():
    app = QApplication(sys.argv)
    janela = Janela()
    janela.show()
    sys.exit(app.exec_())

main()