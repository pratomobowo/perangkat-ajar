---
name: pa-prosem
description: "Use when a teacher asks to distribute learning objectives or topics across weeks and months in one semester. Require the annual plan and official school calendar before calculating the matrix."
---

# Prosem (Program Semestre)

## Prasyarat
- Prota (`pa-prota`) + rekap kalender per bulan (jumlah minggu efektif tiap bulan) yang sudah diverifikasi saat menyusun Prota.

## Langkah
1. Template resmi guru dulu — format Prosem paling bervariasi antar sekolah (matriks minggu vs tabel bulanan). Ikuti yang resmi.
2. Bangun matriks **per semester**:
   - Kolom = bulan (Jul..Des atau Jan..Jun), tiap bulan dipecah sesuai jumlah minggu efektifnya.
   - Baris pertama = **Kegiatan sekolah** per minggu: LIBUR, MPLS, STS, SAS, RAPORT, dst.
   - Baris per bab/TP = angka JP per minggu efektif (sesuai alokasi Prota).
   - Kolom penomoran **Pert. Ke-** per semester (mulai 1 lagi di genap) + kolom Keterangan.
3. ⚠️ Posisi STS/SAS/RAPORT di matriks adalah **perkiraan dari kalender** — selalu minta guru cek ulang tanggal aktualnya.
4. Pertemuan harus konsisten: `Σ pertemuan TP = JP_TP ÷ jp_per_minggu`.

## Format PDF — ATURAN KERAS (hasil uji nyata)
- **WAJIB A4 LANDSCAPE** — portrait memotong kolom kanan (bulan akhir & Keterangan hilang).
  ```bash
  python3 gen_pdf_from_md.py in.md out.pdf "PROSEM <Mapel> — <Sekolah>" landscape
  ```
- **Matriks lebar WAJIB HTML `<table>`**, bukan markdown table — markdown table pecah (nama bulan terpotong, baris Kegiatan terbelah). Struktur teruji:
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

## Pitfall
- Menambah kolom baru → update SEMUA `colspan`.
- Warna sel paling andal via inline `style="background:..."`.
- Halaman kosong setelah tabel besar → jangan pasang `page-break-inside: avoid` pada tabel sangat panjang.
