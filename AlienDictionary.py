from heapq import heappush, heappop, heapify

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        graph = self.build_graph(words)
        if not graph:
            return ""
        return self.topological_sort(graph)

    def build_graph(self, words):
        graph = {}
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set()

        n = len(words)
        for i in range(n - 1):
            min_len = min(len(words[i]), len(words[i + 1]))
            for j in range(min_len):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].add(words[i + 1][j])
                    break
            else:
                if len(words[i]) > len(words[i + 1]):
                    return None

        return graph

    def topological_sort(self, graph):
        indegree = self.get_indegree(graph)
        queue = [node for node in graph if indegree[node] == 0]
        heapify(queue)
        topo_order = ""

        while queue:
            node = heappop(queue)
            topo_order += node
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    heappush(queue, neighbor)

        return topo_order if len(topo_order) == len(graph) else ""

    def get_indegree(self, graph):
        indegree = {node: 0 for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1
        return indegree
