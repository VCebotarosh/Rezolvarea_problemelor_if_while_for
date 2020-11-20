varsta=int(input("Introduceti valoare varstei lui Mihai: "))
an=0
bani1=1
bani2=1
j=1
if(varsta<20):
    for i in range(1,varsta+1):
            bani1=2*bani1+i

    while(bani2<100):
        bani2=2*bani2+j
        an+=1
        j+=1             
    print("Mihai a primit",bani1,"bani la varsta de",i)
    print("Cadoul lui Mihai nu va depasi 100 bani la varsta",an)
else:
    print("Varsta data nu satisface conditiile problemei")