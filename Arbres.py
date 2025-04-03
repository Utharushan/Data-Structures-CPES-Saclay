class Noeud :
    def __init__(self,g,v,d):
        self.gauche = g
        self.valeur = v
        self.droite = d

    def taille(self):
        if self.gauche != None and self.droite != None:
            return 1 + self.gauche.taille() + self.droite.taille()
        if self.gauche != None:
            return 1 + self.gauche.taille()
        elif self.droite != None:
            return 1 + self.droite.taille()
        if self.valeur != None:
            return 1
        else:
            return 0

    def hauteur(self):
        if self.gauche != None and self.droite != None:
            return 1 + max(self.gauche.hauteur(), self.droite.hauteur())
        if self.gauche != None:
            return 1 + self.gauche.hauteur()
        elif self.droite != None:
            return 1 + self.droite.hauteur()
        if self.valeur != None:
            return 1
        else:
            return 0

    def infixe(self):
        if self.gauche is not None:
            self.gauche.infixe()
        print(self.valeur, end=" ")
        if self.droite is not None:
            self.droite.infixe()

    def prefixe(self):
        print(self.valeur, end = " ")
        if self.gauche is not None:
            self.gauche.prefixe()
        if self.droite is not None:
            self.droite.prefixe()

    def suffixe(self):
        if self.gauche is not None:
            self.gauche.suffixe()
        if self.droite is not None:
            self.droite.suffixe()
        print(self.valeur, end = " ")

    def affiche(self):
        print("(", end = '')
        if self.gauche is not None:
            self.gauche.affiche()
        print(self.valeur, end = '')
        if self.droite is not None:
            self.droite.affiche()        
        print(")", end = '')

def parfait(h):
    if h <= 0:
        return None

    gauche = parfait(h - 1)
    droite = parfait(h - 1)

    return Noeud(gauche, 1, droite)

def peigneG(h):
    if h <= 0:
        return None

    gauche = peigneG(h-1)

    return Noeud(gauche, 1, None)
        

a = Noeud(Noeud(None, "B", Noeud(None, "C", None)), "A", Noeud(None, "D", None))
b = Noeud(Noeud(Noeud(None, "D", None), "B", Noeud(None, "E", None)),
          "A", Noeud(Noeud(None, "F", None), "C", Noeud(None, "G", None)))
c = None
d = Noeud(None, "5", None)
e = Noeud(Noeud(Noeud(None, "D", None), "B", Noeud(None, "E", None)),
          "A", Noeud(Noeud(None, "F", None), "C", Noeud(None, "G", a)))

exo10 = Noeud(None, "1", Noeud(Noeud(None, "2", None), "3", None))

abrParfait = parfait(0)
peigne = peigneG(9)

def nbNoeudsProf(A, k):
    if A is None:
        return 0
    elif k == 1:
        return 1
    else:
        return nbNoeudsProf(A.gauche, k - 1) + nbNoeudsProf(A.droite, k - 1)

#print(nbNoeudsProf(e, 3))

def estFeuille(A):
    if A.gauche == None and A.droite == None:
        return True
    return False

def nbFeuillesProf(A, k):
    if A is None:
        return 0
    elif k == 1 and estFeuille(A):
        return 1
    else:
        return nbFeuillesProf(A.gauche, k - 1) + nbFeuillesProf(A.droite, k - 1)

#print(nbFeuillesProf(b, 3))

def egalite(A, B):
    if A is None and B is None:
        return True
    if A.gauche is None and B.gauche is not None:
        return False
    if B.gauche is None and A.gauche is not None:
        return False
    if A.droite is None and B.droite is not None:
        return False
    if B.droite is None and A.droite is not None:
        return False
    return egalite(A.gauche, B.gauche) and egalite(A.droite, B.droite) and A.valeur == B.valeur
    

#print(egalite(e, e))

def miroir(A):
    if A is None:
        return None
    if A.gauche is None and A.droite is None:
        return Noeud(None, A.valeur, None)
    if A.gauche is None:
        return None
    if A.droite is None:
        return None
    return Noeud(A.droite, A.valeur, A.gauche)

abr_miroir = e
##abr_miroir.affiche()
##print()
##miroir(abr_miroir).affiche()
##print()
##miroir(miroir(abr_miroir)).affiche()

def estMiroir(A, B):
    return egalite(miroir(A), B)

#print(estMiroir(e, miroir(e)))

def identiteMiroir(A):
    return egalite(A, miroir(miroir(A)))

#print(identiteMiroir(d))

AE = Noeud(
    Noeud(
        Noeud(None, 3, None), '*',
                 Noeud(Noeud(None, 5, None), '+', Noeud(None, 1, None))),
                       '+',
    Noeud(Noeud(Noeud(None, 6, None), '-', Noeud(None, 2, None))
                       , '/', Noeud(None, 4, None)))

#AE.affiche()

