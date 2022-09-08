lista = [10,4,2,1]
for i in range(len(lista),1,-1):
    for index in range(0,i-1):
        if lista[index] > lista[index+1]:
            lista[index], lista[index+1] = lista[index+1], lista[index]

print(lista)


i = len(lista)
while i >= 1:
    csere = -1
    for index in range(0,i-1):
        if lista[index] > lista[index+1]:
            lista[index], lista[index+1] = lista[index+1], lista[index]
            csere = index
    i = csere

print(lista)