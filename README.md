
# 📦 API de Controle de Estoque – Unifecaf

API REST desenvolvida em **Python** utilizando **Unifecaf**, responsável pelo gerenciamento de estoque de produtos identificados por **SKU único**.
O projeto fornece um **CRUD completo**, documentação automática via **Swagger**, e persistência de dados utilizando **Docker Volume**.

Este projeto foi desenvolvido com foco **acadêmico**, aplicando boas práticas utilizadas em ambientes profissionais.

---

## 🚀 Funcionalidades

- Criar produto
- Listar produtos
- Buscar produto por SKU
- Atualizar produto
- Excluir produto
- Health Check
- Persistência de dados
- Documentação automática (Swagger)

---

## 🧱 Tecnologias Utilizadas

- **Python 3.12**
- **FastAPI**
- **Uvicorn**
- **Docker**
- **Docker Compose**

---

## 📁 Estrutura do Projeto

```
unifecaf-estoque-api/
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
└── README.md
```

---

## 📄 Pré-requisitos

### Execução com Docker (Recomendado)
- Docker 24+
- Docker Compose v2+

Verificação:
```bash
docker --version
docker compose version
```

### Execução Local (Sem Docker)
- Linux (Ubuntu recomendado)
- Python 3.10+
- pip3
- python3-venv

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
```

---

## 🐳 Execução com Docker

```bash
docker compose up -d --build
```

### Acessos
- Swagger: http://localhost:8000/docs
- OpenAPI: http://localhost:8000/openapi.json
- Health: http://localhost:8000/health

---

## 💾 Persistência de Dados

O Docker cria automaticamente o volume:
```bash
docker volume ls | grep estoque_data
```

Arquivo persistido em:
```
/data/estoque.json
```

---

## 🧪 Execução Local

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## ⚙️ Variáveis de Ambiente

| Variável | Descrição | Padrão |
|--------|----------|--------|
| ARQUIVO | Caminho do arquivo de dados | estoque.json |

---

## 📌 Exemplo de Payload

```json
{
  "sku": "SKU001",
  "nome": "Notebook Dell",
  "preco": 3500.00,
  "quantidade": 10
}
```

---

## 🔗 Endpoints

| Método | Endpoint | Descrição |
|------|---------|-----------|
| GET | /health | Health check |
| GET | /produtos | Listar produtos |
| GET | /produtos/{sku} | Buscar produto |
| POST | /produtos | Criar produto |
| PUT | /produtos/{sku} | Atualizar produto |
| DELETE | /produtos/{sku} | Excluir produto |

---

## 👨‍💻 Autor

Projeto desenvolvido para fins acadêmicos e educacionais por

Rodrigo de Moura
Aluno do curso programação em nuvem
