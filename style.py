#!/usr/bin/env python
# coding: utf-8
# Code By Cyber M : https://github.com/x7cyber/Style_Fish

#=============================================================
#----> INDONESIA 🎯
# Dibuat agar mempercantik terminal + mempercepat Tugas!
# Follow me : @cyberm
# Youtube : Cyber M
# Author + code by : x7cyber
# T34M : No team ×
# Terimakasih semua 🌟
#=============================================================
#----> ENGLISH 🎯
# Was created to style the terminal + speed up Tasks!
# Follow me : @cyberm_
# Youtube : Cyber M
# Author + code by : x7cyber
# T34M : No team ×
# Thankyou all 🌟
#=============================================================

import time, os, sys

hijau = "\033[32m"
ungu = "\033[35m"
cyan = "\033[36m"
biru = "\033[34m"
kuning = "\033[33m"
merah = "\033[31m"
putih = "\033[37m"
tbl = "\033[1m"
reset = "\033[0m"

def ketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.010)

ketik(' memuat...')

os.system('apt install fish -y > /dev/null 2>&1')
os.system('apt install lsd -y > /dev/null 2>&1')
os.system('git pull > /dev/null 2>&1')

lokasi_file = "/data/data/com.termux/files/home/.config/fish/config.fish"

if os.path.exists(lokasi_file):
    print("")
else:
    with open(lokasi_file, 'w') as f:
        f.write("")
    print("ok")

os.system('clear')

def banner():
        print(f"""

{biru}╭─────────────────── ❰{reset} VERSION 0.8{biru} ❱ ───────────────────╮
{biru}│ {tbl}{merah}•{tbl}{kuning}•{tbl}{hijau}•                                               {tbl}{merah}•{tbl}{kuning}•{tbl}{hijau}•{tbl}{biru} │
{biru}│    _________ __          .__           {biru} __________    │
{biru}│   /   _____//  |_ ___.__.|  |   ____   {biru} \_   _____/   │
{biru}│   \_____  \\    __|   |  ||  | _/ __ \ {biru}   |    __)     │
{biru}│   /        \|  |  \___  ||  |_\  ___/  {biru}  |     \      │
{biru}│  /_______  /|__|  / ____||____/\___  > {biru}  \___  /      │
{biru}│          \/       \/               \/  {biru}      \/       │
{biru}│                                                       │
{biru}╰───────────────────────────────────────────────────────╯
            ↓                                ↓
╭──────────────────────╮         ╭──────────────────────╮
│  {tbl}{hijau}Code by : x7cyber{biru}   │         │  {tbl}{hijau}Youtube : Cyber M{biru}   │
╰──────────────────────╯         ╰──────────────────────╯


""")
banner()

def atur_prompt(nama_depan, nama_belakang, simbol_tengah):
    lokasi_config_fish = os.path.expanduser("~/.config/fish/config.fish")
    script_nya = f"""
if status is-interactive
# Jangan di ubah!
set -U fish_greeting
  # Menjalankan fungsi
end

function fish_prompt
    set -l last_status $status
    set_color -o blue
    echo -n "╭─"
    set_color -o blue --bold
    echo -n "({nama_depan}"
    set_color -o red --bold
    echo -n "{simbol_tengah}"
    set_color -o blue --bold
    echo -n "{nama_belakang})$current_time "
    set_color -o normal
    echo -n (prompt_pwd)
    if test $last_status -eq 0
        set_color -o red --bold
        echo -n " [ "
        set_color -o normal
        set color -o white --bold
        echo -n "✔"
        set_color -o red --bold
        echo -n " ]"
    else
        set_color -o red --bold
        echo -n " [ "
        set_color -o normal
        set color -o white --bold
        echo -n "✘"
        set_color -o red --bold
        echo -n " ]"
    end

    set_color -o normal
    echo
    set_color -o blue
    echo "╰─\$ "
end

alias ls=lsd

"""
    with open(lokasi_config_fish, "w") as config_file:
        config_file.write(script_nya)

