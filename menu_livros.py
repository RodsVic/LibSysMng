from funcoes import ControleLivros as CL
import sqlite3
    
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

controle_livros = CL(conn, cursor)

done = False
largura = 10
texto = "Menu de Livros"
dec = "-"

while not done:
    print(f"\n{dec*10} {texto} {dec*10}")
    print("""
        [1] - Adicionar
        [2] - Remover
        [3] - Atualizar
        [4] - Buscar
        [5] - Listar
        [6] - Sair
        """)
    print(f"{dec*10} {texto} {dec*10}")

    escolha = (int(input("\n-> Opção:\n")))
    match escolha:
        case 1:
            # titulo = input("Título: ").strip()
            # genero = input("Gênero: ").strip()
            # ano = input("Ano: ").strip()
            # qtd_dsp = input("Quantidade disponível: ").strip()
            controle_livros.inserir_livro()
        case 2:
            id_livro = int(input("Digite o ID do livro que deseja buscar: "))
            controle_livros.remover_livro(id_livro)
        case 3:
            controle_livros.atualizar_livro()
        case 4:
            id_livro = int(input("Digite o ID do livro que deseja buscar: "))
            controle_livros.buscar_livro(id_livro)
        case 5:
            print()
            controle_livros.listar_livros()
        case 6:
            print("\nSaindo...\n")
            break
        case _:
            print("Número inválido")
            
conn.close()
