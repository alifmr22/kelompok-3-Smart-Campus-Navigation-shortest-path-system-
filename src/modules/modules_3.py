from typing import List
from src.data_structures.graph import Graph
from src.data_structures.queue_ll import Queue
from src.data_structures.stack import Stack

def bfs(graph: Graph, source: str) -> List[str]:
    if source not in graph.adj:
        return []
        
    q = Queue()
    q.enqueue(source)
    visited = {source}
    result = []

    while not q.is_empty():
        u = q.dequeue()
        result.append(u)
        
        current_edge = graph.adj[u]
        while current_edge is not None:
            v = current_edge.dest
            if v not in visited:
                visited.add(v)
                q.enqueue(v)
            current_edge = current_edge.next
    return result

def dfs(graph: Graph, source: str) -> List[str]:
    if source not in graph.adj:
        return []
        
    s = Stack()
    s.push(source)
    visited = set()
    result = []

    while not s.is_empty():
        u = s.pop()
        if u not in visited:
            visited.add(u)
            result.append(u)
            
            current_edge = graph.adj[u]
            while current_edge is not None:
                if current_edge.dest not in visited:
                    s.push(current_edge.dest)
                current_edge = current_edge.next
    return result