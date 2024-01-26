#!/usr/bin/env python
# coding: utf-8
# code oleh : https://github.com/M-Cyber7
# open source code :) PENJELASAN CARA MENGGUNAKAN!!
#--->
#==========================================

import time
import os

# Fungsi untuk membersihkan layar terminal
def hapus_layar():
    os.system('clear')

# kode warna untuk teks
class Color:
    RESET = '\033[0m'
    BRIGHT = '\033[1m'
    YELLOW = '\033[33m'
    CYAN = '\033[36m'
    RED = '\033[31m'
    MAGENTA = '\033[35m'
    GREEN = '\033[32m'
    WHITE = "\033[37m"
    BLUE = "\033[34m"

# Fungsi untuk efek mengetik teks
def tipe_efek(color, teks):
    print(Color.BRIGHT + Color.BLUE + "»" + Color.BRIGHT, end=" ")
    for char in teks:
        print(color + char + Color.RESET, end="", flush=True)
        time.sleep(0.005)
    print()
    time.sleep(0.1)

# Fungsi untuk mencetak pesan & efek mengetik
# MOHON DIBACA YA CUY! KHUSUS PENGGUNA LAMA TERMUX!!
# PLEASE READ IT, BRO! OLD TERMUX USERS ONLY!!
def animasi_mengetik():
    try:
        teks_nya = [
            (Color.YELLOW + Color.BRIGHT, "============= WARNING in ENGLISH & Indonesia ============"),
            (Color.RED + Color.BRIGHT, "I hope you have read the documentation in README.md"),
            (Color.RED + Color.BRIGHT, "Run this tool with the command :"),
            (Color.WHITE + Color.BRIGHT, "python3 style.py"),
            (Color.RED + Color.BRIGHT, "And wait 5-10 seconds to install the modul (Fast network)"),
            (Color.RED + Color.BRIGHT, "Then a special text will appear! "),
            (Color.RED + Color.BRIGHT, "The text is a warning of the user old"),
            (Color.RED + Color.BRIGHT, "With this text you agree to..."),
            (Color.RED + Color.BRIGHT, "configuration changes in the .bashrc file & config fish3"),
            (Color.RED + Color.BRIGHT, "If you understand, then you can click ENTER"),
            (Color.RED + Color.BRIGHT, "If an error occurs, then install the rich library"),
            (Color.WHITE + Color.BRIGHT, "pip install rich"),
            (Color.RED + Color.BRIGHT, "If you are stuck/not logged in to script..."),
            (Color.RED + Color.BRIGHT, "You can press CTRL + C "),
            (Color.RED + Color.BRIGHT, "Thank you for your understanding :)"),
            (Color.RED + Color.BRIGHT, "I'm M-Cyber7 ==> See you 👋"),

            (Color.YELLOW + Color.BRIGHT, "============= WARNING in INDONESIA & English ============"),
            (Color.RED + Color.BRIGHT, "Saya harap Anda telah membaca dokumentasi di README.md"),
            (Color.RED + Color.BRIGHT, "Jalankan Tools ini dengan perintah :"),
            (Color.WHITE + Color.BRIGHT, "python3 style.py"),
            (Color.RED + Color.BRIGHT, "Dan tunggu 5-10 detik untuk menginstal modul (Fast Ntwrk)"),
            (Color.RED + Color.BRIGHT, "Kemudian teks khusus akan muncul!"),
            (Color.RED + Color.BRIGHT, "Teks tersebut merupakan peringatan untuk pengguna lama"),
            (Color.RED + Color.BRIGHT, "Dengan teks ini Anda setuju untuk..."),
            (Color.RED + Color.BRIGHT, "perubahan konfigurasi pada file .bashrc dan config fish3"),
            (Color.RED + Color.BRIGHT, "Jika sudah paham maka anda bisa klik ENTER"),
            (Color.RED + Color.BRIGHT, "Jika terjadi kesalahan, instal Modul Yang dibutuhkan"),
            (Color.WHITE + Color.BRIGHT, "pip install rich"),
            (Color.RED + Color.BRIGHT, "Jika Anda terjebak/tidak masuk ke script..."),
            (Color.RED + Color.BRIGHT, "Anda dapat menekan CTRL + C"),
            (Color.RED + Color.BRIGHT, "Terima kasih atas pemahamannya :)"),
            (Color.RED + Color.BRIGHT, "Saya M-Cyber7 ==> Sampai jumpa 👋"),
#---->
        ]
        for color, teks in teks_nya:
            tipe_efek(color, teks)
    except KeyboardInterrupt:
        print("\n")

# Mainkan program
hapus_layar()
animasi_mengetik()
print()
# berhenti sejenak... Ambil nafas 😌
input(f'{Color.BLUE}[=]{Color.RED} INGIN MEMULAI DARI SINI? (Klik enter) : ')
os.system('python3 style.py')
