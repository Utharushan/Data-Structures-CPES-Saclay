class GrapheM:
    """
    Classe pour représenter un graphe orienté sous forme de matrice d'adjacence.
    """
    def __init__(self, n):
        """
        Initialise un graphe avec n sommets sans arcs.
        :param n: Nombre de sommets.
        """
        self.n = n
        self.adj = [[False for _ in range(n)] for _ in range(n)]

    def ajouter_arc(self, s1, s2):
        """
        Ajoute un arc orienté de s1 à s2.
        :param s1: Sommet source.
        :param s2: Sommet destination.
        """
        if 0 <= s1 < self.n and 0 <= s2 < self.n:
            self.adj[s1][s2] = True
        else:
            raise ValueError("Les sommets s1 et s2 doivent être compris entre 0 et n-1.")

    def arc(self, s1, s2):
        """
        Vérifie si un arc existe entre s1 et s2.
        :param s1: Sommet source.
        :param s2: Sommet destination.
        :return: True si l'arc existe, False sinon.
        """
        if 0 <= s1 < self.n and 0 <= s2 < self.n:
            return self.adj[s1][s2]
        else:
            raise ValueError("Les sommets s1 et s2 doivent être compris entre 0 et n-1.")

    def voisins(self, s):
        """
        Renvoie une liste des sommets voisins du sommet s.
        :param s: Sommet pour lequel on cherche les voisins.
        :return: Liste des sommets voisins.
        """
        if 0 <= s < self.n:
            return [j for j in range(self.n) if self.adj[s][j]]
        else:
            raise ValueError("Le sommet s doit être compris entre 0 et n-1.")

    def afficher(self):
        for i in range(self.n):
            voisins = self.voisins(i)
            print("{i} -> ", end = '')
            for j in range(len(voisins)):
                print(voisins[j], end = ' ')
            print()

    def degre(s):
        return len(self.voisins(s))

    def nb_arcs():
        res = 0
        for i in range(self.n):
            res += self.degre(i)
        return res

    def supprimer_arc(s1, s2):
        self.adj[s1][s2] = False

def presence_cycle(g):
    """
    Vérifie si un graphe contient un cycle.
    :param g: Graphe représenté sous forme de matrice d'adjacence.
    :return: True si le graphe contient un cycle, False sinon.
    """
    n = len(g.adj)  # Nombre de sommets
    couleur = ["BLANC"] * n  # Initialisation des couleurs

    def parcours_cycle(g, couleur, s):
        """
        Effectue un parcours en profondeur pour détecter un cycle.
        :param g: Graphe sous forme de matrice d'adjacence.
        :param couleur: Tableau des couleurs des sommets.
        :param s: Sommet courant.
        :return: True si un cycle est détecté, False sinon.
        """
        couleur[s] = "GRIS"
        for voisin in range(len(g.adj[s])):
            if g.adj[s][voisin]:  # Si un arc existe
                if couleur[voisin] == "GRIS":  # Cycle détecté
                    return True
                if couleur[voisin] == "BLANC":  # Continuer le parcours
                    if parcours_cycle(g, couleur, voisin):
                        return True
        couleur[s] = "NOIR"
        return False

    for sommet in range(n):
        if couleur[sommet] == "BLANC":
            if parcours_cycle(g, couleur, sommet):
                return True
    return False

print("Test de GrapheM:")

g_m = GrapheM(3)
g_m.ajouter_arc(0, 1)
g_m.ajouter_arc(1, 2)

print("Arc (0,1):", g_m.arc(0, 1))
print("Arc (1,0):", g_m.arc(1, 0))
print("Voisins de 1:", g_m.voisins(1))
print("Voisins de 0:", g_m.voisins(0))

g = GrapheM(4)

g.ajouter_arc(0, 1)
g.ajouter_arc(1, 2)
g.ajouter_arc(2, 0)
g.ajouter_arc(3, 2)

print("Le graphe contient un cycle :", presence_cycle(g))

