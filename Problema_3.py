import math

numar1=int(input("Dati primul numar: "))
numar2=int(input("Dati al doilea numar: "))
if(numar1<numar2):
    var_auxiliara1=math.log(numar2,numar1)
    var_auxiliara2=round(var_auxiliara1)
    if(numar1**var_auxiliara2==numar2):
        print("da")
    else:
        print("nu")
else:
    print("Datele nu satisfac conditiile problemei")