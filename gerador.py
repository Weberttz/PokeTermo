from buscador import pegar_dados_pokemon

# python3 gerador.py > pokedex.txt

def main():
    id = 1
    while id < 152: # mude para gerar mais dados
        pokemon = pegar_dados_pokemon(id)
        if isinstance(pokemon, dict):
            print(f"{pokemon["id"]} - {pokemon["nome"]}")
        id+=1

if __name__ == "__main__":
    main()