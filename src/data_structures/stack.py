from typing import Any
from src.data_structures.linked_list import LinkedList

class Stack:
    """Implementasi Stack murni menggunakan Custom Linked List"""
    def __init__(self):
        self._list = LinkedList()

    def is_empty(self) -> bool:
        return self._list.is_empty()

    def push(self, item: Any) -> None:
        """Memasukkan data ke tumpukan atas - O(1)"""
        self._list.prepend(item)

    def pop(self) -> Any:
        """Mengambil data dari tumpukan teratas - O(1)"""
        if self.is_empty():
            raise IndexError("Pop dari stack kosong")
        return self._list.remove_first()

    def __len__(self) -> int:
        return len(self._list)