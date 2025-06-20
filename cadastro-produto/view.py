import sqlite3

try:
    con = sqlite3.connect('cadastro_moveis.db')
    print('Conexao com o banco de dados realizado com sucesso')
except sqlite3.Error as e:
    print("Erro ao conectar com o bd",e)

# Tabela de Moveis ----------------------------

# Criar Moveis
def criarMovel(lista):
    with con:
        cur = con.cursor()
        query = "INSERT INTO moveis (nome, descricao, preco, quantidade, categoria_id, fornecedor_id) VALUES(?,?,?,?,?,?)"
        cur.execute(query,lista)

##criarMovel(['Cadeira','Cadeira estofada preta',88.0,89,87,66])

# Ver Moveis
def verMoveis():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM moveis')
        linha = cur.fetchall()
        for i in linha:
            lista.append(i)
    return lista

print(verMoveis())

# Atualizar moveis
def atualizarMoveis(i):
    with con:
        cur = con.cursor()
        query = 'UPDATE moveis SET nome=?, descricao=?, preco=?, quantidade=?, categoria_id=?, fornecedor_id=? WHERE id=?'
        cur.execute(query,i)

l = ['Cadeira formosa', 'Cadeira estofada branca', 88.0, 89, 87, 66, 5]
atualizarMoveis(l)

# Deletar moveis
def deletarMoveis(i):
    with con:
        cur = con.cursor()
        query = 'DELETE FROM moveis WHERE id=?'
        cur.execute(query,i)
