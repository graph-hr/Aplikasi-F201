import fitz
import PySimpleGUI as sg
from datetime import datetime


# KONSTANTA
FONT_SIZE = 9
KOTAK = 12

X_LABEL = 40
X_TITIK = 160
X_ISI = 170

# FUNGSI PDF

def tulis_label(page, text, x, y, size=9, bold=False):
    """
    Menulis teks pada PDF.
    """
    font = "hebo" if bold else "helv"

    page.insert_text((x, y), str(text), fontsize=size, fontname=font)

def gambar_checkbox(page, x, y):
    """
    Membuat kotak checkbox.
    """
    page.draw_rect(fitz.Rect(x, y - 10, x + 12, y + 2), color=(0, 0, 0), width=0.7)

def gambar_baris_kotak(page, x, y, jumlah, text=""):
    """
    Membuat baris kotak per karakter.
    """
    text = str(text).upper()

    for i in range(jumlah):

        r = fitz.Rect(x + i * KOTAK, y, x + (i + 1) * KOTAK, y + KOTAK)

        page.draw_rect(r, color=(0, 0, 0), width=0.5)

        if i < len(text):

            page.insert_text((x + i * KOTAK + 2.5, y + 9), text[i], fontsize=FONT_SIZE, fontname="helv")

def tulis_baris_kotak(page, label, y, jumlah, text=""):
    """
    Label + titik dua + baris kotak.
    """
    tulis_label(page, label, X_LABEL, y)
    tulis_label(page, ":", X_TITIK, y)
    gambar_baris_kotak(page, X_ISI, y - 9, jumlah, text)

# FUNGSI DATA KEMATIAN

def tulis_data_kematian(page, y, data):

    # JUDUL

    tulis_label(page,"KEMATIAN", X_LABEL, y, bold=True)

    y += 18

    # 1. NIK

    tulis_label(page, "NIK", X_LABEL, y)
    tulis_label(page, ":", X_TITIK, y)
    gambar_baris_kotak(page, X_ISI, y - 9,16, data.get("kematian_nik", ""))

    y += 16

    # 2. NAMA LENGKAP

    tulis_label(page, "Nama Lengkap", X_LABEL, y)
    tulis_label(page, ":", X_TITIK, y)
    gambar_baris_kotak(page, X_ISI, y - 9,30, data.get("kematian_nama", ""))

    y += 16

    # 3. TANGGAL KEMATIAN

    tulis_label(page, "Tanggal Kematian", X_LABEL, y)
    tulis_label(page, ":", X_TITIK, y)

    # Tgl
    tulis_label(page, "Tgl:", X_ISI, y)
    gambar_baris_kotak(page, X_ISI + 30, y - 9, 2, data.get("kematian_tgl", ""))

    # Bln
    tulis_label(page, "Bln:", X_ISI + 65, y)
    gambar_baris_kotak(page, X_ISI + 98, y - 9, 2, data.get("kematian_bln", ""))

    # Thn
    tulis_label(page, "Thn:", X_ISI + 135, y)
    gambar_baris_kotak(page, X_ISI + 168, y - 9, 4, data.get("kematian_thn", ""))
    y += 16

    # 4. PUKUL

    tulis_label(page, "Pukul", X_LABEL, y)
    tulis_label(page, ":", X_TITIK, y)
    gambar_baris_kotak(page, X_ISI, y - 9, 2, data.get("kematian_jam", ""))
    tulis_label(page, ":", X_ISI + 29, y)
    gambar_baris_kotak(page, X_ISI + 40, y - 9, 2, data.get("kematian_menit", ""))
    y += 16

    # 5. SEBAB KEMATIAN

    tulis_label(page, "Sebab Kematian", X_LABEL, y)
    tulis_label(page, ":", X_TITIK, y)

    # Baris pertama

    sebab_baris_1 = [
        ("sebab_sakit", "1. Sakit biasa/tua"), ("sebab_wabah", "2. Wabah Penyakit"),
        ("sebab_kecelakaan", "3. Kecelakaan"), ("sebab_kriminalitas", "4. Kriminalitas")
    ]

    x = X_ISI

    posisi_sebab_1 = [x, x + 105, x + 210, x + 300]

    for (key, text), xpos in zip(sebab_baris_1, posisi_sebab_1):
        gambar_checkbox(page, xpos, y)

        if data.get(key):
            tulis_label(page, "X", xpos + 2, y)

        tulis_label(page, text, xpos + 16, y)
    y += 16

    # Baris kedua
    sebab_baris_2 = [("sebab_bunuh_diri", "5. Bunuh Diri"), ("sebab_lainnya", "6. Lainnya")]
    x = X_ISI

    for key, text in sebab_baris_2:

        gambar_checkbox(page, x, y)

        if data.get(key):
            tulis_label(page, "X", x + 2, y)

        tulis_label(page, text, x + 16, y)

        x += 165

    y += 16

    # 6. TEMPAT KEMATIAN

    tulis_label(page, "Tempat Kematian", X_LABEL, y)
    tulis_label(page, ":", X_TITIK, y)
    gambar_baris_kotak(page, X_ISI, y - 9, 30, data.get("kematian_tempat", ""))
    y += 16

    # 7. YANG MENERANGKAN

    tulis_label(page, "Yang Menerangkan", X_LABEL, y)
    tulis_label(page, ":", X_TITIK, y)

    # Baris pertama
    menerangkan_1 = [("terang_dokter", "1. Dokter"), ("terang_nakes", "2. Tenaga Kesehatan")]

    x = X_ISI

    for key, text in menerangkan_1:
        gambar_checkbox(page, x, y)

        if data.get(key):
            tulis_label(page, "X", x + 2, y)

        tulis_label(page, text, x + 16, y)
        x += 165

    y += 16

    # Baris kedua
    menerangkan_2 = [("terang_polisi", "3. Kepolisian"), ("terang_lainnya", "4. Lainnya")]
    x = X_ISI

    for key, text in menerangkan_2:
        gambar_checkbox(page, x, y)

        if data.get(key):
            tulis_label(page,"X", x + 2, y)

        tulis_label(page, text, x + 16, y)
        x += 165

    return y + 16

