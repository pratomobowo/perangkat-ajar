---
name: pa-media
description: Membuat bahan ajar — materi pembelajaran per TP (ringkasan terstruktur, MD+PDF) dan slide/deck pembelajaran (PPTX via python-pptx atau handout PDF). Termasuk konvensi slide yang enak dibaca di kelas (1 konsep, ≤6 bullet, kode monospace).
---

# Materi Ajar & Media Belajar

## Prasyarat
- TP + materi pokok dari ATP/Prota (`pa-atp`); LKPD resmi guru sebagai sumber konten bila ada.

## 1. Materi Pembelajaran (bahan bacaan siswa/guru)
Struktur ringkas per TP:
- `# MATERI: <Topik>` + sub-judul identitas
- **Pengertian/konteks** → **Konsep inti** (bullet, bukan wall of text) → **Contoh nyata** (studi kasus dari LKPD) → **Ringkasan** (5–7 poin)
- Sintaks perintah/kode → block code; tabel perbandingan → markdown table
- Referensi (buku/jurnal/dokumentasi resmi)
Generate PDF via pipeline `pa-core`. Panjang wajar 3–8 halaman per TP — kalau lebih, pecah per pertemuan.

## 2. Slide Pembelajaran
Konvensi slide kelas (teruji):
- **1 konsep = 1 slide**; maksimal ±6 bullet/slide; kalimat pendek, bukan paragraf
- Slide judul (topik + identitas) → agenda singkat → isi → rangkuman/quiz penutup
- Kode/perintah pakai font monospace, ukuran ≥18pt; angka penting besar & berwarna
- Footer konsisten: mapel · TP · halaman
Implementasi (sesuai tooling tersedia):
- **python-pptx** (`pip install python-pptx`): generate .pptx programatik dari outline MD — pilih saat guru butuh file PowerPoint asli.
- **Handout PDF**: outline MD → pipeline PDF biasa — cukup untuk dicetak/dibagikan.
Minta template/logo sekolah dulu bila ada standar tampilan.

## 3. Bank Pertanyaan Interaktif (Quizizz/Kahoot/Wordwall)
Nexie tidak memainkan platform eksternal — yang dibuat adalah **bank pertanyaannya**: tabel No | Pertanyaan | Opsi | Jawaban | Waktu | Penjelasan, siap import. Format import ikuti platform tujuan (tanya gurunya mau pakai apa).

## Pitfall
- Jangan tempel teks panjang ke slide; itu tugas materi bacaan (#1), slide hanya kerangka bicara.
- Gambar/grafik: pakai data nyata dari studi kasus, bukan ilustrasi acak.
- PPTX hasil python-pptx selalu dicek dibuka ulang (jumlah slide + judul) sebelum dikirim.
