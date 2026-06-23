def estrai_info(dati):

    info = {}

    info["nome"] = dati["name"]
    info["numero"] = dati["id"]
    info["altezza_m"] = dati["height"] / 10
    info["peso_kg"] = dati["weight"] / 10
    info["tipo"] = dati["types"][0]["type"]["name"]
    info["esperienza"] = dati["base_experience"]

    return info


