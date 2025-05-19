# analisador_texto.py
# Autor: Symon Cristhian Ramos Barreto
import string


def possui_numeros(texto):
    return any(char.isdigit() for char in texto)


def possui_pontuacao(texto):
    return texto in string.punctuation


def limpar_pontuacao(palavras):
    palavras_sem_pontuacao = []
    for palavra in palavras:
        palavras_sem_pontuacao.append(palavra.strip(string.punctuation))
    return palavras_sem_pontuacao


def contar_palavras(texto):
    palavras = texto.split(" ")
    palavras_sem_pontuacao = limpar_pontuacao(palavras)
    return len(palavras_sem_pontuacao)


def contar_caracteres(texto, opcao):
    if opcao.lower() == "com espaço":
        return len(texto)
    elif opcao.lower() == "sem espaço":
        return len(texto.replace(" ", ""))
    return 0


def texto_valido(texto):
    palavras_validas = []
    palavras = texto.split(" ")
    for palavra in palavras:
        if not possui_pontuacao(palavra):
            palavras_validas.append(palavra)
    if len(palavras_validas) < 10:
        print("Texto muito curto\n")

    if possui_numeros(texto):
        print("Texto contém dados mistos\n")

    return None


def capitalizar(texto):
    return texto.title()


def para_maiuscula(texto):
    return texto.upper()


def para_minuscula(texto):
    return texto.lower()


def manipular_strings(array, opcao):
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
    texto_maiuscula, texto_minuscula, texto_capitalizadas = (
        manipular_strings(array, "maiúscula"),
        manipular_strings(array, "minúscula"),
        manipular_strings(array, "capitalizar"),
    )
    print(f"Palavras Maiúsculas:\n{texto_maiuscula}\n")
    print(f"Palavras Minúsculas:\n{texto_minuscula}\n")
    print(f"Palavras Capitalizadas:\n{texto_capitalizadas}\n")


def estatisticas(texto):
    print(f"Número total de palavras: {contar_palavras(texto)}\n")
    print(f"Número total de caracteres (com espaço): {contar_caracteres(texto,  "com espaço")}\n")
    print(f"Número total de caracteres (sem espaço): {contar_caracteres(texto,  "sem espaço")}\n")


def analisar_texto(texto):
    palavras = texto.split(" ")

    texto_valido(texto)
    transformar_retornar_texto(palavras)
    estatisticas(texto)
    return None


def main():
    continuar = True
    while continuar:
        texto = input("Digite um texto para análise: ")
        analisar_texto(texto)
        resposta = input("Deseja analisar outro texto? (s/n): ").strip().lower()
        continuar = resposta == 's'


if __name__ == "__main__":
    main()
