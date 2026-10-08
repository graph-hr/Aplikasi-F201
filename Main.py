
import PySimpleGUI as sg

import F201_Kelahiran
import F201_Kematian

# ================= MENU UTAMA =================

def main():

    sg.theme("LightBlue3")

    layout = [
        [sg.Text("APLIKASI FORMULIR F-2.01", font=("Arial", 18, "bold"), justification="center", expand_x=True)],
        [sg.HorizontalSeparator()],
        [sg.Text("Pilih jenis formulir yang akan digunakan:", font=("Arial", 11))],
        [sg.Button("FORMULIR KELAHIRAN", key="-KELAHIRAN-", size=(25, 3), font=("Arial", 12, "bold"))],
        [sg.Button("FORMULIR KEMATIAN", key="-KEMATIAN-", size=(25, 3), font=("Arial", 12, "bold"))],
        [sg.HorizontalSeparator()],

        [sg.Button("KELUAR", size=(15, 2))]
    ]

    window = sg.Window("Aplikasi F-2.01", layout, size=(500, 350), element_justification="center", finalize=True)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "KELUAR"):
            break
        elif event == "-KELAHIRAN-":
            F201_Kelahiran.jalankan_mandiri()
        elif event == "-KEMATIAN-":
            F201_Kematian.jalankan_mandiri()

    window.close()


if __name__ == "__main__":
    main()