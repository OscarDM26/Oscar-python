numero1 = int(input("Introdueix el primer número: "))
numero2 = int(input("Introdueix el segon número: "))
numero3 = int(input("Introdueix el tercer número: "))
if numero1 > numero2 and numero1 > numero3:
    print("El número més gran és:", numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("El número més gran és:", numero2)
else:
    print("El número més gran és:", numero3)