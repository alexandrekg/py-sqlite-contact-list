

def cli():
    print("Opções do programa: \n" +
          "1 - Listar contatos\n" +
          "2 - Listar um contato específico\n" +
          "3 - Adicionar contato\n" +
          "4 - Deletar um contato\n" +
          "5 - Atualizar um contato\n")

    option = 0
    while option == 0:
        option = int(input('Qual opção deseja?'))

        if option == 1:
            print('Listando todos os contatos...')

        if option == 2:
            print('Listando um contato específico...')

        if option == 3:
            print('Adicionando um contato...')

        if option == 4:
            print('Deletando um contato...')

        if option == 5:
            print('Atualizando um contato...')


if __name__ == "__main__":
    cli()