# BUAT PDF

def buat_pdf(data):
    doc = fitz.open()
    page = doc.new_page(width=595, height=935)

    # HEADER
    page.draw_rect(fitz.Rect(500, 8, 540, 22), color=(0, 0, 0), width=0.7)
    tulis_label(page, "F-2.01", 504, 18)

    # DATA WILAYAH
    y = 35
    wilayah = [
        ("Provinsi", "Jawa Timur"), ("Kabupaten/Kota", "Kota Batu"), ("Kecamatan", data.get("kec", "").upper()),
        ("Desa/Kelurahan", data.get("desa", "").upper()), ("Kode Wilayah", data.get("kode", ""))
    ]
    for label, isi in wilayah:
        tulis_label(page, label, X_LABEL, y)
        tulis_label(page, ":", X_TITIK, y)
        tulis_label(page, isi, X_ISI, y)

        y += 18

    # JUDUL FORM
    y += 14

    tulis_label(page, "FORMULIR PENCATATAN SIPIL DI DALAM WILAYAH NKRI", 120, y, size=11)
    y += 16

    tulis_label(page, "Jenis Pelaporan Pencatatan Sipil", 40, y)
    gambar_checkbox(page, 210, y)
    tulis_label(page, "Kematian",228, y)

    # DATA PELAPOR
    y += 18

    tulis_label(page, "DATA PELAPOR", 40, y,  bold=True)
    y += 16

    pelapor = [
        ("Nama", "nama", 30), ("NIK", "nik", 16), ("No. Dok. Perjalanan", "dokumen", 16),
        ("Nomor Kartu Keluarga", "kk", 16), ("Kewarganegaraan", "kewarganegaraan", 16),
        ("Nomor Handphone", "hp", 16), ("Alamat Email", "email", 30)
    ]

    for label, key, jumlah in pelapor:
        tulis_baris_kotak(page, label, y, jumlah, data.get(key, ""))
        y += 16

    # DATA SAKSI I
    y += 2

    tulis_label(page, "DATA SAKSI I", 40, y, bold=True)
    y += 16

    saksi1 = [
        ("Nama", "saksi1_nama", 30), ("NIK", "saksi1_nik", 16),
        ("Nomor Kartu Keluarga", "saksi1_kk", 16), ("Kewarganegaraan", "saksi1_warga", 16)
    ]

    for label, key, jumlah in saksi1:
        tulis_baris_kotak(page, label, y, jumlah,  data.get(key, ""))
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
        tulis_baris_kotak(page, label, y, jumlah, data.get(key, ""))
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
        tulis_baris_kotak(page, label, y, jumlah, data.get(key, ""))
        y += 16

    # DATA KEMATIAN
    y += 12

    tulis_data_kematian(page, y, data)

    # TANGGAL & NAMA PELAPOR
    hari_ini = datetime.now().strftime("%d %B %Y")

    tulis_label(page, f"Batu, {hari_ini}", 380, 822)

    tulis_label(page, data.get("nama", ""), 380, 872)

    # NAMA FILE
    nama_mayit = str(data.get("kematian_nama", "")).strip()
    nama_file = (nama_mayit.split()[0]
        if nama_mayit
        else "F201_Hasil_Isi"
    )

    nama_file = (f"Kematian_{nama_file}.pdf")

    # SIMPAN PDF
    doc.save(nama_file)
    doc.close()
    sg.popup(f"Selesai!\nFile: {nama_file}")

