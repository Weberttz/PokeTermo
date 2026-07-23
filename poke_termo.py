from buscador import pegar_dados_pokemon, encontrar_geracao, TIPOS_PT, GERACOES
import random
import os

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def menu():
    limpar_tela()
    mostrar_banner()
    print("―" * 55)
    print("1 - Fazer palpite")
    print("2 - Ver Pokedex")
    print("0 - Sair\n")

def escolher_pokemon_aleatorio():
    numero_aleatorio = random.randint(1, 151)
    return pegar_dados_pokemon(numero_aleatorio)

def instruir():
    print(" ✓ - certo  % - parcial  x - errado   ↑ - maior   ↓ - menor ")
    print("\nDigite nome, número da dex ou '0' para voltar\n")

def fazer_palpite():
    entrada = input("Faça o seu palpite: ")

    if entrada == '0' or entrada == "": return entrada

    pokemon = pegar_dados_pokemon(entrada)
    return pokemon

def comparar_pokemon(pokemon_escolhido, pokemon_aleatorio):
    def obter_seta(atual, alvo):
        if atual == alvo: return "✓"
        return "↑" if alvo > atual else "↓"
    
    def obter_confirmacao(atual, alvo):
        if atual == alvo: return "✓"
        return "x"
    
    def comparar_tipo(atual, alvo, index):
        tipos_atual = [TIPOS_PT.get(t, t) for t in atual]
        tipos_alvo  = [TIPOS_PT.get(t, t) for t in alvo]

        if len(tipos_atual) < 2: tipos_atual.append("-")
        if len(tipos_alvo) < 2: tipos_alvo.append("-")

        if tipos_atual[index] == tipos_alvo[index]:
            return "✓"
        if tipos_atual[index] == tipos_alvo[1 - index]:
            return "%"
        return "x"

    comparacoes = {
        "nome": obter_confirmacao(pokemon_escolhido["id"], pokemon_aleatorio["id"]),
        "id": obter_seta(pokemon_escolhido["id"], pokemon_aleatorio["id"]),
        "altura": obter_seta(pokemon_escolhido["altura"], pokemon_aleatorio["altura"]),
        "peso": obter_seta(pokemon_escolhido["peso"], pokemon_aleatorio["peso"]),
        "tipo1": comparar_tipo(pokemon_escolhido["tipos"], pokemon_aleatorio["tipos"], 0),
        "tipo2": comparar_tipo(pokemon_escolhido["tipos"], pokemon_aleatorio["tipos"], 1),
        "geracao": obter_seta(pokemon_escolhido["geracao"], pokemon_aleatorio["geracao"])
    }
    return comparacoes

def mostrar_banner():
    with open("banner.txt", "r", encoding="utf-8") as arquivo:
        banner = arquivo.read()
        print(banner)

def abrir_pokedex():
    with open("pokedex.txt", "r", encoding="utf-8") as arquivo_dex:
        print(arquivo_dex.read())

    c = input("Pressione enter para voltar tecla...")

def mostrar_tabela(lista_pokemon, lista_comparacoes):
    print("―" * 87)
    cabecalho = f"| {'Nº':<6} | {'Nome':<16} | {'Altura':<7} | {'Peso':<9} | {'Tipo 1':<10} | {'Tipo 2':<10} | {'Geração':<6} |"
    print(cabecalho)
    print("―" * len(cabecalho))

    if not lista_pokemon:
        print("Lista de palpites vazia!")

    for pokemon, comparacoes in zip(lista_pokemon, lista_comparacoes):
        if isinstance(pokemon, dict):
            id = pokemon["id"]
            nome = pokemon["nome"]
            altura = pokemon["altura"]/10
            peso = pokemon["peso"]/10
            geracao = pokemon["geracao"]
            tipos_pt = [TIPOS_PT.get(t, t) for t in pokemon["tipos"]]
 
            tipo1 = tipos_pt[0]
            tipo2 = "-"

            if len(tipos_pt) > 1: tipo2 = tipos_pt[1]

            c_id = comparacoes["id"]
            c_altura = comparacoes["altura"]
            c_peso = comparacoes["peso"]
            c_nome = comparacoes["nome"]
            c_tipo1 = comparacoes["tipo1"]
            c_tipo2 = comparacoes["tipo2"]
            c_geracao = comparacoes["geracao"]

            print(
                f"| {id:<4} {c_id} "
                f"| {nome:<14} {c_nome} "
                f"| {altura:<4}m {c_altura} "
                f"| {peso:<5}kg {c_peso} "
                f"| {tipo1:<8} {c_tipo1} "
                f"| {tipo2:<8} {c_tipo2} "
                f"| {geracao:<5} {c_geracao} |"
            )

    print()
   
def gerenciar_palpites(jogo, pokemon_aleatorio, lista_escolhidos, lista_comparacoes):
    acertou = jogo["acertou_pokemon"]

    limpar_tela()
    mostrar_banner()
    mostrar_tabela(lista_escolhidos, lista_comparacoes)
    instruir()

    pokemon_escolhido = ""

    while not acertou:
        pokemon_escolhido = fazer_palpite()

        if not isinstance(pokemon_escolhido, dict): 
            if pokemon_escolhido == '0': break
            limpar_tela()
            mostrar_banner()
            mostrar_tabela(lista_escolhidos, lista_comparacoes)
            instruir()
            print("Pokémon não encontrado! Tente novamente.")

            continue

        if pokemon_aleatorio["id"] == pokemon_escolhido["id"]: 
            acertou = True
            jogo["acertou_pokemon"] = True

        comparacoes = comparar_pokemon(pokemon_escolhido, pokemon_aleatorio)

        lista_escolhidos.append(pokemon_escolhido)
        lista_comparacoes.append(comparacoes)
        jogo["contador_palpites"] +=1

        limpar_tela()
        mostrar_banner()
        mostrar_tabela(lista_escolhidos, lista_comparacoes)
        instruir()

    if acertou:
        print(f"Parabéns, você acertou o pokemon com {jogo["contador_palpites"]} palpites")
        input("Pressione enter para voltar")
    else:
        print(f"Você foi bem")
    

def main():
    fim = False
    jogo = {"contador_palpites":0, "acertou_pokemon": False}
    lista_escolhidos = []
    lista_comparacoes = []
    pokemon_aleatorio = escolher_pokemon_aleatorio()

    while not fim:
        menu()
        opcao = input("Digite uma opção: ")

        match opcao:
            case '1': fim = gerenciar_palpites(jogo, pokemon_aleatorio, lista_escolhidos, lista_comparacoes)
            case '2': 
                limpar_tela() 
                abrir_pokedex()
            case '0': fim = True
            case _: print("Comando desconhecido!")  
            
    

if __name__ == "__main__":
    main()