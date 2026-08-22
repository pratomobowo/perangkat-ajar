---
name: pa-wali-kelas
description: "Use when a homeroom teacher asks for a class program, seating plan, attendance or case record, class analysis, or other wali kelas document. Treat all student and case data as sensitive and keep it local."
---

# Wali Kelas (Homeroom Module)

Semua output simpan di folder output profil; data murid = sensitif (aturan #9 `pa-core`). Minta template resmi sekolah dulu untuk tiap dokumen.

## 1. Data Siswa Kelas
Tabel identitas: No | Nama | NIS/NISN | JK | TTL | Orang Tua/Wali | Kontak | Alamat.
- Sumber tunggal: daftar induk dari sekolah - jangan rekonstruksi dari chat.
- Kontak ortu hanya di dokumen ini, tidak dibawa ke dokumen lain.

## 2. Program Kerja Wali Kelas (per semester/tahun)
Tabel: No | Bidang (akademik/karakter/keterampilan/komunikasi ortu) | Kegiatan | Sasaran | Waktu | Indikator Keberhasilan.
- Selaraskan dengan agenda sekolah (kalender pendidikan) & profil kelas hasil asesmen diagnostik (`pa-soal`).

## 3. Struktur Organisasi Kelas
Susunan pengurus + pembagian tugas; grid HTML bila pakai bagan.

## 4. Jadwal Piket
Tabel hari × nama (grup piket); rotasi merata - hitung jumlah piket per anak sama.

## 5. Denah Duduk
HTML `<table>` grid posisi bangku (baris × kolom), tandai murid berkebutuhan khusus/penglihatan dengan catatan singkat.
- Update saat ada perubahan; versi lama ke `Arsip/`.

## 6. Buku Kasus (Catatan Pembinaan)
Tabel: Tanggal | Nama | Uraian Kasus | Tindakan | Hasil/Tindak Lanjut | Status (terbuka/selesai).
- Bahasa objektif-faktual (fakta yang terjadi, bukan label emosional); ini bisa diminta supervisor/ortu.
- Kasus berlanjut = baris baru dengan referensi kasus awal, jangan edit riwayat lama.

## 7. Analisis Ketuntasan / Kenaikan Kelas
Dari leger (`pa-admin`) + KKTP (`pa-kktp`): persentase tuntas per TP/mapel, daftar murid perlu perhatian + program pendampingan.
- Verifikasi terprogram: persentase = hitung ulang dari data, bukan manual.
- Diskusikan temuan di chat dengan kepala sekolah sebelum diformalkan.

## Pitfall
- Jangan taruh nilai rinci murid di dokumen publik kelas (denah duduk, piket) - hanya administratif.
- Analisis kenaikan mengikuti kriteria resmi dinas (KKM/batas tuntas sekolah), konfirmasi angkanya dulu.
