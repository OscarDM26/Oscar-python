def calcular_preu(preu_peces, ma_obra):
    total = preu_peces + ma_obra
    return total
    

preu = calcular_preu(45, 30) 
print("El cost total és:", preu, "€")
# Quants paràmetres té la funció? 2
# Quin valor retorna? 75
# Què passaria si eliminéssim el return? que la funcio no retornaria i no aniria.