Consultar Produtos/Cartões
Versão: 1.4
Autor: Gabriel Matheus - gab_matheus@hotmail.com

Este projeto é uma aplicação de consulta de informações sobre produtos e cartões em aberto para a empresa onde trabalho. Foi desenvolvida utilizando Electron no frontend e Flask no backend, permitindo a consulta de informações armazenadas em um banco de dados PostgreSQL. A interface gráfica é simples e feita com HTML, CSS, e JavaScript.

📋 Sumário
Descrição do Projeto
Fluxo do Processo
Por que Isso Funciona?
Tecnologias Utilizadas
Estrutura do Projeto
Instalação
Uso
Empacotamento e Distribuição
Observações Importantes
Descrição do Projeto
O projeto é uma aplicação desktop que se conecta a um banco de dados para consultar informações de produtos e cartões em aberto. A interface gráfica do usuário foi desenvolvida com Electron, enquanto o backend utiliza Flask para gerenciar a lógica de negócios e executar consultas SQL. O Flask permite a conexão ao banco de dados e responde às solicitações feitas pela interface do Electron.

Fluxo do Processo
O Flask serve uma API no backend, geralmente em um endereço como http://localhost:5000.
O Electron faz uma requisição HTTP para essa API sempre que precisa de dados.
O Flask processa a requisição, consulta o banco de dados, e envia de volta os dados solicitados.
O Electron recebe a resposta da API e usa os dados para atualizar a interface gráfica ou realizar outras tarefas.
Por que Isso Funciona?
O Flask age como uma API REST, onde o Electron atua como cliente, consumindo os dados servidos pela API. O Electron, sendo baseado em tecnologias web (HTML, CSS, JavaScript), está apto a fazer requisições HTTP como qualquer navegador, permitindo que a aplicação desktop consuma dados do backend.

Tecnologias Utilizadas
Backend:
Python: Linguagem principal para a lógica do servidor.
Flask: Framework web para gerenciar as rotas, a comunicação com o banco de dados e fornecer a API que o Electron consome no frontend.
PostgreSQL: Banco de dados utilizado para armazenar e consultar as informações de produtos e cartões.
Frontend:
Electron: Framework para desenvolvimento de aplicativos desktop utilizando tecnologias web (HTML, CSS, JavaScript).
HTML/CSS/JavaScript: Usados para criar a interface gráfica do usuário.
Empacotamento:
Electron Builder: Ferramenta usada para empacotar a aplicação Electron em instaladores executáveis para diferentes plataformas.
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
├── app.py                   # Backend Flask
├── /electron/                # Código do Electron
│   ├── main.js               # Arquivo principal do Electron
│   └── package.json          # Configurações e scripts do Electron
├── requeriments.txt          # Dependências do Python
└── /dist/                    # Arquivos empacotados (gerados após o build)
Principais Arquivos:

app.py: Lida com as rotas do Flask e a lógica do backend (consultas SQL).
main.js: Código principal do Electron que inicia a aplicação e interage com o backend.
package.json: Contém as configurações do Electron e scripts de build/start.
Instalação
Requisitos:
Node.js (inclui o NPM)
Python
Flask e outras dependências listadas no requeriments.txt
Passos para Instalação:
Clone o repositório:

git clone https://github.com/seu-usuario/consulta-produtos.git
cd consulta-produtos
Instale as dependências do Python:

pip install -r requeriments.txt
Navegue até a pasta do Electron e instale as dependências do NPM:

cd electron
npm install
Uso
Executando a Aplicação para Desenvolvimento:
Inicie o servidor Flask:

python app.py
Em outra janela do terminal, execute o Electron:

cd electron
npm start
A interface do aplicativo será aberta automaticamente e você poderá começar a consultar os produtos.

Empacotamento e Distribuição
Para gerar um instalador da aplicação para distribuição, rode o seguinte comando na pasta electron:

npm run build
O instalador será gerado na pasta dist. Você pode distribuí-lo para os usuários finais.

Observações Importantes
Consultas SQL e Conexão com o Banco de Dados: As consultas e a conexão com o banco foram removidas, então é necessário ajustar o código conforme a realidade de quem for utilizá-lo.

Rodando localmente: Apenas rodar o app.py permite que a aplicação funcione localmente via interface web, mas o instalador é necessário para distribuir a aplicação a outros usuários.

Acesso ao Banco de Dados: O código funciona apenas localmente, na mesma rede onde o banco de dados está rodando. Conexões externas não foram configuradas.

Atualização de Senha: Se a senha do banco de dados for alterada, será necessário modificar o arquivo app.py e recompilar a aplicação.

Distribuição: Para outros usuários, basta compartilhar o instalador gerado na pasta dist. Não é necessário copiar outros arquivos.

Se tiver dúvidas, sugestões ou problemas, entre em contato pelo gab_matheus@hotmail.com.
