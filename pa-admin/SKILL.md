---
name: pa-admin
description: "Use when a teacher asks for a teaching journal, attendance list, class ledger, or other routine classroom administration. Check the school's policy and existing application before creating duplicate documents."
---

# Admin Mengajar Harian

## Cek dulu (WAJIB)
Tanya guru/sekolah:
1. "Sekolah masih minta jurnal manual?" — arah nasional menyederhanakan admin guru; banyak sekolah sudah lewat aplikasi.
2. Kalau sekolah punya format resmi (Excel/PDF), pakai ITU — skill ini hanya membantu mengisi/menghasilkan datanya.

## 1. Jurnal Mengajar
Per bulan per kelas: Tanggal | Jam ke | Kelas | Materi/Kegiatan (dari Prosem!) | Hadir | Ket.
- Isi kolom materi bisa AUTO-FILL dari Prosem (`pa-prosem`) minggu bersangkutan — guru tinggal melengkapi realisasinya.
- Konsisten dengan daftar hadir (jumlah hadir).

## 2. Daftar Hadir
Grid: baris = nama murid, kolom = tanggal/pertemuan; isi S/I/A (Sakit/Izin/Alpa).
- Nama urut alfabetis, nomor induk konsisten dengan dokumen sekolah lain.
- Rekap akhir bulan: total S/I/A per murid + persentase kehadiran (hitung terprogram).

## 3. Leger Nilai
Tabel: No | Nama | nilai per TP | Rata-rata | Predikat (interval KKTP `pa-kktp`).
- Verifikasi terprogram: rata-rata & predikat dihitung dari data, bukan diketik manual.
- Predikat harus cocok interval KKTP — audit silang.

## Pitfall
- Data murid sensitif (aturan #9 `pa-core`) — simpan lokal, kirim hanya ke guru pemiliknya.
- Jangan bikin versi manual kalau sekolah sudah digital — itu pekerjaan dobel.
- Bulan baru = file/baris baru, arsip bulan lama jangan ditumpuk.
