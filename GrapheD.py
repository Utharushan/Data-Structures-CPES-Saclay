class GrapheD:
	"""
	Classe pour représenter un graphe orienté sous forme de dictionnaire d'adjacence.
	"""
	def __init__(self):
		"""
		Initialise un graphe vide.
		"""
		self.adj = {}

	def ajouter_sommet(self, s):
		"""
		Ajoute un sommet s au graphe.
		:param s: Étiquette du sommet.
		"""
		if s not in self.adj:
			self.adj[s] = set()
		else:
			raise ValueError(f"Le sommet {s} existe déjà.")

	def ajouter_arc(self, s1, s2):
		"""
		Ajoute un arc orienté de s1 à s2.
		:param s1: Sommet source.
		:param s2: Sommet destination.
		"""
		if s1 not in self.adj:
			self.ajouter_sommet(s1)
		if s2 not in self.adj:
			self.ajouter_sommet(s2)
		self.adj[s1].add(s2)

	def arc(self, s1, s2):
		"""
		Vérifie si un arc existe entre s1 et s2.
		:param s1: Sommet source.
		:param s2: Sommet destination.
		:return: True si l'arc existe, False sinon.
		"""
		return s1 in self.adj and s2 in self.adj[s1]

	def voisins(self, s):
		"""
		Renvoie une liste des sommets voisins du sommet s.
		:param s: Sommet pour lequel on cherche les voisins.
		:return: Liste des sommets voisins.
		"""
		if s in self.adj:
			return list(self.adj[s])
		else:
			raise ValueError(f"Le sommet {s} n'existe pas.")

	def afficher(self):
		"""Affiche le graphe sous forme : sommet {voisins}."""
		for sommet, voisins in self.adj.items():
			print(f"{sommet} {voisins}")

	def nb_sommets(self):
		"""Renvoie le nombre de sommets dans le graphe."""
		return len(self.adj)

	def degre(self, s):
		"""Renvoie le degré du sommet s."""
		if s in self.adj:
			return len(self.adj[s])
		else:
			raise ValueError(f"Le sommet {s} n'existe pas.")

	def nb_arcs(self):
		"""Renvoie le nombre d'arcs dans le graphe."""
		return sum(len(voisins) for voisins in self.adj.values())

	def supprimer_arc(self, s1, s2):
		"""Supprime l'arc de s1 à s2, si l'arc existe."""
		if s1 in self.adj and s2 in self.adj[s1]:
			self.adj[s1].remove(s2)

print("\nTest de GrapheD:")
g_d = GrapheD()
g_d.ajouter_sommet("A")
g_d.ajouter_sommet("B")
g_d.ajouter_arc("A", "B")
g_d.ajouter_arc("A", "C")
print("Arc (A,B):", g_d.arc("A", "B"))
print("Arc (B,A):", g_d.arc("B", "A"))
print("Voisins de A:", g_d.voisins("A"))
print("Voisins de B:", g_d.voisins("B"))

g = GrapheD()
g.ajouter_sommet(0)
g.ajouter_sommet(1)
g.ajouter_sommet(2)
g.ajouter_sommet(3)
g.ajouter_arc(0, 1)
g.ajouter_arc(0, 2)
g.ajouter_arc(1, 2)
g.ajouter_arc(1, 3)
g.ajouter_arc(2, 1)
g.ajouter_arc(3, 2)

print("Graphe affiché :")
g.afficher()
print("\nNombre de sommets :", g.nb_sommets())
print("Degré du sommet 1 :", g.degre(1))
print("Nombre d'arcs :", g.nb_arcs())

g.supprimer_arc(1, 2)
print("\nAprès suppression de l'arc (1,2) :")
g.afficher()

