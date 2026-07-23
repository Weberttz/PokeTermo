import requests

# dicionário
TIPOS_PT = {
    "normal": "Normal",
    "fire": "Fogo",
    "water": "Água",
    "electric": "Elétrico",
    "grass": "Planta",
    "ice": "Gelo",
    "fighting": "Lutador",
    "poison": "Veneno",
    "ground": "Terra",
    "flying": "Voador",
    "psychic": "Psíquico",
    "bug": "Inseto",
    "rock": "Pedra",
    "ghost": "Fantasma",
    "dragon": "Dragão",
    "dark": "Sombrio",
    "steel": "Aço",
    "fairy": "Fada",
}

GERACOES = [
    {"numero": 1, "inicio": 1, "fim": 151, "total": 151},
    {"numero": 2, "inicio": 152, "fim": 251, "total": 100},
    {"numero": 3, "inicio": 252, "fim": 386, "total": 135},
    {"numero": 4, "inicio": 387, "fim": 493, "total": 107},
    {"numero": 5, "inicio": 494, "fim": 649, "total": 156},
    {"numero": 6, "inicio": 650, "fim": 721, "total": 72},
    {"numero": 7, "inicio": 722, "fim": 809, "total": 88},
    {"numero": 8, "inicio": 810, "fim": 905, "total": 96},
    {"numero": 9, "inicio": 906, "fim": 1025, "total": 120}
]


def pegar_dados_pokemon(nome_ou_id):
    # url para o endpoint da PokeAPI
    url = f"https://pokeapi.co/api/v2/pokemon/{str(nome_ou_id).lower()}"
    
    response = requests.get(url)
    
    # se funcionar, os dados são extraidos
    if response.status_code == 200:
        dados = response.json()
        
        # extração de informações
        informacoes_pokemon = {
            "nome": dados["name"].capitalize(),
            "id": dados["id"],
            "altura": dados["height"],
            "peso": dados["weight"],
            "tipos": [t["type"]["name"] for t in dados["types"]],
            "sprite": dados["sprites"]["front_default"],
            "geracao": encontrar_geracao(dados["id"])
        }
        return informacoes_pokemon
    else:
        return f"Erro: Não foi possível encontrar o pokemon de nome/id: '{nome_ou_id}' (Status: {response.status_code})"

def encontrar_geracao(id):
    for geracao in GERACOES:
        if id >= geracao["inicio"] and id <= geracao["fim"]:
            return geracao["numero"]

def mostrar_dados_pokemon(pokemon):
    if isinstance(pokemon, dict):
        print(f"Número da dex: {pokemon["id"]}")
        print(f"Nome: {pokemon["nome"]}")
        print(f"Altura: {pokemon["altura"]/10}m")
        print(f"Peso: {pokemon["peso"]/10}kg")

        tipos_pt = [TIPOS_PT.get(t, t) for t in pokemon["tipos"]]
        print(f"Tipo(s): {', '.join(tipos_pt)}")
        print(f"Geração: {pokemon["geracao"]}")
    else:
        print(pokemon) # imprime erro, caso ocorra

def main():
    pokemon = input("Digite o nome ou número da pokedex do pokemon que deseja olhar os dados: ")

    if pokemon == "": return

    dados_pokemon = pegar_dados_pokemon(pokemon)
    mostrar_dados_pokemon(dados_pokemon)

if __name__ == "__main__":
    main()