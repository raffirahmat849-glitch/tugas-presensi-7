"""
╔══════════════════════════════════════════════════════════╗
║     SISTEM KLASIFIKASI PRESENSI MAHASISWA                ║
║     Decision Tree Sederhana (IF-ELSE)                    ║
║     Mata Kuliah: Kecerdasan Komputasional                 ║
╚══════════════════════════════════════════════════════════╝
"""

import os
import time

# ─── WARNA TERMINAL (ANSI Escape Codes) ───────────────────
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"

# Foreground
MERAH   = "\033[91m"
HIJAU   = "\033[92m"
KUNING  = "\033[93m"
BIRU    = "\033[94m"
UNGU    = "\033[95m"
CYAN    = "\033[96m"
PUTIH   = "\033[97m"

# Background
BG_BIRU  = "\033[44m"
BG_HIJAU = "\033[42m"
BG_MERAH = "\033[41m"
BG_ABU   = "\033[100m"

# ─── DATA MAHASISWA (Array of Dict) ───────────────────────
data_mahasiswa = [
    {
        "nama"     : "Bahlil",
        "nim"      : "2021001",
        "kehadiran": "Tinggi",   # Tinggi / Rendah
        "tugas"    : "Lengkap",  # Lengkap / Tidak Lengkap
        "nilai_uts": 85
    },
    {
        "nama"     : "jokowi",
        "nim"      : "2021002",
        "kehadiran": "Rendah",
        "tugas"    : "Tidak Lengkap",
        "nilai_uts": 50
    },
    {
        "nama"     : "anis",
        "nim"      : "2021003",
        "kehadiran": "Tinggi",
        "tugas"    : "Tidak Lengkap",
        "nilai_uts": 72
    },
    {
        "nama"     : "prabowo",
        "nim"      : "2021004",
        "kehadiran": "Rendah",
        "tugas"    : "Lengkap",
        "nilai_uts": 60
    },
    # ★ Data mahasiswa baru (tambahan wajib)
    {
        "nama"     : "marwa kaltim",
        "nim"      : "2021005",
        "kehadiran": "Tinggi",
        "tugas"    : "Lengkap",
        "nilai_uts": 91
    },
    {
        "nama"     : "sri mulyani",
        "nim"      : "2021006",
        "kehadiran": "Rendah",
        "tugas"    : "Tidak Lengkap",
        "nilai_uts": 40
    },
]


# ══════════════════════════════════════════════════════════
#  FUNGSI DECISION TREE
# ══════════════════════════════════════════════════════════

def klasifikasi_status(kehadiran: str) -> str:
    """Node 1: Cabang utama berdasarkan kehadiran."""
    if kehadiran == "Tinggi":
        return "Aktif"
    else:  # Rendah
        return "Tidak Aktif"


def klasifikasi_keterangan(kehadiran: str, tugas: str, nilai_uts: int) -> str:
    """
    Node 2 & 3: Cabang lanjutan untuk keterangan detail.
    Fitur tambahan: mempertimbangkan nilai UTS.
    """
    if kehadiran == "Tinggi":
        if tugas == "Lengkap":
            if nilai_uts >= 80:
                return "★ Mahasiswa Berprestasi & Disiplin"
            else:
                return "✔ Mahasiswa Disiplin"
        else:  # Tugas tidak lengkap
            return "⚠ Kehadiran Baik, Tugas Perlu Dilengkapi"
    else:  # Kehadiran Rendah
        if tugas == "Lengkap":
            return "⚠ Tugas Baik, Kehadiran Perlu Ditingkatkan"
        else:
            return "✘ Perlu Bimbingan Intensif"


def grade_nilai(nilai: int) -> str:
    """Fitur tambahan: konversi nilai UTS ke grade huruf."""
    if nilai >= 85:
        return "A"
    elif nilai >= 75:
        return "B"
    elif nilai >= 65:
        return "C"
    elif nilai >= 55:
        return "D"
    else:
        return "E"


# ══════════════════════════════════════════════════════════
#  FUNGSI TAMPILAN
# ══════════════════════════════════════════════════════════

def cetak_header():
    lebar = 68
    print()
    print(f"{BOLD}{CYAN}{'═' * lebar}{RESET}")
    print(f"{BOLD}{BG_BIRU}{PUTIH}{'  SISTEM PRESENSI MAHASISWA — DECISION TREE':^{lebar}}{RESET}")
    print(f"{BOLD}{CYAN}{'  Mata Kuliah: Kecerdasan Komputasional':^{lebar}}{RESET}")
    print(f"{BOLD}{CYAN}{'═' * lebar}{RESET}")
    print()


