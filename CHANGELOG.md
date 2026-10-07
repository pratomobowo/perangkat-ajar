# Changelog paket perangkat-ajar

## v1.5.0 (2026-10-07)
Pembaruan dari hasil pemakaian nyata bersama guru SMK. Data pribadi pada
contoh konvensi sudah disanitasi (`[Nama Guru]` / `[NIP]` / `[Nama Sekolah]` /
`[Nama Kepala Sekolah]` / `[mitra DUDI]` / `[Kota]`) agar aman dibagikan.

- **pa-analisis-cp** (1.4.0 → 1.5.0): konvensi format dokumen Analisis CP —
  judul, baris identitas, bagian CP nasional & hasil sinkronisasi, tabel
  pemetaan (kode `BD-F.n`, TP bernomor `n.m` diawali "Peserta didik mampu ..."),
  tabel catatan analisis, status DRAF/Disetujui, blok tanda tangan rata kanan.
- **pa-atp** (1.4.0 → 1.5.0): konvensi ATP — pembagian semester efektif
  (XII genap = PKL, TP dipadatkan di ganjil), kolom tabel, 8 dimensi profil
  lulusan, aturan penggabungan tabel markdown, format TTD + NIP.
- **pa-core** (1.3.0, tetap): varian blok tanda tangan rata kanan (HTML),
  catatan instalasi dependensi PDF (`--break-system-packages`, verifikasi ulang
  setelah VM diganti).
- **pa-kktp** (1.4.0 → 1.5.0): format KKTP resmi sekolah (interval
  0–68 / 68–78 / 79–89 / 90–100), aturan pecah tabel landscape maksimal
  5 baris data per halaman.
- **pa-prosem** (1.4.0 → 1.5.0): konvensi prosem 3 semester @1 halaman
  landscape, alokasi TP per minggu efektif, audit silang JP vs Prota,
  status persetujuan sementara.
- **pa-prota** (1.4.0 → 1.5.0): konvensi prota (76/68/76 JP per semester
  efektif), alokasi JP per TP hasil kesepakatan guru, baris total alokasi
  per semester.
- **pa-rpp** (1.3.0, tetap): konvensi kolom Penyusun (nama tanpa NIP;
  NIP tetap di blok TTD).

Skill lain (pa-admin, pa-lkpd, pa-media, pa-nilai, pa-p5, pa-pkl, pa-rapor,
pa-riset, pa-soal, pa-wali-kelas) tidak berubah dari sumber asli.

Sumber asli: https://github.com/pratomobowo/perangkat-ajar (MIT).
Cara instal: salin folder `pa-*` ke direktori skills (mis. `~/workspace/skills/`
atau `~/.hermes/skills/`), lalu `pip install markdown-it-py weasyprint`
untuk pipeline PDF.
