valueInt = 1
print(f"Tipo: {type(valueInt)}")

valueReal = 1.00
print(f"Tipo: {type(valueReal)}")

valueCompl = 3 + 4j
print(f"Tipo: {type(valueCompl)}")

valueBool = False
print(f"Tipo: {type(valueBool)}")

valueStr = "Hello"
print(f"Tipo: {type(valueStr)}")

valueConj = {"arroz", "feijão", "batata"}
print(f"Tipo: {type(valueConj)}")

valueList = ["arroz", "feijão", "batata"]
print(f"Tipo: {type(valueList)}")

valueTup = ("arroz",2,"vendido")
print(f"Tipo: {type(valueTup)}")

valueDict = {"nome": "arroz", "valor": 2.00, "vendido": True}
print(f"Tipo: {type(valueDict)}")

print(valueInt)

'''
+  adição
- subtração
* multiplicação
/ divisão
% resto da divisão
// módulo
** exponenciação
'''

a = 2
b = 1
print(a-b**2)

x, y, z = "arroz", "feijão", "batata"
print(x, y, z)

nota = float(input("Informe a nota: "))
if 8.0 < nota <= 10.0:
    print("Aprovado com mérito: %.2f\nParabéns!!!"% nota)
elif 6.0 < nota <= 8.0:
    print("Aprovado: %.2f" % nota)
elif 0 <= nota <= 6.0:
    print("Nota Obtida: %.2f" % nota)
else:
    print("Valor inválido!!!")

'''
AND: True se ambos forem True
OR: True se pelo menos um for True
NOT: Inverte o valor lógico (True vira False, e vice-versa)
'''

a = True
b = False

# AND: só dá True se os dois forem True
print(a and b)  # False

# OR: dá True se pelo menos um for True
print(a or b)   # True

# NOT: inverte
print(not a)    # False
print(not b)

'''
WHILE: repete enquanto a condição for True
FOR: percorre itens de uma sequência (como lista, string, range)
'''

x = 0
while x < 5:
    print(f"Print com while: {x}")
    x += 1

# Percorre cada número de 0 até 4
for i in range(5):
    print(f"Print com for e range: {i}")

# FOR com lista
for cor in ["vermelho", "azul", "verde"]:
    print(f"Print com for e range: {cor}")