class GraphePondereDict:
    """
    Classe pour représenter un graphe pondéré orienté en utilisant un dictionnaire d'adjacence.
    """
    def __init__(self):
        self.adj = {}  # Dictionnaire {sommet: {voisin: poids}}

    def ajouter_sommet(self, s):
        """Ajoute un sommet au graphe."""
        if s not in self.adj:
            self.adj[s] = {}

    def ajouter_arc(self, s1, s2, poids):
        """Ajoute un arc orienté avec un poids entre s1 et s2."""
        if s1 not in self.adj:
            self.ajouter_sommet(s1)
        if s2 not in self.adj:
            self.ajouter_sommet(s2)
        self.adj[s1][s2] = poids

    def supprimer_arc(self, s1, s2):
        """Supprime l'arc de s1 à s2."""
        if s1 in self.adj and s2 in self.adj[s1]:
            del self.adj[s1][s2]

    def voisins(self, s):
        """Renvoie les voisins du sommet s."""
        if s in self.adj:
            return list(self.adj[s].keys())
        else:
            raise ValueError(f"Le sommet {s} n'existe pas.")

    def nb_sommets(self):
        """Renvoie le nombre de sommets."""
        return len(self.adj)

    def degre(self, s):
        """Renvoie le degré du sommet s."""
        if s in self.adj:
            return len(self.adj[s])
        else:
            raise ValueError(f"Le sommet {s} n'existe pas.")

    def nb_arcs(self):
        """Renvoie le nombre d'arcs."""
        return sum(len(voisins) for voisins in self.adj.values())

    def afficher(self):
        """Affiche le graphe sous forme de dictionnaire d'adjacence."""
        for sommet, voisins in self.adj.items():
            print(f"{sommet}: {voisins}")


print("Graphe Pondéré avec Dictionnaire d'Adjacence :")
g_dict = GraphePondereDict()
g_dict.ajouter_arc("A", "B", 5)
g_dict.ajouter_arc("A", "C", 3)
g_dict.ajouter_arc("B", "C", 1)
g_dict.afficher()
print("Nombre de sommets :", g_dict.nb_sommets())
print("Degré du sommet A :", g_dict.degre("A"))
print("Nombre d'arcs :", g_dict.nb_arcs())

print("\nAprès suppression de l'arc (A, C) :")
g_dict.supprimer_arc("A", "C")
g_dict.afficher()
