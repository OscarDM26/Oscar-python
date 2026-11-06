haynegativo = False
for i in range(10):
    numero = int(input("Introdueix un número: "))
    if numero < 0:
        haynegativo = True

if haynegativo:
    print("Hi ha algun número negatiu")
else:
    print("No hi ha ningun número negatiu")