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
        
    def add(self):
        try:
            name = str(input('Digite o nome do contato: '))
            email = str(input('Digite o email do contato: '))
            phone = str(input('Digite o telefone do contato: '))
            self.connect()
            cursor = self.conn.cursor()
            query_insert = """INSERT INTO contato (name, email, phone) VALUES (?, ?, ?)"""
            query_params = (name, email, phone)
            cursor.execute(query_insert, query_params)
            self.conn.commit()
            self.conn.close()
            print('Contato adicionado!')
        except Exception as e:
            print(f'Ocorreu um erro!  \n{e}')

    def delete(self):
        try:
            self.connect()
            cursor = self.conn.cursor()
            query = """DELETE FROM contato WHERE name = ?"""
            query_param = str(input("Digite o nome do contato que deseja deletar: "))
            cursor.execute(query, (query_param,))
            self.conn.commit()
            self.conn.close()
            print('Contato deletado!')
        except Exception as e:
            print(f'Erro: {e}')

    def update(self):
        cursor = self.conn.cursor()
        cursor.execute('UPDATE contato SET email = "alexandrecorrigido@gmail.com" WHERE c_id = 1')
        self.conn.commit()
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
        option = int(input('Qual opção deseja?'))
        if option == 1:
            contato.get()
            return False

        if option == 2:
            contato.get_one(1)
            return False

        if option == 3:
            contato.add()
            return False

        if option == 4:
            contato.delete()
            return False

        if option == 5:
            contato.update()
            return False

        if option == 0:
            print('Programa encerrado')
            break

if __name__ == "__main__":
    cli()