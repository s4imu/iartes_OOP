# 🧩 Tarefa: Aplicando Conceitos de POO em Python

## 🎯 Objetivo
Aplicar os conceitos de **encapsulamento**, **herança** e **polimorfismo** por meio da definição de uma hierarquia de classes em Python.

---

## 📝 Instruções

1. **Defina uma classe base**, por exemplo:
   - `Animal`, `Veículo` ou `Sensor`.

2. **Crie uma hierarquia** com:
   - Pelo menos **uma subclasse** herdando da classe base;
   - Pelo menos **dois métodos especializados** (um deles deve ser sobrescrito na subclasse).

3. **Implemente um trecho de código** que demonstre:
   - ✔️ Uso da **herança**;
   - ✔️ Uso do **polimorfismo**;
   - ✔️ Uso do **encapsulamento** com atributos protegidos ou privados.

---

## 💡 Exemplo de Referência

```python
class Animal:
    def __init__(self, nome):
        self._nome = nome

    def emitir_som(self):
        return "Som genérico"

    def get_nome(self):
        return self._nome

class Cachorro(Animal):
    def emitir_som(self):
        return "Au au"

class Gata(Animal):
    def emitir_som(self):
        return "Miau"

# Demonstração de polimorfismo
animais = [Cachorro("Rex"), Gata("Mimi")]

for animal in animais:
    print(f"{animal.get_nome()} diz: {animal.emitir_som()}")
```

---

## ✅ Critérios de Avaliação

- Uso correto dos conceitos de POO.
- Clareza e organização do código.
- Comentários explicativos, se necessário.
