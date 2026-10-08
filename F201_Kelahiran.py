import fitz
import PySimpleGUI as sg
from datetime import datetime

FONT_SIZE, KOTAK = 9, 12
X_LABEL, X_TITIK, X_ISI = 40, 160, 170

# ================= FUNGSI PDF =================
def tulis_label(page, text, x, y, size=9, bold=False):
    page.insert_text((x, y), str(text), fontsize=size,
                     fontname="hebo" if bold else "helv")


def gambar_checkbox(page, x, y):
    page.draw_rect(fitz.Rect(x, y-10, x+12, y+2),
                   color=(0, 0, 0), width=0.7)


def gambar_baris_kotak(page, x, y, jumlah, text=""):
    text = str(text).upper()
    for i in range(jumlah):
        r = fitz.Rect(x+i*KOTAK, y, x+(i+1)*KOTAK, y+KOTAK)
        page.draw_rect(r, color=(0, 0, 0), width=0.5)
        if i < len(text):
            page.insert_text((x+i*KOTAK+2.5, y+9),
                             text[i], fontsize=FONT_SIZE)


def tulis_baris_kotak(page, label, y, jumlah, text=""):
    tulis_label(page, label, X_LABEL, y)
    tulis_label(page, ":", X_TITIK, y)
    gambar_baris_kotak(page, X_ISI, y-9, jumlah, text)

def tulis_nama_bayi_2_baris(page, y, text=""):
    text = str(text).upper()

    # Baris pertama - 30 kotak
    gambar_baris_kotak(page, X_ISI, y - 9, 30, text[:30])

    # Baris kedua - 30 kotak
    gambar_baris_kotak(page, X_ISI, y + 7, 30, text[30:60])