def untuk_di_bashrc(pengguna, aktifkan_figlet):
    bashrc_path = os.path.expanduser("~/.bashrc")

    figlet_command = f"echo -e \"\\033[0;34m\\033[1m\" && figlet -f slant {pengguna} && echo"
    exec_fish_command = "exec fish"

    with open(bashrc_path, "r") as bashrc_file:
        bashrc_content = bashrc_file.read()

        lines = bashrc_content.split("\n")
        for i in range(len(lines)):
            if "figlet" in lines[i] or "exec fish" in lines[i] or "clear" in lines[i]:
                lines[i] = "#" + lines[i]

        with open(bashrc_path, "w") as bashrc_file_write:
            bashrc_file_write.write("\n".join(lines))

        with open(bashrc_path, "a") as bashrc_file_append:
            bashrc_file_append.write("clear\n")

        if aktifkan_figlet:
            with open(bashrc_path, "a") as bashrc_file_append:
                bashrc_file_append.write(f"echo -e \"\\033[0;34m\\033[1m\" && {figlet_command}\n")

        with open(bashrc_path, "a") as bashrc_file_append:
            bashrc_file_append.write(f"# Fish Shell \n{exec_fish_command}\n")

    os.system('python background.py')
    print(f"{merah}[{putih}!{merah}]{putih} Konfigurasi berhasil diubah")
    print(f"{merah}[{putih}!{merah}]{putih} Buka New Session untuk melihat")
    print(f"{merah}[{putih}!{merah}]{putih} Jika ada bug/saran, inbox Admin {hijau}@indonesiancyber7") 

def create_bashrc_if_not_exists():
    bashrc_path = os.path.expanduser("~/.bashrc")

    if not os.path.exists(bashrc_path):
        with open(bashrc_path, "w") as bashrc_file:
            bashrc_file.write("# Konfigurasi Bash\n")

if __name__ == "__main__":
    try:
        create_bashrc_if_not_exists()

        nama_depan = input(f"{merah}[{putih}»{merah}]{putih} Nama depan    : ")

        if not nama_depan:
           pass

        nama_belakang = input(f"{merah}[{putih}»{merah}]{putih} Nama belakang : ")

        if not nama_belakang:
            pass

        else:
            try:
                print()
                print(f"{merah}[{putih}»{merah}]{putih} Pilih simbol Tengah :")
                print()
                print(f"{ungu}[{biru}1{ungu}]{biru} ★         {ungu}[{biru}5{ungu}]{biru} ∆ ")
                print(f"{ungu}[{biru}2{ungu}]{biru} •         {ungu}[{biru}6{ungu}]{biru} Ω ")
                print(f"{ungu}[{biru}3{ungu}]{biru} ~         {ungu}[{biru}7{ungu}]{biru} ? ")
                print(f"{ungu}[{biru}4{ungu}]{biru} ©         {ungu}[{biru}8{ungu}]{biru} ≠ ")
                print()
                print(f"{ungu}[{biru}m{ungu}]{biru} Atau Masukan manual (ketik m) ")
                print(f"{ungu}[{biru}k{ungu}]{biru} Atau Kosongkan (ketik k)")
                print()
                simbol_tengah_choice = input(f"{merah}[{putih}»{merah}]{putih} Masukan pilihan : ")

                if simbol_tengah_choice == 'm':
                    custom_simbol_tengah = input(f"{merah}[{putih}»{merah}]{putih} Masukkan simbol manual : ")
                    simbol_tengah = custom_simbol_tengah
                elif simbol_tengah_choice == 'k':
                    simbol_tengah = ''
                else:
                    simbol_tengah_options = {'1': '★', '2': '•', '3': '~', '4': '©', '5': '∆', '6': 'Ω', '7': '?', '8': '≠'}
                    simbol_tengah = simbol_tengah_options.get(simbol_tengah_choice, '•')

                atur_prompt(nama_depan, nama_belakang, simbol_tengah)

                aktifkan_figlet = input(f"{merah}[{putih}»{merah}]{putih} Aktifkan Teks Nama untuk banner? {merah}(y/t) : ").lower() == 'y'

                if aktifkan_figlet:
                    pengguna = input(f"{merah}[{putih}»{merah}]{putih} Masukkan nama untuk Teks banner : ")
                else:
                    pengguna = ""

                untuk_di_bashrc(pengguna, aktifkan_figlet)

                print(f"{merah}[{putih}✓{merah}]{putih} done")

            except KeyboardInterrupt:
                pass

    except KeyboardInterrupt:
        pass

