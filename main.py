from model.contato import Contato


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