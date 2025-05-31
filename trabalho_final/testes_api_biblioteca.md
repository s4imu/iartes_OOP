
# 📄 Enunciado: Testes para Rotas da API de Biblioteca

## 🎯 Objetivo

Desenvolver testes automatizados para garantir o comportamento correto das seguintes rotas da API REST:

- `GET /livros` – Obter todos os livros cadastrados
- `GET /livros/<id>` – Obter um livro específico pelo ID
- `DELETE /livros/<id>` – Remover um livro do acervo

Um livro na biblioteca tem os seguintes atributos:
```json
livro = {
    "titulo": "...",
    "autor": "...",
    "ano": int:,
    "isbn": "..."
}
```
---

## 🧪 Requisitos de Teste

### 🟦 1. `GET /livros` – Listar todos os livros

- [ ] Cenário A: Deve retornar lista vazia se nenhum livro estiver cadastrado.
- [ ] Cenário B: Deve retornar todos os livros após inserções.
- [ ] Validações: status 200, resposta em lista JSON.

### 🟩 2. `GET /livros/<id>` – Buscar livro por ID

- [ ] Cenário A: Deve retornar o livro correto quando o ID existir.
- [ ] Cenário B: Deve retornar erro 404 quando o ID não existir.
- [ ] Validações: status 200 (sucesso) ou 404 (erro), estrutura JSON correta.

### 🟥 3. `DELETE /livros/<id>` – Remover livro

- [ ] Cenário A: Deve remover o livro com sucesso (status 204).
- [ ] Cenário B: O livro removido não deve estar mais disponível.
- [ ] Cenário C: Remoção de ID inexistente deve retornar 404.

---

## 🧪 Stubs de Testes

```python
import unittest
import json
from app import app

class TestAPILivros(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.headers = {"Content-Type": "application/json"}

    def test_listar_livros_vazio(self):
        # TODO: Verificar resposta vazia quando não há livros
        pass

    def test_listar_livros_apos_criacao(self):
        # TODO: Criar livros e verificar se aparecem na listagem
        pass

    def test_obter_livro_existente(self):
        # TODO: Criar um livro e buscá-lo pelo ID
        pass

    def test_obter_livro_inexistente(self):
        # TODO: Buscar um ID que não existe
        pass

    def test_remover_livro_existente(self):
        # TODO: Criar um livro e depois removê-lo
        pass

    def test_remover_livro_inexistente(self):
        # TODO: Tentar remover um ID inexistente
        pass

    def test_livro_nao_encontrado_apos_remocao(self):
        # TODO: Verificar que livro removido não pode mais ser consultado
        pass
```

---

## ✅ Instruções

1. Implemente os testes usando `self.client` com chamadas `GET`, `POST` e `DELETE`.
2. Use `assertEqual`, `assertIn`, `assertIsInstance` para validar as respostas.
3. Execute com:

```bash
python -m unittest discover -s tests
```

---

Bom trabalho! 🧪📚
