=======
# 🎓 Smart Campus Navigation & Shortest Path System
=======
# 🗂️ Branch: feat/ziiza-BST
(Smart Campus Navigation System)
>>>>>>> f9cdd3b (Update README)

[![Author](https://img.shields.io/badge/Author-Azlizatussalwa_(25051030114)-blue.svg)]()
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)]()

## 📌 Deskripsi Tugas
Branch ini didedikasikan untuk membangun sistem direktori pencarian gedung yang efisien. Struktur data utama yang diimplementasikan di sini adalah Binary Search Tree (Modul 4) yang dikembangkan murni dari nol.

## 🚀 Fitur yang Dikembangkan
- *Modul 4: Binary Search Tree (src/modules/modul_4_bst.py)*
  - Mengimplementasikan objek BSTNode untuk menyimpan Key (Kode Gedung, misal "A1") dan Value (Nama Lengkap Gedung).
  - Mengurutkan data secara otomatis berdasarkan alfabetis kode gedung.
  - Memastikan pencarian nama gedung memiliki kompleksitas waktu rata-rata $O(\log V)$, jauh lebih optimal dibandingkan array/list biasa.
  - Menyediakan fungsi penelusuran (opsional Inorder) untuk menampilkan seluruh direktori gedung.

<<<<<<< HEAD
---

## 👥 Tim Pengembang (Kelompok)

| NIM | Nama Lengkap |
| :--- | :--- |
| **25051030094** | Alif Muhammad Rizqi |
| **25051030089** | Muhammad Arif Nur Widhiyanto |
| **25051030113** | Riana |
| **25051030114** | Azlizatussalwa |

---

## ✨ Fitur & Modul Utama

Sistem ini dipecah menjadi 6 modul fungsional yang saling terintegrasi:

1. **Modul 1: Representasi Graph Berbobot**
   - Menggunakan *Adjacency List* berbasis *Custom Linked List*.
   - Kompleksitas Penambahan Edge: $O(1)$.
2. **Modul 2: Dijkstra Shortest Path**
   - Menghitung jarak rute terpendek dalam satuan meter.
   - Kompleksitas: $O(V^2 + E)$ menggunakan pendekatan array sederhana.
3. **Modul 3: Traversal BFS & DFS**
   - **BFS** (berbasis *Custom Queue*): Untuk eksplorasi gedung level-by-level (radius terdekat).
   - **DFS** (berbasis *Custom Stack*): Untuk eksplorasi kedalaman wilayah.
4. **Modul 4: Direktori Gedung (BST)**
   - Menggunakan *Binary Search Tree* terurut secara alfabetis berdasarkan kode gedung (A1-F5).
   - Kompleksitas Pencarian Data: Rata-rata $O(\log V)$.
5. **Modul 5: Deteksi Komponen Terisolasi**
   - Audit jaringan jalan menggunakan penelusuran graf untuk mencari gedung yang terputus dari Gerbang Utama.
6. **Modul 6: Command Line Interface (CLI)**
   - Antarmuka interaktif yang aman dari *crash* (*error handling*).

---

## 📂 Struktur Direktori

```text
📁 Smart-Campus-NavSys/
├── 📄 README.md                 # Dokumentasi Proyek
├── 📁 src/                      # Source Code Utama
│   ├── 📄 main.py               # Entry Point (Modul 6 - CLI)
│   ├── 📁 data_structures/      # Struktur Data Murni (From Scratch)
│   │   ├── linked_list.py
│   │   ├── stack.py
│   │   ├── queue_ll.py
│   ├── 📁 modules/              # Implementasi Algoritma
│   │   ├── modul_1_graph.py
│   │   ├── modul_2_dijkstra.py
│   │   ├── modul_3_traversal.py
│   │   ├── modul_4_bst.py
│   │   ├── modul_5_isolasi.py
├── 📁 experiments/              # Skrip Uji Coba Performa
│   └── 📄 benchmark.py          # Uji runtime V dan E dinamis
├── 📁 docs/                     # Berkas Laporan Laporan
│   ├── Laporan_Final.pdf
│   └── Slide_Presentasi.pdf
└── 📁 AI_Log/                   # Log Penggunaan AI Assistant
    ├── Log_prompt.txt
    └── screenshots/
>>>>>>> 9dd9465b2dfb26869006188561d8f6ba5ed3774d
=======
## 🧪 Cara Pengujian
Inisialisasi BSTGedung, masukkan beberapa kode dan nama gedung menggunakan insert(), lalu validasi algoritma dengan memanggil fungsi search("A1").
>>>>>>> f9cdd3b (Update README)
