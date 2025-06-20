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
    movel_id: INTEGER
    """
    query = "DELETE FROM moveis WHERE id = ?"
    try:
        with con:
            con.execute(query, (movel_id,))
    except sqlite3.Error as e:
        print("Erro ao deletar móvel:", e)

# Tabela de Categorias ----------------------------

def criarCategoria(dados):
    """
    Insere uma nova categoria no banco.
    dados: lista [nome]
    """
    query = """
    INSERT INTO categorias (nome)
    VALUES (?)
    """
    try:
        with con:
            con.execute(query, dados)
    except sqlite3.Error as e:
        print("Erro ao inserir categoria:", e)

def verCategorias():
    """
    Retorna uma lista com todas as categorias.
    """
    try:
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM categorias")
            return cur.fetchall()
    except sqlite3.Error as e:
        print("Erro ao buscar categorias", e)
        return []

def atualizarCategoria(dados):
    """
    Atualiza os dados de uma categoria existente.
    dados: lista [nome, id]
    """
    query = """
    UPDATE categorias
    SET nome = ?
    WHERE id = ?
    """
    try:
        with con:
            con.execute(query, dados)
    except sqlite3.Error as e:
        print("Erro ao atualizar Categoria:", e)

def deletarCategoria(categoria_id):
    """
    Deleta uma categoria pelo id.
    categoria_id: INTEGER
    """
    query = "DELETE FROM categorias WHERE id = ?"
    try:
        with con:
            con.execute(query, (categoria_id,))
    except sqlite3.Error as e:
        print("Erro ao deletar categoria:", e)


# Tabela de Fornecedores ----------------------------

def criarFornecedor(dados):
    """
    Insere um novo fornecedor no banco.
    dados: lista [nome, telefone, email, endereco]
    """
    query = """
    INSERT INTO fornecedores (nome, telefone, email, endereco)
    VALUES (?, ?, ?, ?)
    """
    try:
        with con:
            con.execute(query, dados)
    except sqlite3.Error as e:
        print("Erro ao inserir fornecedor:", e)

def verFornecedores():
    """
    Retorna uma lista com todos os fornecedores.
    """
    try:
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM fornecedores")
            return cur.fetchall()
    except sqlite3.Error as e:
        print("Erro ao buscar fornecedores:", e)
        return []

def atualizarFornecedor(dados):
    """
    Atualiza os dados de um fornecedor existente.
    dados: lista [nome, telefone, email, endereco, id]
    """
    query = """
    UPDATE fornecedores
    SET nome = ?, telefone = ?, email = ?, endereco = ?
    WHERE id = ?
    """
    try:
        with con:
            con.execute(query, dados)
    except sqlite3.Error as e:
        print("Erro ao atualizar fornecedor:", e)

def deletarFornecedor(fornecedor_id):
    """
    Deleta um fornecedor pelo id.
    fornecedor_id = INTEGER
    """
    query = "DELETE FROM fornecedores WHERE id = ?"
    try:
        with con:
            con.execute(query, (fornecedor_id,))
    except sqlite3.Error as e:
        print("Erro ao deletar fornecedor:", e)

# Tabela de Movimentações ----------------------------

def criarMovimentacoes(dados):
    """
    Insere uma nova movimentacao no banco.
    dados: lista [movel_id, tipo, quantidade, data, observação]
    """
    query = """
    INSERT INTO movimentacoes (movel_id, tipo, quantidade, data, observacao)
    VALUES (?, ?, ?, ?, ?)
    """
    try:
        with con:
            con.execute(query, dados)
    except sqlite3.Error as e:
        print("Erro ao inserir movimentação:", e)

def verMovimentacoes():
    """
    Retorna uma lista com todos as movimentaçoes.
    """
    try:
        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM movimentacoes")
            return cur.fetchall()
    except sqlite3.Error as e:
        print("Erro ao buscar movimentaçoes:", e)
        return []

def atualizarMovimentacao(dados):
    """
    Atualiza os dados de uma movimentacao existente.
    dados: lista [movel_id, tipo, quantidade, data, observação, id]
    """
    query = """
    UPDATE movimentacoes
    SET movel_id = ?, tipo = ?, quantidade = ?, data = ?, observacao = ?
    WHERE id = ?
    """
    try:
        with con:
            con.execute(query, dados)
    except sqlite3.Error as e:
        print("Erro ao atualizar movimentacao:", e)

def deletarMovimentacao(movimentacao_id):
    """
    Deleta uma movimentacao pelo id.
    movimentacao_id: INTEGER
    """
    query = "DELETE FROM movimentacoes WHERE id = ?"
    try:
        with con:
            con.execute(query, (movimentacao_id,))
    except sqlite3.Error as e:
        print("Erro ao deletar movimentacao", e)


criarMovel(['Cadeira', 'Cadeira estofada preta', 88.0, 89, 1, 1])
atualizarMovel(['Cadeira reformada', 'Nova cor azul', 90.0, 80, 1, 1, 1])
deletarMovel(20)
print(verMoveis())
criarCategoria(['Quintal'])
atualizarCategoria(['Banheiro',1])
deletarCategoria(1)
print(verCategorias())
criarFornecedor(['Joaquin','81998809135','emailruim@gmail.com','Rua casa do krl-PE'])
atualizarFornecedor(['Pedro','81998809135','emailruim@gmail.com','Rua casa do krl-PE',1])
print(verFornecedores())
deletarFornecedor(1)
