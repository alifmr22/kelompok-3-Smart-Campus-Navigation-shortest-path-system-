from typing import List
from src.data_structures.graph import Graph
from src.modules.modul_3_traversal import bfs

def get_isolated_nodes(graph: Graph, gateway: str = "A1") -> List[str]:
    if gateway not in graph.adj:
        return list(graph.adj.keys())
        
    # Ambil semua node yang terjangkau dari gateway menggunakan BFS
    reachable_nodes = set(bfs(graph, gateway))
    all_nodes = set(graph.adj.keys())
    
    # Gedung terisolasi adalah selisih himpunan (total node dikurangi node yang terjangkau)
    isolated_nodes = list(all_nodes - reachable_nodes)
    return isolated_nodes