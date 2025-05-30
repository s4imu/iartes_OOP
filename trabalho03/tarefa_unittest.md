# 🧪 Tarefa Complementar: Testes Automatizados com `unittest`

## 🎯 Objetivo

Desenvolver testes automatizados para a classe implementada na atividade anterior, utilizando o módulo `unittest` da linguagem Python. Essa atividade reforça os conceitos de verificação de comportamento e confiabilidade de código orientado a objetos.

---

## 📝 Instruções

1. **Reutilize a classe** que você criou na tarefa anterior (ex.: `Animal`, `Sensor`, `Veículo`).
2. Crie um novo arquivo Python chamado `test_<nome_da_classe>.py`.
3. Importe o módulo `unittest` e a classe que você implementou.
4. Defina uma nova classe de teste que herda de `unittest.TestCase`.
5. Escreva **pelo menos três métodos de teste**, usando os seguintes critérios:
   - Teste de comportamento esperado (ex.: som emitido, leitura de sensor, etc.)
   - Teste de alteração de estado interno (ex.: uso de métodos públicos como setters ou entradas/saídas)
   - Teste de encapsulamento ou de controle de acesso (via métodos/propriedades)
6. Execute os testes utilizando:
   ```bash
   python -m unittest test_<nome_da_classe>.py
   ```

---

## 💡 Exemplo de Estrutura

```python
import unittest
from trabalho03.produto import Produto


class TestProduto(unittest.TestCase):
    def test_valor_inicial(self):
        p = Produto("Café", "2025/12/31", 10)
        self.assertEqual(p._qtde, 10)

    def test_saida_valida(self):
        p = Produto("Café", "2025/12/31", 10)
        self.assertTrue(p.saida_produto(5))
        self.assertEqual(p._qtde, 5)

    def test_validade_setter(self):
        p = Produto("Café", "2025/12/31", 10)
        p.validade = "2026/01/01"
        self.assertEqual(p.validade, "2026/01/01")
```

---

## 🧠 Dica

Você pode utilizar os métodos `setUp()` e `tearDown()` se precisar preparar ou limpar objetos antes/depois de cada teste.
