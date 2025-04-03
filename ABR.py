class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droite = None

class ABR:
    def __init__(self):
        self.racine = None

    def ajouter(self, valeur):
        """Ajoute un élément dans l'ABR"""
        if self.racine is None:
            self.racine = Noeud(valeur)
        else:
            self._ajouter_recursive(self.racine, valeur)
 
   def _ajouter_recursive(self, noeud, valeur):
        if valeur < noeud.valeur:
            if noeud.gauche is None:
                noeud.gauche = Noeud(valeur)
            else:
                self._ajouter_recursive(noeud.gauche, valeur)
        else:
            if noeud.droite is None:
                noeud.droite = Noeud(valeur)
            else:
                self._ajouter_recursive(noeud.droite, valeur)

    def afficher_esthetique(self):
        """Affiche l'ABR de manière esthétique"""
        self._afficher_recursive(self.racine, "", True)

    def _afficher_recursive(self, noeud, indent, last):
        if noeud is not None:
            print(indent, "`- " if last else "|- ", noeud.valeur, sep="")
            indent += "   " if last else "|  "
            self._afficher_recursive(noeud.gauche, indent, False)
            self._afficher_recursive(noeud.droite, indent, True)

    def hauteur(self):
        """Renvoie la hauteur de l'arbre"""
        return self._hauteur_recursive(self.racine)

    def _hauteur_recursive(self, noeud):
        if noeud is None:
            return 0
        return 1 + max(self._hauteur_recursive(noeud.gauche), self._hauteur_recursive(noeud.droite))

    def afficher(self):
        """Affiche l'ABR de manière centrée avec les sous-arbres gauche et droit."""
        if not self.racine:
            print("Arbre vide")
            return

        # Calculer la hauteur de l'arbre pour connaître la profondeur maximale
        hauteur_arbre = self.hauteur()

        # Appel à la méthode récursive pour afficher chaque niveau
        self._afficher_niveau([self.racine], hauteur_arbre, 0)

    def _afficher_niveau(self, noeuds, hauteur_totale, niveau_actuel):
        """Affiche chaque niveau de l'arbre."""
        if not noeuds or all(noeud is None for noeud in noeuds):
            return

        espacement = 2**(hauteur_totale - niveau_actuel - 1)  # Calcul de l'espacement entre les nœuds
        nouvelle_ligne = ""
        prochaine_ligne = []

        for noeud in noeuds:
            if noeud is None:
                nouvelle_ligne += " " * espacement * 2
                prochaine_ligne.extend([None, None])
            else:
                nouvelle_ligne += f"{noeud.valeur}".center(espacement * 2)
                prochaine_ligne.extend([noeud.gauche, noeud.droite])

        print(nouvelle_ligne)
        self._afficher_niveau(prochaine_ligne, hauteur_totale, niveau_actuel + 1)

    def appartient(self, valeur):
        """Teste si un élément appartient à l'ABR"""
        return self._appartient_recursive(self.racine, valeur)

    def _appartient_recursive(self, noeud, valeur):
        if noeud is None:
            return False
        if noeud.valeur == valeur:
            return True
        elif valeur < noeud.valeur:
            return self._appartient_recursive(noeud.gauche, valeur)
        else:
            return self._appartient_recursive(noeud.droite, valeur)

    def taille(self):
        """Renvoie la taille de l'arbre (nombre de noeuds)"""
        return self._taille_recursive(self.racine)

    def _taille_recursive(self, noeud):
        if noeud is None:
            return 0
        return 1 + self._taille_recursive(noeud.gauche) + self._taille_recursive(noeud.droite)

    def infixe(self):
        """Renvoie le parcours infixe de l'arbre"""
        elements = []
        self._infixe_recursive(self.racine, elements)
        return elements

    def _infixe_recursive(self, noeud, elements):
        if noeud is not None:
            self._infixe_recursive(noeud.gauche, elements)
            elements.append(noeud.valeur)
            self._infixe_recursive(noeud.droite, elements)

    def lister(self):
        """Renvoie un tableau contenant les éléments de l'ABR dans l'ordre croissant"""
        return self.infixe()

    def supprimer(self, valeur):
        """Supprime un élément de l'ABR"""
        self.racine = self._supprimer_recursive(self.racine, valeur)

    def _supprimer_recursive(self, noeud, valeur):
        if noeud is None:
            return noeud

        if valeur < noeud.valeur:
            noeud.gauche = self._supprimer_recursive(noeud.gauche, valeur)
        elif valeur > noeud.valeur:
            noeud.droite = self._supprimer_recursive(noeud.droite, valeur)
        else:
            # Cas où le noeud a un ou aucun enfant
            if noeud.gauche is None:
                return noeud.droite
            elif noeud.droite is None:
                return noeud.gauche

            # Cas où le noeud a deux enfants
            noeud.valeur = self._min_valeur(noeud.droite)
            noeud.droite = self._supprimer_recursive(noeud.droite, noeud.valeur)

        return noeud

    def _min_valeur(self, noeud):
        """Renvoie la plus petite valeur à partir du noeud"""
        current = noeud
        while current.gauche is not None:
            current = current.gauche
        return current.valeur

# Exemple d'utilisation de la classe ABR
if __name__ == "__main__":
    abr = ABR()
    abr.ajouter(50)
    abr.ajouter(30)
    abr.ajouter(70)
    abr.ajouter(20)
    abr.ajouter(40)
    abr.ajouter(60)
    abr.ajouter(80)
    abr.ajouter(530)
    abr.ajouter(330)
    abr.ajouter(570)
    abr.ajouter(520)
    abr.ajouter(640)
    abr.ajouter(460)
    abr.ajouter(840)

    print("Appartient à l'ABR:", abr.appartient(40))  # True
    print("Taille de l'ABR:", abr.taille())           # 7
    print("Hauteur de l'ABR:", abr.hauteur())         # 3
    print("Parcours infixe:", abr.infixe())           # [20, 30, 40, 50, 60, 70, 80]

    print("Affichage esthétique de l'ABR :")
    #abr.afficher_esthetique()
    abr.afficher()

    abr.supprimer(70)
    print("Parcours infixe après suppression de 70:", abr.infixe())  # [20, 30, 40, 50, 60, 80]

    print("Affichage esthétique de l'ABR :")
    #abr.afficher_esthetique()
    abr.afficher()
