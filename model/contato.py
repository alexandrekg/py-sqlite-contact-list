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
        self.connect()
        cursor = self.conn.cursor()
        name = str(input('Digite o nome do contato que quer atualizar: '))
        result_cursor = next(cursor.execute('SELECT * FROM contato WHERE name = ?', (name, )))
        print('Dados atuais do contato:\n'
              f'id: {result_cursor[0]}\n'
              f'nome: {result_cursor[1]}\n'
              f'email: {result_cursor[2]}\n'
              f'telefone: {result_cursor[3]}\n')
        new_name = str(input('Digite o novo nome do contato: '))
        query = """UPDATE contato SET name = ? WHERE id = ?"""
        params = (new_name, int(result_cursor[0]))
        cursor.execute(query, params)
        self.conn.commit()
        self.conn.close()
