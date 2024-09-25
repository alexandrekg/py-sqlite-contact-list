import sqlite3



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
            print('Adicionando contato')
            try:
                conn = sqlite3.connect('contact_list')
                cursor = conn.cursor()
                cursor.execute("""
                                      INSERT INTO contato VALUES
                                      (1, 'Teste 1', '5199345123', 'alexandreteste1@gmail.com'),
                                      (2, 'Teste 2', '5555532321', 'alexandreteste2@gmail.com')
                                   """)
                conn.commit()
                conn.close()
            except Exception as e:
                print(f'Registro já existe  \n{e}')
            print('Contato adicionado')

        if option == 4:
            print('Deletando um contato...')

        if option == 5:
            print('Atualizando um contato...')


if __name__ == "__main__":
    cli()