---
name: pa-kktp
description: "Use when a teacher asks to define criteria for achieving learning objectives, including qualitative descriptors, score intervals, or mastery evidence. Confirm the school's assessment policy before drafting."
version: 1.5.0
author: Hermes Agent
license: MIT
---

# KKTP (Kriteria Ketercapaian Tujuan Pembelajaran)

## Prasyarat
- Daftar TP final (ATP/Prota).

## Output minimum

KKTP minimum menjelaskan bukti yang menunjukkan TP tercapai. Gunakan deskripsi kriteria, rubrik, atau interval sesuai kebijakan sekolah. Jangan mengubah KKTP menjadi satu angka batas secara otomatis.

Jika TP belum tersedia, berhenti dan minta TP atau sumber CP/ATP terlebih dahulu. Jika format atau interval sekolah belum tersedia, jangan menyebut, menawarkan, atau mengisi angka interval apa pun. Tawarkan hanya KKTP deskriptif berbasis bukti, dengan label draf, setelah guru menyetujui bahwa format resmi belum tersedia. Kata "angka umum" atau permintaan untuk "pakai default" tidak mengubah aturan ini.

## Langkah
1. Template resmi guru dulu - format KKTP sangat bervariasi (ada yang pakai rubrik indikator, ada yang deskripsi interval). Kasus nyata: draf dibuat "indikator + bentuk asesmen", ternyata format resmi = deskripsi kualitatif → rework total.
   - Untuk guru: format resmi diambil dari dokumen KKTP resmi sekolah — kolom: No | Bab | Materi Pokok | Tujuan Pembelajaran | Perlu Bimbingan (0–68) | Cukup (68–78) | Baik (79–89) | Sangat Baik (90–100). Interval ini kebijakan resmi sekolah, pakai apa adanya.
   - Blok identitas: Satuan Pendidikan / Mata Pelajaran / Semester: 3 (Ganjil), 4 (Genap), 5 (Ganjil) / Kelas / Fase: XI–XII / F / Tahun Pelajaran. Bagian per semester: "SEMESTER GANJIL (3) — KELAS XI (No 1–18)" dst. Kolom Bab diisi kode elemen (BD-F.1, dst.).
2. Konfirmasi kebijakan sekolah. Jangan menawarkan, memilih, atau mengisi interval angka sebelum guru memberikan interval resmi atau menyetujui draf angka secara eksplisit. Jika belum ada, gunakan bukti deskriptif tanpa angka dan beri label draf.
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
- PDF landscape 8 kolom: sel kriteria deskriptif itu tinggi — hasil ukur: maksimal **5 baris data asli per halaman**. Pecah tabel per bagian menjadi chunk ≤5 baris (halaman pertama dengan blok judul: 3 baris), pagebreak antar chunk, dan `tr{page-break-inside:avoid}` agar tidak ada baris yatim. Blok TTD ikut di halaman terakhir bila muat, sesuai pola TTD kanan + NIP di pa-core.
