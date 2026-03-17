import time

def print_board(board, step, action):
    print(f"Langkah {step} - {action}:")
    for row in board:
        print(" ".join(row))
    print("-" * 20)
    time.sleep(0.8) # Jeda waktu agar visualisasi mudah diikuti

def is_safe(board, row, col, N):
    # Cek baris di sebelah kiri
    for i in range(col):
        if board[row][i] == 'Q':
            return False
            
    # Cek diagonal atas kiri
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
            
    # Cek diagonal bawah kiri
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
            
    return True

def solve_n_queens_util(board, col, N, step_counter):
    # Base case: Apakah semua bidak ratu (N) sudah diletakkan?
    if col >= N:
        return True

    # Cek semua baris di kolom saat ini
    for i in range(N):
        if is_safe(board, i, col, N):
            # Jika aman, letakkan ratu (Q)
            board[i][col] = 'Q'
            step_counter[0] += 1
            print_board(board, step_counter[0], f"Mencoba Ratu di Baris {i}, Kolom {col}")

            # Rekursi: geser ke kolom selanjutnya
            if solve_n_queens_util(board, col + 1, N, step_counter):
                return True

            # Jika penempatan tidak menghasilkan solusi, BACKTRACKING
            board[i][col] = '.'
            step_counter[0] += 1
            print_board(board, step_counter[0], f"BACKTRACK: Mencabut Ratu dari Baris {i}, Kolom {col}")

    return False

def solve_n_queens(N):
    # Inisialisasi papan kosong dengan titik (.)
    board = [['.' for _ in range(N)] for _ in range(N)]
    step_counter = [0]
    
    print(f"=== Memulai N-Queen Problem ({N}x{N}) ===")
    print("Mencari semua kemungkinan kombinasi dalam menyelesaikan masalah [cite: 4]\n")
    
    if not solve_n_queens_util(board, 0, N, step_counter):
        print("Solusi tidak dapat dicapai.")
        return False
        
    print("=== Solusi Akhir Berhasil Ditemukan! ===")
    for row in board:
        print(" ".join(row))
    return True

if __name__ == "__main__":
    # Menggunakan N=4 untuk demonstrasi
    solve_n_queens(4)