# ================= BUAT PDF =================
def buat_pdf(data):
    doc = fitz.open()
    page = doc.new_page(width=595, height=935)

    # ----- HEADER -----
    page.draw_rect(fitz.Rect(500, 8, 540, 22),
                   color=(0, 0, 0), width=0.7)
    tulis_label(page, "F-2.01", 504, 18)

    # ----- WILAYAH -----
    y = 35
    wilayah = [
        ("Provinsi", "Jawa Timur"), ("Kabupaten/Kota", "Kota Batu"),
        ("Kecamatan", data["kec"].upper()),
        ("Desa/Kelurahan", data["desa"].upper()),
        ("Kode Wilayah", data["kode"])
    ]

    for label, isi in wilayah:
        tulis_label(page, label, X_LABEL, y)
        tulis_label(page, ":", X_TITIK, y)
        tulis_label(page, isi, X_ISI, y)       # SEMUA TEKS BIASA
        y += 18

    # ----- JUDUL -----
    y += 18
    tulis_label(page, "FORMULIR PENCATATAN SIPIL DI DALAM WILAYAH NKRI",120, y, size=11)

    y += 16
    tulis_label(page, "Jenis Pelaporan Pencatatan Sipil", 40, y)
    gambar_checkbox(page, 210, y)
    tulis_label(page, "Kelahiran", 228, y)

    # DATA PELAPOR
    y += 16
    tulis_label(page, "DATA PELAPOR", 40, y, bold=True)
    y += 16

    pelapor = [
        ("Nama", "nama", 30),
        ("NIK", "nik", 16),
        ("No. Dok. Perjalanan", "dokumen", 16),
        ("Nomor Kartu Keluarga", "kk", 16),
        ("Kewarganegaraan", "kewarganegaraan", 16),
        ("Nomor Handphone", "hp", 16),
        ("Alamat Email", "email", 30)
    ]

    for label, key, jumlah in pelapor:
        tulis_baris_kotak(page, label, y, jumlah, data[key])
        y += 16

    # DATA SAKSI I
    y += 2
    tulis_label(page, "DATA SAKSI I", 40, y, bold=True)
    y += 16

    saksi = [
        ("Nama", "saksi1_nama", 30), ("NIK", "saksi1_nik", 16),
        ("Nomor Kartu Keluarga", "saksi1_kk", 16), ("Kewarganegaraan", "saksi1_warga", 16)
    ]

    for label, key, jumlah in saksi:
        tulis_baris_kotak(page, label, y, jumlah, data[key])
        y += 16

    # DATA SAKSI II
    y += 2
    tulis_label(page, "DATA SAKSI II", 40, y, bold=True)
    y += 16

    saksi2 = [
        ("Nama", "saksi2_nama", 30), ("NIK", "saksi2_nik", 16),
        ("Nomor Kartu Keluarga", "saksi2_kk", 16), ("Kewarganegaraan", "saksi2_warga", 16)
    ]

    for label, key, jumlah in saksi2:
        tulis_baris_kotak(page, label, y, jumlah, data[key])
        y += 16

    # DATA ORANG TUA
    y += 2
    tulis_label(page, "DATA ORANG TUA", 40, y, bold=True)
    y += 16

    ortu = [
        ("Nama Ayah", "ayah_nama", 30), ("NIK Ayah", "ayah_nik", 16), ("Tempat Lahir Ayah", "ayah_tempat", 16),
        ("Tanggal Lahir Ayah", "ayah_tgl", 10), ("Kewarganegaraan", "ayah_warga", 16), ("Nama Ibu", "ibu_nama", 30),
        ("NIK Ibu", "ibu_nik", 16), ("Tempat Lahir Ibu", "ibu_tempat", 16), ("Tanggal Lahir Ibu", "ibu_tgl", 10),
        ("Kewarganegaraan", "ibu_warga", 16)
    ]

    for label, key, jumlah in ortu:
        tulis_baris_kotak(page, label, y, jumlah, data[key])
        y += 16

    # DATA BAYI / ANAK
    y += 2
    tulis_label(page, "DATA BAYI / ANAK", X_LABEL, y, bold=True)
    y += 16

    # Nama
    tulis_label(page, "Nama", X_LABEL, y)
    tulis_label(page, ":", X_TITIK, y)
    tulis_nama_bayi_2_baris(page, y, data["bayi_nama"])
    y += 31

    # Jenis Kelamin
    tulis_label(page, "Jenis Kelamin", X_LABEL, y)
    tulis_label(page, ":", X_TITIK, y)

    x = X_ISI
    for key, text in [("jk_laki", "Laki-Laki"), ("jk_perempuan", "Perempuan")]:
        gambar_checkbox(page, x, y)
        if data.get(key):
            tulis_label(page, "X", x + 2, y)
        tulis_label(page, text, x + 16, y)
        x += 85

    y += 16

    # Tempat Dilahirkan
    tulis_label(page, "Tempat Dilahirkan", X_LABEL, y)
    tulis_label(page, ":", X_TITIK, y)

    x = X_ISI
    tempat = [
        ("td_rs", "RS/RB"), ("td_puskes", "Puskesmas"), ("td_polindes", "Polindes"),
        ("td_rumah", "Rumah"), ("td_lain", "Lainnya")
    ]

    for key, text in tempat:
        gambar_checkbox(page, x, y)
        if data.get(key):
            tulis_label(page, "X", x + 2, y)
        tulis_label(page, text, x + 16, y)
        x += 75

    y += 16

    # Tempat Kelahiran
    tulis_baris_kotak(page, "Tempat Kelahiran", y, 14, data["bayi_tempat"])
    y += 16

    # Hari, Tanggal
    tulis_label(page, "Hari", X_LABEL, y)
    tulis_label(page, ":", X_TITIK, y)
    gambar_baris_kotak(page, X_ISI, y - 9, 6, data["bayi_hari"])

    tulis_label(page, "Tanggal", X_ISI + 85, y)
    tulis_label(page, ":", X_ISI + 125, y)
    gambar_baris_kotak(page, X_ISI + 140, y - 9, 10, data["bayi_tgl"])

    y += 16

    # Pukul
    tulis_label(page, "Pukul", X_LABEL, y)
    tulis_label(page, ":", X_TITIK, y)
    gambar_baris_kotak(page, X_ISI, y - 9, 6, data["bayi_pukul"])

    y += 16

    # Jenis Kelahiran
    tulis_label(page, "Jenis Kelahiran", X_LABEL, y)
    tulis_label(page, ":", X_TITIK, y)

    x = X_ISI
    jenis = [
        ("jkl_tunggal", "Tunggal"), ("jkl_2", "Kembar 2"), ("jkl_3", "Kembar 3"),
        ("jkl_4", "Kembar 4"), ("jkl_lain", "Lainnya")
    ]

    for key, text in jenis:
        gambar_checkbox(page, x, y)
        if data.get(key):
            tulis_label(page, "X", x + 2, y)
        tulis_label(page, text, x + 16, y)
        x += 75

    y += 16

    # Kelahiran Ke
    tulis_baris_kotak(page, "Kelahiran Ke", y, 1, data["bayi_ke"])
    y += 16

    # Penolong Kelahiran
    tulis_label(page, "Penolong Kelahiran", X_LABEL, y)
    tulis_label(page, ":", X_TITIK, y)

    x = X_ISI
    penolong = [
        ("pk_dokter", "Dokter"), ("pk_bidan", "Bidan"),
        ("pk_dukun", "Dukun"), ("pk_lain", "Lainnya")
    ]

    for key, text in penolong:
        gambar_checkbox(page, x, y)
        if data.get(key):
            tulis_label(page, "X", x + 2, y)
        tulis_label(page, text, x + 16, y)
        x += 85

    y += 16

    # Berat Bayi
    tulis_label(page, "Berat Bayi", X_LABEL, y)
    tulis_label(page, ":", X_TITIK, y)
    gambar_baris_kotak(page, X_ISI, y - 9, 3, data["bayi_berat"])
    tulis_label(page, "Kg", X_ISI + 45, y)

    y += 16

    # Panjang Bayi
    tulis_label(page, "Panjang Bayi", X_LABEL, y)
    tulis_label(page, ":", X_TITIK, y)
    gambar_baris_kotak(page, X_ISI, y - 9, 3, data["bayi_panjang"])
    tulis_label(page, "CM", X_ISI + 45, y)

    # ----- TANGGAL & NAMA PELAPOR -----
    hari_ini = datetime.now().strftime("%d %B %Y")
    tulis_label(page, f"Batu, {hari_ini}", 350, 852)

    # Titik-titik sekarang diisi nama pelapor
    tulis_label(page, data["nama"], 350, 892)

    nama_bayi = str(data["bayi_nama"]).strip()
    nama_file = nama_bayi.split()[0].upper() if nama_bayi else "F201_Hasil_Isi"
    nama_file = f"Kelahiran_{nama_file}.pdf"

    doc.save(nama_file)
    sg.popup(f"Selesai!\nFile: {nama_file}")

