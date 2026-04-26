class pc:
    def __init__(self, processador, memória, armazenamento, placadevideo, rgb):
        self.armazenamento = armazenamento
        self.placadevideo = placadevideo
        self.processador = processador
        self.memória = memória
        self.rgb = rgb

    def jogando(self):
        print(f'Acelerando a placa de vídeo {self.placadevideo}')

    def editando(self):
        print(f'O {self.processador} está processando!')

    def especificações(self):
        print(f'{self.processador} {self.memória}GB {self.armazenamento}GB {self.placadevideo}')