from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict
import json
import os

ARQUIVO = "estoque.json"

app = FastAPI(
    title="API de Controle de Estoque",
    version="1.0.0",
    description="Desenvolvendo um Sistema de Controle de Estoque com Python: Soluções para Gerenciamento em uma Loja de Eletrônico"
)



@app.get("/health")
def health():
    return {"status": "ok"}

# =========================
# MODELOS (Swagger)
# =========================
class ProdutoCreate(BaseModel):
    sku: str = Field(..., min_length=1, description="Código único do produto (SKU)")
    nome: str = Field(..., min_length=1, description="Nome do produto")
    preco: float = Field(..., ge=0, description="Preço do produto (>= 0)")
    quantidade: int = Field(..., ge=0, description="Quantidade em estoque (>= 0)")


class ProdutoUpdate(BaseModel):
    nome: str = Field(..., min_length=1, description="Nome do produto")
    preco: float = Field(..., ge=0, description="Preço do produto (>= 0)")
    quantidade: int = Field(..., ge=0, description="Quantidade em estoque (>= 0)")


class ProdutoResponse(BaseModel):
    sku: str
    nome: str
    preco: float
    quantidade: int


# =========================
# PERSISTÊNCIA (JSON)
# =========================
def carregar_estoque() -> Dict[str, dict]:
    if not os.path.exists(ARQUIVO):
        return {}
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}


def salvar_estoque(estoque: Dict[str, dict]) -> None:
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(estoque, f, indent=4, ensure_ascii=False)


# =========================
# ENDPOINTS
# =========================
@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/produtos", response_model=list[ProdutoResponse])
def listar_produtos():
    estoque = carregar_estoque()
    return [
        ProdutoResponse(sku=sku, **dados)
        for sku, dados in estoque.items()
    ]


@app.get("/produtos/{sku}", response_model=ProdutoResponse)
def obter_produto(sku: str):
    estoque = carregar_estoque()
    if sku not in estoque:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")
    return ProdutoResponse(sku=sku, **estoque[sku])


@app.post("/produtos", response_model=ProdutoResponse, status_code=201)
def criar_produto(produto: ProdutoCreate):
    estoque = carregar_estoque()

    if produto.sku in estoque:
        raise HTTPException(status_code=409, detail="SKU já existe.")

    estoque[produto.sku] = {
        "nome": produto.nome,
        "preco": produto.preco,
        "quantidade": produto.quantidade
    }
    salvar_estoque(estoque)

    return ProdutoResponse(
        sku=produto.sku,
        nome=produto.nome,
        preco=produto.preco,
        quantidade=produto.quantidade
    )


@app.put("/produtos/{sku}", response_model=ProdutoResponse)
def atualizar_produto(sku: str, dados: ProdutoUpdate):
    estoque = carregar_estoque()

    if sku not in estoque:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")

    estoque[sku] = {
        "nome": dados.nome,
        "preco": dados.preco,
        "quantidade": dados.quantidade
    }
    salvar_estoque(estoque)

    return ProdutoResponse(sku=sku, **estoque[sku])


@app.delete("/produtos/{sku}", status_code=204)
def excluir_produto(sku: str):
    estoque = carregar_estoque()

    if sku not in estoque:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")

    del estoque[sku]
    salvar_estoque(estoque)
    return
