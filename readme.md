# Projeto Flix API com autenticação JWT
    API RESTful para gerenciamento de filmes, atores, gêneros e avaliações, construída com Django e Django REST Framework.

## Índice
    - Sobre o Projeto
    - Estrutura do Projeto
    - Principais Tecnologias
    - Pré-requisitos
    - Instalação
    - Configuração
    - Executando o Projeto
    - Endpoints da API
    - Autenticação
    - Permissões
    
## Sobre o Projeto
    A Flix API é uma API REST completa que permite gerenciar um catálogo de filmes com recursos como:
    - listagem e cadastro de filmes, atores, gêneros e avaliações.
    - Sistema de avaliações com estrelas (1–5)
    - Autenticação JWT via SimpleJWT
    - Controle de permissões por nível de acesso (admin, usuários comuns e grupo de usuários)
    - Filtros, buscas e paginação nos endpoints

## Estrutura do Projeto
    flix-api/
    ├── app/                    <- Configurações principais do projeto
    │   ├── settings.py
    │   ├── urls.py
    │   ├── permissions.py      <- Permissões globais customizadas
    │   ├── asgi.py
    │   └── wsgi.py
    ├── api/
    │   └── urls.py             <- Roteador raiz da API (/api/v1/)
    ├── actors/                 <- App de atores
    │   ├── models.py
    │   ├── serializer.py
    │   ├── views.py
    │   ├── urls.py
    │   └── admin.py
    ├── genres/                 <- App de gêneros
    │   ├── models.py
    │   ├── serializers.py
    │   ├── views.py
    │   ├── urls.py
    │   ├── permissions.py      <- Permissões específicas de gêneros
    │   └── admin.py
    ├── movies/                 <- App de filmes
    │   ├── models.py
    │   ├── serializers.py
    │   ├── views.py
    │   ├── urls.py
    │   └── admin.py
    ├── reviews/                <- App de avaliações
    │   ├── models.py
    │   ├── serializer.py
    │   ├── views.py
    │   ├── urls.py
    │   └── admin.py
    ├── authentication/         <- App de autenticação JWT
    │   ├── views.py
    │   └── urls.py
    ├── manage.py
    └── requirements.txt

## Principais Tecnologias
    - Python | 3.14+ |
    - Django | 6.0.2 |
    - Django REST Framework | 3.16.1 |
    - djangorestframework-simplejwt | 5.5.1 |
    - SQLite | (padrão de dev) |
    
## Pré-requisitos
    - Python (Versão utilizada: 3.14)
    - DRF (Django Rest Framework)

## Instalação

    1. Clone o repositório
        git clone https://github.com/MagnumRR/Flix_API.git
        cd flix-api

    2. Crie e um ambiente virtual
        python -m venv .venv

    2.1 Ativar:
    # Linux / macOS
        source .venv/bin/activate

    # Windows
        .venv\Scripts\activate

    3. Instale as dependências
        pip install -r requirements.txt        
    
## Configuração

    - Variáveis de ambiente (importante para quase todos os projetos)
    Crie um arquivo ".env" na raiz do projeto:
        SECRET_KEY=informe sua chave
        DEBUG=True
        ALLOWED_HOSTS=localhost,127.0.0.1
    
    > Obs: Em produção, defina "DEBUG=False" e configure um banco de dados adequado mais completo.

## Executando o Projeto

    1. Realizar as migrations
        python manage.py migrate
    
    2. Crie um superusuário (dica!)
        python manage.py createsuperuser
    
    3. Inicie o servidor
        python manage.py runserver
    
    A API estará disponível em: "http://127.0.0.1:8000/"

## Endpoints da API

    Recurso | Endpoint base
    
    Admin        | "/admin/"
    Autenticação | "/api/v1/authentication/"
    Filmes       | "/api/v1/movies/"
    Atores       | "/api/v1/actors/"
    Gêneros      | "/api/v1/genres/"
    Avaliações   | "/api/v1/reviews/"
    
## Autenticação
    A Flix API usa JWT (JSON Web Tokens) através da biblioteca "djangorestframework-simplejwt".

## Obtendo token

    - http: 
        POST /api/v1/authentication/token/
        Content-Type: application/json

        {
        "username": "nome_usuario",
        "password": "senha"
        }
    
    - Resposta:
        json
        {
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
        }

## Renovando token

    - http
        POST /api/v1/authentication/token/refresh/
        Content-Type: application/json

        {
        "refresh": "refresh_token"
        }
    
## Utilizando token nas requisições

    - http
        GET /api/v1/movies/
        Authorization: (Bearer_token): "access_token"
    
## Permissões
    Listar / Detalhar recursos | Não (leitura pública)
    Criar / Atualizar / Deletar
    Gerenciar gêneros | Admin
    Painel admin ("/admin/") | Superusuário
---    
## Autor
    Magnum Ribeiro Rodrigues dos Santos