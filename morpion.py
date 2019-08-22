import random
ran = random.randint(1, 9)

def computer():
    global a, b, c, d, e, f, g, h, i, key, valide, ran, xo, ox, ia, z
    #computer
    key = ""
    for z in range(0, 1):
        if (z == 0):
            ia = ox
        else:
            ia = xo
        if ((b == ia and c == ia and a == " ") or (d == ia and g == ia and a == " ") or (e == ia and i == ia and a == " ")):
            key = "1"
        if ((a == ia and c == ia and b == " ") or (e == ia and h == ia and b == " ")):
            key = "2"
        if ((a == ia and b == ia and c == " ") or (g == ia and e == ia and c == " ") or (f == ia and i == ia and c == " ")):
            key = "3"
        if ((a == ia and g == ia and d == " ") or (e == ia and f == ia and d == " ")):
            key = "4"
        if ((a == ia and i == ia and e == " ") or (d == ia and f == ia and e == " ") or (g == ia and c == ia and e == " ") or (b == ia and h == ia and e == " ")):
            key = "5"
        if ((d == ia and e == ia and f == " ") or (c == ia and i == ia and f == " ")):
            key = "6"
        if ((a == ia and d == ia and g == " ") or (e == ia and c == ia and g == " ") or (h == ia and i == ia and g == " ")):
            key = "7"
        if ((g == ia and i == ia and h == " ") or (b == ia and e == ia and h == " ")):
            key = "8"
        if ((a == ia and e == ia and i == " ") or (g == ia and h == ia and i == " ") or (c == ia and f == ia and i == " ")):
            key = "9"
    if (a == " " and b == " " and c == " " and d == " " and e == " " and f == " " and g == " " and h == " " and i == " "):
        key = str(ran)
    if (key == ""):
        valide = 0
        while (valide == 0):
            ran = random.randint(1, 9)
            if ((ran == 1 and a == " ") or (ran == 2 and b == " ") or (ran == 3 and c == " ") or (ran == 4 and d == " ") or (ran == 5 and e == " ") or (ran == 6 and f == " ") or (ran == 7 and g == " ") or (ran == 8 and h == " ") or (ran == 9 and i == " ")):
                key = str(ran)
                valide = 1
    print("> ", key)
    #return key

def display():
    global a, b, c, d, e, f, g, h, i, key, valide, ran, xo
    print(a,"|",b,"|",c,"   1|2|3") 
    print("- - - - -    - - -")
    print(d,"|",e,"|",f,"   4|5|6") 
    print("- - - - -    - - -")
    print(g,"|",h,"|",i,"   7|8|9") 
    print("")
    
game = 0
print("TTTTT  III   CCC    TTTTT   AA    CCC    TTTTT   OO   TTTTT")
print("T T T   I   C       T T T  A  A  C       T T T  O  O  T T T")
print("  T     I   C    =    T    AAAA  C    =    T    O  O    T  ")
print("  T     I   C         T    A  A  C         T    O  O    T  ")
print(" TTT   III   CCC     TTT   A  A   CCC     TTT    OO    TTT ")
print("")

while (game == 0):
    joueur = input("Nombre de Joueur ? >")
    print("")
    a = b = c = d  = e = f = g = h = i = " "
    xo = "X"
    ox = "O"
    coup = 9

    display()

    while (coup > 0):
        key = "" 
        print("Joueur", xo, "c'est a votre tour.")
        print("")

        if (xo == "X"):
            if (int(joueur) > 0):    
                key = input(">")
            else:
                computer()
        else:
            if (int(joueur) > 1):    
                key = input(">")
            else:
                computer()
                
        if (key == "1"):
            if (a == " "):
                a = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "2"):
            if (b == " "):
                b = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "3"):
            if (c == " "):
                c = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "4"):
            if (d == " "):
                d = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "5"):
            if (e == " "):
                e = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")            
        if (key == "6"):
            if (f == " "):
                f = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "7"):
            if (g == " "):
                g = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "8"):
            if (h == " "):
                h = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")
        if (key == "9"):
            if (i == " "):
                i = xo
                coup = coup - 1
            else:
                print("Ce n'est pas un coup valide.")

        print("")
        display()
        
        if ((a == xo and b == xo and c == xo) or (a == xo and d == xo and g == xo) or (a == xo and e == xo and i == xo) or (g == xo and e == xo and c == xo) or (b == xo and e == xo and h == xo) or (c == xo and f == xo and i == xo) or (d == xo and e == xo and f == xo) or (g == xo and h == xo and i == xo)):
            print(xo, "a Gagné!")
            print("")
            coup = 0
        else:
            if (coup == 0):
                print("Partie Null!")
                print("")
                
        if (coup == 8 or coup == 6 or coup == 4 or coup == 2):
            xo = "O"
            ox = "X"
        else:
            xo = "X"
            ox = "O"

    print("Jouer une partie ?")
    key = input("[oui / non] >")
    if (key.upper() == "NON"):
        print("bye bye")
        exit()
    print("")
