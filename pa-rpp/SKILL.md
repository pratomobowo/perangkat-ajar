---
name: pa-rpp
description: "Use when a teacher asks to create, adapt, or revise a PPM, Modul Ajar, RPP, RPM, or another lesson plan for a specific class or learning objective. Check the school's requested format before drafting."
version: 1.3.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [rencana-pembelajaran, modul-ajar, rpp, ppm]
    related_skills: [pa-core, pa-lkpd, pa-media, pa-soal]
---

# Rencana Pembelajaran: PPM, Modul Ajar, atau RPP

## Tujuan

Buat rencana pembelajaran yang cukup untuk kebutuhan guru dan sekolah. Jangan otomatis membuat format panjang. Rencana pembelajaran dapat berupa dokumen baru, adaptasi dari dokumen yang sudah ada, atau revisi terbatas.

## Langkah 0: pastikan kebutuhan dan format

Sebelum menulis, tanyakan:

- dokumen apa yang diminta sekolah;
- apakah ada template resmi;
- dokumen atau materi apa yang sudah dimiliki guru;
- apakah guru ingin membuat baru, mengadaptasi, atau merevisi;
- jumlah pertemuan, durasi, kelas, dan tujuan pembelajaran.

Jika format sekolah belum diketahui, jangan menyatakan bahwa satu format adalah format nasional yang wajib.

## Langkah 1: pilih mode dokumen

### Mode ringkas

Gunakan jika sekolah hanya membutuhkan komponen inti atau guru meminta versi singkat:

1. Tujuan pembelajaran
2. Media atau sumber belajar
3. Langkah atau kegiatan pembelajaran
4. Asesmen

### Mode lengkap

Tambahkan bagian yang memang dibutuhkan sekolah atau membantu pelaksanaan:

- identitas dan karakteristik murid;
- kompetensi awal;
- sarana dan prasarana;
- model atau praktik pedagogis;
- pemahaman bermakna dan pertanyaan pemantik;
- pengalaman belajar memahami, mengaplikasi, dan merefleksi;
- diferensiasi, remedial, pengayaan, refleksi, dan lampiran.

Jangan mengisi bagian tambahan dengan paragraf generik hanya untuk membuat dokumen terlihat lengkap.

## Langkah 2: tentukan format yang diminta sekolah
1. **PPM**: gunakan jika sekolah memakai format ini atau guru memintanya. Istilah lokal seperti RPM atau RPPM dapat dipertahankan.
2. Modul Ajar Kurikulum Merdeka (format generasi sebelumnya, masih dipakai luas).
3. RPP K13 (sekolah yang belum transisi).

Minta template resmi sekolah dahulu dan ikuti istilah serta susunannya. Jika tidak ada template, sepakati mode ringkas atau lengkap sebelum drafting.

## Format PPM: kerangka 4 komponen
Struktur dokumen mengikuti template resmi; kalau belum ada, pakai pola berikut:

**A. Identitas & Identifikasi**
- Penyusun, sekolah, tahun pelajaran, mapel/fase/kelas/JP
- Identifikasi murid (hasil asesmen diagnostik awal - lihat `pa-soal` bagian Diagnostik)
- Materi pelajaran (faktual & konseptual)
- **Dimensi Profil Lulusan** yang dikembangkan (8 DPL: keimanan & ketakwaan, kewargaan, penalaran kritis, kreativitas, kolaborasi, kemandirian, kesehatan, komunikasi)

**B. Desain Pembelajaran**
- Tujuan Pembelajaran (+ pertemuan ke berapa)
- Topik pembelajaran
- Praktik pedagogis (model/pendekatan + SINTAKS lengkap vertikal)
- Kemitraan pembelajaran (kolaborasi orang tua/komunitas/DUDI bila relevan)
- Lingkungan pembelajaran (virtual/fisik/budaya)
- Pemanfaatan digital

**C. Pengalaman Belajar per pertemuan** - 3 tahap wajib:
- **Memahami** (AWAL + inti bagian konsep)
- **Mengaplikasi** (praktik/diskusi/proyek)
- **Merefleksi** (PENUTUP + refleksi)
Tiap tahap berlabel prinsip yang disentuh: *mindful / meaningful / joyful*. Alokasi menit per tahap harus menjumlah pas (`Σ = JP × menit_per_JP`; contoh pola seimbang: AWAL 15' / Memahami 40' / Mengaplikasi 80' / Merefleksi 30' / PENUTUP 15').

**D. Asesmen**: awal (diagnostik), proses (formatif), akhir (sumatif) + tindak lanjut remedial-pengayaan (rujuk `pa-soal`).

**TTD**: blok `kotak-ttd` dua kolom (Kepala Sekolah | Guru) + NIP bila diberikan.

## Fallback: Modul Ajar Kurikulum Merdeka
Informasi Umum (kompetensi awal, dimensi profil/pelajar, sarana) → Komponen Inti (TP, pemahaman bermakna, pertanyaan pemantik, kegiatan AWAL-INTI-PENUTUP, asesmen, pengayaan-remedial, refleksi) → Lampiran (LKPD via `pa-lkpd`, bahan bacaan, glosarium, pustaka).

## Fallback: RPP K13
Identitas → KD/IPK → TP → indikator → langkah pembelajaran → penilaian.

## Aturan angka
- **Alokasi waktu wajib tulis jumlah pertemuan**: `4 x 45 menit (180 menit), 1 pertemuan`; `pertemuan = JP ÷ jp_per_minggu`.
- Verifikasi `Σ menit tahap == JP × menit_per_JP`. Jika guru mengatakan angkanya salah, hitung dulu sebelum mengubah.
- Konsisten dengan Prota/Prosem (audit silang aturan #4 `pa-core`).

## Sumber isi
- Studi kasus dan materi ambil dari **LKPD atau sumber guru** (`pa-lkpd`) jika tersedia. Jangan mengarang materi resmi.
- Versi sederhana 3 komponen (tujuan, langkah, asesmen) dapat digunakan jika sesuai kebutuhan. Tanyakan mode yang diinginkan sekolah.
- Tanda prinsip MMJ ditulis italic singkat, bukan paragraf teori panjang.

## Pitfall
- Dokumen rawan halaman sepi. Jangan `page-break-inside: avoid` pada blok besar; pakai `h2/h4 { page-break-after: avoid }`.
- Konten LKPD tidak dicampur ke PPM. Keduanya adalah dokumen berbeda.
- Setelah revisi besar: grep keyword materi lama di SELURUH MD.

## Verifikasi
- Format output sesuai permintaan sekolah atau mode yang disepakati.
- Tujuan, kegiatan, dan asesmen saling selaras.
- Semua input wajib tersedia atau ditandai sebagai placeholder.
- Alokasi waktu setiap tahap dan total pertemuan dapat dihitung.
- Tidak ada materi atau kebijakan resmi yang dikarang.
- Jika PDF dibuat, jalankan pemeriksaan PyMuPDF bila tersedia. Jika dependensi atau script tidak tersedia, laporkan bahwa verifikasi PDF belum dijalankan.
- Σ menit per pertemuan benar; jumlah pertemuan = JP ÷ JP/minggu.
- Keyword struktur sesuai format. Untuk PPM, cek "Dimensi Profil Lulusan" dan "Memahami/Mengaplikasi/Merefleksi" jika memang diminta template.
- TTD utuh satu halaman, tidak jatuh ke halaman sepi.
