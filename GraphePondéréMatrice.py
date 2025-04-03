import heapq

class GraphePondereMatrice:
    """
    Classe pour représenter un graphe pondéré orienté en utilisant une matrice d'adjacence.
    """
    def __init__(self, n):
        self.n = n
        self.adj = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            self.adj[i][i] = 0  # Distance de chaque sommet à lui-même = 0

    def ajouter_arc(self, s1, s2, poids):
        """Ajoute un arc orienté avec un poids entre s1 et s2."""
        if 0 <= s1 < self.n and 0 <= s2 < self.n:
            self.adj[s1][s2] = poids
        else:
            raise ValueError("Indices des sommets hors limites.")

    def supprimer_arc(self, s1, s2):
        """Supprime l'arc de s1 à s2."""
        if 0 <= s1 < self.n and 0 <= s2 < self.n:
            self.adj[s1][s2] = float('inf')
        else:
            raise ValueError("Indices des sommets hors limites.")

    def voisins(self, s):
        """Renvoie les voisins du sommet s."""
        if 0 <= s < self.n:
            return [j for j in range(self.n) if self.adj[s][j] != float('inf') and j != s]
        else:
            raise ValueError("Indice du sommet hors limites.")

    def nb_sommets(self):
        """Renvoie le nombre de sommets."""
        return self.n

    def degre(self, s):
        """Renvoie le degré du sommet s."""
        if 0 <= s < self.n:
            return len(self.voisins(s))
        else:
            raise ValueError("Indice du sommet hors limites.")

    def nb_arcs(self):
        """Renvoie le nombre d'arcs."""
        return sum(1 for i in range(self.n) for j in range(self.n) if self.adj[i][j] != float('inf') and i != j)

    def afficher(self):
        """Affiche la matrice d'adjacence."""
        for row in self.adj:
            print(" ".join(f"{x:.1f}" if x != float('inf') else "inf" for x in row))

def floyd_warshall(g):
    """
    Implémente l'algorithme de Floyd-Warshall pour trouver les distances minimales entre tous les sommets.
    :param g: Graphe pondéré représenté par une matrice d'adjacence.
    :return: Une matrice des distances minimales.
    """
    n = g.nb_sommets()
    dist = [[g.adj[i][j] for j in range(n)] for i in range(n)]  # Initialisation des distances

    # Distance de chaque sommet à lui-même est de 0
    for i in range(n):
        dist[i][i] = 0

    # Boucles de Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

def floyd_warshall_avec_chemins(g):
    """
    Implémente l'algorithme de Floyd-Warshall et reconstruit les chemins les plus courts.
    :param g: Graphe pondéré représenté par une matrice d'adjacence.
    :return: (matrice des distances minimales, matrice des prédécesseurs)
    """
    n = g.nb_sommets()
    dist = [[g.adj[i][j] for j in range(n)] for i in range(n)]  # Initialisation des distances
    chemin = [[None if g.adj[i][j] == float('inf') else i for j in range(n)] for i in range(n)]  # Initialisation des chemins

    # Distance de chaque sommet à lui-même est de 0
    for i in range(n):
        dist[i][i] = 0
        chemin[i][i] = i

    # Boucles de Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    chemin[i][j] = chemin[k][j]  # Mettre à jour le prédécesseur

    return dist, chemin


def reconstruire_chemin(chemin, u, v):
    """
    Reconstruit le chemin le plus court entre deux sommets u et v à partir de la matrice des prédécesseurs.
    :param chemin: Matrice des prédécesseurs.
    :param u: Sommet source.
    :param v: Sommet destination.
    :return: Liste représentant le chemin le plus court de u à v.
    """
    if chemin[u][v] is None:
        return None  # Pas de chemin
    path = []
    while v != u:
        path.append(v)
        v = chemin[u][v]
    path.append(u)
    path.reverse()
    return path

def dijkstra(g, src):
    """
    Implémente l'algorithme de Dijkstra pour un graphe pondéré représenté par une matrice d'adjacence.
    :param g: Graphe pondéré (classe GraphePondereMatrice).
    :param src: Sommet source.
    :return: Tableau des distances minimales.
    """
    n = g.nb_sommets()
    dist = [float('inf')] * n  # Initialisation des distances
    dist[src] = 0
    vus = [False] * n  # Indique si le sommet a été définitivement traité
    file_priorite = [(0, src)]  # File de priorité : (distance, sommet)

    while file_priorite:
        d, u = heapq.heappop(file_priorite)  # Extraction du sommet avec la plus petite distance
        if vus[u]:
            continue
        vus[u] = True

        # Parcourir les voisins
        for v in g.voisins(u):
            poids = g.adj[u][v]
            if dist[u] + poids < dist[v]:
                dist[v] = dist[u] + poids
                heapq.heappush(file_priorite, (dist[v], v))

    return dist

