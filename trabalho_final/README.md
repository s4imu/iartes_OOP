# Trabalho Final - Programação Orientada a Objetos (IARTES)

## 📘 Descrição do Projeto

Este projeto consiste no desenvolvimento de uma aplicação backend utilizando **Python** e o framework **Flask**, com foco em **Test-Driven Development (TDD)**. A aplicação tem como objetivo gerenciar o inventário de produtos de um pequeno comércio, permitindo o cadastro, consulta, atualização e controle de estoque.

---

## 🎯 Objetivo Geral

Implementar um sistema de gerenciamento de inventário que permita:

- Cadastrar e atualizar produtos.
- Consultar e listar o estoque.
- Registrar entradas e saídas de mercadorias.
- Acompanhar o nível de estoque de cada item.

---

## 📦 Bibliotecas Utilizadas

- **Flask**: Framework web leve e flexível para Python, utilizado para criar APIs REST e aplicações web. Ele facilita o desenvolvimento rápido e organizado de sistemas backend.
- **Werkzeug**: Biblioteca que fornece ferramentas para manipulação de requisições e respostas HTTP, além de funcionalidades como roteamento e depuração. É um dos componentes principais do Flask.
- **Faker**: Biblioteca para geração de dados fictícios, como nomes, endereços e números. É útil para criar dados de teste em aplicações e cenários de desenvolvimento.
- **itsdangerous**: Biblioteca para manipulação segura de dados, como geração e validação de tokens. É usada para implementar autenticação e proteger informações sensíveis.

---

## 📋 Funcionalidades Implementadas

1. **Cadastro de Produto**:
   - Permite cadastrar produtos com os campos: `nome`, `categoria`, `quantidade_inicial` e `preco_unitario`.
   - Restrições: `quantidade_inicial` ≥ 0 e `preco_unitario` > 0.

2. **Listagem de Produtos**:
   - Exibe todos os produtos cadastrados.
   - Suporte a filtros por `nome` ou `categoria` via query string.

3. **Consulta de Produto por ID**:
   - Retorna os dados completos de um produto específico.

4. **Atualização de Produto**:
   - Permite atualizar os campos `nome`, `categoria` ou `preco_unitario`.

5. **Operações de Estoque**:
   - Entrada: aumenta a quantidade disponível de um produto.
   - Saída: reduz a quantidade disponível, sem permitir estoque negativo.

6. **Remoção de Produto**:
   - Permite excluir um produto do inventário.

---

## 🧪 Testes Automatizados

Os testes foram implementados seguindo a metodologia **TDD** e cobrem os seguintes cenários:

| Código  | Nome                          | Descrição                                                                 | Entrada de Teste                                                                 | Resultado Esperado                                                                 |
|---------|-------------------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| CT001   | Criar Produto Válido          | Testa a criação de um produto com dados válidos.                          | `{"nome": "Notebook", "categoria": "Eletrônicos", "quantidade_inicial": 10, "preco_unitario": 2500.00}` | Produto criado com sucesso, status 201.                                           |
| CT002   | Listar Produtos               | Testa a listagem de todos os produtos cadastrados.                        | Nenhuma entrada.                                                                | Lista de produtos cadastrados, status 200.                                        |
| CT003   | Buscar Produto por ID         | Testa a busca de um produto existente pelo ID.                            | ID do produto: 1                                                                | Dados do produto retornados, status 200.                                          |
| CT004   | Buscar Produtos com Filtro    | Testa a busca de produtos com filtro por categoria.                       | Query string: `?categoria=Eletrônicos`                                          | Lista de produtos filtrados, status 200.                                          |
| CT005   | Atualizar Produto             | Testa a atualização de dados de um produto existente.                     | ID do produto: 1, `{"nome": "Notebook Pro", "preco_unitario": 3000.00}`          | Produto atualizado com sucesso, status 200.                                       |
| CT006   | Entrada de Estoque            | Testa a entrada de estoque para um produto existente.                     | ID do produto: 1, `{"quantidade": 5}`                                           | Quantidade atualizada, status 200.                                                |
| CT007   | Saída de Estoque              | Testa a saída de estoque para um produto existente.                       | ID do produto: 1, `{"quantidade": 5}`                                           | Quantidade atualizada, status 200.                                                |
| CT008   | Remover Produto               | Testa a remoção de um produto existente.                                  | ID do produto: 1                                                                | Produto removido com sucesso, status 200.                                         |
| CT009   | Criar Produto Inválido        | Testa a criação de um produto com dados inválidos.                        | `{"nome": "Notebook", "categoria": "Eletrônicos", "quantidade_inicial": -5, "preco_unitario": 2500.00}` | Erro de validação, status 400.                                                    |
| CT010   | Cadastrar Produto Sem Dados   | Testa o cadastro de um produto sem fornecer dados.                        | Nenhuma entrada.                                                                | Erro de validação, status 400.                                                    |
| CT011   | Entrada de Estoque Inválida   | Testa a entrada de estoque com quantidade negativa.                       | ID do produto: 1, `{"quantidade": -5}`                                          | Erro de validação, status 400.                                                    |
| CT012   | Atualizar Produto Sem Dados   | Testa a atualização de um produto sem fornecer dados.                     | ID do produto: 1                                                                | Erro de validação, status 400.                                                    |
| CT013   | Atualizar Produto Inválido    | Testa a atualização de um produto com dados inválidos.                    | ID do produto: 1, `{"nome": "", "preco_unitario": -3000.00}`                     | Erro de validação, status 400.                                                    |
| CT014   | Buscar Produto Inexistente    | Testa a busca de um produto inexistente pelo ID.                          | ID do produto: 999                                                              | Produto não encontrado, status 404.                                               |
| CT015   | Buscar Produtos com Parâmetros Inválidos | Testa a busca de produtos com parâmetros inválidos.                       | Query string: `?filtroInvalido=Inexistente`                                      | Erro de parâmetro inválido, status 404.                                           |
| CT016   | Atualizar Produto Inexistente | Testa a atualização de um produto inexistente.                            | ID do produto: 999, `{"nome": "Notebook Pro", "preco_unitario": 3000.00}`        | Produto não encontrado, status 404.                                               |
| CT017   | Remover Produto Inexistente   | Testa a remoção de um produto inexistente.                                | ID do produto: 999                                                              | Produto não encontrado, status 404.                                               |
| CT018   | Saída de Estoque Insuficiente | Testa a saída de estoque com quantidade maior que o disponível.           | ID do produto: 1, `{"quantidade": 10}`                                          | Erro de estoque insuficiente, status 400.                                         |
| CT019   | Saída de Estoque Zerado       | Testa a saída de estoque para um produto com quantidade inicial igual a 0.| ID do produto: 1, `{"quantidade": 5}`                                           | Erro de estoque insuficiente, status 400.                                         |


---

## 🛠️ Instruções de Execução

Para executar o projeto, siga os passos abaixo:

1. Certifique-se de ter o **Python 3.8+** instalado.
2. Execute o script `script.sh` no terminal para configurar o ambiente, iniciar a API, executar os testes automatizados e exibir os relatórios CSV no terminal.:

```bash
./script.sh