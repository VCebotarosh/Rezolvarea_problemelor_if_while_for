numar=int(input("Dati un numar: "))
for i in range(1,numar):
    suma=0
    for j in range(1, i):
        if(i%j==0):
            suma+=j
    if (suma==i):
        print(i)
