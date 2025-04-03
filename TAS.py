class TAS:
    def __init__(self):
        raise NotImplementedError

class Vide(TAS):
    def __init__(self):
        pass

    def afficher(self, hauteur = 1, rep = ""):
       rep = hauteur * "  " + "|-->x\n"
       return rep

    def fusion(self, autre):
        return autre
    
    def minimum(self):
        return None

    def appartient(self, v):
        return False
    
    def taille(self):
        return 0

    def hauteur(self):
        return 0

    def ajouter(self, v):
        return Noeud(Vide(), v, Vide())
    
    def supprimer(self):
        return Vide()

class Noeud(TAS):
    def __init__(self, gauche, valeur, droite):
        self.gauche = gauche
        self.valeur = valeur
        self.droite = droite

    def afficher(self, hauteur = 1, rep = ""):
        rep = hauteur * "  " + "|-->" + str(self.valeur) + "," + str(hauteur) + "\n"
        repgauche = (self.gauche).afficher(hauteur + 1, rep)
        rep += repgauche
        repdroite = (self.droite).afficher(hauteur + 1, rep)
        rep += repdroite
        return rep

    def fusion(self, autre):
        if isinstance(autre, Vide):
            return self
        if self.valeur < autre.valeur:
            nouveau_noeud = Noeud(self.gauche, self.valeur, self.droite.fusion(autre))
            if nouveau_noeud.gauche.hauteur() < nouveau_noeud.droite.hauteur():
                nouveau_noeud.gauche, nouveau_noeud.droite = nouveau_noeud.droite, nouveau_noeud.gauche
            return nouveau_noeud
        else:
            return autre.fusion(self)

    def minimum(self):
        return self.valeur

    def appartient(self, x):
        if self.valeur == x:
            return True
        else:
            return self.gauche.appartient(x) or self.droite.appartient(x)

    def taille(self):
        return 1 + self.gauche.taille() + self.droite.taille()

    def hauteur(self):
        """Calcule la hauteur en tenant compte des sous-arbres gauche et droit"""
        if isinstance(self.gauche, Vide) and isinstance(self.droite, Vide):
            return 1
        elif isinstance(self.gauche, Vide):
            return 1 + self.droite.hauteur()
        elif isinstance(self.droite, Vide):
            return 1 + self.gauche.hauteur()
        else:
            return 1 + max(self.gauche.hauteur(), self.droite.hauteur())

    def ajouter(self, x):
        nouveau_noeud = Noeud(Vide(), x, Vide())
        return self.fusion(nouveau_noeud)

    def supprimer(self):
        return self.gauche.fusion(self.droite)


if __name__ == "__main__":
    tas = Vide()
    tas = tas.ajouter(20)
    tas = tas.ajouter(10)
    tas = tas.ajouter(5)

    assert tas.taille() == 3, "Erreur: la taille du tas devrait être 3"
    assert tas.minimum() == 5, "Erreur: le minimum devrait être 5"
    assert tas.appartient(10) == True, "Erreur: 10 devrait être dans le tas"
    assert tas.appartient(30) == False, "Erreur: 30 ne devrait pas être dans le tas"
    assert tas.hauteur() == 3, "Erreur: la hauteur du tas devrait être 3"
    
    tas = tas.supprimer()  # Suppression du minimum (5)
    assert tas.taille() == 2, "Erreur: la taille du tas après suppression devrait être 2"
    assert tas.minimum() == 10, "Erreur: le minimum après suppression devrait être 10"

    tas1 = Vide().ajouter(10).ajouter(20).ajouter(5)
    tas2 = Vide().ajouter(15).ajouter(25)
    tas_fusion = tas1.fusion(tas2)
    assert tas_fusion.taille() == 5, "Erreur: la taille après fusion devrait être 5"
    assert tas_fusion.minimum() == 5, "Erreur: le minimum après fusion devrait être 5"
    assert tas.appartient(10) == True, "Erreur: 10 devrait être dans le tas"
    assert tas.appartient(15) == False, "Erreur: 15 ne devrait pas être dans le tas"

    tas = Vide().ajouter(10).ajouter(20).ajouter(5)

    assert tas.appartient(10) == True, "Erreur: 10 devrait être dans le tas"
    assert tas.appartient(15) == False, "Erreur: 15 ne devrait pas être dans le tas"

    tas = Vide()

    assert tas.taille() == 0, "Erreur: la taille du tas vide devrait être 0"
    assert tas.hauteur() == 0, "Erreur: la hauteur du tas vide devrait être 0"
    assert tas.minimum() == None, "Erreur: le minimum d'un tas vide devrait être None"
    assert tas.supprimer().taille() == 0, "Erreur: supprimer dans un tas vide ne doit pas changer la taille"
    assert tas.appartient(10) == False, "Erreur: aucun élément ne devrait appartenir à un tas vide"

    tas = Vide().ajouter(10).ajouter(20).ajouter(5)
    print(tas.afficher())

    tas1 = Vide().ajouter(10).ajouter(20).ajouter(5)
    tas_vide = Vide()

    tas_fusion = tas1.fusion(tas_vide)
    assert tas_fusion.taille() == 3, "Erreur: la taille après fusion avec un tas vide devrait être 3"
    assert tas_fusion.minimum() == 5, "Erreur: le minimum après fusion avec un tas vide devrait être 5"
