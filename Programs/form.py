import tkinter as tk
from tkinter import filedialog

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    entry_path.delete(0, tk.END)
    entry_path.insert(0, file_path)

def submit():
    selected_file = entry_path.get()
    # Lakukan sesuatu dengan file yang dipilih, misalnya cetak path file
    print("File yang dipilih:", selected_file)
    # Anda dapat menambahkan logika lain sesuai kebutuhan

# Membuat jendela utama
root = tk.Tk()
root.title("Popup Pemilihan File MP4")

# Membuat label
label_instruction = tk.Label(root, text="Pilih file MP4:")
label_instruction.pack(pady=10)

# Membuat entry untuk menampilkan path file
entry_path = tk.Entry(root, width=40)
entry_path.pack(pady=10)

# Membuat tombol untuk membuka dialog pemilihan file
button_browse = tk.Button(root, text="Browse", command=browse_file)
button_browse.pack(pady=10)

# Membuat tombol untuk mengonfirmasi pemilihan file
button_submit = tk.Button(root, text="Submit", command=submit)
button_submit.pack(pady=10)

# Menjalankan jendela
root.mainloop()
