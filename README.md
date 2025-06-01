# API Embrapa

Este é um projeto de desenvolvido de API com Flask, que inclui web scraping, autenticação básica e rotas de acesso aos dados da Embrapa.

## 📖 Descrição
A **API Embrapa** é uma aplicação Python que permite autenticação de usuários, consultas de dados e funcionalidades específicas por meio de endpoints RESTful.

## 🚀 Funcionalidades

- **Autenticação Básica**: Protege rotas sensíveis usando autenticação HTTP básica.
- **Rotas**: Cadastro, login e consulta aos dados.
- **Web Scraping**: Extrai dados do site 'http://vitibrasil.cnpuv.embrapa.br/index.php'.
- **Documentação**: Documentação automática com Swagger.

## 📁 Estrutura do Projeto

```bash
API_Embrapa/
├── config/
│   └── configuracoes.py          # Configurações do projeto
├── db/
│   └── database.py               # Configurações do banco de dados
├── instance/
│   └── app.db                    # Banco de dados SQLite local
├── models/
│   ├── __init__.py
│   └── usuarios.py               # Modelo de usuários
├── routes/
│   ├── __init__.py
│   ├── autenticacao.py           # Rotas de autenticação
│   └── consulta.py               # Rotas de consulta
├── services/
│   └── webscraping.py            # Serviços de web scraping
├── .gitignore                    # Arquivos e pastas a serem ignorados pelo Git
├── app.py                        # Arquivo principal para rodar a API
├── requirements.txt              # Dependências do projeto
└── README.md                     # Este arquivo
```

## 🛠️ Como Executar o Projeto

### 1. Clone o Repositório

```bash
git clone https://github.com/GustavoMiguel28/API_Embrapa.git
cd API_Embrapa
```

### 2. Crie um Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o Aplicativo

```bash
python run.py
```

## 📖 Documentação da API

A documentação da API é gerada automaticamente com Swagger e está disponível em `http://localhost:5000/apidocs/`.