def cetak_pohon_keputusan():
    print(f"{BOLD}{KUNING}  📌 STRUKTUR DECISION TREE:{RESET}")
    print(f"{DIM}  {'─' * 50}{RESET}")
    print(f"  {BOLD}[KEHADIRAN?]{RESET}")
    print(f"  ├── {HIJAU}Tinggi{RESET} ──► Status: {HIJAU}AKTIF{RESET}")
    print(f"  │       ├── {HIJAU}Tugas Lengkap + UTS ≥80{RESET} → ★ Berprestasi & Disiplin")
    print(f"  │       ├── {KUNING}Tugas Lengkap + UTS <80{RESET} → ✔ Disiplin")
    print(f"  │       └── {KUNING}Tugas Tidak Lengkap{RESET}   → ⚠ Tugas Perlu Dilengkapi")
    print(f"  └── {MERAH}Rendah{RESET} ──► Status: {MERAH}TIDAK AKTIF{RESET}")
    print(f"          ├── {KUNING}Tugas Lengkap{RESET}         → ⚠ Kehadiran Perlu Ditingkatkan")
    print(f"          └── {MERAH}Tugas Tidak Lengkap{RESET}   → ✘ Perlu Bimbingan Intensif")
    print()


def cetak_garis_tabel():
    print(f"{DIM}  {'─' * 64}{RESET}")


def cetak_header_tabel():
    cetak_garis_tabel()
    print(
        f"  {BOLD}{BG_ABU}{PUTIH}"
        f"  {'No':<3} {'Nama':<8} {'NIM':<9} {'Hadir':<7} {'Tugas':<14} "
        f"{'UTS':<5} {'Grade':<6} {'Status':<12}"
        f"{RESET}"
    )
    cetak_garis_tabel()


def warna_status(status: str) -> str:
    if status == "Aktif":
        return f"{BOLD}{HIJAU}{status}{RESET}"
    else:
        return f"{BOLD}{MERAH}{status}{RESET}"


def warna_kehadiran(kehadiran: str) -> str:
    if kehadiran == "Tinggi":
        return f"{HIJAU}{kehadiran}{RESET}"
    else:
        return f"{MERAH}{kehadiran}{RESET}"


def warna_grade(grade: str) -> str:
    warna_map = {
        "A": HIJAU, "B": CYAN, "C": KUNING, "D": MERAH, "E": MERAH
    }
    w = warna_map.get(grade, PUTIH)
    return f"{BOLD}{w}{grade}{RESET}"


def tampilkan_semua_mahasiswa(data: list):
    hasil = []
    for mhs in data:
        status     = klasifikasi_status(mhs["kehadiran"])
        keterangan = klasifikasi_keterangan(
            mhs["kehadiran"], mhs["tugas"], mhs["nilai_uts"]
        )
        grade = grade_nilai(mhs["nilai_uts"])
        hasil.append({**mhs, "status": status, "keterangan": keterangan, "grade": grade})
    return hasil


def cetak_tabel(hasil: list):
    cetak_header_tabel()
    for i, mhs in enumerate(hasil, 1):
        # Baris data ringkas
        print(
            f"  {DIM}{i:<3}{RESET} "
            f"{BOLD}{mhs['nama']:<8}{RESET} "
            f"{DIM}{mhs['nim']:<9}{RESET} "
            f"{warna_kehadiran(mhs['kehadiran']):<18} "
            f"{mhs['tugas']:<14} "
            f"{KUNING}{mhs['nilai_uts']:<5}{RESET} "
            f"{warna_grade(mhs['grade']):<16} "
            f"{warna_status(mhs['status'])}"
        )
    cetak_garis_tabel()
    print()


def cetak_detail_per_mahasiswa(hasil: list):
    print(f"\n{BOLD}{UNGU}  📋 DETAIL KLASIFIKASI PER MAHASISWA:{RESET}")
    print(f"{DIM}  {'═' * 64}{RESET}\n")

    for mhs in hasil:
        # Pilih warna kartu berdasarkan status
        if mhs["status"] == "Aktif":
            aksen = HIJAU
            ikon  = "🟢"
        else:
            aksen = MERAH
            ikon  = "🔴"

        print(f"  {aksen}┌── {ikon} {BOLD}{mhs['nama'].upper()}{RESET}{aksen} (NIM: {mhs['nim']}){RESET}")
        print(f"  {aksen}│{RESET}  Kehadiran  : {warna_kehadiran(mhs['kehadiran'])}")
        print(f"  {aksen}│{RESET}  Tugas      : {mhs['tugas']}")
        print(f"  {aksen}│{RESET}  Nilai UTS  : {KUNING}{mhs['nilai_uts']}{RESET} "
              f"({warna_grade(mhs['grade'])})")
        print(f"  {aksen}│{RESET}  Status     : {warna_status(mhs['status'])}")
        print(f"  {aksen}└─ Keterangan: {BOLD}{mhs['keterangan']}{RESET}")
        print()