# FUNGSI GUI
def field(label, key, size=24):

    return [
        sg.Text(label, size=(22, 1)), sg.Input(key=key, size=(size, 1))
    ]

def section(judul, fields):

    return sg.Frame(judul,
        [
            [
                sg.Text(label, size=(22, 1)),
                sg.Input(key=key, size=(size, 1))
            ]

            for label, key, size in fields
        ],

        expand_x=True,
        relief=sg.RELIEF_GROOVE,
        border_width=1
    )

# DATA FIELD PELAPOR
pelapor_fields = [
    ("Nama", "nama", 30), ("NIK", "nik", 20), ("No. Dok. Perjalanan", "dokumen", 20),
    ("Nomor Kartu Keluarga", "kk", 20), ("Kewarganegaraan", "kewarganegaraan", 20),
    ("Nomor Handphone", "hp", 20), ("Alamat Email", "email", 30)
]

# DATA FIELD SAKSI I
saksi1_fields = [
    ("Nama", "saksi1_nama", 30), ("NIK", "saksi1_nik", 20),
    ("Nomor Kartu Keluarga", "saksi1_kk", 20), ("Kewarganegaraan", "saksi1_warga", 20)
]

# DATA FIELD SAKSI II
saksi2_fields = [
    ("Nama", "saksi2_nama", 30), ("NIK", "saksi2_nik", 20),
    ("Nomor Kartu Keluarga", "saksi2_kk", 20), ("Kewarganegaraan", "saksi2_warga", 20)
]

# DATA FIELD ORANG TUA
ortu_fields = [
    ("Nama Ayah", "ayah_nama", 30), ("NIK Ayah", "ayah_nik", 20), ("Tempat Lahir Ayah", "ayah_tempat", 20),
    ("Tanggal Lahir Ayah", "ayah_tgl", 12), ("Kewarganegaraan", "ayah_warga", 20),
    ("Nama Ibu", "ibu_nama", 30), ("NIK Ibu", "ibu_nik", 20), ("Tempat Lahir Ibu", "ibu_tempat", 20),
    ("Tanggal Lahir Ibu", "ibu_tgl", 12), ("Kewarganegaraan", "ibu_warga", 20)
]

