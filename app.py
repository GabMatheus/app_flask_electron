from flask import Flask, render_template, request, Response, jsonify
import psycopg2 
import csv
import io

app = Flask(__name__)

# Função para conectar ao banco de dados
def get_db_connection():
    conn = psycopg2.connect(
        host="ip",
        database="nomeBanco",
        user="user",
        password="senha"
    )
    return conn

# Rota para a página inicial com a seleção de empresa
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cod_empresa = request.form['cod_empresa']
        if cod_empresa:
            return consulta_produtos(cod_empresa)
        else:
            return render_template('index.html', empresas=empresas, error="Selecione uma empresa.")

    # Obtém as empresas disponíveis
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT cod_empresa, nom_empresa,... FROM NOME-DA-SUA-TABELA WHERE CONDIÇÃO  ORDER BY cod_empresa')  
    empresas = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template('index.html', empresas=empresas)

# Função para consultar os produtos
def consulta_produtos(cod_empresa):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = '''
    Código da consulta de produtos sql;
    '''
    
    cursor.execute(query, (cod_empresa, cod_empresa))
    colunas = [desc[0] for desc in cursor.description]
    produtos = [dict(zip(colunas, produto)) for produto in cursor.fetchall()]
    
    cursor.close()
    conn.close()
    
    return render_template('produtos.html', produtos=produtos, cod_empresa=cod_empresa)

# Rota para pesquisar produtos
@app.route('/pesquisar', methods=['GET'])
def pesquisar_produtos():
    nome_produto = request.args.get('nome_produto')
    cod_empresa = request.args.get('cod_empresa')
    conn = get_db_connection()
    cursor = conn.cursor()

    query = '''
        CONSULTA AQUI;
    '''

    cursor.execute(query, (f'%{nome_produto}%',))  
    colunas = [desc[0] for desc in cursor.description]
    produtos = [dict(zip(colunas, produto)) for produto in cursor.fetchall()]
    
    cursor.close()
    conn.close()

    return render_template('produtos.html', produtos=produtos, cod_empresa=cod_empresa)

@app.route('/exportar_csv', methods=['GET'])
def exportar_csv():
    # Obtendo os parâmetros de consulta
    nome_produto = request.args.get('nome_produto')
    cod_empresa = request.args.get('cod_empresa')

    # Conectar ao banco de dados
    conn = get_db_connection()
    cursor = conn.cursor()

    # Montando a consulta SQL com base nos parâmetros
    query = '''
       CONSULTA SQL AQUI TAMBEM;
    '''

    cursor.execute(query, params)
    colunas = [desc[0] for desc in cursor.description]
    produtos = [dict(zip(colunas, produto)) for produto in cursor.fetchall()]

    cursor.close()
    conn.close()

    # Criar um buffer em memória
    si = io.StringIO()
    cw = csv.writer(si)

    # Escrever os cabeçalhos
    cw.writerow(['Codigo', 'Descricao', 'Preco', 'Saldo', 'Codigo da empresa'])

    # Escrever os dados dos produtos
    for produto in produtos:
        cw.writerow([produto['cod_item'], produto['des_item'], produto['valor_preco'], produto['saldo'], produto['cod_empresa']])

    # Criar a resposta com o conteúdo CSV
    response = Response(si.getvalue(), mimetype='text/csv')
    response.headers['Content-Disposition'] = 'attachment; filename=produtos.csv'
    return response

@app.route('/cartoes', methods=['GET', 'POST'])
def cartoes():
    # Obter parâmetros de paginação
    pagina = int(request.args.get('pagina', 1))
    tamanho_pagina = int(request.args.get('tamanho', 8500))
    
    # Calcular limites para a consulta SQL
    offset = (pagina - 1) * tamanho_pagina
    
    # Conectar ao banco de dados
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Consultar os cartões com limites
    cursor.execute(""" 
        CONSULTA SQL
    """, (tamanho_pagina, offset))
    
    cartoes = cursor.fetchall()
    cursor.close()
    conn.close()
    
    # Retornar os dados em formato JSON para a requisição AJAX
    return render_template('cartoes.html', cartoes=cartoes)

@app.route('/exportar_cartoes_csv', methods=['GET'])
def exportar_cartoes_csv():
    # Parâmetros de paginação
    pagina = int(request.args.get('pagina', 1))
    tamanho_pagina = int(request.args.get('tamanho', 8500))
    offset = (pagina - 1) * tamanho_pagina

    # Conectar ao banco de dados
    conn = get_db_connection()
    cursor = conn.cursor()

    # Consulta SQL para cartões
    cursor.execute(""" 
       CONSULTA SQL
    """, (tamanho_pagina, offset))

    cartoes = cursor.fetchall()
    cursor.close()
    conn.close()

    # Criar um buffer para o CSV
    si = io.StringIO()
    cw = csv.writer(si)

    # Escrever cabeçalhos do CSV
    cw.writerow(['Codigo Empresa', 'Nome Fantasia', 'Cod Sacado', 'Nome Pessoa', 'Seq Titulo', 
                 'Tipo Cobranca', 'Fatura', 'Status', 'Data Vencimento', 'Valor Original', 
                 'Desconto', 'Valor Liquidado', 'Dias Aberto'])

    # Escrever dados dos cartões
    for cartao in cartoes:
        cw.writerow(cartao)

    # Gerar resposta com CSV
    response = Response(si.getvalue(), mimetype='text/csv')
    response.headers['Content-Disposition'] = 'attachment; filename=cartoes.csv'
    return response

if __name__ == '__main__':
    app.run(debug=True)

