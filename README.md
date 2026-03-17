# Implementasi Algoritma Backtracking: N-Queen Problem

Repositori ini dibuat untuk memenuhi tugas mata kuliah Algoritma, fokus pada implementasi dan visualisasi algoritma **Backtracking**. Masalah yang diselesaikan adalah **N-Queen Problem**, di mana tujuannya adalah meletakkan $N$ bidak ratu pada papan catur $N \times N$ tanpa ada ratu yang saling menyerang.

## Deskripsi Algoritma
[cite_start]Backtracking adalah teknik pencarian solusi secara **incremental** (satu per satu)[cite: 7]. [cite_start]Prinsip utamanya adalah mencari semua kemungkinan kombinasi [cite: 4] [cite_start]dan segera **meng-eliminasi solusi** yang tidak memenuhi batasan (**constraint**) yang ditentukan[cite: 7]. [cite_start]Jika program mencapai titik di mana tidak ada jalan lagi, program akan kembali ke langkah sebelumnya di mana ada percabangan dan mencoba jalur lain[cite: 28].

### Batasan (Constraints)
[cite_start]Sesuai dengan prinsip masalah N-Queen[cite: 113]:
1. Satu kolom tidak boleh berisi lebih dari satu bidak ratu.
2. Satu baris tidak boleh berisi lebih dari satu bidak ratu.
3. Diagonal tidak boleh berisi lebih dari satu bidak ratu.
4. Semua bidak ratu tidak boleh bisa memakan satu sama lain dalam satu langkah.

## Dokumentasi Penyelesaian

### Pseudocode
[cite_start]Berikut adalah logika penyelesaian yang diimplementasikan dalam program ini[cite: 114, 115, 116, 117]:

1. **Mulai** dari baris/kolom pertama.
2. **Cek Keamanan**: Sebelum meletakkan ratu, cek apakah posisi tersebut aman dari serangan ratu lain.
3. **Tempatkan Bidak**:
   - Jika aman, letakkan bidak ratu dan geser ke baris/kolom selanjutnya.
4. **Rekursi**: Ulangi langkah untuk bidak ratu berikutnya.
5. **Backtrack**:
   - Jika solusi tidak dapat dicapai di jalur tersebut, berhenti dan tandai sebagai *unsolved*.
   - Hapus bidak ratu dari posisi saat ini dan kembali ke langkah sebelumnya untuk mencoba posisi kolom/baris yang berbeda.
6. **Selesai** jika semua $N$ ratu berhasil diletakkan.

### Flowchart Sederhana
```text
[Mulai] 
   |
[Cek: Apakah semua Ratu sudah diletakkan?] --(Ya)--> [Selesai/Solusi Ditemukan]
   | (Belum)
   v
[Coba letakkan Ratu di kolom/baris berikutnya]
   |
[Cek Aman? (Constraint Check)] --(Tidak)--> [Coba kolom berikutnya]
   | (Ya)
   v
[Simpan Posisi & Lanjut Rekursi]
   |
[Apakah jalur ini buntu?] --(Ya)--> [Hapus Ratu (Backtrack)] --> [Coba kolom berikutnya]
