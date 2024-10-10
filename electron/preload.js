// preload.js
const { contextBridge, ipcRenderer } = require('electron');

// Expor funções seguras para o front-end
contextBridge.exposeInMainWorld('electronAPI', {
  send: (channel, data) => ipcRenderer.send(channel, data),
  on: (channel, func) => ipcRenderer.on(channel, (event, ...args) => func(...args))
});
