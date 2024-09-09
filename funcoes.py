import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# adição de valores
def inserir_dados_livros():
    while True:
        try:
            titulo = input("Nome do livro: ")
            genero = input("Gênero do livro: ")
            try:
                current_year = 2024
                ano = int(input("Ano de lançamento: "))
                if ano > current_year:
                    raise ValueError("Ano inválido\n")
            except ValueError as e:
                print(f"Erro: {e}")
                continue 
            
            qtd_dsp = int(input("Quantidade disponível: "))
            
            cursor.execute("""
                INSERT INTO Livros (Titulo, Gênero, Ano, Qtd_dsp)
                VALUES (?, ?, ?, ?)
            """, (titulo, genero, ano, qtd_dsp))
            conn.commit()
            print("\nLivro adicionado com sucesso!")
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados no banco: {e}")
            conn.rollback()
            
        while True:
            print("""
                    [1] - Adicionar mais um livro
                    [2] - Sair
                    """)
            continuar = input("-> Opção:\n")
            match continuar:
                case '1':
                    break
                case '2':
                    return
                case _:
                    print("\nOpção inválida. Digite 1 ou 2")

# remoção de valores
def remover_dados_livros():
    while True:
        try:
            id_livro = int(input("\nID do Livro:\n"))
            cursor.execute("""
                SELECT ID_Livro, Titulo FROM Livros
                WHERE ID_Livro = ?
                        """, (id_livro,))
            livro = cursor.fetchone()
            
            if livro:
                titulo = livro[1]
                try:
                    cursor.execute("""
                        DELETE FROM Livros
                        WHERE ID_Livro = ?
                                """, (id_livro,))
                    conn.commit()
                    print(f"\nLivro {titulo} removido  com sucesso")
                except sqlite3.Error as e:
                    print(f"\nLivro não encontrado na tabela {e}")
                    conn.rollback()
            else:
                print("Livro não encontrado na tabela")
        except ValueError:
            print("ID inválido. Insira um número válido")
        except sqlite3.Error as e:
            print(f"\nErro no banco de dados: {e}")
            
        while True:
            print("""
                [1] - Remover mais um livro
                [2] - Sair
                """)
            continuar = input("-> Opção: ")
            match continuar:
                case "1":
                    break
                case "2":
                    return
                case _:
                    print("Opção inválida. Digite 1 ou 2")
            
# atualização de valores
def atualizar_valores():
    while True:
        id_livro = int(input("\nID do Livro:\n"))
        cursor.execute("""
            SELECT ID_Livro FROM Livros
            WHERE ID_Livro = ?
                       """, (id_livro,))
        livro = cursor.fetchone()
        
        if livro:
            pergunta = int(input("""
                Qual registro deseja alterar?
                [1] - Título
                [2] - Gênero
                [3] - Ano
                [4] - Quantidade Disponível\n
                -> Opção:\n"""))
            
            match pergunta:
                case 1:
                    novo_titulo = input("Novo título: ")
                    cursor.execute("""
                        UPDATE Livros
                        SET Titulo = ?
                        WHERE ID_Livro = ?
                                   """, (novo_titulo, id_livro))
                    conn.commit()
                    print("\nTítulo atualizado com sucesso")
                case 2:
                    novo_genero = input("Novo gênero: ")
                    cursor.execute("""
                        UPDATE Livros
                        SET Gênero = ?
                        WHERE ID_Livro = ?
                                   """,novo_genero, id_livro)
                    conn.commit()
                    print("\nGênero atualizado com sucesso")
                case 3:
                    novo_ano = int(input("Novo ano: "))
                    cursor.execute("""
                        UPDATE Livros
                        SET Ano = ?
                        WHERE ID_Livro = ?
                                   """, (novo_ano, id_livro))
                    conn.commit()
                    print("\nAno atualizado com sucesso")
                case 4:
                    nova_qtd_dsp = int(input("Nova quantidade disponível: "))
                    cursor.execute("""
                        UPDATE Livros
                        SET Qtd_dsp = ?
                        WHERE ID_Livro = ?
                                   """, nova_qtd_dsp, id_livro)
                    conn.commit()
                    print("\nQuantidade disponível atualizada com sucesso")
                case _:
                    print("\nOpção inválida. Digite 1, 2, 3 ou 4")
                    continue
        else:
            print("\nID do livro não encontrado")
        
        continuar = input("""
           Deseja continuar? [S/N]
            -> Opção:  """)
        if continuar.lower() != 's':
            break
            
# busca de valores
def buscar_valores():
    while True:
        id_livro = int(input("\nID do Livro:\n"))
        cursor.execute("""
            SELECT ID_Livro, Titulo, Gênero, Ano, Qtd_dsp FROM Livros
            WHERE ID_Livro = ?
                       """, (id_livro,))
        livro = cursor.fetchone()
        
        if livro:
            id_livro, titulo, genero, ano, qtd_dsp = livro
            print(f"\n{'-'*10} Detalhes do livro {'-'*10}\n")
            print(f"ID do Livro: {id_livro}")
            print(f"Título: {titulo}")
            print(f"Gênero: {genero}")
            print(f"Ano: {ano}")
            print(f"Quantidade Disponível: {qtd_dsp}\n")
            break
        else:
            print("\nLivro não encontrado na base de dados.")

# listar valores
def listar_valores():
    cursor.execute("""
        SELECT ID_Livro, Titulo FROM Livros
                    """)
    livros = cursor.fetchall()
    for id_livro, titulo in enumerate(livros):
        print(f"{id_livro} - {titulo}")    
        