# DATA KEMATIAN - GUI
def section_kematian():

    rows = [
        # 1. NIK
        [
            sg.Text("NIK", size=(20, 1)),
            sg.Input(key="kematian_nik", size=(25, 1))
        ],

        # 2. NAMA LENGKAP
        [
            sg.Text("Nama Lengkap", size=(20, 1)),
            sg.Input(key="kematian_nama", size=(35, 1))
        ],

        # 3. TANGGAL KEMATIAN
        [
            sg.Text("Tanggal Kematian", size=(20, 1)),
            sg.Text("Tgl"),
            sg.Input(key="kematian_tgl", size=(5, 1)),
            sg.Text("Bln"),
            sg.Input(key="kematian_bln", size=(5, 1)),
            sg.Text("Thn"),
            sg.Input(key="kematian_thn", size=(7, 1))
        ],

        # 4. PUKUL
        [
            sg.Text("Pukul", size=(20, 1)),
            sg.Input(key="kematian_jam", size=(5, 1)),
            sg.Text(":"),
            sg.Input(key="kematian_menit", size=(5, 1))
        ],

        # 5. SEBAB KEMATIAN
        [
            sg.Text("Sebab Kematian", size=(20, 1)),
            sg.Checkbox("1. Sakit biasa/tua", key="sebab_sakit"),
            sg.Checkbox("2. Wabah Penyakit", key="sebab_wabah")
        ],

        [
            sg.Text("", size=(20, 1)),
            sg.Checkbox("3. Kecelakaan", key="sebab_kecelakaan"),
            sg.Checkbox("4. Kriminalitas", key="sebab_kriminalitas")
        ],

        [
            sg.Text("", size=(20, 1)),
            sg.Checkbox("5. Bunuh Diri", key="sebab_bunuh_diri"),

            sg.Checkbox("6. Lainnya", key="sebab_lainnya")
        ],

        # 6. TEMPAT KEMATIAN
        [
            sg.Text("Tempat Kematian", size=(20, 1)),
            sg.Input(key="kematian_tempat", size=(35, 1))
        ],

        # 7. YANG MENERANGKAN
        [
            sg.Text("Yang Menerangkan", size=(20, 1)),
            sg.Radio("1. Dokter", "MENERANGKAN", key="terang_dokter"),
            sg.Radio("2. Tenaga Kesehatan","MENERANGKAN", key="terang_nakes")
        ],

        [
            sg.Text("", size=(20, 1)),
            sg.Radio("3. Kepolisian", "MENERANGKAN", key="terang_polisi"),
            sg.Radio("4. Lainnya", "MENERANGKAN", key="terang_lainnya")
        ]
    ]

    return sg.Frame("DATA KEMATIAN", rows, expand_x=True)

# DATA WILAYAH
def section_wilayah():

    rows = [

        [
            sg.Text("Kecamatan", size=(16, 1)),
            sg.Input(key="kec", size=(22, 1)),
            sg.Text("Desa/Kelurahan", size=(16, 1)),
            sg.Input(key="desa", size=(22, 1)),
            sg.Text("Kode Wilayah", size=(16, 1)),
            sg.Input(key="kode", size=(22, 1))
        ]
    ]

    return sg.Frame("DATA WILAYAH", rows, expand_x=True)

# LAYOUT GUI
def buat_layout():
    layout = [
        # JUDUL
        [
            sg.Text("FORMULIR F-2.01 KEMATIAN", font=("Arial", 15, "bold"),
                expand_x=True,
                justification="center"
            )
        ],
    
        # WILAYAH
        [section_wilayah()],
        [sg.HorizontalSeparator()],
    
        # BARIS ATAS
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
        [sg.HorizontalSeparator()
        ],
    
        # BARIS BAWAH
        [
            sg.Column(
                [
                    [section("DATA ORANG TUA", ortu_fields)]
                ],
                vertical_alignment="top",
                expand_x=True,
                expand_y=True
            ),
            sg.VSeparator(),
            sg.Column(
                [
                    [section_kematian()]
                ],
                vertical_alignment="top",
                expand_x=True,
                expand_y=True
            )
        ],
    
        [sg.HorizontalSeparator()],
    
        # TOMBOL
        [
    
            sg.Push(),
            sg.Button("REFRESH", size=(15, 2)),
            sg.Button("GENERATE PDF", size=(18, 2)),
            sg.Button("KELUAR", size=(15, 2)),
            sg.Push()
        ]
    ]
    return layout

# ================= JALANKAN FORM KEMATIAN MANDIRI =================

def jalankan_mandiri():
    layout = buat_layout()

    window = sg.Window(
        "F-2.01 - Formulir Pencatatan Kematian",
        layout,
        resizable=True,
        finalize=True
    )

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
                    elif isinstance(element, sg.Checkbox):
                        element.update(False)
                    elif isinstance(element, sg.Radio):
                        element.update(False)
            continue

        if event == "GENERATE PDF":
            buat_pdf(values)

    window.close()


# Jalankan mandiri hanya jika file dibuka langsung
if __name__ == "__main__":
    jalankan_mandiri()
