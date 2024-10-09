let products = [];
let paginaAtual = 1;
const tamanhoPagina = 2000; // Número de produtos a serem carregados a cada vez

// Função para buscar produtos da API
function fetchProducts() {
    fetch(`/api/products?pagina=${paginaAtual}&tamanho=${tamanhoPagina}`)
        .then(response => response.json())
        .then(data => {
            products = products.concat(data); 
            renderProducts();
        });
}

// Função para renderizar a lista de produtos na tabela
function renderProducts() {
    const productTable = document.getElementById('product-table').getElementsByTagName('tbody')[0];
    productTable.innerHTML = ''; 
    products.forEach((product, index) => {
        const row = productTable.insertRow();
        row.innerHTML = `
            <td>${product.name}</td>
            <td>${product.code}</td>
            <td>R$ ${product.price.toFixed(2)}</td>
            <td>${product.quantity}</td>
            <td><button onclick="viewDetails(${index})">Ver Detalhes</button></td>
        `;
    });
}

// Função para exibir detalhes do produto
function viewDetails(index) {
    const product = products[index];
    document.getElementById('detail-name').textContent = product.name;
    document.getElementById('detail-code').textContent = product.code;
    document.getElementById('detail-price').textContent = product.price.toFixed(2);
    document.getElementById('detail-quantity').textContent = product.quantity;
    document.getElementById('product-details').style.display = 'block';
}

// Função para filtrar produtos na tabela
function filterProducts() {
    const searchTerm = document.getElementById('search-bar').value.toLowerCase();
    const filteredProducts = products.filter(product =>
        product.name.toLowerCase().includes(searchTerm) ||
        product.code.toString().includes(searchTerm)
    );

    renderFilteredProducts(filteredProducts);
}

// Renderiza a lista filtrada
function renderFilteredProducts(filteredProducts) {
    const productTable = document.getElementById('product-table').getElementsByTagName('tbody')[0];
    productTable.innerHTML = '';
    filteredProducts.forEach((product, index) => {
        const row = productTable.insertRow();
        row.innerHTML = `
            <td>${product.name}</td>
            <td>${product.code}</td>
            <td>R$ ${product.price.toFixed(2)}</td>
            <td>${product.quantity}</td>
            <td><button onclick="viewDetails(${index})">Ver Detalhes</button></td>
        `;
    });
}

// Função para verificar o scroll e carregar mais produtos
function verificarScroll() {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 200) {
        paginaAtual++;
        fetchProducts();
    }
}

window.addEventListener('scroll', verificarScroll);

// Inicializa o carregamento dos produtos
fetchProducts();
