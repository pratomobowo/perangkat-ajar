---
name: pa-kktp
description: "Use when a teacher asks to define criteria for achieving learning objectives, including qualitative descriptors, score intervals, or mastery evidence. Confirm the school's assessment policy before drafting."
version: 1.4.0
author: Hermes Agent
license: MIT
---

# KKTP (Kriteria Ketercapaian Tujuan Pembelajaran)

## Prasyarat
- Daftar TP final (ATP/Prota).

## Output minimum

KKTP minimum menjelaskan bukti yang menunjukkan TP tercapai. Gunakan deskripsi kriteria, rubrik, atau interval sesuai kebijakan sekolah. Jangan mengubah KKTP menjadi satu angka batas secara otomatis.

## Langkah
1. Template resmi guru dulu - format KKTP sangat bervariasi (ada yang pakai rubrik indikator, ada yang deskripsi interval). Kasus nyata: draf dibuat "indikator + bentuk asesmen", ternyata format resmi = deskripsi kualitatif → rework total.
2. Konfirmasi interval nilai ke guru (contoh lazim): Perlu Bimbingan <68 · Cukup 68-78 · Baik 79-89 · Sangat Baik 90-100. Angka = kebijakan sekolah, jangan dipakai tanpa konfirmasi.
3. Format tabel:

   | No | Bab | Materi Pokok | TP | Perlu Bimbingan (0-x) | Cukup (x-y) | Baik (y-z) | Sangat Baik (z-100) |

4. Pola deskripsi tiap TP (gradasi konsisten):
   - Perlu Bimbingan: "**Belum mampu** ..." (+ apa yang belum)
   - Cukup: "**Mampu ... sebagian/dasar**, namun ..."
   - Baik: "**Mampu ... dengan baik**, sedikit kesalahan"
   - Sangat Baik: "**Mampu ... sepenuhnya/presisi penuh**"
5. Generate PDF, verifikasi.

## Urutan pembuatan
Umumnya KKTP dibuat **setelah Prosem** (butuh daftar materi final per semester) - tapi selalu tanya guru; beberapa sekolah minta lebih awal. Jangan asumsikan.

## Pitfall
- Deskripsi harus spesifik per TP (sebut konten/materinya), bukan kalimat generik copy-paste.
- Interval harus kontinu & tidak tumpang-tindih (68-78 lalu 79-89, bukan 68-80/80-89 ambigu - konvensi batas atas eksklusif atau inklusif konsisten satu gaya).
- Konsisten dengan batas tuntas yang nanti dipakai di program remedial (`pa-soal`) - catat angkanya di profil bila guru menetapkan.

## Verifikasi
- Tiap TP punya tepat 4 deskripsi.
- Rentang semua TP sama & menjumlah penuh 0-100.
- Setiap kriteria dapat diamati atau dinilai dari bukti asesmen yang jelas.
- PDF: kolom deskripsi tidak terpotong (tabel cukup lebar - pertimbangkan landscape jika 8+ kolom).
