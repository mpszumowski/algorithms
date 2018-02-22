class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, obj):
        self.items.insert(0, obj)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


def breadth_first_search(graph, source):
    bfs_info = [{"distance": None, "predecessor": None} for n in graph]
    bfs_info[source]["distance"] = 0

    bfs_queue = Queue()
    bfs_queue.enqueue(source)

    while not bfs_queue.is_empty():
        current_vector = bfs_queue.dequeue()

        for next_vector in graph[current_vector]:
            if bfs_info[next_vector]["distance"] is None:

                bfs_info[next_vector]["distance"] = \
                    bfs_info[current_vector]["distance"] + 1

                bfs_info[next_vector]["predecessor"] = current_vector

                bfs_queue.enqueue(next_vector)

    return bfs_info


adjList = [
[1],
[0, 4, 5],
[3, 4, 5],
[2, 6],
[1, 2],
[1, 2, 6],
[3, 5],
[]
]

print(breadth_first_search(adjList, 3))
