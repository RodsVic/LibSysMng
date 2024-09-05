import sqlite3

# conectando DB
connection = sqlite3.connect("library.db")

# criando cursor
cursor = connection.cursor()
cursor.execute("""
    CREATE TABLE Livros(
        ID_Livro INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        ID_Autor INTEGER,
        Titulo TEXT NOT NULL,
        Gênero TEXT NOT NULL,
        Ano TEXT NOT NULL,
        Qtd_dsp INTEGER NOT NULL,
        FOREIGN KEY(ID_Autor) REFERENCES Autores(ID_Autor)
    );
               """)

# criando tabela
cursor.execute("""
    CREATE TABLE Livros(
        ID_Livro INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Título TEXT NOT NULL,
        Gênero TEXT NOT NULL,
        Ano INTEGER NOT NULL,
        Qtd_dsp INTEGER NOT NULL
    );
               """)
cursor.execute("""
    CREATE TABLE Autores(
        ID_Autor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Nacionalidade TEXT NOT NULL,
        Data_Nasc INTEGER NOT NULL
    );
               """)
cursor.execute("""
    CREATE TABLE Users(
        ID_User INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Email TEXT NOT NULL,
        Data_Cad INT NOT NULL
    );
               """)
cursor.execute("""
    CREATE TABLE Empréstimos(
        ID_Empréstimo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        ID_Livro INTEGER NOT NULL,
        ID_User INTEGER NOT NULL,
        Data_Emp INTEGER NOT NULL,
        Data_Dev INTEGER NOT NULL,
        FOREIGN KEY (ID_Livro) REFERENCES Livros(ID_Livro),
        FOREIGN KEY (ID_User) REFERENCES Usuários(ID_User)
    );
               """)

# fechando conexão
print("Tabela criada")
connection.close()

