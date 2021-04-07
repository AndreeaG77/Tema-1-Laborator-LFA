# GEAMANU ANDREEA
# GRUPA 133

# Problema a (DFA)
# Citirea datelor
f = open("date.in")
n = int(f.readline())
# Codul functioneaza si cu stari care nu sunt consecutive
stari = [int(x) for x in f.readline().split()]
m = int(f.readline())
tranzitii = []
for i in range(m):
    tranzitii.append([x for x in f.readline().split()])
s = int(f.readline())
nrf = int(f.readline())
stari_finale = [int(x) for x in f.readline().split()]
nrCuv = int(f.readline())
cuvinte = []
for i in range(nrCuv):
    cuvinte.append(f.readline().strip())
f.close()
g = open("date.out", "w")

# Parcurg lista de cuvinte
for cuv in cuvinte:
    i = 0
    nod_curent = s
    solutie = str(s) + " "
    # Cat timp mai am de citit caractere din cuvant verific
    while i<len(cuv):
        ok = 0
        # Caut o tranzitie care sa corespunda nodului si caracterului curent
        for lista in tranzitii:
            if int(lista[0])==nod_curent and lista[2]==cuv[i] :
                ok = 1
                break
        # Daca am gasit o tranzitie trec la urmatorul caracter si actualizez nodul curent
        if ok == 1:
            nod_curent = int(lista[1])
            i += 1
            solutie = solutie + str(nod_curent) + " "
        # Daca nu am gasit nicio tranzitie inseamna ca am citit un cuvant care nu este acceptat
        else:
            break
    # Daca nodul curent este o stare finala si am parcurs tot cuvantul
    # Atunci acesta este un cuvant acceptat
    if nod_curent in stari_finale and i==len(cuv):
        # Afisez si drumul parcurs prin graf
        g.write("DA  Drum: " + solutie + "\n")
    else:
        g.write("NU" + "\n")

g.close()