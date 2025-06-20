import sqlite3

try:
    con = sqlite3.connect('cadastro_moveis.db')
    print('Conexao com o banco de dados realizado com sucesso')
except sqlite3.Error as e:
    print("Erro ao conectar com o bd",e)

# Tabela de Moveis ----------------------------

def criarMovel(dados):
    """
    Insere um novo móvel no banco.
    dados: lista [nome, descricao, preco, quantidade, categoria_id, fornecedor_id]
    """
    query = """
    INSERT INTO moveis (nome, descricao, preco, quantidade, categoria_id, fornecedor_id)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    try:
        with con:
            con.execute(query, dados)
    except sqlite3.Error as e:
        print("Erro ao inserir móvel:", e)

def verMoveis():
    """
    Retorna uma lista com todos os móveis.
    """
    try:
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM moveis")
            return cur.fetchall()
    except sqlite3.Error as e:
        print("Erro ao buscar móveis:", e)
        return []

def atualizarMovel(dados):
    """
    Atualiza os dados de um móvel existente.
    dados: lista [nome, descricao, preco, quantidade, categoria_id, fornecedor_id, id]
    """
    query = """
    UPDATE moveis
    SET nome = ?, descricao = ?, preco = ?, quantidade = ?, categoria_id = ?, fornecedor_id = ?
    WHERE id = ?
    """
    try:
        with con:
            con.execute(query, dados)
    except sqlite3.Error as e:
        print("Erro ao atualizar móvel:", e)

def deletarMovel(movel_id):
    """
    Deleta um móvel pelo id.
    movel_id: inteiro
    """
    query = "DELETE FROM moveis WHERE id = ?"
    try:
        with con:
            con.execute(query, (movel_id,))
    except sqlite3.Error as e:
        print("Erro ao deletar móvel:", e)


criarMovel(['Cadeira', 'Cadeira estofada preta', 88.0, 89, 1, 1])
atualizarMovel(['Cadeira reformada', 'Nova cor azul', 90.0, 80, 1, 1, 1])
deletarMovel(3)
print(verMoveis())