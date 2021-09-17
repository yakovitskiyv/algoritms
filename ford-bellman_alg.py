from collections import defaultdict

# Класс для представления графа


class Graph:

    def __init__(self, vertices):
        self.V = vertices  # количество вершин
        self.graph = []  # словарь по умолчанию для хранения графа

    # функция для добавления ребер к графу
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # служебная функция, используемая для печати решения
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("% d \t\t % d" % (i, dist[i]))

        # Основная функция, которая находит кратчайшие расстояния от src до

    # всех остальных вершин с использованием алгоритма Беллмана-Форда. Функция
    # также обнаруживает цикл отрицательного веса
    def BellmanFord(self, src):

        # Шаг 1. Инициализируйте расстояния от src до всех остальных вершин.
        # как INFINITE
        dist = [10000.0] * self.V
        dist[src] = 0

        # Шаг 2: Ослабьте все края | V | - 1 раз. Простой кратчайший
        # путь из src в любую другую вершину может иметь не более | V | - 1 края
        for i in range(self.V - 1):
            # Обновить значение расстояния и родительский индекс смежных вершин выбранной вершины.
            # Учитывать только те вершины, которые еще находятся в очереди.
            for u, v, w in self.graph:
                if dist[u] != 10000.0 and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

                # Шаг 3: проверьте циклы с отрицательным весом.
        # Вышеупомянутый шаг гарантирует кратчайшие расстояния, если график не содержит цикла отрицательного веса.
        #  Если мы получим более короткий путь, значит, есть цикл.

        for u, v, w in self.graph:
            if dist[u] != 10000.0 and dist[u] + w < dist[v]:
                print
                "Graph contains negative weight cycle"
                return

        # Вывести все расстояние
        self.printArr(dist)

#####################################


n = int(input("к-во вершин="))
m = int(input("к-во ребер="))

g = Graph(n)

for i in range(m):
    u, v, w = tuple(map(int, input(str(i)+"-е ребро: ").split(" ")))
    g.addEdge(u, v, w)

#g.addEdge(0, 1, -1)
#g.addEdge(0, 2, 4)
#g.addEdge(1, 2, 3)
#g.addEdge(1, 3, 2)
#g.addEdge(1, 4, 2)
#g.addEdge(3, 2, 5)
#g.addEdge(3, 1, 1)
#g.addEdge(4, 3, -3)

# Вывести решение

g.BellmanFord(0)
