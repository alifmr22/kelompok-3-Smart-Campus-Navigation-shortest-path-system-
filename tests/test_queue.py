from typing import Any
from src.data_structures.linked_list import LinkedList

class Queue:
    """Implementasi Queue murni menggunakan Custom Linked List"""
    def __init__(self):
        self._list = LinkedList()

    def is_empty(self) -> bool:
        return self._list.is_empty()

    def enqueue(self, item: Any) -> None:
        """Memasukkan data ke antrean belakang - O(1)"""
        self._list.append(item)

    def dequeue(self) -> Any:
        """Mengambil data dari antrean paling depan - O(1)"""
        if self.is_empty():
            raise IndexError("Dequeue dari queue kosong")
        return self._list.remove_first()

    def __len__(self) -> int:
        return len(self._list)