priklad = input("Priklad: ")
znamienko = []
cisla = []
predchadzajuce_znamienko_poz = 0
for i in range(len(priklad)):
    if priklad[i] in "+-/*":
        znamienko.append(priklad[i])
        cisla.append(int(priklad[predchadzajuce_znamienko_poz:i]))
        predchadzajuce_znamienko_poz = i + 1
cisla.append(int(priklad[predchadzajuce_znamienko_poz:]))

vysledok = cisla[0]
for i in range(len(znamienko)):
    if znamienko[i] == '+':
        vysledok = vysledok + cisla[i+1]
    elif znamienko[i] == '-':
        vysledok = vysledok - cisla[i+1]
    elif znamienko[i] == '/':
        vysledok = vysledok / cisla[i+1]
    elif znamienko[i] == '*':
        vysledok = vysledok * cisla[i+1]

#print(znamienko)
#print(cisla)
print(int(vysledok))