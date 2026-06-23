import requests

URL_BASE = "https://pokeapi.co/api/v2/pokemon/"

def scarica_pokemon(nome):
    """
    Chiama PokéAPI e ritorna il dizionario JSON del Pokémon.
    """
    # costruiamo il link per la richiesta con il pokemon
    url=URL_BASE + nome.lower().strip()
    try:
        # facciamo la chiamata al link per ottenere il json
        risposta = requests.get(url,timeout=10)

        if risposta.status_code ==200:
            return risposta.json() #ritorna in dizionario con i dati
        else:
            print(f"errore: il pokemon {nome} non esiste")
            return None
    except requests.exceptions.ConnectionError:
        print("Errore: nessuna connessione a internet")
        return None
