# import os

# def policz_pliki(katalog):
#     try:
#         pliki = [f for f in os.listdir(katalog) if os.path.isfile(os.path.join(katalog, f))]
#         print(f"Liczba plikow w katalogu '{katalog}': {len(pliki)}")
#     except FileNotFoundError:
#         print("Nie znaleziono katalogu!")

# policz_pliki("C:\\Users\\Lenovo\\OneDrive\\Pulpit\\BR-2025-71-CEF_Maciej_Filipiak_iaeste") 


# import os

# def wypisz_pliki(katalog):
#     for root, dirs, files in os.walk(katalog):
#         for nazwa in files:
#             print(os.path.join(root, nazwa))

# wypisz_pliki("C:\\Users\\Lenovo\\OneDrive\\Pulpit\\BR-2025-71-CEF_Maciej_Filipiak_iaeste") 


# # import re

# # def usun_slowa_re(tekst, slowa_do_usuniecia):
# #     pattern = r"\b(" + "|".join(map(re.escape, slowa_do_usuniecia)) + r")\b"
# #     return re.sub(pattern, "", tekst)

# # tekst = "Python jest prosty, bulka z maslem!"
# # slowa = ["prosty", "bulka"]
# # wynik = usun_slowa_re(tekst, slowa)
# # print(wynik)

# import re

# def zamien_slowa_re(tekst, zamiany):
#     pattern = r"\b(" + "|".join(map(re.escape, zamiany.keys())) + r")\b"
#     return re.sub(pattern, lambda m: zamiany[m.group(0)], tekst)

# tekst = "Python jest prosty, bulka z maslem."
# zamiany = {"prosty": "latwy", "bulka": "kromka"}
# wynik = zamien_slowa_re(tekst, zamiany)
# print(wynik)


# import random

# def generuj_liczby(n, min_val=0, max_val=100):
#     return [random.randint(min_val, max_val) for _ in range(n)]

# def bubble_sort(tab):
#     t = tab.copy()
#     n = len(t)
#     for i in range(n - 1):
#         for j in range(0, n - i - 1):
#             if t[j] > t[j + 1]:
#                 t[j], t[j + 1] = t[j + 1], t[j]
#     return t

# def insertion_sort(tab):
#     t = tab.copy()
#     for i in range(1, len(t)):
#         klucz = t[i]
#         j = i - 1
#         while j >= 0 and t[j] > klucz:
#             t[j + 1] = t[j]
#             j -= 1
#         t[j + 1] = klucz
#     return t


# if __name__ == "__main__":
  
#     N = random.randint(5, 20)
#     liczby = generuj_liczby(N)
#     print(f"Wylosowano {N} liczb: {liczby}")

#     posortowane_bubble = bubble_sort(liczby)
#     posortowane_insertion = insertion_sort(liczby)
#     posortowane_builtin = sorted(liczby)

#     print("\nBubble sort:   ", posortowane_bubble)
#     print("Insertion sort:", posortowane_insertion)
#     print("Wbudowana sort:", posortowane_builtin)

#     if posortowane_bubble == posortowane_builtin and posortowane_insertion == posortowane_builtin:
#         print("\nWyniki obu metod sa poprawne.")
#     else:
#         print("\nWyniki nie sa zgodne!")


# class Node:
#     def __init__(self, value=None):
#         self.value = value
#         self.children = []  # lista krotek: (Node, edge_value)

#     def add_child(self, node, edge_value=None):
#         self.children.append((node, edge_value))

#     def __str__(self, level=0):
#         ret = "\t"*level + f"Node({self.value})\n"
#         for child, edge_val in self.children:
#             ret += "\t"*(level+1) + f"Edge({edge_val}) -> " + child.__str__(level+2)
#         return ret

#     def traverse(self):
#         """Zwraca listę wszystkich wartości wezlow (DFS)"""
#         result = [self.value]
#         for child, _ in self.children:
#             result.extend(child.traverse())
#         return result


# # Klasa Tree
# class Tree:
#     def __init__(self, root_value=None):
#         self.root = Node(root_value)

#     def __str__(self):
#         return self.root.__str__()

#     def traverse(self):
#         return self.root.traverse()


# # 🧪 Przykład użycia
# if __name__ == "__main__":
#     tree = Tree("root")

#     # dodajemy dzieci do korzenia
#     child1 = Node("A")
#     child2 = Node("B")
#     tree.root.add_child(child1, edge_value=5)
#     tree.root.add_child(child2, edge_value=10)

#     # dodajemy dzieci do child1
#     child1.add_child(Node("A1"), edge_value=2)
#     child1.add_child(Node("A2"), edge_value=3)

#     # dodajemy dzieci do child2
#     child2.add_child(Node("B1"), edge_value=7)

#     print("Drzewo:")
#     print(tree)

#     print("Przechodzenie wszystkich wezlow (DFS):")
#     print(tree.traverse())



# import unittest

# # -------------------
# # Definicja klas Node i Tree
# # -------------------

# class Node:
#     def __init__(self, value=None):
#         self.value = value
#         self.children = []  # lista krotek: (Node, edge_value)

#     def add_child(self, node, edge_value=None):
#         self.children.append((node, edge_value))

#     def __str__(self, level=0):
#         ret = "\t"*level + f"Node({self.value})\n"
#         for child, edge_val in self.children:
#             ret += "\t"*(level+1) + f"Edge({edge_val}) -> " + child.__str__(level+2)
#         return ret

#     def traverse(self):
#         """Zwraca listę wszystkich wartości węzłów (DFS)"""
#         result = [self.value]
#         for child, _ in self.children:
#             result.extend(child.traverse())
#         return result


# class Tree:
#     def __init__(self, root_value=None):
#         self.root = Node(root_value)

#     def __str__(self):
#         return self.root.__str__()

#     def traverse(self):
#         return self.root.traverse()


# # -------------------
# # Unit Testy
# # -------------------

# class TestTree(unittest.TestCase):

#     def setUp(self):
#         """Tworzymy drzewo do testów"""
#         self.tree = Tree("root")
#         child1 = Node("A")
#         child2 = Node("B")
#         self.tree.root.add_child(child1, edge_value=5)
#         self.tree.root.add_child(child2, edge_value=10)

#         child1.add_child(Node("A1"), edge_value=2)
#         child1.add_child(Node("A2"), edge_value=3)
#         child2.add_child(Node("B1"), edge_value=7)

#     def test_root_value(self):
#         self.assertEqual(self.tree.root.value, "root")

#     def test_children_count(self):
#         self.assertEqual(len(self.tree.root.children), 2)
#         self.assertEqual(len(self.tree.root.children[0][0].children), 2)
#         self.assertEqual(len(self.tree.root.children[1][0].children), 1)

#     def test_traverse(self):
#         expected = ["root", "A", "A1", "A2", "B", "B1"]
#         self.assertEqual(self.tree.traverse(), expected)

#     def test_str_contains_values(self):
#         tree_str = str(self.tree)
#         for value in ["root", "A", "A1", "A2", "B", "B1"]:
#             self.assertIn(value, tree_str)

#     def test_edge_values_preserved(self):
#         edges = [edge for _, edge in self.tree.root.children]
#         self.assertIn(5, edges)
#         self.assertIn(10, edges)


# # -------------------
# # Uruchomienie testów
# # -------------------

# if __name__ == "__main__":
#     unittest.main()

