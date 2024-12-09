def factoriel_for(n):
    factoriel = 1
    for i in range(1, n + 1):
        factoriel *= i
    return factoriel

def afficher_multiples():
    
    nom = "Fidele"     
    prenom = "Riconcilio"     

    for i in range(1, 51):
        # On vérifie d'abord les multiples de 3 et 5
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i}: {nom} {prenom}")
        # Si ce n'est pas un multiple de 3 et 5, on vérifie les multiples de 3
        elif i % 3 == 0:
            print(f"{i}: {nom}")
        # Si ce n'est pas un multiple de 3, on vérifie les multiples de 5
        elif i % 5 == 0:
            print(f"{i}: {prenom}")
        # Sinon, on affiche juste un tiret
        else:
            print(f"{i}: -")

n = 10  
print(f"Factoriel de {n} avec for : {factoriel_for(n)}")

print("\nAffichage des multiples :")
afficher_multiples()
