# Consultar Produtos/Cartões

**Versão:** 1.4  
**Autor:** Gabriel Matheus - [gab_matheus@hotmail.com](mailto:gab_matheus@hotmail.com)

---

## 📋 Sumário

- Descrição do Projeto
- Fluxo do Processo
- Por que Isso Funciona?
- Tecnologias Utilizadas
- Estrutura do Projeto
- Instalação
- Uso
- Empacotamento e Distribuição
- Observações Importantes

---

## 📖 Descrição do Projeto

Este projeto é uma aplicação desktop que permite a consulta de informações sobre produtos e cartões em aberto para a empresa onde trabalho. Desenvolvida utilizando **Electron** no frontend e **Flask** no backend, a aplicação acessa dados armazenados em um banco de dados **PostgreSQL**. A interface gráfica foi construída com HTML, CSS e JavaScript.

---

## 🔄 Fluxo do Processo

1. **API Backend**: O Flask serve a API no backend ouvindo em um endereço como `http://localhost:5000`.
2. **Requisição**: O Electron faz uma requisição HTTP para essa API ao precisar de dados.
3. **Processamento**: O Flask processa a requisição, consulta o banco de dados e envia de volta os dados solicitados.
4. **Atualização**: O Electron recebe a resposta da API e atualiza a interface gráfica ou realiza outras tarefas.

---

## ❓ Por que Isso Funciona?

O Flask atua como uma API REST, enquanto o Electron funciona como cliente, consumindo os dados servidos. Baseado em tecnologias web (HTML, CSS, JavaScript), o Electron é capaz de fazer requisições HTTP, permitindo que a aplicação desktop consuma dados do backend.

---

## 🛠️ Tecnologias Utilizadas

### Backend

- **Python**: Linguagem principal para a lógica do servidor.
- **Flask**: Framework web para gerenciar rotas e fornecer a API.
- **PostgreSQL**: Banco de dados utilizado para armazenar informações.

### Frontend

- **Electron**: Framework para desenvolvimento de aplicativos desktop.
- **HTML/CSS/JavaScript**: Usados para criar a interface gráfica.

### Empacotamento

- **Electron Builder**: Ferramenta para empacotar a aplicação em instaladores executáveis.

---

## 📂 Estrutura do Projeto

```plaintext
/consulta-produtos/
│
├── /static/
│   ├── styles.css
│   └── script.js
├── /templates/
│   ├── index.html
│   ├── produtos.html
│   └── cartoes.html
├── app.py                   
├── /electron/                
│   ├── main.js               
│   └── package.json          
├── requeriments.txt          
└── /dist/  # Arquivos empacotados (gerado após build, deve criar também outras pastas e arquivos como por exemplo node_modules)
```
---

## Principais Arquivos
1. app.py: Lida com as rotas do Flask e a lógica do backend.

2. main.js: Código principal do Electron que inicia a aplicação.

3. package.json: Contém as configurações do Electron e scripts de build/start.

---

## ⚙️ Instalação
Requisitos
1. Node.js (inclui o NPM)
2. Python
3. Flask e outras dependências listadas no requeriments.txt
4. Passos para Instalação

Clone o repositório:

1. git clone 
2. cd consulta-produtos

Instale as dependências do Python:

-pip install -r requeriments.txt

Navegue até a pasta do Electron e instale as dependências do NPM:

-cd electron
-npm install

---

## 🚀 Uso
Executando a Aplicação para Desenvolvimento
Inicie o servidor Flask:

1. python app.py
Em outra janela do terminal, execute o Electron:

1. cd electron
2. npm start
A interface do aplicativo será aberta automaticamente e você poderá começar a consultar os produtos.

---

## 📦 Empacotamento e Distribuição
Para gerar um instalador da aplicação, execute o seguinte comando na pasta electron:

1. npm run build

O instalador será gerado na pasta dist e poderá ser distribuído para os usuários finais.

---

## ⚠️ Observações Importantes
1. Consultas SQL: As consultas e a conexão com o banco foram removidas. Ajustes no código são necessários.

2. Rodando Localmente: Apenas rodar app.py permite que a aplicação funcione via interface web, mas o instalador é necessário para distribuição.

3. Acesso ao Banco de Dados: O código funciona apenas localmente. Conexões externas não foram configuradas.

4. Atualização de Senha: Se a senha do banco de dados for alterada, modifique app.py e recompilhe a aplicação.

5. Distribuição: Compartilhe apenas o instalador gerado na pasta dist, já é suficiente para funcionamento após finalizar tudo.

Se tiver dúvidas, sugestões ou problemas, entre em contato pelo gab_matheus@hotmail.com

---
