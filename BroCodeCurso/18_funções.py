# Funções = E um bloco de código reutilizável
#           coloque () depois do nome da função para invoca-la

def aniversário(nome, anos):
    print(f'Feliz aniversário {nome}!')
    print(f'Você está fazendo {anos} anos!')
    print(f'Feliz aniversário!')

aniversário('Joás', 18)

# return = É uma declaração que finaliza uma função
#          e retorna um valor para o código que a chamou

def nomecompleto(primeiro, último):
    primeiro = primeiro.capitalize()
    último = último.capitalize()
    return primeiro + ' ' + último

print(nomecompleto('joás', 'franco'))