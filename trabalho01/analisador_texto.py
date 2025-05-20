"""
analisador_texto.py
Autor: Symon Cristhian Ramos Barreto
Descrição: Módulo para análise textual com várias estatísticas e transformações de texto.
"""

import string


def possui_numeros(texto):
    """Verifica se o texto contém números."""
    return any(char.isdigit() for char in texto)


def possui_pontuacao(texto):
    """Verifica se a palavra é pontuação isolada."""
    return texto in string.punctuation


def limpar_pontuacao(palavras):
    """Remove pontuações das palavras da lista."""
    palavras_sem_pontuacao = []
    for palavra in palavras:
        palavras_sem_pontuacao.append(palavra.strip(string.punctuation))
    return palavras_sem_pontuacao


def contar_palavras(texto):
    """Conta o número de palavras no texto."""
    palavras = texto.split(" ")
    palavras_sem_pontuacao = limpar_pontuacao(palavras)
    print(f"Número de palavras: {len(palavras_sem_pontuacao)}")


def contar_caracteres(texto, opcao):
    """Conta o número de caracteres com ou sem espaço, ignorando pontuação."""
    texto_sem_pontuacao = texto.translate(str.maketrans("", "", string.punctuation))

    if opcao.lower() == "com espaço":
        print(f"Número de caracteres (com espaço): {len(texto_sem_pontuacao)}")
    elif opcao.lower() == "sem espaço":
        print(
            f"Número de caracteres (sem espaço): {len(texto_sem_pontuacao.replace(' ', ''))}"
        )


def contar_vogais(texto):
    """Conta a frequência de cada vogal no texto."""
    texto = texto.lower()
    vogais = [
        f"a={texto.count('a')}",
        f"e={texto.count('e')}",
        f"i={texto.count('i')}",
        f"o={texto.count('o')}",
        f"u={texto.count('u')}",
    ]
    print("Frequência de vogais:", ", ".join(vogais))


def palavras_mais_longas(texto):
    """Exibe as três palavras mais longas do texto."""
    palavras = texto.split()
    palavras_sem_pontuacao = limpar_pontuacao(palavras)

    tamanho_palavras = [(len(palavra), palavra) for palavra in palavras_sem_pontuacao]
    tamanho_palavras_ordenado = sorted(tamanho_palavras, reverse=True)

    maiores = tamanho_palavras_ordenado[:3]
    palavras_maiores = [palavra for _, palavra in maiores]

    print("Três palavras mais longas:", ", ".join(palavras_maiores) + "\n")


def texto_valido(texto):
    """Verifica se o texto possui tamanho mínimo e se contém números."""
    palavras_validas = []
    palavras = texto.split(" ")
    for palavra in palavras:
        if not possui_pontuacao(palavra):
            palavras_validas.append(palavra)
    if len(palavras_validas) < 10:
        print("Texto muito curto")

    if possui_numeros(texto):
        print("Texto contém dados mistos")


def capitalizar(texto):
    """Capitaliza cada palavra do texto."""
    return texto.title()


def para_maiuscula(texto):
    """Converte o texto para letras maiúsculas."""
    return texto.upper()


def para_minuscula(texto):
    """Converte o texto para letras minúsculas."""
    return texto.lower()


def manipular_strings(array, opcao):
    """Manipula as strings de acordo com a opção fornecida."""
    texto = ""
    if opcao.lower() == "maiúscula":
        array_maiusculas = map(para_maiuscula, array)
        texto = " ".join(array_maiusculas)
    elif opcao.lower() == "minúscula":
        array_minusculas = map(para_minuscula, array)
        texto = " ".join(array_minusculas)
    elif opcao.lower() == "capitalizar":
        array_capitalizadas = map(capitalizar, array)
        texto = " ".join(array_capitalizadas)
    else:
        print("Opção Inválida")
    return texto


def transformar_retornar_texto(array):
    """Exibe o texto em três versões: maiúscula, minúscula e capitalizada."""
    texto_maiuscula, texto_minuscula, texto_capitalizadas = (
        manipular_strings(array, "maiúscula"),
        manipular_strings(array, "minúscula"),
        manipular_strings(array, "capitalizar"),
    )
    print(f"Texto em maiúsculas: {texto_maiuscula}")
    print(f"Texto em minúsculas: {texto_minuscula}")
    print(f"Texto capitalizado: {texto_capitalizadas}")


def estatisticas(texto):
    """Executa todas as estatísticas sobre o texto."""
    contar_palavras(texto)
    contar_caracteres(texto, "com espaço")
    contar_caracteres(texto, "sem espaço")
    contar_vogais(texto)
    palavras_mais_longas(texto)


def analisar_texto(texto, opcoes):
    """Executa a análise do texto conforme as opções escolhidas."""
    palavras = texto.split(" ")

    texto_valido(texto)
    for opcao in opcoes:
        if opcao == 1:
            print(f"Texto em maiúsculas: { manipular_strings(palavras, 'maiúscula')}")
        elif opcao == 2:
            print(f"Texto em minúsculas: { manipular_strings(palavras, 'minúscula')}")
        elif opcao == 3:
            print(f"Texto capitalizado: { manipular_strings(palavras, 'capitalizar')}")
        elif opcao == 4:
            contar_palavras(texto)
        elif opcao == 5:
            contar_caracteres(texto, "com espaço")
        elif opcao == 6:
            contar_caracteres(texto, "sem espaço")
        elif opcao == 7:
            contar_vogais(texto)
        elif opcao == 8:
            palavras_mais_longas(texto)
        elif opcao == 9:
            transformar_retornar_texto(palavras)
            estatisticas(texto)
        else:
            print("Opção Inválida!")


def leitura_opcoes_do_usuario():
    """Lê as opções do usuário e valida os valores de 1 a 9."""
    opcoes_lidas = input(
        "Informe as opções a serem exibidas separadas por espaço (Ex: 1 2 3):\n"
        "1 - Mostrar texto em maiúsculas;\n"
        "2 - Mostrar texto em minúsculas;\n"
        "3 - Mostrar texto capitalizado;\n"
        "4 - Mostrar número total de palavras;\n"
        "5 - Mostrar número total de caracteres (com espaço);\n"
        "6 - Mostrar número total de caracteres (sem espaço);\n"
        "7 - Frequência de cada vogal;\n"
        "8 - As 3 palavras mais longas;\n"
        "9 - Exibir todos os anteriores;\n"
    )

    opcoes = opcoes_lidas.split()
    opcoes_validas = []

    for opcao in opcoes:
        if opcao.isdigit() and 1 <= int(opcao) <= 9:
            opcoes_validas.append(int(opcao))
        else:
            print(f"Opção inválida ignorada: {opcao}")

    print("Opções válidas selecionadas:", opcoes_validas)
    return opcoes_validas


def main():
    """Função principal que executa o programa em loop."""
    continuar = True
    while continuar:
        texto = input("Digite um texto para análise: ")
        opcoes = leitura_opcoes_do_usuario()
        analisar_texto(texto, opcoes)
        resposta = input("Deseja analisar outro texto? (s/n): ").strip().lower()
        continuar = resposta == "s"


if __name__ == "__main__":
    main()