def cetak_statistik(hasil: list):
    total      = len(hasil)
    aktif      = sum(1 for m in hasil if m["status"] == "Aktif")
    tidak_aktif = total - aktif
    disiplin   = sum(1 for m in hasil if "Disiplin" in m["keterangan"]
                                       or "Berprestasi" in m["keterangan"])
    rata_uts   = sum(m["nilai_uts"] for m in hasil) / total

    print(f"{BOLD}{KUNING}  📊 RINGKASAN STATISTIK:{RESET}")
    cetak_garis_tabel()
    print(f"  Total Mahasiswa     : {BOLD}{total}{RESET}")
    print(f"  Mahasiswa Aktif     : {BOLD}{HIJAU}{aktif}{RESET} "
          f"({aktif/total*100:.0f}%)")
    print(f"  Mahasiswa Tidak Aktif: {BOLD}{MERAH}{tidak_aktif}{RESET} "
          f"({tidak_aktif/total*100:.0f}%)")
    print(f"  Mahasiswa Disiplin  : {BOLD}{CYAN}{disiplin}{RESET}")
    print(f"  Rata-rata Nilai UTS : {BOLD}{KUNING}{rata_uts:.1f}{RESET} "
          f"({warna_grade(grade_nilai(int(rata_uts)))})")
    cetak_garis_tabel()
    print()


def cetak_footer():
    print(f"{DIM}{'─' * 68}{RESET}")
    print(f"{DIM}  Program: Decision Tree Presensi Mahasiswa | Kecerdasan Komputasional{RESET}")
    print(f"{DIM}{'─' * 68}{RESET}\n")


# ══════════════════════════════════════════════════════════
#  FITUR TAMBAHAN: Pencarian Mahasiswa
# ══════════════════════════════════════════════════════════

def cari_mahasiswa(hasil: list, nama_cari: str):
    print(f"\n{BOLD}{BIRU}  🔍 HASIL PENCARIAN: '{nama_cari}'{RESET}")
    cetak_garis_tabel()
    ditemukan = [m for m in hasil if nama_cari.lower() in m["nama"].lower()]
    if ditemukan:
        for mhs in ditemukan:
            print(f"  {BOLD}{mhs['nama']}{RESET} ({mhs['nim']})")
            print(f"  Status     : {warna_status(mhs['status'])}")
            print(f"  Keterangan : {mhs['keterangan']}")
    else:
        print(f"  {MERAH}Mahasiswa tidak ditemukan.{RESET}")
    cetak_garis_tabel()
    print()


# ══════════════════════════════════════════════════════════
#  MENU UTAMA
# ══════════════════════════════════════════════════════════

def tampilkan_menu():
    lebar = 26  # lebar isi dalam kotak (antara ║ kiri dan ║ kanan)
    menu_items = [
        "1. Lihat Tabel Ringkas",
        "2. Detail Per Mahasiswa",
        "3. Statistik Kelas",
        "4. Cari Mahasiswa",
        "5. Tampilkan Semua",
        "0. Keluar",
    ]
    garis  = "═" * lebar
    judul  = "MENU UTAMA".center(lebar)

    print(f"\n{BOLD}{CYAN}  ╔{garis}╗{RESET}")
    print(f"{BOLD}{CYAN}  ║{judul}║{RESET}")
    print(f"{BOLD}{CYAN}  ╠{garis}╣{RESET}")
    for item in menu_items:
        isi = f"  {item}".ljust(lebar)   # padding kiri 2 spasi, rata kanan dgn spasi
        print(f"{BOLD}{CYAN}  ║{RESET}{isi}{BOLD}{CYAN}║{RESET}")
    print(f"{BOLD}{CYAN}  ╚{garis}╝{RESET}")
    print()


def main():
    os.system("cls" if os.name == "nt" else "clear")
    cetak_header()

    # Proses klasifikasi seluruh data
    hasil = tampilkan_semua_mahasiswa(data_mahasiswa)

    # Tampilkan pohon keputusan saat pertama kali
    cetak_pohon_keputusan()

    while True:
        tampilkan_menu()
        pilihan = input(f"  {BOLD}Pilih menu [0-5]: {RESET}").strip()

        if pilihan == "1":
            print(f"\n{BOLD}{CYAN}  📋 TABEL RINGKAS DATA MAHASISWA:{RESET}\n")
            cetak_tabel(hasil)

        elif pilihan == "2":
            cetak_detail_per_mahasiswa(hasil)

        elif pilihan == "3":
            cetak_statistik(hasil)

        elif pilihan == "4":
            nama = input(f"\n  {BOLD}Masukkan nama yang dicari: {RESET}").strip()
            cari_mahasiswa(hasil, nama)

        elif pilihan == "5":
            print()
            cetak_pohon_keputusan()
            print(f"\n{BOLD}{CYAN}  📋 TABEL RINGKAS DATA MAHASISWA:{RESET}\n")
            cetak_tabel(hasil)
            cetak_detail_per_mahasiswa(hasil)
            cetak_statistik(hasil)

        elif pilihan == "0":
            cetak_footer()
            print(f"  {HIJAU}Program selesai. Sampai jumpa! 👋{RESET}\n")
            break

        else:
            print(f"\n  {MERAH}Pilihan tidak valid. Silakan coba lagi.{RESET}\n")


# ══════════════════════════════════════════════════════════
if __name__ == "__main__":
    main()