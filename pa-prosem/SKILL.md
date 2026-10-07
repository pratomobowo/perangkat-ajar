---
name: pa-prosem
description: "Use when a teacher asks to distribute learning objectives or topics across weeks and months in one semester. Require the annual plan and official school calendar before calculating the matrix."
version: 1.5.0
author: Hermes Agent
license: MIT
---

# Prosem (Program Semestre)

## Prasyarat
- Prota (`pa-prota`) + rekap kalender per bulan (jumlah minggu efektif tiap bulan) yang sudah diverifikasi saat menyusun Prota.

## Output minimum

Prosem memetakan TP atau unit belajar ke waktu dalam satu semester. Matriks landscape dan baris kegiatan sekolah hanya dibuat jika format sekolah memerlukannya.

## Langkah
1. Template resmi guru dulu - format Prosem paling bervariasi antar sekolah (matriks minggu vs tabel bulanan). Ikuti yang resmi.
2. Bangun matriks **per semester**:
   - Kolom = bulan (Jul..Des atau Jan..Jun), tiap bulan dipecah sesuai jumlah minggu efektifnya.
   - Baris pertama = **Kegiatan sekolah** per minggu: LIBUR, MPLS, STS, SAS, RAPORT, dst.
   - Baris per bab/TP = angka JP per minggu efektif (sesuai alokasi Prota).
   - Kolom penomoran **Pert. Ke-** per semester (mulai 1 lagi di genap) + kolom Keterangan.
3. ⚠️ Posisi STS/SAS/RAPORT di matriks adalah **perkiraan dari kalender** - selalu minta guru cek ulang tanggal aktualnya.
4. Pertemuan harus konsisten: `Σ pertemuan TP = JP_TP ÷ jp_per_minggu`.

## Format PDF - ATURAN KERAS (hasil uji nyata)
- **WAJIB A4 LANDSCAPE** - portrait memotong kolom kanan (bulan akhir & Keterangan hilang).
  ```bash
  python3 gen_pdf_from_md.py in.md out.pdf "PROSEM <Mapel> - <Sekolah>" landscape
  ```
- **Matriks lebar WAJIB HTML `<table>`**, bukan markdown table - markdown table pecah (nama bulan terpotong, baris Kegiatan terbelah). Struktur teruji:
  - Baris 1: nama bulan dengan `colspan` = jumlah minggu bulan tsb; kolom No & Unit juga `colspan` baris ini.
  - Baris 2: nomor minggu 1..n per kolom.
  - Baris Kegiatan: `colspan` No+Unit lalu label per kolom dengan class `keg`.
  - Sel isi pakai class `c` (center); label kegiatan class `keg` (sudah disediakan CSS pipeline).
- Idealnya **1 halaman per semester**; pisahkan Ganjil/Genap dengan `<div class="pagebreak"></div>`. Jangan biarkan tabel terpotong antar halaman.

## Verifikasi (WAJIB)
```python
import fitz, re
doc = fitz.open(pdf)
text = "".join(p.get_text() for p in doc)
# semua nama bulan + "Keterangan" harus ada (kalau hilang = terpotong/portrait)
assert all(b in text for b in ["Juli","Agustus","September","Oktober","November","Desember","Keterangan"])
```
- Cek orientasi halaman 1: `doc[0].rect.width > doc[0].rect.height`.
- Jumlah pertemuan & JP per TP = Prota (audit silang).
- Total minggu efektif pada matriks = rekap kalender yang disetujui.

## Pitfall
- Menambah kolom baru → update SEMUA `colspan`.
- Warna sel paling andal via inline `style="background:..."`.
- Halaman kosong setelah tabel besar → jangan pasang `page-break-inside: avoid` pada tabel sangat panjang.
- Generator skrip menimpa ulang MD dari nol — status dokumen & revisi manual HARUS ikut diurus di dalam skrip, bukan diedit langsung di MD (akan hilang saat regenerate).

## Konvensi hasil praktik (SMK, disetujui sementara guru 2026-10-07)

Prosem Basis Data Fase F ([Nama Guru], NIP [NIP]):
- Satu dokumen, 3 semester efektif @1 halaman landscape: XI Ganjil (19 ME: Jul 3, Agu 4, Sep 5, Okt 4, Nov 3), XI Genap (17 ME: Jan 3, Feb 3, Mar 2, Apr 4, Mei 4, Jun 1), XII Ganjil (19 ME, struktur bulan sama dengan XI ganjil).
- Bulan asesmen (Desember/Juni, ME kecil/nol) tetap diberi kolom kegiatan non-efektif (SAS, Remedial, Porseni, Rapor) agar baris Kegiatan lengkap; sel JP TP dikosongkan di kolom tsb.
- Tiap TP dialokasikan ke minggu efektif berurutan @4 JP/minggu (TP 2 JP berbagi minggu); kolom Pert. Ke- = nomor minggu (rentang bila >1 minggu, mis. "6–8"), dinomori ulang per semester.
- Baris Kegiatan: MPLS, Tes Kompetensi, Ujian Praktek, SAS, Rapor, libur — posisi perkiraan dari kalender, selalu minta guru cek ulang tanggal aktual.
- Audit silang terprogram: Σ sel JP per baris TP == alokasi Prota untuk semua TP.
- Status: `DRAF` sampai disetujui; persetujuan bisa bersifat sementara ("format dapat disesuaikan kemudian") — catat itu di status line dan memori.
- Blok tanda tangan rata kanan + NIP (format di `pa-core`); kecilkan font tabel via `extra_css` bila kolom sangat banyak.
