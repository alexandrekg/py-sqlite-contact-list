import sqlite3


class Contato:
    def __init__(self):
        self.conn = None

    def connect(self):
        if self.conn is None:
            self.conn = sqlite3.connect('contact_list')

    def get(self):
        self.connect()
        cursor = self.conn.cursor()
        cursor = cursor.execute('SELECT * FROM contato;')
        for data in cursor:
            print(data)
        self.conn.close()

    def get_one(self, c_id):
        self.connect()
        cursor = self.conn.cursor()
        cursor = cursor.execute(f'SELECT * FROM contato WHERE id = {c_id}')
        for data in cursor:
            print(data)
        self.conn.close()


def cli():
    contato = Contato()

    print("Opções do programa: \n" +
          "0 - Encerrar programa\n" +
          "1 - Listar contatos\n" +
          "2 - Listar um contato específico\n" +
          "3 - Adicionar contato\n" +
          "4 - Deletar um contato\n" +
          "5 - Atualizar um contato\n")
    option = 0
    while True:
        conn = contato.conn
        option = int(input('Qual opção deseja?'))

        if option == 1:
            contato.get()

        if option == 2:
            contato.get_one(1)

        if option == 3:
            print('Adicionando contato')
            try:
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
            cursor = conn.cursor()
            cursor.execute('DELETE FROM contato WHERE c_id = 1')
            conn.commit()
            conn.close()
            print('Contato deletado!')
        if option == 5:
            print('Atualizando um contato...')
            cursor = conn.cursor()
            cursor.execute('UPDATE contato SET email = "alexandrecorrigido@gmail.com" WHERE c_id = 1')
            conn.commit()
            print('Contato atualizado')
        if option == 0:
            print('Programa encerrado')
            break

if __name__ == "__main__":
    cli()