import numpy as np
from src.data_structures.graph import Graph
from src.data_structures.bst import BSTGedung
from src.modules.modul_2_dijkstra import dijkstra, reconstruct_path
from src.modules.modul_3_traversal import bfs, dfs
from src.modules.modul_5_isolasi import get_isolated_nodes

np.random.seed(7)

def generate_edges(nodes, seed=7):
    rng = np.random.default_rng(seed)
    n = len(nodes)
    edges = []
    
    perm = rng.permutation(n)
    for i in range(1, n):
        u = nodes[perm[i-1]][0]
        v = nodes[perm[i]][0]
        w = int(rng.integers(50, 500))
        edges.append((u, v, w))
        
    # Memastikan terbentuk persis 55 edge sesuai parameter dosen
    extra = 55 - (n - 1) 
    for _ in range(extra):
        i, j = rng.choice(n, 2, replace=False)
        w = int(rng.integers(50, 500))
        edges.append((nodes[i][0], nodes[j][0], w))
        
    return edges

def main():
    g = Graph()
    bst = BSTGedung()
    
    GEDUNG_DATA = [
        ('A1', 'Gerbang Utama'), ('A2', 'Rektorat'), ('A3', 'Pusat Administrasi Keuangan'), ('A4', 'Gedung Pertemuan Alumni'), ('A5', 'Masjid Pusat Kampus'),
        ('B1', 'FT-Gedung A'), ('B2', 'FT-Gedung B'), ('B3', 'Lab Elektronika'), ('B4', 'Lab Komputer'), ('B5', 'Workshop Teknik Mesin'),
        ('C1', 'FMIPA-Gedung A'), ('C2', 'Perpustakaan Pusat'), ('C3', 'Laboratorium Kimia Terpadu'), ('C4', 'Gedung Dekanat MIPA'), ('C5', 'Pusat Riset Sains'),
        ('D1', 'Stadion Kampus'), ('D2', 'GOR'), ('D3', 'Poliklinik Kampus'), ('D4', 'Pusat Kegiatan Mahasiswa'), ('D5', 'Gedung Kesenian & Budaya'),
        ('E1', 'FEB-Gedung Manajemen'), ('E2', 'FEB-Gedung Akuntansi'), ('E3', 'FISIP-Gedung HI'), ('E4', 'Gedung Kuliah Bersama'), ('E5', 'Auditorium Utama'),
        ('F1', 'Asrama Putra'), ('F2', 'Asrama Putri'), ('F3', 'Kantin Pusat'), ('F4', 'Koperasi & Toko Buku'), ('F5', 'Gedung Keamanan & Parkir')
    ]
    
    for gid, gname in GEDUNG_DATA:
        g.add_node(gid, gname)
        bst.insert(gid, gname)
        
    edges = generate_edges(GEDUNG_DATA, seed=7)
    for u, v, w in edges:
        g.add_edge(u, v, w)

    print("="*70)
    print("🎓 SMART CAMPUS NAVIGATION SYSTEM - UNY")
    print("="*70)

    while True:
        try:
            cmd_input = input("\n[NavSys]> ").strip().split()
            if not cmd_input:
                continue
                
            cmd = cmd_input[0].upper()

            if cmd == "KELUAR":
                print(">> Menutup sistem. Terima kasih!")
                break
                
            elif cmd == "BANTUAN":
                print("\n1. CARI_GEDUNG <kode>\n2. JALUR <asal> <tujuan>\n3. JELAJAH_BFS <awal>\n4. JELAJAH_DFS <awal>\n5. TERISOLASI\n6. LAPORAN_GRAPH\n7. KELUAR")

            elif cmd == "CARI_GEDUNG":
                if len(cmd_input) < 2: continue
                kode = cmd_input[1].upper()
                hasil = bst.search(kode)
                print(f">> Ditemukan: {hasil}" if hasil else f">> [!] Kode '{kode}' tidak ditemukan.")

            elif cmd == "JALUR":
                if len(cmd_input) < 3: continue
                asal, tujuan = cmd_input[1].upper(), cmd_input[2].upper()
                if not bst.search(asal) or not bst.search(tujuan):
                    print(">> [!] Kode tidak valid.")
                    continue
                    
                dist, parent = dijkstra(g, asal)
                path = reconstruct_path(parent, asal, tujuan)
                if not path:
                    print(">> [!] Tidak ada jalur darat yang tersedia.")
                else:
                    rute_lengkap = [f"{p} ({bst.search(p)})" for p in path]
                    print(f">> Jarak Total: {dist[tujuan]} meter\n>> Rute: {' -> '.join(rute_lengkap)}")

            elif cmd == "JELAJAH_BFS":
                if len(cmd_input) < 2: continue
                print(f">> BFS Kunjung: {' -> '.join(bfs(g, cmd_input[1].upper()))}")
                
            elif cmd == "JELAJAH_DFS":
                if len(cmd_input) < 2: continue
                print(f">> DFS Kunjung: {' -> '.join(dfs(g, cmd_input[1].upper()))}")

            elif cmd == "TERISOLASI":
                terisolasi = get_isolated_nodes(g, "A1") 
                print(f">> Terisolasi: {', '.join(terisolasi)}" if terisolasi else ">> Aman. Semua terhubung ke A1.")

            elif cmd == "LAPORAN_GRAPH":
                total_edges = sum(len(g.neighbors(u)) for u in g.adj) // 2
                print(f"Total Gedung (V): {len(g.adj)} | Total Jalan (E): {total_edges}")
                
            else:
                print(">> Perintah tidak valid. Ketik BANTUAN.")

        except Exception as e:
            print(f">> [Sistem Error] Program di-recover. Pesan: {e}")

if __name__ == '__main__':
    main()