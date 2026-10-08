
import fitz

# ================= KONSTANTA PDF =================

FONT_SIZE = 9
KOTAK = 12

X_LABEL = 40
X_TITIK = 160
X_ISI = 170

# ================= FUNGSI TULIS LABEL =================

def tulis_label(page, text, x, y, size=9, bold=False):
    """
    Menulis teks pada halaman PDF.
    Font helv untuk normal dan hebo untuk bold.
    """
    font = "hebo" if bold else "helv"

    page.insert_text((x, y), str(text), fontsize=size, fontname=font)


# ================= FUNGSI CHECKBOX =================

def gambar_checkbox(page, x, y):

#    Menggambar kotak checkbox pada PDF.

    page.draw_rect(fitz.Rect(x, y - 10, x + 12, y + 2), color=(0, 0, 0), width=0.7)

# ================= FUNGSI BARIS KOTAK =================

def gambar_baris_kotak(page, x, y, jumlah, text=""):

#    Menggambar kotak per karakter dan mengisi teks.

    text = str(text).upper()

    for i in range(jumlah):
        r = fitz.Rect(x + i * KOTAK, y, x + (i + 1) * KOTAK, y + KOTAK)
        page.draw_rect(r, color=(0, 0, 0), width=0.5)

        if i < len(text):

            page.insert_text((x + i * KOTAK + 2.5, y + 9), text[i], fontsize=FONT_SIZE, fontname="helv")

# ================= FUNGSI LABEL + KOTAK =================

def tulis_baris_kotak(page, label, y, jumlah, text=""):
    """
    Menulis label, tanda titik dua, dan baris kotak.
    """
    tulis_label(page, label, X_LABEL, y)
    tulis_label(page, ":", X_TITIK, y)

    gambar_baris_kotak(page, X_ISI, y - 9, jumlah, text)