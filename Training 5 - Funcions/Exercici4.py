def calcular_preu(preu_peces, ma_obra):
    total = preu_peces + ma_obra
    return total

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

def mostrar_menu():
    print("\n===== SERVEI TÈCNIC INFORMÀTIC =====")
    print("1. Introduir una nova reparació")
    print("2. Consultar el nombre de reparacions")
    print("3. Consultar la facturació acumulada")
    print("4. Sortir")

def mostrar_factura(nom, preu_inicial, tipus_client):
    preu_descomptat = aplicar_descompte(preu_inicial, tipus_client)
    descompte = preu_inicial - preu_descomptat
    iva = calcular_iva(preu_descomptat)
    total = calcular_factura(preu_inicial, tipus_client)

    print("\n========== FACTURA ==========")
    print("Client:", nom)
    print("Preu inicial:", round(preu_inicial, 2), "€")
    print("Descompte:", round(descompte, 2), "€")
    print("IVA (21%):", round(iva, 2), "€")
    print("TOTAL A PAGAR:", round(total, 2), "€")
    print("=============================")

def introduir_reparacio():
    nom = input("Nom del client: ")

    peces = float(input("Cost de les peces (€): "))
    ma_obra = float(input("Cost de la mà d'obra (€): "))

    tipus_client = input(
        "Tipus de client (particular, empresa, habitual): "
    ).lower()

    while tipus_client not in ["particular", "empresa", "habitual"]:
        print("Tipus de client no vàlid.")
        tipus_client = input(
            "Introdueix particular, empresa o habitual: "
        ).lower()

    preu_inicial = calcular_preu(peces, ma_obra)

    mostrar_factura(nom, preu_inicial, tipus_client)

    total = calcular_factura(preu_inicial, tipus_client)

    return total

def main():
    nombre_reparacions = 0
    facturacio_acumulada = 0

    opcio = ""

    while opcio != "4":
        mostrar_menu()
        opcio = input("Selecciona una opció: ")

        if opcio == "1":
            total = introduir_reparacio()
            nombre_reparacions += 1
            facturacio_acumulada += total

        elif opcio == "2":
            print("Nombre de reparacions:", nombre_reparacions)

        elif opcio == "3":
            print(
                "Facturació acumulada:",
                round(facturacio_acumulada, 2),
                "€"
            )

        elif opcio == "4":
            print("Gràcies per utilitzar el servei tècnic!")

        else:
            print("Opció no vàlida. Torna-ho a intentar.")

main()