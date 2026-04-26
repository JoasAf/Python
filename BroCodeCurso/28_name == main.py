#                              ┌────────────────────────────────────────────────────────────────────┐
# if __name__ == '__main__': = │ Esse script verifica se o arquivo é o arquivo que está esse script │
#                              │ Podendo ser executado ou importado de forma idependente ┌──────────┘
#                ┌─────────────└────┐────────────────────────────────────────────────────┘
#                │ código é modular └────┐
# Boas práticas: │ ajuda na legibilidade └────────┐
#                │ abandona variáveis não globais └─┐
#                │ previne execução não intencional │
#                └──────────────────────────────────┘

def main():
    print('Esse código só pode ser executado no script "28_name == main.py"!')

if __name__ == '__main__':
    main()