# DATA FIELD UNTUK GUI
def field(label, key, size=24):
    return [sg.Text(label, size=(22, 1)),
            sg.Input(key=key, size=(size, 1))]

def section(judul, fields):
    return sg.Frame(
        judul,
        [[sg.Text(label, size=(22, 1)),
          sg.Input(key=key, size=(size, 1))]
         for label, key, size in fields],
        expand_x=True,
        relief=sg.RELIEF_GROOVE,
        border_width=1
    )

# FIELD
pelapor_fields = [
    ("Nama", "nama", 30), ("NIK", "nik", 20), ("No. Dok. Perjalanan", "dokumen", 20),
    ("Nomor Kartu Keluarga", "kk", 20), ("Kewarganegaraan", "kewarganegaraan", 20),
    ("Nomor Handphone", "hp", 20), ("Alamat Email", "email", 30)
]

saksi1_fields = [
    ("Nama", "saksi1_nama", 30), ("NIK", "saksi1_nik", 20),
    ("Nomor Kartu Keluarga", "saksi1_kk", 20), ("Kewarganegaraan", "saksi1_warga", 20)
]

saksi2_fields = [
    ("Nama", "saksi2_nama", 30), ("NIK", "saksi2_nik", 20),
    ("Nomor Kartu Keluarga", "saksi2_kk", 20), ("Kewarganegaraan", "saksi2_warga", 20)
]

ortu_fields = [
    ("Nama Ayah", "ayah_nama", 30), ("NIK Ayah", "ayah_nik", 20), ("Tempat Lahir Ayah", "ayah_tempat", 20),
    ("Tanggal Lahir Ayah", "ayah_tgl", 12), ("Kewarganegaraan", "ayah_warga", 20), ("Nama Ibu", "ibu_nama", 30),
    ("NIK Ibu", "ibu_nik", 20), ("Tempat Lahir Ibu", "ibu_tempat", 20),
    ("Tanggal Lahir Ibu", "ibu_tgl", 12), ("Kewarganegaraan", "ibu_warga", 20)
]

