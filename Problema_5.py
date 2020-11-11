an=int(input("Dati anul: "))
if((an>=1000)and(an<10000)):
    if(an%12==0):
        print("Anul Maimutei")
    elif(an%12==1):
        print("Anul Cocosului")
    elif(an%12==2):
        print("Anul Cainelui")
    elif(an%12==3):
        print("Anul Porcului")
    elif(an%12==4):
        print("Anul Sobolanului")
    elif(an%12==5):
        print("Anul Boului")
    elif(an%12==6):
        print("Anul Tigrului")
    elif(an%12==7):
        print("Anul Iepurelui")
    elif(an%12==8):
        print("Anul Dragonului")
    elif(an%12==9):
        print("Anul Sarpelui")
    elif(an%12==10):
        print("Anul Calului")
    elif(an%12==11):
        print("Anul Oii")
else:
    print("Ati introdus gresit datele")
    