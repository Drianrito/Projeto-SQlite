import sqlite3


# Criando conexao
try:
    con = sqlite3.connect('cadastro_moveis.db')
    print('Conexao com o banco de dados realizado com sucesso')
except sqlite3.Error as e:
    print("Erro ao conectar com o bd",e)


# Tabela de alimentos

try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS moveis(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        preco REAL NOT NULL,
        quantidade INTEGER DEFAULT 0,
        categoria_id INTEGER,
        fornecedor_id INTEGER,
        FOREIGN KEY (categoria_id) REFERENCES categorias(id),
        FOREIGN KEY (fornecedor_id) REFERENCES fornecedores(id)   
        )""")
        print('Tabela moveis criada com sucesso!')

except sqlite3.Error as e:
    print('Erro ao criar tabela de produtos', e)


# Tabela de Categorias
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS categorias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE
        )""")
        print('Tabela categorias criada com sucesso!')

except sqlite3.Error as e:
    print('Erro ao criar tabela de categorias', e)

# Tabela Fornecedores
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS fornecedores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        email TEXT,
        endereco TEXT
        )""")
        print('Tabela fornecedores criada com sucesso!')

except sqlite3.Error as e:
    print('Erro ao criar tabela de fornecedores', e)

# Tabela movimentaçoes
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS movimentacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        movel_id INTEGER NOT NULL,
        tipo TEXT CHECK(tipo IN ('entrada', 'saida')) NOT NULL,
        quantidade INTEGER NOT NULL,
        data TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        observacao TEXT,
        FOREIGN KEY (movel_id) REFERENCES moveis(id)
        )""")
        print('Tabela movimentaçoes criada com sucesso!')

except sqlite3.Error as e:
    print('Erro ao criar tabela de movimentaçoes', e)

