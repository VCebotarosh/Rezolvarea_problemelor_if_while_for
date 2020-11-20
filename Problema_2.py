numar=int(input("Dati un numar: "))
suma=0
produs=1
if(numar>1):
    for i in range(1,numar+1):
        produs*=i
        suma+=produs
    print("suma este egala cu",suma)
else:
    print("Ati introdus gresit datele.")