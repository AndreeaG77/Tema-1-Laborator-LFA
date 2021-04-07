# GEAMANU ANDREEA
# GRUPA 133

# Codul functioneaza si pentru Problema a (DFA) si pentru Problema b (NFA)
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

# Creez un dictionar cu liste de adiacenta pentru fiecare nod
dict_tranzitii = {}
for lista in tranzitii:
    if lista[0] not in dict_tranzitii:
        dict_tranzitii[lista[0]] = [(lista[1], lista[2])]
    else:
        dict_tranzitii[lista[0]].append((lista[1], lista[2]))
for stare in stari:
    if str(stare) not in dict_tranzitii:
        dict_tranzitii[str(stare)] = []

def BFS(stare_initiala, cuvant):
    i = 0
    coada = []
    coada.append((stare_initiala,i))
    while coada != []:
        (nod_crt, i) = coada[0]
        coada.pop(0)
        if dict_tranzitii[str(nod_crt)] != []:
            for (vecin_nod_crt, litera_tranz) in dict_tranzitii[str(nod_crt)]:
                if i<len(cuvant) and cuvant[i]==litera_tranz:
                    if i == len(cuvant)-1 and int(vecin_nod_crt) in stari_finale:
                        return "DA"
                    else:
                        coada.append((vecin_nod_crt, i+1))
    return "NU"

for cuv in cuvinte:
    g.write(BFS(s,cuv) + "\n")

g.close()