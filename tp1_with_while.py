
nom = "Fidele"
prenom = "Riconcilio"

def factorielle_while(n):
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result

n = 6  


print(f"Factorielle de {n} (boucle while): {factorielle_while(n)}")


i = 1
while i <= 50:
    if i % 15 == 0:  # Multiple de 3 et de 5
        print(f"{i}: {nom} {prenom}")
    elif i % 3 == 0:  # Multiple de 3
        print(f"{i}: {nom}")
    elif i % 5 == 0:  # Multiple de 5
        print(f"{i}: {prenom}")
    else:
        print(i)
    i += 1
