import time
import random
import sys
import os

# Menambahkan root directory proyek ke path agar bisa melakukan import dari folder src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Mengimpor modul struktur data dan algoritma yang sudah di buat
from src.modules.modul_1_graph import Graph
from src.modules.modul_2_dijkstra import dijkstra
from src.modules.modul_3_traversal import bfs

def generate_random_graph(num_nodes: int, num_edges: int) -> Graph:
    """Fungsi helper untuk membuat graf dengan V dan E tertentu untuk uji coba."""
    g = Graph()
    nodes = [f"N{i}" for i in range(num_nodes)]
    
    # Daftarkan semua node
    for node in nodes:
        g.add_node(node, f"Gedung {node}")
        
    # Buat spanning tree terlebih dahulu, agar graf dipastikan terhubung.
    for i in range(1, num_nodes):
        g.add_edge(nodes[i-1], nodes[i], random.randint(10, 100))
        
    # Tambahkan sisa edge secara acak
    sisa_edge = num_edges - (num_nodes - 1)
    if sisa_edge > 0:
        for _ in range(sisa_edge):
            u, v = random.sample(nodes, 2)
            g.add_edge(u, v, random.randint(10, 100))
            
    return g

def run_benchmark():
    # 3 Ukuran Dataset: (Node/V, Edge/E)
    datasets = [(30, 55), (150, 300), (300, 1000)]
    
    print("=" * 75)
    print("LAPORAN EKSPERIMEN PERBANDINGAN RUNTIME (DIJKSTRA vs BFS)")
    print("=" * 75)
    print(f"{'Dataset (V, E)':<20} | {'Dijkstra (Detik)':<22} | {'BFS (Detik)':<22}")
    print("-" * 75)
    
    for v, e in datasets:
        g = generate_random_graph(v, e)
        source = "N0"
        
        # Benchmark Algoritma Dijkstra
        start = time.perf_counter()
        for _ in range(100):  # Dilakukan iterasi 100x agar waktunya stabil & bisa diukur
            dijkstra(g, source)
        dijkstra_time = (time.perf_counter() - start) / 100
        
        # Benchmark Algoritma BFS
        start = time.perf_counter()
        for _ in range(100):
            bfs(g, source)
        bfs_time = (time.perf_counter() - start) / 100
        
        # Cetak hasil baris per baris
        print(f"V={v:<4}, E={e:<6} | {dijkstra_time:.6f} detik        | {bfs_time:.6f} detik")
        
    print("=" * 75)
    print("*Catatan: Waktu di atas adalah nilai rata-rata dari 100 kali eksekusi algoritma.")

if __name__ == "__main__":
    run_benchmark()