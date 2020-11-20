numar=int(input("Dati o valoare: "))
suma1=suma2=suma3=suma4=0
if(numar>=0):
    for i in range(1,numar+1):
        suma1+=i**3
        suma2+=i
        suma3+=i**2
        suma4+=i

    suma2=suma2**2
    if(suma1>suma2):
        print("Suma 1 este mai mare ca suma 2")
    elif(suma1==suma2):
        print("Sumele sunt egale")
    else:
        print("Suma 2 mai mare ca suma 1")
    suma3=3*suma3
    suma4=numar**3+numar**2+suma4
    if(suma3>suma4):
        print("Suma 3 este mai mare ca suma 4")
    elif(suma3==suma4):
        print("Sumele sunt egale")
    else:
        print("Suma 4 este mai mare ca suma 3")
else:
    print("Ati introdus datele gresit")