def section_bayi():
    rows = [
        [sg.Text("Nama", size=(20,1)),
         sg.Input(key="bayi_nama", size=(30,1))],

        [sg.Text("Jenis Kelamin", size=(20,1)),
         sg.Radio("Laki-Laki", "JK", key="jk_laki"),
         sg.Radio("Perempuan", "JK", key="jk_perempuan")],

        [sg.Text("Tempat Dilahirkan", size=(20,1)),
         sg.Radio("RS/RB", "TD", key="td_rs"),
         sg.Radio("Puskesmas", "TD", key="td_puskes"),
         sg.Radio("Polindes", "TD", key="td_polindes"),
         sg.Radio("Rumah", "TD", key="td_rumah"),
         sg.Radio("Lainnya", "TD", key="td_lain")],

        [sg.Text("Tempat Kelahiran", size=(20,1)),
         sg.Input(key="bayi_tempat", size=(20,1))],

        [sg.Text("Hari", size=(20,1)), sg.Input(key="bayi_hari", size=(10,1)), sg.Text("Tanggal", size=(8,1)),
         sg.Input(key="bayi_tgl", size=(10,1)), sg.Text("Pukul", size=(6,1)), sg.Input(key="bayi_pukul", size=(7,1))],

        [sg.Text("Jenis Kelahiran", size=(20,1)), sg.Radio("Tunggal", "JKL", key="jkl_tunggal"),
         sg.Radio("Kembar 2", "JKL", key="jkl_2"), sg.Radio("Kembar 3", "JKL", key="jkl_3"),
         sg.Radio("Kembar 4", "JKL", key="jkl_4"), sg.Radio("Lainnya", "JKL", key="jkl_lain")],

        [sg.Text("Kelahiran Ke", size=(20,1)), sg.Input(key="bayi_ke", size=(5,1))],

        [sg.Text("Penolong Kelahiran", size=(20,1)), sg.Radio("Dokter", "PK", key="pk_dokter"),
         sg.Radio("Bidan", "PK", key="pk_bidan"), sg.Radio("Dukun", "PK", key="pk_dukun"),
         sg.Radio("Lainnya", "PK", key="pk_lain")],

        [sg.Text("Berat Bayi (Kg)", size=(20,1)), sg.Input(key="bayi_berat", size=(8,1)),
         sg.Text("Panjang Bayi (CM)", size=(16,1)), sg.Input(key="bayi_panjang", size=(8,1))]
    ]

    return sg.Frame("DATA BAYI / ANAK", rows, expand_x=True)

# GUI
def section_wilayah():
    rows = [
        [sg.Text("Kecamatan", size=(16,1)), sg.Input(key="kec", size=(22,1)), sg.Text("Desa/Kelurahan", size=(16,1)),
         sg.Input(key="desa", size=(22,1)), sg.Text("Kode Wilayah", size=(16, 1)), sg.Input(key="kode", size=(22, 1))]
    ]

    return sg.Frame("DATA WILAYAH", rows, expand_x=True)

def buat_layout():
    layout = [
        [sg.Text("FORMULIR F-2.01 KELAHIRAN",
                 font=("Arial", 15, "bold"),
                 expand_x=True,
                 justification="center")],
    
        [section_wilayah()],
    
        [sg.HorizontalSeparator()],
    
        # ===== BARIS ATAS =====
        [
            sg.Column(
                [[section("DATA PELAPOR", pelapor_fields)]],
                vertical_alignment="top",
                expand_x=True,
                expand_y=True
            ),
    
            sg.VSeparator(),
    
            sg.Column(
                [
                    [section("DATA SAKSI I", saksi1_fields)],
                    [sg.Text("")],
                    [section("DATA SAKSI II", saksi2_fields)]
                ],
                vertical_alignment="top",
                expand_x=True,
                expand_y=True
            )
        ],
    
        [sg.HorizontalSeparator()],
    
        # ===== BARIS BAWAH =====
        [
            sg.Column([[section("DATA ORANG TUA", ortu_fields)]], vertical_alignment="top", expand_x=True, expand_y=True),
            sg.VSeparator(),
            sg.Column([[section_bayi()]], vertical_alignment="top", expand_x=True, expand_y=True)
        ],
    
        [sg.HorizontalSeparator()],
    
        [
            sg.Push(),
            sg.Button("REFRESH", size=(15,2)),
            sg.Button("GENERATE PDF", size=(18,2)),
            sg.Button("KELUAR", size=(15,2)),
            sg.Push()
        ]
    ]
    return layout

# ================= JALANKAN FORM KELAHIRAN MANDIRI =================

def jalankan_mandiri():
    layout = buat_layout()
    window = sg.Window("F-2.01 - Formulir Pencatatan Kelahiran", layout, resizable=True, finalize=True)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "KELUAR"):
            break
        if event == "REFRESH":
            for key in values:
                if key in window.AllKeysDict:
                    element = window[key]
                    if isinstance(element, sg.Input):
                        element.update("")
                    elif isinstance(element, sg.Radio):
                        element.update(False)
            continue

        if event == "GENERATE PDF":
            buat_pdf(values)

    window.close()

# Jalankan mandiri hanya jika file dibuka langsung
if __name__ == "__main__":
    jalankan_mandiri()
