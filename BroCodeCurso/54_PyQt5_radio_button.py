# PyQt5 GUI Radio Button (Botão de opção)

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QRadioButton, QButtonGroup, QLabel

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.opcao1 = QRadioButton('Pizza', self)
        self.opcao2 = QRadioButton('Sushi', self)
        self.opcao3 = QRadioButton('Arigato', self)
        self.grupo_botao = QButtonGroup()
        self.label = QLabel(self)
        self.arilabel = QLabel(self)
        IU.inic_IU(self)

    def botao_opcao_mudou(self):
        botao = self.sender()
        match botao.text():
            case 'Pizza':
                self.label.setGeometry(130, 10, 200, 35)
                self.label.setText('🍕')
            case 'Sushi':
                self.label.setGeometry(130, 60, 200, 35)
                self.label.setText('🍣')
            case 'Arigato':
                self.arilabel.setGeometry(130, 110, 200, 35)
                self.arilabel.setText('🐈‍⬛')
        if not botao.isChecked() and botao.text() == 'Arigato':
            self.arilabel.setText('')
            
            
class IU(Janela):
    def __init__(self):
        super().__init__()

    def inic_IU(self):
        self.opcao1.setGeometry(10, 0, 300, 50)
        self.opcao2.setGeometry(10, 50, 300, 50)
        self.opcao3.setGeometry(10, 100, 300, 50)
        self.label.setGeometry(100, 100, 100, 100)
        self.label.setStyleSheet('font-size: 30px')
        self.arilabel.setGeometry(100, 100, 100, 100)
        self.arilabel.setStyleSheet('font-size: 30px')
        self.setStyleSheet('QRadioButton {'
                           'font-size: 30px;'
                           'font-family: Calibri;'
                           '}')
        
        self.grupo_botao.addButton(self.opcao1)
        self.grupo_botao.addButton(self.opcao2)

        self.opcao1.toggled.connect(self.botao_opcao_mudou)
        self.opcao2.toggled.connect(self.botao_opcao_mudou)
        self.opcao3.toggled.connect(self.botao_opcao_mudou)




def main():
    app = QApplication(sys.argv)
    janela = Janela()
    janela.show()
    sys.exit(app.exec_())

main()