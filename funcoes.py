import sqlite3

class Livro:
    def __init__(self, titulo, genero, ano, quantidade_disponivel):
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        self.qtd_dsp = quantidade_disponivel
    
    def coletar_dados_livro(self):
        while True:
            try:
                titulo = TratamentoDeErros.validar_titulo(input("Título: ").strip())
                genero = TratamentoDeErros.validar_genero(input("Gênero: ").strip())
                ano = TratamentoDeErros.validar_ano(input("Ano: ").strip())
                qtd_dsp = TratamentoDeErros.validar_quantidade_disponivel(input("Quantidade disponível: ").strip())
                return titulo, genero, ano, qtd_dsp
            except ValueError as ve:
                print(f"{ve}")
                print("Por favor, tente novamente.\n")


class TratamentoDeErros:
    CURRENT_YEAR = 2024

    @staticmethod
    def validar_titulo(titulo):
        if not titulo.strip():
            raise ValueError("Erro: O título não pode ser vazio.")
        return titulo

    @staticmethod
    def validar_genero(genero):
        if not genero.strip():
            raise ValueError("Erro: O gênero não pode ser vazio.")
        return genero

    @staticmethod
    def validar_ano(ano):
        if not ano.isdigit() or int(ano) > TratamentoDeErros.CURRENT_YEAR or int(ano) < 0:
            raise ValueError("Erro: Ano inválido.")
        return int(ano)

    @staticmethod
    def validar_quantidade_disponivel(quantidade_disponivel):
        if not quantidade_disponivel.isdigit() or int(quantidade_disponivel) < 0:
            raise ValueError("Erro: Quantidade disponível inválida.")
        return int(quantidade_disponivel)


class ControleLivros:
    def __init__(self, conn, cursor):
        self.conn = conn
        self.cursor = cursor

    def inserir_livro(self):
        titulo, genero, ano, quantidade_disponivel = Livro.coletar_dados_livro(self)
        
        try:
            self.cursor.execute("""
                INSERT INTO Livros (Titulo, Gênero, Ano, Qtd_dsp)
                VALUES (?, ?, ?, ?)
            """, (titulo, genero, ano, quantidade_disponivel))
            
            self.conn.commit()
            print("\nLivro adicionado com sucesso!")
        except ValueError as ve:
            print(f"{ve}")
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados no banco: {e}")
            self.conn.rollback()

    def remover_livro(self, id_livro):
        try:
            self.cursor.execute("SELECT Titulo FROM Livros WHERE ID_Livro = ?", (id_livro,))
            livro = self.cursor.fetchone()

            if livro:
                self.cursor.execute("DELETE FROM Livros WHERE ID_Livro = ?", (id_livro,))
                self.conn.commit()
                print(f"\nLivro '{livro[0]}' removido com sucesso!")
            else:
                print("Erro: Livro não encontrado.")
        except sqlite3.Error as e:
            print(f"Erro no banco de dados: {e}")
            self.conn.rollback()

    def atualizar_livro(self, id_livro, titulo=None, genero=None, ano=None, quantidade_disponivel=None):
        titulo, genero, ano, quantidade_disponivel = Livro.coletar_dados_livro(self)
        try:
            campos = []
            valores = []
            
            if titulo:
                campos.append("Titulo = ?")
                valores.append(titulo)
            if genero:
                campos.append("Gênero = ?")
                valores.append(genero)
            if ano:
                campos.append("Ano = ?")
                valores.append(ano)
            if quantidade_disponivel:
                campos.append("Qtd_dsp = ?")
                valores.append(quantidade_disponivel)
            
            valores.append(id_livro)

            if campos:
                self.cursor.execute(f"""
                    UPDATE Livros
                    SET {', '.join(campos)}
                    WHERE ID_Livro = ?
                """, tuple(valores))
                self.conn.commit()
                print("Livro atualizado com sucesso!")
            else:
                print("Nenhum campo para atualizar.")
        except sqlite3.Error as e:
            print(f"Erro ao atualizar o banco de dados: {e}")
            self.conn.rollback()

    def buscar_livro(self, id_livro):
        try:
            self.cursor.execute("SELECT ID_Livro, Titulo, Gênero, Ano, Qtd_dsp FROM Livros WHERE ID_Livro = ?", (id_livro,))
            livro = self.cursor.fetchone()
            if livro:
                print(f"\nID: {livro[0]} \nTítulo: {livro[1]} \nGênero: {livro[2]} \nAno: {livro[3]} \nQuantidade: {livro[4]}")
            else:
                print("Livro não encontrado.")
        except sqlite3.Error as e:
            print(f"Erro ao buscar o livro: {e}")

    def listar_livros(self):
        try:
            self.cursor.execute("SELECT ID_Livro, Titulo FROM Livros")
            livros = self.cursor.fetchall()
            for livro in livros:
                print(f"ID: {livro[0]} \nTítulo: {livro[1]} \n{'=' * 50}\n")
        except sqlite3.Error as e:
            print(f"Erro ao listar os livros: {e}")
#vsf