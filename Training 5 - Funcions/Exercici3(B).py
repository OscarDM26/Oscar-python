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

def calcular_iva(preu):
    iva = preu * 0.21
    return iva

def calcular_factura(preu, tipus_client):
    preu_descomptat = aplicar_descompte(preu, tipus_client)
    iva = calcular_iva(preu_descomptat)

    total = preu_descomptat + iva
    return total

print("Factura particular:", calcular_factura(100, "particular"), "€")
print("Factura empresa:", calcular_factura(100, "empresa"), "€")
print("Factura habitual:", calcular_factura(100, "habitual"), "€")