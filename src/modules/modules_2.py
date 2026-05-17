from typing import Dict, Optional, Tuple, List
from src.data_structures.graph import Graph

def dijkstra(graph: Graph, source: str) -> Tuple[Dict[str, int], Dict[str, Optional[str]]]:
    INF = float('inf')
    dist: Dict[str, int] = {v: INF for v in graph.adj}
    parent: Dict[str, Optional[str]] = {v: None for v in graph.adj}
    visited = set()

    if source not in dist:
        return dist, parent

    dist[source] = 0

    for _ in range(len(graph.adj)):
        min_dist = INF
        u = None
        
        # Cari node dengan jarak terpendek yang belum dikunjungi
        for node in graph.adj:
            if node not in visited and dist[node] < min_dist:
                min_dist = dist[node]
                u = node

        if u is None:
            break

        visited.add(u)
        
        # Relaksasi tetangga
        current_edge = graph.adj[u]
        while current_edge is not None:
            v = current_edge.dest
            weight = current_edge.bobot
            if v not in visited and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u
            current_edge = current_edge.next

    return dist, parent

def reconstruct_path(parent: Dict[str, Optional[str]], source: str, target: str) -> List[str]:
    """Merekontruksi jalur dari parent dict."""
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        if curr == source:
            break
        curr = parent.get(curr)
        
    if not path or path[-1] != source:
        return []
    path.reverse()
    return path