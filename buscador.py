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
            "sprite": dados["sprites"]["front_default"]
        }
        return informacoes_pokemon
    else:
        return f"Erro: Não foi possível encontrar o pokemon de nome/id: '{nome_ou_id}' (Status: {response.status_code})"

def mostrar_dados_pokemon(pokemon):
    if isinstance(pokemon, dict):
        print(f"Número da dex: {pokemon["id"]}")
        print(f"Nome: {pokemon["nome"]}")
        print(f"Altura: {pokemon["altura"]/10}m")
        print(f"Peso: {pokemon["peso"]/10}kg")

        tipos_pt = [TIPOS_PT.get(t, t) for t in pokemon["tipos"]]
        print(f"Tipo(s): {', '.join(tipos_pt)}")
    else:
        print(pokemon) # imprime erro, caso ocorra

def main():
    pokemon = input("Digite o nome ou número da pokedex do pokemon que deseja olhar os dados: ")

    if pokemon == "": return

    dados_pokemon = pegar_dados_pokemon(pokemon)
    mostrar_dados_pokemon(dados_pokemon)

main()