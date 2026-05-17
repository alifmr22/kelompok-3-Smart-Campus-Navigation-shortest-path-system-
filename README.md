# 🎓 Smart Campus Navigation & Shortest Path System

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Course](https://img.shields.io/badge/Mata%20Kuliah-Algoritma%20%26%20Struktur%20Data-success.svg)]()
[![Status](https://img.shields.io/badge/Status-In%20Progress-yellow.svg)]()

Proyek **Sistem Navigasi Kampus Pintar** ini dikembangkan sebagai pemenuhan tugas *Team Based Project* (TA 2025/2026) untuk mata kuliah **ELT60213 Algoritma dan Struktur Data**, Teknik Elektro, Universitas Negeri Yogyakarta. 

Sistem ini memodelkan tata letak $\pm$ 100 hektar area kampus menjadi sebuah *Graph* berbobot (30 Gedung, 55 Koridor/Jalan) untuk membantu mahasiswa baru menemukan rute paling optimal antar gedung. Seluruh struktur data dibangun secara murni (*from scratch*) tanpa menggunakan pustaka koleksi bawaan Python untuk mendemonstrasikan pemahaman fundamental algoritma.

---

## 👥 Tim Pengembang (Kelompok)

| NIM | Nama Lengkap |
| :--- | :--- |
| **25051030089** | Muhammad Arif Nur Widhiyanto |
| **25051030094** | Alif Muhammad Rizqi |
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
📁 PROJECT3/
├── 📁 AI_log/                   # Log Penggunaan AI Assistant
│   └── 📄 log_promt.txt
├── 📁 docs/                     # Berkas Laporan & Presentasi
│   ├── 📄 laporan_final.pdf
│   └── 📄 slide_presentasi.pdf
├── 📁 experiment/               # Folder Eksperimen
├── 📁 src/                      # Source Code Utama
│   ├── 📁 data_structures/      # Struktur Data Murni (From Scratch)
│   │   ├── 📄 bst.py
│   │   ├── 📄 graph.py
│   │   ├── 📄 linked_list.py
│   │   ├── 📄 queue.py
│   │   └── 📄 stack.py
│   ├── 📁 modules/              # Implementasi Algoritma
│   │   ├── 📄 modules_1.py
│   │   ├── 📄 modules_2.py
│   │   ├── 📄 modules_3.py
│   │   ├── 📄 modules_4.py
│   │   ├── 📄 modules_5.py
│   │   └── 📄 modules_6.py
│   └── 📄 main.py               # Entry Point Aplikasi
├── 📁 tests/                    # Unit Testing
│   ├── 📄 test_bst.py
│   ├── 📄 test_graph.py
│   ├── 📄 test_linked_list.py
│   ├── 📄 test_queue.py
│   └── 📄 test_stack.py
├── 📄 .gitignore                # Git Ignore File
└── 📄 README.md                 # Dokumentasi Proyek