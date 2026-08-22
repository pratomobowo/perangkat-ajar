---
name: pa-pkl
description: Dokumen PKL/Prakerin SMK (Praktik Kerja Lapangan) — pedoman pelaksanaan, jurnal harian siswa, catatan kunjungan pembimbing, instrumen penilaian DU/DI & pembimbing sekolah, dan rekap konversi nilai PKL. Fokus dokumen sisi pembelajaran; surat-menyurat resmi di luar skill ini.
---

# PKL — Praktik Kerja Lapangan (SMK)

PKL adalah mata pelajaran wajib SMK (SN-Dikmen). Skill ini membuat dokumen **sisi pembelajaran**: pedoman, jurnal, penilaian, konversi nilai. (Surat pengantar/moU = urusan tata usaha; buat manual atau lewat format sekolah.)

## LANGKAH 0 — Cek kebijakan sekolah dulu
1. Minta **Pedoman/Petunjuk Pelaksanaan PKL resmi sekolah** + format penilaian yang dipakai (perintah download di `pa-core`). Tiap sekolah beda bobot & durasi.
2. Data dasar: jurusan/konsentrasi keahlian · kelas yang melaksanakan · durasi (umum 3–6 bulan) · periode · jumlah siswa & sebaran industri.

## Dokumen yang bisa dibuat

### 1. Pedoman Pelaksanaan PKL (buku panduan siswa)
Struktur standar: dasar hukum/kebijakan sekolah → tujuan → peserta & syarat → tempat pelaksanaan → hak & kewajiban siswa/pembimbing → jadwal & tahapan (persiapan–pelaksanaan–laporan) → mekanisme bimbingan → sistem penilaian (+ bobot) → tata cara laporan → penghargaan/sanksi.

### 2. Jurnal Harian Siswa
Tabel per hari: `Tanggal/Hari · Kegiatan yang dilakukan (uraian konkret) · Kendala · Paraf pembimbing DU/DI`.
- Sediakan versi cetak (tabel kosong per halaman) DAN versi rekap digital.
- Kalau guru punya foto/scan jurnal isi murid, transkrip rapi pakai vision (aturan `pa-core`).

### 3. Catatan Kunjungan Pembimbing Sekolah
Per kunjungan: tanggal · tempat · temuan (kesesuaian kerja vs kompetensi, kendala murid, komunikasi DU/DI) · tindak lanjut · paraf. Rekap semua murid dalam satu tabel matriks kunjungan.

### 4. Instrumen Penilaian
**a. Pembimbing DU/DI** (yang paling sering dicetak ulang karena hilang 😅):
- **Sikap kerja**: kedisiplinan (kehadiran, ketepatan waktu), tanggung jawab, inisiatif, kerjasama, etika/kesopanan, kerapian & keselamatan kerja (K3)
- **Keterampilan kerja**: penguasaan alat/bahan, proses produksi/pelayanan sesuai kompetensi, hasil kerja/kualitas produk
- Skala 1–4 atau 0–100 (ikuti format sekolah) + deskripsi kualitatif

**b. Pembimbing sekolah**: kelengkapan jurnal · kemajuan laporan · responsivitas bimbingan · laporan akhir

**c. Penilaian Laporan**: struktur (BAB I–V: pendahuluan, profil tempat PKL, isi kegiatan, pembahasan, penutup), substansi teknis, sistematika bahasa.

### 5. Konversi Nilai PKL → Rapor
- Bobot umum dipakai sekolah: `Nilai PKL = w1×DU/DI + w2×Pembimbing sekolah + w3×Laporan` — **bobot WAJIB dari kebijakan sekolah** (contoh lazim 40/30/30, tapi jangan diasumsikan).
- Output `pa-nilai`-style: tabel per siswa (nilai komponen → nilai akhir → predikat A/B/C/D sesuai interval KKTP) siap masuk leger & e-Rapor.
- Verifikasi nama-tidak-tertukar WAJIB (`pa-core`) — salah konversi nilai = komplain orang tua.

## Output
Semua MD → HTML → PDF via pipeline `pa-core`. Instrumen penilaian & jurnal cetak pakai orientasi portrait dengan kolom paraf lega untuk tanda tangan basah.

## Pitfall
- Jangan generate penilaian atas nama pembimbing DU/DI — instrumen yang dibuat itu KOSONG untuk diisi mereka; yang boleh diolah hanya data yang sudah diisi & difoto/diketik guru
- Laporan siswa jangan ditulis-hasilkan utuh untuk murid (plagiarisme & tidak mengajar); buatkan outline + checklist kelengkapan + feedback atas draft murid
- Satu murid satu industri ≠ satu pembimbing sekolah — cek pembagian bimbingan sebelum bikin rekap
