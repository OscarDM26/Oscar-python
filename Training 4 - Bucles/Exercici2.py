nota = 0
hay10 = False
while nota != -1:
    nota = int(input("Fica un numero o -1 per acabar: "))
    if nota == 10:
        hay10 = True
if hay10:
    print("Hi ha un 10")
else:
    print("No hi ha cap 10")