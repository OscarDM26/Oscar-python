def aplicar_descompte(preu, tipus_client):
    if tipus_client == "particular":
        descompte = 0
    elif tipus_client == "empresa":
        descompte = 0.10
    elif tipus_client == "habitual":
        descompte = 0.15
    else:
        print("Tipus de client no vàlid")
        return preu
    
    preu_final = preu - (preu * descompte)
    return preu_final
print("Particular:", aplicar_descompte(100, "particular"), "€")
print("Empresa:", aplicar_descompte(100, "empresa"), "€")
print("Habitual:", aplicar_descompte(100, "habitual"), "€")
print("Incorrecte:", aplicar_descompte(100, "estudiant"), "€")