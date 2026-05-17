from typing import Optional, List, Tuple

class BSTNode:
    def _init_(self, key: str, nama: str):
        self.key: str = key          # Kode gedung (misal: "A1")
        self.nama: str = nama        # Nama lengkap gedung
        self.left: Optional['BSTNode'] = None
        self.right: Optional['BSTNode'] = None

class BSTGedung:
    def _init_(self):
        self.root: Optional[BSTNode] = None

    def insert(self, key: str, nama: str) -> None:
        """Menyisipkan data gedung baru ke dalam pohon (O(log V))"""
        self.root = self._insert_helper(self.root, key, nama)

    def _insert_helper(self, node: Optional[BSTNode], key: str, nama: str) -> BSTNode:
        if node is None:
            return BSTNode(key, nama)
            
        if key < node.key:
            node.left = self._insert_helper(node.left, key, nama)
        elif key > node.key:
            node.right = self._insert_helper(node.right, key, nama)
        else:
            # Jika kunci sudah ada, perbarui namanya
            node.nama = nama
        return node

    def search(self, key: str) -> Optional[str]:
        """Mencari nama gedung berdasarkan kode. Return None jika tidak ada."""
        current = self.root
        while current is not None:
            if key == current.key:
                return current.nama
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None

    def inorder(self) -> List[Tuple[str, str]]:
        """Mengembalikan data terurut alfabetis (A-Z) untuk pelaporan"""
        result: List[Tuple[str, str]] = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, node: Optional[BSTNode], result: List[Tuple[str, str]]) -> None:
        if node is not None:
            self._inorder_helper(node.left, result)
            result.append((node.key, node.nama))
            self._inorder_helper(node.right, result)
            
    def delete(self, key: str) -> None:
        """Menghapus data gedung dari direktori (Opsional/Ekstra)"""
        self.root = self._delete_helper(self.root, key)

    def _delete_helper(self, node: Optional[BSTNode], key: str) -> Optional[BSTNode]:
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete_helper(node.left, key)
        elif key > node.key:
            node.right = self._delete_helper(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node dengan 2 anak: ambil Inorder Successor
            successor = self._find_min(node.right)
            node.key = successor.key
            node.nama = successor.nama
            node.right = self._delete_helper(node.right, successor.key)

        return node

    def _find_min(self, node: BSTNode) -> BSTNode:
        current = node
        while current.left is not None:
            current = current.left
        return current