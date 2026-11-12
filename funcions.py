
# Exercici 1 - Calculadora de preus

def calcular_preu(peces, ma_obra):
    total = peces + ma_obra
    return total

preu = calcular_preu(45, 30)
print("Cost total:", preu, "€")


# Exercici 2 - Funcions amb condicions

def aplicar_descompte(preu, tipus_client):

    
    if tipus_client == "particular":
        descompte = 0
    elif tipus_client == "empresa":
        descompte = 0.10
    elif tipus_client == "habitual":
        descompte = 0.15
    else:
        print("Error: tipus de client incorrecte")
        return preu

    preu_final = preu - (preu * descompte)
    return preu_final


print("Particular:", aplicar_descompte(100, "particular"), "€")
print("Empresa:", aplicar_descompte(100, "empresa"), "€")
print("Habitual:", aplicar_descompte(100, "habitual"), "€")
print("Incorrecte:", aplicar_descompte(100, "altre"), "€")



# Exercici 3 - Funcions que criden altres funcions


def calcular_iva(preu):
    iva = preu * 0.21
    return iva



def calcular_factura(preu, tipus_client):

    preu_descompte = aplicar_descompte(preu, tipus_client)

    iva = calcular_iva(preu_descompte)

    total = preu_descompte + iva

    return total



print("IVA de 100 €:", calcular_iva(100), "€")

print("Factura particular:", calcular_factura(100, "particular"), "€")
print("Factura empresa:", calcular_factura(100, "empresa"), "€")
print("Factura habitual:", calcular_factura(100, "habitual"), "€")


# Exercici 4 - Programa complet: servei tecnic


def calcular_preu(peces, ma_obra):
    return peces + ma_obra



def aplicar_descompte(preu, tipus_client):

    if tipus_client == "particular":
        descompte = 0
    elif tipus_client == "empresa":
        descompte = 0.10
    elif tipus_client == "habitual":
        descompte = 0.15
    else:
        print("Error: tipus de client incorrecte")
        return preu

    return preu - (preu * descompte)



def calcular_iva(preu):
    return preu * 0.21



def calcular_factura(preu, tipus_client):

    preu_descompte = aplicar_descompte(preu, tipus_client)
    iva = calcular_iva(preu_descompte)

    return preu_descompte + iva



def mostrar_menu():
    print("\n===== SERVEI TÈCNIC INFORMÀTIC =====")
    print("1. Introduir una nova reparació")
    print("2. Consultar el nombre de reparacions")
    print("3. Consultar la facturació acumulada")
    print("4. Sortir")



def nova_reparacio():

    nom = input("Nom del client: ")
    peces = float(input("Cost de les peces: "))
    ma_obra = float(input("Cost de la mà d'obra: "))
    tipus = input("Tipus de client (particular/empresa/habitual): ").lower()

    preu_inicial = calcular_preu(peces, ma_obra)

    preu_descompte = aplicar_descompte(preu_inicial, tipus)

    descompte = preu_inicial - preu_descompte

    iva = calcular_iva(preu_descompte)

    total = calcular_factura(preu_inicial, tipus)

    print("\n===== FACTURA =====")
    print("Client:", nom)
    print("Preu inicial:", round(preu_inicial, 2), "€")
    print("Descompte:", round(descompte, 2), "€")
    print("IVA:", round(iva, 2), "€")
    print("Total a pagar:", round(total, 2), "€")

    return total



reparacions = 0
facturacio = 0

while True:

    mostrar_menu()

    opcio = input("Selecciona una opció: ")

    if opcio == "1":

        total = nova_reparacio()

        reparacions = reparacions + 1
        facturacio = facturacio + total

    elif opcio == "2":

        print("Nombre de reparacions:", reparacions)

    elif opcio == "3":

        print("Facturació acumulada:", round(facturacio, 2), "€")

    elif opcio == "4":

        print("Programa finalitzat")
        break

    else:

        print("Opció incorrecta")



# Ampliacio opcional - Mostrar reparacions

def mostrar_reparacions(llista):

    if len(llista) == 0:
        print("Encara no hi ha reparacions")
    else:
        for reparacio in llista:
            print("\nClient:", reparacio["nom"])
            print("Preu inicial:", reparacio["preu"], "€")
            print("Descompte:", reparacio["descompte"], "€")
            print("IVA:", reparacio["iva"], "€")
            print("Total:", reparacio["total"], "€")
