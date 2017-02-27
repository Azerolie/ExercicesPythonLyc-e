def exercice1():
    """
    Écrire un programme permettant de trouver une équation cartésienne d’une droite à
partir de deux point fournis par l’utilisateur.
    D : ax + by + c = 0
    """
    print("Donner les coordonnées des points")
    xA = int(input("Point A : x = ? "))
    yA = int(input("Point A : y = ? "))
    xB = int(input("Point B : x = ? "))
    yB = int(input("Point B : y = ? "))
    
    #Vecteur directeur :
    xAB = xB - xA
    yAB = yB - yA
    
    #Coefficients droites :
    a = yAB
    b = -xAB
    c = -a*xA -b*yA
    
    #Equation droite :
    print("L'équation de la droite reliant A et B est :")
    print("D: {0}x+{1}y+{2} = 0".format(a,b,c))
    
def exercice2():
    """
    Écrire un programme qui donne le tableau de valeur d’une fonction du second degré entre
deux bornes entières.
    """
    print("Donner les coefficients a,b et c tels que f(x) = ax²+bx+c.")
    a = int(input("a ? "))
    #Facultatif : if a==0 : return "Choix non conforme"
    b = int(input("b ? "))
    c = int(input("c ? "))
    
    print("Donner les bornes B1 et B2 entre lesquelles les valeurs de f seront calculées")
    B1 = int(input("B1 ? "))
    B2 = int(input("B2 ? "))
    #Facultatif : if B2<B1 : return "Choix non conforme"
    
    #Affichage :
    print("x \t f(x)")
    while B1<=B2 :
        image = a*B1*B1 + b*B1 + c
        print("{0} \t {1}".format(B1,image))
        B1 = B1 + 1

def exercice3():
    """
    Écrire un programme qui détermine l’ensemble des points de coordonnées entières d’une
droite compris entre deux bornes entières.
    """
    print("Donner les coefficients a,b et c tels que D : ax+by+c=0.")  
    a = int(input("a ? "))
    b = int(input("b ? "))
    #Facultatif : if a==0 and b==0 : return "Choix non conforme"
    c = int(input("c ? "))     
    
    print("Donner les bornes B1 et B2 entre lesquelles les coordonnées seront recherchées")
    B1 = int(input("B1 ? "))
    B2 = int(input("B2 ? "))
    #Facultatif : if B2<B1 : return "Choix non conforme"
    
    #Recherche des coordonnées :
    while B1<=B2 :
        x = B1
        y = (-a*x-c)/b
        if y == int(y) :
            print("({0};{1})".format(x,int(y)))
        B1 = B1 + 1
        
def exercice4():
    """
    Écrire un programme qui détermine la nature d’un triangle à partir de 3 points.
    """
    print("Donner les coordonnées des points du triangle ABC")
    xA = int(input("Point A : x = ? "))
    yA = int(input("Point A : y = ? "))
    xB = int(input("Point B : x = ? "))
    yB = int(input("Point B : y = ? "))
    xC = int(input("Point C : x = ? "))
    yC = int(input("Point C : y = ? "))
    
    #Calcule des longueurs des côtés :
    AB2 = (xA-xB)**2 + (yA-yB)**2
    AC2 = (xA-xC)**2 + (yA-yC)**2
    CB2 = (xC-xB)**2 + (yC-yB)**2
    
    #Recherche de la nature du triangle :
    if AB2 == AC2 or AB2 == CB2 or AC2 == CB2 :
        if AB2 == AC2 and AB2 == CB2 :
            print ("Le triangle ABC est équilatéral")
        else :
            print ("Le triangle est isocèle")
    else : 
        print("Les trois côtés sont différents")
    
    if AB2==AC2+CB2 or AC2==AB2+CB2 or CB2==AB2+AC2:
        print("D'après la réciproque du théorème de Pythagore, le triangle est rectangle.")
        
def exercice5():
    """
    Écrire un programme qui détermine la nature d’un quadrilatère à partir de 4 points.
    """
    print("Donner les coordonnées des points du quadrilatère ABCD")
    xA = int(input("Point A : x = ? "))
    yA = int(input("Point A : y = ? "))
    xB = int(input("Point B : x = ? "))
    yB = int(input("Point B : y = ? "))
    xC = int(input("Point C : x = ? "))
    yC = int(input("Point C : y = ? "))
    xD = int(input("Point D : x = ? "))
    yD = int(input("Point D : y = ? "))
    
    #Calcule des milieux des diagonales :
    xmAC = (xA+xC)/2
    ymAC = (yA+yC)/2
    xmBD = (xB+xD)/2
    ymBD = (yB+yD)/2
    
    if xmAC==xmDB and ymAC == ymBD :
        
        #Calcul de la longueur des côtés :
        AB2 = (xA-xB)**2 + (yA-yB)**2
        BC2 = (xC-xB)**2 + (yC-yB)**2
        CD2 = (xC-xD)**2 + (yC-yD)**2
        AD2 = (xA-xD)**2 + (yA-yD)**2
        
        if AB2 == CD2 and BC2 == AD2 :           
            if AB2 == BC2 :
                if AC2 == AB2+BC2:
                    print("Le quadrilatère ABCD est un carré")
                else :
                    print("Le quadrilatère ABCD est un losange")
            else :
                print("Le quadrilatère ABCD est un rectangle")
        else :
            print ("Le quadrilatère ABCD est un parallélogramme")    
           
        
    else : 
        print("Le quadrilatère ABCD est quelconque")    
    

