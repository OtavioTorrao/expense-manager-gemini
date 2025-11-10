# Gemini Project — Expense Manager (MVP)

## Visão Geral
Aplicativo de **gerenciamento de despesas**, desenvolvido por um **time pequeno** com foco em validar o conceito e estruturar um banco de dados sólido desde o início.

O **objetivo do MVP** é implementar e testar o **módulo de registro de gastos**, garantindo:
- Entrada e categorização de despesas;
- Persistência confiável e escalável;
- Base pronta para relatórios e expansão futura.

---

## Arquitetura do MVP

### Stack inicial
- **Backend**: Python + FastAPI  
- **Banco de Dados**: SQLite
- **Frontend**: React + TailwindCSS
- **Infraestrutura**: Docker + Docker Compose  

### Estrutura modular
- `/users` → autenticação e gerenciamento básico de usuários  
- `/expenses` → registro, atualização e listagem de despesas  
- `/categories` → categorias personalizadas (alimentação, transporte, etc.)

---

## Estrutura de diretórios
```bash
backend/
├── app/
│   ├── core/             # Configurações, middlewares e utilitários
│   ├── users/            # Lógica de autenticação e cadastro
│   ├── expenses/         # CRUD de despesas e categorias
│   ├── database/         # Conexão, models e migrações
│   ├── schemas/          # Pydantic models (validação)
│   ├── main.py           # Ponto de entrada da aplicação
│   └── config.py         # Variáveis de ambiente e setup
└── tests/                # Testes automatizados (pytest)
frontend/
└── src/
    ├── components/
    ├── pages/
    └── services/
docker-compose.yml
.env.example
GEMINI.MD
README.md
```

## Como executar

### Backend
1. Navegue até a pasta `backend`
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente virtual: `source venv/bin/activate` (ou `venv\Scripts\activate` no Windows)
4. Instale as dependências: `pip install -r requirements.txt`
5. Rode a aplicação: `uvicorn app.main:app --reload`

### Frontend
Ainda a ser implementado.

### Com Docker
1. Certifique-se de ter o Docker e o Docker Compose instalados.
2. Na raiz do projeto, execute: `docker-compose up --build`
