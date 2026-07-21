from buscador import pegar_dados_pokemon
import random
import os

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def escolher_pokemon_aleatorio():
    numero_aleatorio = random.randint(1, 151)
    return pegar_dados_pokemon(numero_aleatorio)

def fazer_palpite():
    entrada = input("Faça o seu palpite (nome, número da dex ou '#' para desistir): ")

    if entrada == "#" or entrada == "": return entrada

    pokemon = pegar_dados_pokemon(entrada)
    return pokemon

def comparar_pokemon(pokemon_escolhido, pokemon_aleatorio):
    def obter_seta(atual, alvo):
        if atual == alvo: return " "
        return "↑" if alvo > atual else "↓"

    comparacoes = {
        "id": obter_seta(pokemon_escolhido["id"], pokemon_aleatorio["id"]),
        "altura": obter_seta(pokemon_escolhido["altura"], pokemon_aleatorio["altura"]),
        "peso": obter_seta(pokemon_escolhido["peso"], pokemon_aleatorio["peso"]),
    }
    return comparacoes

def mostrar_banner():
    with open("banner.txt", "r", encoding="utf-8") as arquivo:
        banner = arquivo.read()
        print(banner)

def mostrar_tabela(lista_pokemon, lista_comparacoes):
    cabecalho = f"{'Nº':<6} | {'Nome':<16} | {'Altura':<7} | {'Peso':<8} |"
    print(cabecalho)
    print("-" * len(cabecalho))

    if not lista_pokemon:
        print("Lista de palpites vazia!")

    for pokemon, comparacoes in zip(lista_pokemon, lista_comparacoes):
        if isinstance(pokemon, dict):
            id = pokemon["id"]
            nome = pokemon["nome"]
            altura = pokemon["altura"]/10
            peso = pokemon["peso"]/10

            comp_id = comparacoes["id"]
            comp_altura = comparacoes["altura"]
            comp_peso = comparacoes["peso"]

            print(f"{id:<4} {comp_id} | {nome:<16} | {altura:<4}m {comp_altura} | {peso:<4}kg {comp_peso} |")

    print()


def main():
    fim = False
    acertou = False
    lista_escolhidos = []
    lista_comparacoes = []

    pokemon_aleatorio = escolher_pokemon_aleatorio()
    pokemon_escolhido = ""

    limpar_tela()
    mostrar_banner()
    mostrar_tabela(lista_escolhidos, lista_comparacoes)

    while not fim:
        pokemon_escolhido = fazer_palpite()

        if not isinstance(pokemon_escolhido, dict): 
            limpar_tela()
            mostrar_banner()
            mostrar_tabela(lista_escolhidos, lista_comparacoes)
            print("Pokémon não encontrado! Tente novamente.")

            if pokemon_escolhido == "#": fim = True
            continue

        if pokemon_aleatorio["id"] == pokemon_escolhido["id"]: 
            fim = True
            acertou = True

        comparacoes = comparar_pokemon(pokemon_escolhido, pokemon_aleatorio)

        lista_escolhidos.append(pokemon_escolhido)
        lista_comparacoes.append(comparacoes)
        
        limpar_tela()
        mostrar_banner()
        mostrar_tabela(lista_escolhidos, lista_comparacoes)

    if acertou:
        print("Você acertou, parabéns!!")
    else:
        print("Você foi bem!")

if __name__ == "__main__":
    main()