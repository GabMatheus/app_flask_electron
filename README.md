Consultar Produtos/cartões
Versão: 1.4
Autor: Gabriel Matheus - gab_matheus@hotmail.com

Este projeto é uma aplicação de consulta de informações produtos e cartões em aberto para a empresa que trabalho, desenvolvida utilizando Electron para o frontend e Flask para o backend. Ele permite a consulta de informações em um banco de dados postgreSQL, com uma interface gráfica simples feita em HTML,CSS e Javascript.

📋 Sumário
Descrição do Projeto
Fluxo do processo
Porque isso funciona?
Tecnologias Utilizadas
Estrutura do Projeto
Instalação
Uso
Empacotamento e Distribuição
Observações importantes

Descrição do Projeto
O projeto é uma aplicação desktop que conecta-se a um banco de dados para consultar informações de produtos da empresa (que trabalho em questão) e cartões em aberto. A interface gráfica do usuário é desenvolvida com Electron, enquanto o backend utiliza Flask para gerenciar a lógica de negócio e executar consultas SQL. O Flask permite a conexão ao banco de dados e responde às solicitações da interface Electron.

Fluxo do processo:
O Flask serve a API no backend, ouvindo em um endereço como http://localhost:5000.
O Electron, quando precisa de dados, faz uma requisição HTTP para essa API.
O Flask processa a requisição, consulta o banco de dados, e envia de volta os dados.
O Electron recebe a resposta da API e usa esses dados para atualizar a interface ou realizar alguma outra tarefa.

Por que isso funciona?
O Flask age como uma API REST, onde o Electron atua como o cliente, consumindo os dados servidos por essa API.
O Electron é baseado em tecnologias web (HTML, CSS, JavaScript), e essas tecnologias são projetadas para trabalhar com APIs através de requisições HTTP. Então, mesmo sendo uma aplicação desktop, o Electron pode consumir APIs da mesma forma que um navegador web.

Tecnologias Utilizadas
Backend:
Python: Linguagem de programação principal para a lógica do servidor.
Flask: Framework web para gerenciar as rotas e a comunicação com o banco de dados e enviar como API para o Electron consumir no frontend.
PostgreSQL: Usado para consultar informações de produtos e cartões, no meu caso o banco já existia, apenas requisitei as informações.
Frontend:
Electron: Framework para desenvolvimento de aplicativos desktop com tecnologias web (HTML, CSS e JavaScript).
HTML/CSS/JavaScript: Utilizados para construir a interface gráfica do usuário.
Empacotamento:
Electron Builder: Ferramenta usada para empacotar o aplicativo Electron em instaladores executáveis para diferentes plataformas.
Estrutura do Projeto
A estrutura de diretórios do projeto é a seguinte:

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
└── package.json     
└── requeriments.txt
└── /dist/             # Arquivos empacotados (gerado após build, deve criar também outras pastas e arquivos como por exemplo node_modules, mas essas sao as principais)
Arquivos principais:
app.py: Lida com as rotas do Flask e a lógica do backend (consultas SQL).
main.js: Código principal do Electron que inicia a aplicação e interage com o backend Flask.
package.json: Contém as configurações do Electron e os scripts de build/start.
Instalação
Requisitos:
Node.js (inclui o NPM)
Python
Flask e outras dependências listadas no requeriments.txt
Passos para instalar:
Clone o repositório:

git clone https://github.com/seu-usuario/consulta-produtos.git
cd consulta-produtos
Instale as dependências do Python:

pip install -r requeriments.txt
Navegue até a pasta electron e instale as dependências do NPM:

cd electron
npm install
Uso
Executando a aplicação para desenvolvimento:
Inicie o servidor Flask:

python app.py
Em outra janela do terminal, execute o Electron:

cd electron
npm start
A interface do aplicativo abrirá automaticamente e você poderá começar a consultar produtos.

Empacotamento e Distribuição
Para gerar um instalador da aplicação para distribuição:

Rode o seguinte comando na pasta electron:

npm run build
O instalador será gerado na pasta dist. Distribua este instalador para os usuários finais.

Observações importantes: 
1. Tirei todas as consultas SQL e conexão com o BD da empresa, logo quem for fazer precisa arrumar conforme a sua realidade.

2. Apenas copiando e rodando o app.py já funciona localmente via interface web, contudo tive que criar um instalador para distribuir para algumas pessoas específicas utilizarem dessas informações do aplicativo, daria para adicionar mais funcionalidades, pode ser que implemente no futuro além dessas consultas atuais apenas.

3. O código funcionará apenas localmente, na mesma faixa de ip em que o banco de dados está atuando, não arrumei nada para conexões externas. 
   
4. O que fazer se a senha do banco de dados mudar?
Se a senha do banco de dados for alterada, será necessário atualizar o arquivo app.py com a nova senha e recompilar o aplicativo.

5. Posso distribuir apenas o instalador para outros usuários?
Sim, basta compartilhar o instalador gerado na pasta dist. Não é necessário copiar outros arquivos.

Se tiver dúvidas, sugestões ou problemas, entre em contato pelo gab_matheus@hotmail.com
