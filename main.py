# main.py — fornito dal professore
from poke_api  import scarica_pokemon
from poke_info import estrai_info
from poke_file import salva_scheda
import time

if __name__ == "__main__":
    print("=== POKÉDEX COLLABORATIVO ===")
    print()
    while True:

        nome=input("Inserisci il nome di un pokemon o exit per uscire: ")
        nome=nome.strip().lower()
        if nome=="exit":
            print("Termino il programma, arrivederci!")
            break
        print(f"Cerco {nome}...")

        dati_grezzi = scarica_pokemon(nome)

        if dati_grezzi is None:
            print(f"  {nome}: impossibile scaricare i dati")
        else:
            info      = estrai_info(dati_grezzi)
            nome_file = nome + ".txt"
            salva_scheda(info, nome_file)
            print(f"  Salvato: {nome_file}")

    print()
    print("Finito! Controlla i file .txt nella cartella.")