def evalExpression(AE):
    if AE is None:
        return 0
    if type(AE.valeur) == int:
        return AE.valeur
    elif AE.gauche is None and AE.droite is not None:
        return AE.droite
    elif AE.gauche is not None and AE.droite is None:
        return AE.gauche
    if AE.valeur == '+':
        return evalExpression(AE.gauche) + evalExpression(AE.droite)
    if AE.valeur == '-':
        return evalExpression(AE.gauche) - evalExpression(AE.droite)
    if AE.valeur == '*':
        return evalExpression(AE.gauche) * evalExpression(AE.droite)
    if AE.valeur == '/':
        if evalExpression(AE.droite) == 0:
            raise ZeroDivisionError
        else:
            return evalExpression(AE.gauche) / evalExpression(AE.droite)
        
#print(evalExpression(AE))
"""
def evalIterExpression(E):
    i = 0
    res = 0
    signe = []
    nombre = []
    while i < len(E):
        if E[i] == ' ':
            i += 1
        elif E[i] == '(':
            signe.append(E[i + 1])
            i += 2
        elif E[i] == ')' and len(nombre) > 1:
            val = 0
            nb2 = nombre.pop()
            nb1 = nombre.pop()
            op = signe.pop()
            if op == '+':
                val = nb1 + nb2
            elif op == '-':
                val = nb1 - nb2
            elif op == '*':
                val = nb1 * nb2
            elif op == '/':
                if nb2 == 0:
                    raise ZeroDivisionError
                else:
                    val = nb1 / nb2
            res += val
            nombre.append(val)
        else:
            tmp = ''
            while E[i] not in [' ', ')']:
                tmp += E[i]
                i += 1
            nombre.append(int(tmp))
E = "(+ (* 3 (+ 5 1)) (/ (- 6 2) 4))"      
print(evalIterExpression(E))
"""

def strahler(A):
    if A is None:
        return 0
    if strahler(A.gauche) == strahler(A.droite):
        return strahler(A.gauche) + 1
    else:
        return max(strahler(A.gauche), strahler(A.droite))

#print(strahler(AE))

ABR = Noeud(Noeud(Noeud(None, 1, None), 2, Noeud(None, 3, None)),
          4, Noeud(Noeud(None, 5, None), 6, Noeud(None, 7, None)))

def minimum(a):
    if a is None:
        return None
    elif a.gauche is None:
        return a.valeur
    else:
        return minimum(a.gauche)

#print(minimum(ABR))

def appartient(x, a):
    if a is None:
        return False
    elif x == a.valeur:
        return True
    elif x < a.valeur and a.gauche is not None:
        return appartient(x, a.gauche)
    elif x > a.valeur and a.droite is not None:
        return appartient(x, a.droite)
    return False

#print(appartient(7, c))

def compte(x, a):
    if a is None:
        return 0
    elif x == a.valeur:
        return 1 + compte(x, a.gauche)
    elif x < a.valeur and a.gauche is not None:
        return compte(x, a.gauche)
    elif x > a.valeur and a.droite is not None:
        return compte(x, a.droite)
    return 0

#print(compte(4, c))

def ajouteNaif(x, a):
    if a is None:
        a = Noeud(None, x, None)
    elif x < a.valeur:
        if a.gauche is None:
            a.gauche = Noeud(None, x, None)
        else:
            ajouteNaif(x, a.gauche)
    elif x > a.valeur:
        if a.droite is None:
            a.droite = Noeud(None, x, None)
        else:
            ajouteNaif(x, a.droite)

##print(ajouteNaif(8, ABR))
##ABR.affiche()
        
def ajoute(x, a):
    if a is None:
        return Noeud(None, x, None)
    if x < a.valeur:
        return Noeud(ajoute(x, a.gauche), a.valeur, a.droite)
    else:
        return Noeud(a.gauche, a.valeur, ajoute(x, a.droite))

exo7 = Noeud(Noeud(None, 1, None), 3, Noeud(None, 4, None))
exo7 = ajoute(2, exo7)
##exo7.affiche()
##print()
exo7rep = ajoute(3, c)
exo7rep = ajoute(1, exo7rep)
exo7rep = ajoute(4, exo7rep)
exo7rep = ajoute(2, exo7rep)
##exo7rep.affiche()

exo8 = ajoute(3, exo7)
#exo8.affiche()

def ajoute(x, a):
    if a is None:
        return Noeud(None, x, None)
    if x <= a.valeur:
        return Noeud(ajoute(x, a.gauche), a.valeur, a.droite)
    else:
        return Noeud(a.gauche, a.valeur, ajoute(x, a.droite))

exo8 = ajoute(3, exo7)
##exo8.affiche()

def ajouteSansDoublon(x, a):
    if compte(x, a) > 0:
        return a
    else:
        return ajoute(x, a)

def remplir(a, t):
    if a.gauche is not None:
        remplir(a.gauche, t)
    t.append(a.valeur)
    if a.droite is not None:
        remplir(a.droite, t)
    return t

##t = remplir(ABR, [])
##print(t)

def trier(t):
    a = None
    for i in range(len(t)):
        a = ajoute(t.pop(), a)
    t = remplir(a, t)
    return t

#print(trier([6, 4, 8, 3, 5, 1, 2]))
    
    
