# poke_file.py — STUDENTE 3 — branch: feature/file
# Scrivi la funzione salva_scheda(info, percorso)


def salva_scheda(info, percorso):
    """
    Scrive le informazioni del Pokémon in un file di testo.
    info è il dizionario prodotto da estrai_info().
    percorso è il nome del file da creare.
    """

    # PASSO 1: apri il file in scrittura
    with open(percorso, "w", encoding="utf-8") as f:

        # PASSO 2: scrivi l'intestazione
        f.write("--- SCHEDA POKÉMON git---\n")

        # PASSO 3: scrivi ogni campo su una riga
        f.write(f"Nome: {info["nome"]}\n")              # TODO: scrivi il nome
        f.write(f"Numero: {info["numero"]}\n")          # TODO: scrivi il numero
        f.write(f"Tipo: {info["tipo"]}\n")              # TODO: scrivi il tipo
        f.write(f"Altezza: {info["altezza_m"]}\n")        # TODO: scrivi l'altezza
        f.write(f"Peso: {info["peso_kg"]}\n")              # TODO: scrivi il peso
        f.write(f"Esperinza: {info["esperienza"]}\n")   # TODO: scrivi l'esperienza

    # PASSO 4: stampa un messaggio di conferma
    print(f"Salvato: {percorso}")


# Test: esegui questo file direttamente per provare
if __name__ == "__main__":
    info_finta = {
        "nome":       "pikachu",
        "numero":     25,
        "altezza_m":  0.4,
        "peso_kg":    6.0,
        "tipo":       "electric",
        "esperienza": 112
    }
    salva_scheda(info_finta, "test_pikachu.txt")
    # Poi apri test_pikachu.txt e controlla il contenuto!