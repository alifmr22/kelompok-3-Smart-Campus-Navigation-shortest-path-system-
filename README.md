# 🗺️ Branch: `feat/arif-graph`
*(Smart Campus Navigation System)*

[![Author](https://img.shields.io/badge/Author-Muhammad_Arif_Nur_W_(25051030089)-blue.svg)]()
[![Status](https://img.shields.io/badge/Status-Completed-success.svg)]()

## 📌 Deskripsi Tugas
Branch ini adalah fondasi tata letak kampus sekaligus kerangka utama sistem. Fokusnya adalah merancang *Graph* untuk merepresentasikan peta (Modul 1), serta merakit seluruh pekerjaan anggota tim ke dalam satu antarmuka interaktif (Modul 6).

## 🚀 Fitur yang Dikembangkan
- **Modul 1: Adjacency List Graph (`src/modules/modul_1_graph.py`)**
  - Membangun struktur *Weighted Undirected Graph* (Graf Berbobot Tak Berarah) menggunakan pointer `EdgeNode` (Linked List murni).
  - Menjamin kompleksitas penambahan node dan edge beroperasi pada $O(1)$.
- **Modul 6: Command Line Interface & Integrasi Utama (`src/main.py`)**
  - Merakit integrasi antara Graph, Dijkstra (Alif), BFS/DFS (Riana), dan BST (Ziza).
  - Menyusun *looping* menu navigasi interaktif (*Error-handled UI*).
  - Menulis generator `generate_edges()` yang memastikan graf kampus memenuhi tepat 30 Node (Gedung) dan 55 Edge (Koridor).
  - Menyediakan fitur *self-audit* parameter (*Laporan Graph* dan deteksi Node Terisolasi).

## 🧪 Cara Pengujian
Jalankan file `main.py`. Program harus menampilkan antarmuka tanpa *crash*. Buktikan keandalan Graph dengan memanggil opsi pengecekan konektivitas (Laporan Graph) untuk memvalidasi jumlah parameter.