from typing import Optional, Dict, List, Tuple

class EdgeNode:
    def __init__(self, dest: str, bobot: int):
        self.dest: str = dest
        self.bobot: int = bobot
        self.next: Optional['EdgeNode'] = None

class Graph:
    def __init__(self):
        # Dictionary untuk memetakan ID gedung ke head Linked List
        self.adj: Dict[str, Optional[EdgeNode]] = {}
        # Dictionary untuk menyimpan nama asli gedung
        self.node_names: Dict[str, str] = {}

    def add_node(self, node_id: str, nama: str) -> None:
        """Menambahkan titik/gedung baru ke dalam graf (O(1))"""
        if node_id not in self.adj:
            self.adj[node_id] = None
            self.node_names[node_id] = nama

    def add_edge(self, u: str, v: str, bobot: int) -> None:
        """Menambahkan jalan dua arah (undirected) di HEAD linked list (O(1))"""
        if u not in self.adj or v not in self.adj:
            return

        # Tambahkan u -> v
        new_edge_v = EdgeNode(v, bobot)
        new_edge_v.next = self.adj[u]
        self.adj[u] = new_edge_v

        # Tambahkan v -> u
        new_edge_u = EdgeNode(u, bobot)
        new_edge_u.next = self.adj[v]
        self.adj[v] = new_edge_u

    def neighbors(self, u: str) -> List[Tuple[str, int]]:
        """Mengambil semua tetangga dari node u (O(deg(u)))"""
        res: List[Tuple[str, int]] = []
        if u not in self.adj:
            return res
            
        current = self.adj[u]
        while current is not None:
            res.append((current.dest, current.bobot))
            current = current.next
        return res

    def is_connected(self, u: str, v: str) -> bool:
        """Mengecek apakah dua gedung terhubung langsung"""
        if u not in self.adj or v not in self.adj:
            return False
            
        current = self.adj[u]
        while current is not None:
            if current.dest == v:
                return True
            current = current.next
        return False