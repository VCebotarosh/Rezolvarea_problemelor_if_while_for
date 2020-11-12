latura1,latura2,latura3=eval(input("Dati lungimile a 3 laturi ale triunghilui:"))
if((latura1>0)and(latura2>0)and(latura3>0)):
    if((latura1+latura2>latura3)and(latura2+latura3>latura1)and(latura1+latura3>latura2)):
        if(((latura1==latura2)and(latura1!=latura3))or((latura1==latura3)and(latura1!=latura2))or((latura2==latura3)and(latura2!=latura1))):
            print("Exista un triunghi isoscel cu laturile",latura1,"",latura2,"",latura3)
        elif((latura1!=latura2)and(latura2!=latura3)):
            print("Exista un triunghi scalen cu laturile",latura1,"",latura2,"",latura3)
        elif(latura1==latura2)and(latura1==latura3):
            print("Exista un triunghi echilateral cu laturile",latura1,"",latura2,"",latura3)
    else:
        print("Nu exista asa un triunghi cu laturile",latura1,"",latura2,"",latura3)
else:
    print("Ati introdus datele gresit.")        