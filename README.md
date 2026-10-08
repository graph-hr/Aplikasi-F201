# Aplikasi F201

Aplikasi desktop sederhana untuk membantu pengisian dan pembuatan dokumen **F-2.01** secara digital.

Aplikasi ini dibuat menggunakan **Python**, dengan antarmuka grafis dan kemampuan menghasilkan dokumen PDF.

## Fitur

* Pengisian data **F-2.01 Kelahiran**
* Pengisian data **F-2.01 Kematian**
* Pembuatan dokumen PDF
* Tombol **Refresh** untuk mengosongkan/memperbarui form
* Dapat dijalankan sebagai aplikasi Windows tanpa harus menginstal Python pada komputer pengguna

## Struktur Program

```text
Aplikasi-F201/
│
├── Main.py
├── F201_Kelahiran.py
├── F201_Kematian.py
├── Fungsi_Umum.py
├── Aplikasi_F201.spec
├── .gitignore
└── README.md
```

### Penjelasan File

| File                 | Fungsi                                                  |
| -------------------- | ------------------------------------------------------- |
| `Main.py`            | Menu utama aplikasi                                     |
| `F201_Kelahiran.py`  | Modul pengisian F-2.01 Kelahiran                        |
| `F201_Kematian.py`   | Modul pengisian F-2.01 Kematian                         |
| `Fungsi_Umum.py`     | Fungsi-fungsi umum yang digunakan oleh aplikasi         |
| `Aplikasi_F201.spec` | Konfigurasi PyInstaller                                 |
| `.gitignore`         | Menentukan file/folder yang tidak perlu disimpan di Git |
| `README.md`          | Dokumentasi proyek                                      |

## Teknologi

* Python
* PySimpleGUI
* PyMuPDF
* PyInstaller
* Git
* GitHub

## Menjalankan Aplikasi

Aplikasi dapat dijalankan melalui Python pada lingkungan pengembangan.

Untuk distribusi ke komputer lain, aplikasi dapat dibuat menjadi aplikasi Windows menggunakan **PyInstaller**.

Build yang digunakan dalam pengembangan:

```powershell
python -m PyInstaller --onedir --windowed --name Aplikasi_F201 Main.py
```

Hasil build berada di:

```text
dist\Aplikasi_F201\
```

Folder hasil build tersebut dapat digunakan untuk menjalankan aplikasi pada komputer Windows lain tanpa lingkungan Python.

## Status Proyek

**Versi awal — dalam tahap pengembangan.**

Fokus saat ini adalah menjaga aplikasi tetap stabil sebelum menambahkan fitur atau modul baru.

## Catatan

Proyek ini dikembangkan secara bertahap dengan tujuan agar aplikasi dapat terus dikembangkan menjadi alat yang lebih lengkap dan mudah digunakan.

---

**Aplikasi F201**
Developed by **graph-hr**
