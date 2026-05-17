from typing import Optional, Any

class Node:
    """Simpul tunggal untuk Linked List"""
    def __init__(self, data: Any):
        self.data: Any = data
        self.next: Optional['Node'] = None

class LinkedList:
    """Implementasi murni Single Linked List dengan penunjuk Tail O(1)"""
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0

    def is_empty(self) -> bool:
        return self.head is None

    def append(self, data: Any) -> None:
        """Menambahkan elemen di akhir (Digunakan oleh Queue) - O(1)"""
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, data: Any) -> None:
        """Menambahkan elemen di awal (Digunakan oleh Stack) - O(1)"""
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._size += 1

    def remove_first(self) -> Any:
        """Menghapus elemen dari depan - O(1)"""
        if self.is_empty():
            raise IndexError("List kosong")
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return data

    def __len__(self) -> int:
        return self._size