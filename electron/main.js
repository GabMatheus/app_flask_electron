const { app, BrowserWindow } = require('electron');
const { exec } = require('child_process');
const path = require('path');

let mainWindow;

// Função para iniciar o servidor Flask
function startFlaskServer() {
  // Caminho correto para o app.py
  const flaskPath = path.join(__dirname, '../app.py');
  
  const flaskProcess = exec(`python ${flaskPath}`, (error, stdout, stderr) => {
    if (error) {
      console.error(`Erro ao iniciar o servidor Flask: ${error.message}`);
      return;
    }
    if (stderr) {
      console.error(`Stderr: ${stderr}`);
      return;
    }
    console.log(`Stdout: ${stdout}`);
  });

  flaskProcess.on('exit', (code) => {
    console.log(`Servidor Flask encerrado com código: ${code}`);
  });

  return flaskProcess;
}

// Função para criar a janela do Electron
function createWindow() {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'), 
      contextIsolation: true, 
      enableRemoteModule: false, 
    }
  });

  // Acessa a aplicação Flask local
  mainWindow.loadURL('http://localhost:5000');
  
  mainWindow.on('closed', function () {
    mainWindow = null;
  });
}

// Quando o Electron inicializar, start Flask server e cria a janela
app.on('ready', () => {
  startFlaskServer();
  createWindow();
});

// Fecha o Electron quando todas as janelas são fechadas
app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', function () {
  if (mainWindow === null) {
    createWindow();
  }
});
