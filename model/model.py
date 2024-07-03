import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._metodi=DAO.getAllMethods()
        self._productsId=[]
        self._products=DAO.getAllProducts()
        self._mapProd={}
        for p in self._products:
            self._mapProd[p.Product_number]=p
        self._grafo=nx.DiGraph()

    def creaGrafo(self,metodo,anno):
        self._grafo.clear()
        self._productsId=DAO.getAllProductsN(metodo,anno)
        for id in self._productsId:
            self._grafo.add_node(self._mapProd[id])

    def metodi(self):
        return self._metodi

    def getNumNodes(self):
        return self._grafo.number_of_nodes()

    def getNumEdges(self):
        return self._grafo.number_of_edges()