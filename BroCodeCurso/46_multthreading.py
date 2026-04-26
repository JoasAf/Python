# multithreading = Usado para executar múltiplas tarefas simultaneamente (multitarefa)
#                  Bom para tarefas com E/S como leitura de arquivos ou obtenção de dados de APIs
#                  threading.Thread(target=minha_funcao)

import threading
from time import sleep as demora

def fazer_cafe():
    demora(3)
    print('Você terminou de fazer café')

def estudar(oque):
    demora(6)
    print(f'Você terminou de estudar {oque}')

def treinar():
    demora(2)
    print('Você terminou de treinar')

tarefa1 = threading.Thread(target=fazer_cafe)
tarefa2 = threading.Thread(target=estudar, args=('Python',))
tarefa3 = threading.Thread(target=treinar)

tarefa1.start()
tarefa2.start()
tarefa3.start()

tarefa1.join()
tarefa2.join()
tarefa3.join()

print('Todas as tarefas foram feitas')
