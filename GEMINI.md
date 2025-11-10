# 💰 Gemini Project — Expense Manager (MVP)

## 🧭 Visão Geral
Aplicativo de **gerenciamento de despesas**, desenvolvido por um **time pequeno** com foco em validar o conceito e estruturar um banco de dados sólido desde o início.

O **objetivo do MVP** é implementar e testar o **módulo de registro de gastos**, garantindo:
- Entrada e categorização de despesas;
- Persistência confiável e escalável;
- Base pronta para relatórios e expansão futura.

---

## ⚙️ Arquitetura do MVP

### Stack inicial
- **Backend**: Python + FastAPI  
- **Banco de Dados**: PostgreSQL  
- **Frontend**: React (ou Flutter, se for validado como prioridade futura)  
- **Infraestrutura**: Docker + Docker Compose  
- **Autenticação**: JWT (com refresh token opcional)  

### Estrutura modular
- `/users` → autenticação e gerenciamento básico de usuários  
- `/expenses` → registro, atualização e listagem de despesas  
- `/categories` → categorias personalizadas (alimentação, transporte, etc.)

O sistema será **monolítico modular**, preparado para evoluir em microsserviços no futuro (por exemplo, `auth-service`, `expense-service`, `report-service`).

---

## 🧩 Estrutura de diretórios
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