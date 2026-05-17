from typing import Optional, List, Tuple

class BSTNode:
    """Simpul untuk Binary Search Tree"""
    def __init__(self, key: str, nama: str):
        self.key: str = key          # Kode gedung (misal: "A1")
        self.nama: str = nama        # Nama lengkap
        self.left: Optional['BSTNode'] = None
        self.right: Optional['BSTNode'] = None

class BSTGedung:
    """Sistem Direktori berbasis Pohon Biner Pencarian"""
    def __init__(self):
        self.root: Optional[BSTNode] = None

    def insert(self, key: str, nama: str) -> None:
        """Menambahkan gedung secara rekursif - Rata-rata O(log V)"""
        self.root = self._insert_helper(self.root, key, nama)

    def _insert_helper(self, node: Optional[BSTNode], key: str, nama: str) -> BSTNode:
        if node is None:
            return BSTNode(key, nama)
            
        if key < node.key:
            node.left = self._insert_helper(node.left, key, nama)
        elif key > node.key:
            node.right = self._insert_helper(node.right, key, nama)
        else:
            node.nama = nama # Update jika key sudah ada
        return node

    def search(self, key: str) -> Optional[str]:
        """Pencarian Non-Linear tanpa List - Rata-rata O(log V)"""
        current = self.root
        while current is not None:
            if key == current.key:
                return current.nama
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None