def dijkstra_avec_chemins(g, src):
    """
    Implémente l'algorithme de Dijkstra pour trouver les plus courts chemins à partir d'une source.
    :param g: Graphe pondéré représenté par une matrice d'adjacence.
    :param src: Sommet source.
    :return: (tableau des distances minimales, tableau des prédécesseurs).
    """
    n = g.nb_sommets()
    dist = [float('inf')] * n  # Initialisation des distances
    dist[src] = 0
    precedent = [None] * n  # Garde une trace des précédents pour reconstruire les chemins
    vus = [False] * n  # Indique si le sommet a été définitivement traité
    file_priorite = [(0, src)]  # File de priorité : (distance, sommet)

    while file_priorite:
        d, u = heapq.heappop(file_priorite)  # Extraction du sommet avec la plus petite distance
        if vus[u]:
            continue
        vus[u] = True

        # Parcourir les voisins de u
        for v in g.voisins(u):
            poids = g.adj[u][v]
            if dist[u] + poids < dist[v]:
                dist[v] = dist[u] + poids
                precedent[v] = u
                heapq.heappush(file_priorite, (dist[v], v))

    return dist, precedent


def reconstruire_chem(precedent, src, dest):
    """
    Reconstruit le chemin le plus court de src à dest à partir du tableau des précédents.
    :param precedent: Tableau des précédents (list d'entiers ou None).
    :param src: Sommet source.
    :param dest: Sommet destination.
    :return: Liste représentant le chemin le plus court de src à dest, ou [] si aucun chemin n'existe.
    """
    chemin = []
    current = dest
    while current is not None:
        chemin.append(current)
        current = precedent[current]
    chemin.reverse()
    if chemin[0] == src:
        return chemin
    else:
        return []  # Aucun chemin trouvé

print("\nGraphe Pondéré avec Matrice d'Adjacence :")
g_mat = GraphePondereMatrice(4)
g_mat.ajouter_arc(0, 1, 2)
g_mat.ajouter_arc(0, 2, 4)
g_mat.ajouter_arc(1, 2, 1)
g_mat.ajouter_arc(2, 3, 3)
g_mat.afficher()
print("Nombre de sommets :", g_mat.nb_sommets())
print("Degré du sommet 0 :", g_mat.degre(0))
print("Nombre d'arcs :", g_mat.nb_arcs())

print("\nAprès suppression de l'arc (0, 2) :")
g_mat.supprimer_arc(0, 2)
g_mat.afficher()
print("Nombre de sommets :", g_mat.nb_sommets())
print("Degré du sommet 0 :", g_mat.degre(0))
print("Nombre d'arcs :", g_mat.nb_arcs(), '\n')

g = GraphePondereMatrice(4)
g.ajouter_arc(0, 1, 5)
g.ajouter_arc(0, 3, 10)
g.ajouter_arc(1, 2, 3)
g.ajouter_arc(2, 3, 1)
    
print("Matrice d'adjacence :")
g.afficher()

# Exécution de Floyd-Warshall
print("\nDistances minimales avec Floyd-Warshall :")
dist, chemin = floyd_warshall_avec_chemins(g)
for row in dist:
    print(row)

print("\nMatrice des prédécesseurs :")
for row in chemin:
    print(row)

# Reconstruction des chemins
print("\nChemin le plus court de 0 à 3 :", reconstruire_chemin(chemin, 0, 3))
print("Chemin le plus court de 1 à 3 :", reconstruire_chemin(chemin, 1, 3))
print("Chemin le plus court de 2 à 0 :", reconstruire_chemin(chemin, 2, 0))

g = GraphePondereMatrice(5)
g.ajouter_arc(0, 1, 2)
g.ajouter_arc(1, 2, 3)
g.ajouter_arc(3, 4, 1)  # Composante séparée

print("Matrice d'adjacence :")
g.afficher()

# Test de Dijkstra
print("\nDistances depuis la source 0 :")
dist, precedent = dijkstra_avec_chemins(g, 0)
print(dist)

print("\nChemins les plus courts depuis 0 :")
for dest in range(g.nb_sommets()):
    chemin = reconstruire_chem(precedent, 0, dest)
    print(f"Chemin vers {dest} :", chemin)

# Vérifier les sommets inaccessibles
print("\nTest des sommets inaccessibles :")
for dest in range(g.nb_sommets()):
    if dist[dest] == float('inf'):
        print(f"Aucun chemin vers le sommet {dest}.")

