from typing import Optional, Dict, List, Tuple

class EdgeNode:
    """Simpul khusus untuk merepresentasikan koneksi jalan antar gedung"""
    def __init__(self, dest: str, bobot: int):
        self.dest: str = dest
        self.bobot: int = bobot
        self.next: Optional['EdgeNode'] = None

class Graph:
    """Implementasi Weighted Undirected Graph berbasis Array of Linked Lists"""
    def __init__(self):
        # Memetakan ID Gedung ke head dari Linked List jalan
        self.adj: Dict[str, Optional[EdgeNode]] = {}
        # Metadata nama gedung
        self.node_names: Dict[str, str] = {}

    def add_node(self, node_id: str, nama: str) -> None:
        """Mendaftarkan gedung baru - O(1)"""
        if node_id not in self.adj:
            self.adj[node_id] = None
            self.node_names[node_id] = nama

    def add_edge(self, u: str, v: str, bobot: int) -> None:
        """Membangun koridor dua arah (Undirected) - O(1)"""
        if u not in self.adj or v not in self.adj:
            return

        # U mengarah ke V (Insert at head)
        new_edge_v = EdgeNode(v, bobot)
        new_edge_v.next = self.adj[u]
        self.adj[u] = new_edge_v

        # V mengarah ke U (Insert at head)
        new_edge_u = EdgeNode(u, bobot)
        new_edge_u.next = self.adj[v]
        self.adj[v] = new_edge_u

    def neighbors(self, u: str) -> List[Tuple[str, int]]:
        """Mendapatkan daftar persimpangan dari suatu gedung - O(Degree(u))"""
        res: List[Tuple[str, int]] = []
        if u not in self.adj:
            return res
            
        current = self.adj[u]
        while current is not None:
            res.append((current.dest, current.bobot))
            current = current.next
        return res