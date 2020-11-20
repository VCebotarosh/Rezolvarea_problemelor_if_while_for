zile=int(input("Dati numarul de zile a unei luni: "))
if((zile>=28)and(zile<=31)):
    if(zile==28):
        print("februarie")
    elif(zile==29):
        print("februarie in timpului anului bisect")
    elif(zile==30):
        print("aprilie,iunie,septembrie,noiembrie")
    elif(zile==31):
        print("ianuarie,martie,mai,iulie,august,octombrie,decembrie")
else:
    print("Ati introdus datele gresit.")