graph = {'a': {'b': 10, 'c': 3}, 'b': {'c': 1, 'd': 2}, 'c': {'b': 4, 'd': 8, 'e': 2}, 'd': {'e': 7},
         'e': {'d': 9}}  # стартовые вершины и расстояние в словаре


def dijkstra(graph, start, goal):  # функция для поиска минимального пути, параметры:
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999  # изначальное расстояние равно бесконечности
    path = []
    j = 0
    k = 0
    for node in unseenNodes:
        shortest_distance[node] = infinity      # задаём изначально бесконечное расстояние
    shortest_distance[start] = 0        # для стартовой точки 0
    print(unseenNodes)
    print(shortest_distance)
    while unseenNodes:      # изначально точки невидимы, проходимся по словарю
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
                print(j, 'minNode =', minNode)
                j += 1
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node
                print('minNode =', minNode, '|shortes_distance[node] =', shortest_distance[node], '|shortes_distance[miNode] =', shortest_distance[minNode], '|count =', k)
                k += 1

        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)

    currentNode = goal
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0, start)
    if shortest_distance[goal] != infinity:
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('And the path is ' + str(path))


a = str(input('enter the starting point:'))  # вводим стартовую точку
b = str(input('enter your goal:'))  # вводим конечную точку
dijkstra(graph, a, b)