def exercice8():
    """
    Écrire un programme qui permet de faire une course avec l’ordinateur.
    """
    import random
    class JeuPiste():
        def __init__(self):
            self.j = ["O","J"]
            random.shuffle(self.j)
            self.xo = 0
            self.xj = 0
            self.nb_cases = 10
            self.d = [-3,-2,-1,1,2,3]
            
        def affichage_piste(self):
            case_l = "+---"
            case_h = "|   "
            case_ho = "| O "
            case_hj = "| J "
            piste_l = case_l * self.nb_cases + case_l[0]
            piste_ho = [case_h] * self.nb_cases + [case_h[0]]
            piste_ho[self.xo]=case_ho
            piste_hj = [case_h] * self.nb_cases + [case_h[0]]
            piste_hj[self.xj]=case_hj
            
            print("{0}\n{1}\n{2}\n{0}\n".format(piste_l,"".join(piste_ho),"".join(piste_hj)))
        
        def lancer_de(self):
            return random.choice(self.d)
         
        def position(self,pos):
            if pos < 0 : return 0
            elif pos > self.nb_cases-1 : return self.nb_cases-1
            else : return pos 
                
        def manche(self,j) :
            print("--- Tour {} ---".format(j))
            if j == "J" :
                input("> A vous de lancer le dé (press enter) ")
                d = self.lancer_de()
                print("> RESULTAT : ",d)
                self.xj = self.position(self.xj + d)
            else :
                input("> Je peux lancer le dé ? (press enter) ")
                d = self.lancer_de()  
                print("> RESULTAT : ",d)
                self.xo = self.position(self.xo + d)
        
        def partie(self):
            if self.xo == self.nb_cases-1 :
                print("> J'ai gagné !")
                return False
            elif self.xj == self.nb_cases-1 :  
                print("> Vous m'avez vaincu !")
                return False
            else :
                return True   
                  
        def jeu(self):
            sep = "-"
            h = "Bienvenue dans un jeu de l'oie"
            b = "BUT : Etre le premier arrivé sur la dernière case."
            r = "REGLE : Lancer un dé de mouvement chacun son tour.\n\tO = Ordinateur\n\tJ = Joueur"
            
            print("+{0}+\n| {1} |\n+{0}+\n- {2}\n- {3}\n".format(sep*(len(h)+2),h,b,r))
            
            self.affichage_piste()
            i = 0
            
            while self.partie() :
                j = self.j[i%2]
                self.manche(j)
                self.affichage_piste()
                i += 1
                
    JP=JeuPiste()
    JP.jeu()
    
def exercice9():
    """
    Écrire un programme qui permet à l’utilisateur de jouer au pendu.
    """
    import random
    import numpy as np
    
    class Pendu():
        def __init__(self):
            self.mots=["lapin","voiture","voyage","elephant","montagne","bonnet","bibliotheque",
            "abracadabra","randonnee","plage","paysage","fusee","ordinateur","melancolie","decouverte",
            "changement","construction","potager","pyramide","zebre","clown","zigzag"]
            
            self.mot = random.choice(self.mots)
            self.cache = ["_"]*len(self.mot)
            self.propositions = []
            self.erreurs = 0
            self.max = 10
            
        def affichage(self):
            print("\t{}\n".format(" ".join(self.cache)))
            print("Erreurs {}/{}".format(self.erreurs,self.max))
            if self.propositions : print("Propositions : {}".format(", ".join(self.propositions)))
        
        def manche(self):
        
            l = input("> Proposition : ").lower()
            
            if l in self.propositions :
                print("> Vous perdez un essai pour rien, cette lettre a déjà été proposée")
                self.erreurs +=1
            elif l.isalpha() :
                self.propositions.append(l)
                if len(l) > 1 :      
                    if l==self.mot :
                        self.cache = list(l)
                    else :
                        print("> Ce n'est pas le bon mot")
                        self.erreurs +=1
            
                elif len(l) == 1 :      
                    if l in self.mot : 
                        print("> Cette lettre est bien dans le mot")
                        self.maj_mot_cache(l)   
                    else :
                        print("> Cette lettre n'est pas dans le mot")
                        self.erreurs +=1
            else :
                print("> Concentrez-vous un peu")
                    
        def maj_mot_cache(self,l):
            self.cache = [l if self.mot[x]==l else self.cache[x] for x in range(len(self.mot))]
        
        def partie(self):
        
            if "".join(self.cache) == self.mot :
                print("> Bravo ! Vous avez trouvé le mot caché.")
                return False
            elif self.erreurs >= self.max :
                print("> Pendu ! Le mot était : ", self.mot)
                return False
            return True 
               
        def jeu(self):
            sep = "-"
            h = "Bienvenue dans un jeu de pendu"
            b = "BUT : Trouver le mot caché en moins de 10 erreurs."
            r = "REGLE : Proposer une lettre à chaque tour."
            
            print("+{0}+\n| {1} |\n+{0}+\n- {2}\n- {3}\n".format(sep*(len(h)+2),h,b,r))
            
            self.affichage()
            
            while self.partie() :
                self.manche()
                self.affichage()
      
    P = Pendu()     
    P.jeu() 
exercice8()  
