# arbreabeignet = [1, 2, 3, 4, 5, 6]

# # faire self.arbreabeignet dans une fonction __init__(self) une liste vide | Self représente le beignet sur lequel on travaille
# # Si on travaille sur un beignet en particulier, c'est le self

# m = 1
# a = 0 
# arbreabeignet.append(a)

# if a < m : 
#     m = a

# print(m) 
# print(arbreabeignet)

# arbreapancake = [6, 7, 8, 9, 12]
# w = 6
# arbreabeignet.append(arbreapancake)

# if w < m: 
#     m = w

# del arbreabeignet[arbreabeignet.index(m)] # arbreabeignet.pop(m) j'ai battu le prof. Toc. è_é ! 



# print(arbreabeignet)
# print(m)

class Heap(object):
    """
    Une heap est une structure de données sous forme d'arbre.
    https://en.wikipedia.org/wiki/Heap_(data_structure)
    """

    def insert(self, value: int):
        """
        Ajoute une valeur dans l'arbre
        """

        
        
        

    def find_min(self):
        """
        Retourne la valeur minimum dans l'arbre
        """


        
            

    def delete_min(self):
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """



    def decrease_key(self, current_value: int, new_value :int):
        """
        Modify une valeur dans l'arbre
        """
        pass

    def merge(self, fibonnaci_heap: object):
        """
        Fusionne deux arbres
        """

        
    

            


        


class FibonacciHeap():
    """
    Une fibonnaci heap est un arbre permettant de stocker et trier des donnés efficacement
    https://en.wikipedia.org/wiki/Fibonacci_heap
    L'implémentation est décrite en anglais : https://en.wikipedia.org/wiki/Fibonacci_heap#Implementation_of_operations
    et en français : https://fr.wikipedia.org/wiki/Tas_de_Fibonacci#Implémentation_des_opérations
    """

    def __init__(self, value):  
        self.value = value
        self.child = []
        self.order = 0
        

    def insert(self, value):
        
        tableau_min = []
        self.child.append(value)
        print(self.child)
        print(tableau_min)

        
        

    def find_min(self) -> int:
        """
        Retourne la valeur minimum dans l'arbre
        """
        tableau_min = []
        
        for m  in self.child: 
            tableau_min.append(m)
            
            n = sorted(tableau_min) # On trie le tableau
            return n[0] # On enlève la valeur en position 0



    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        j = self.find_min()
        for i in self.child:
            if j == i :
                min = i
                self.child.remove(i)
                return min[0]
     
        

    def merge(self, fibonacci_heap: Heap) -> None:
        """
        Fusionne deux arbres
        """
       suppr = self.delete_min()
       
        
        

       


tableau = []
test = FibonacciHeap(tableau)
a = test.insert(1)
b = test.insert(9)
c = test.insert(200)
d = test.insert(31)
