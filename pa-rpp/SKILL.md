---
name: pa-rpp
description: Membuat rencana pembelajaran per TP — format primer PPM (Perencanaan Pembelajaran Mendalam, kebijakan nasional Pembelajaran Mendalam Kemendikdasmen) dengan kerangka 4 komponen; fallback Modul Ajar Kurikulum Merdeka atau RPP K13 atau varian lokal sekolah (RPM/RPPM). WAJIB ambil template resmi sekolah dulu.
---

# Rencana Pembelajaran — PPM / Modul Ajar / RPP

## LANGKAH 0 — Tentukan format yang diminta sekolah
1. **PPM (primer nasional)** — format era Pembelajaran Mendalam (Permendikdasmen; rujukan kurikulum.kemendikdasmen.go.id). Banyak sekolah menyebutnya dengan istilah lokal (kasus nyata: "RPM").
2. Modul Ajar Kurikulum Merdeka (format generasi sebelumnya, masih dipakai luas).
3. RPP K13 (sekolah yang belum transisi).

Minta template resmi sekolah DULU dan ikuti persis (perintah download di `pa-core`) — ini pitfall #1 global.

## Format PPM — kerangka 4 komponen
Struktur dokumen mengikuti template resmi; kalau belum ada, pakai pola berikut:

**A. Identitas & Identifikasi**
- Penyusun, sekolah, tahun pelajaran, mapel/fase/kelas/JP
- Identifikasi murid (hasil asesmen diagnostik awal — lihat `pa-soal` bagian Diagnostik)
- Materi pelajaran (faktual & konseptual)
- **Dimensi Profil Lulusan** yang dikembangkan (8 DPL: keimanan & ketakwaan, kewargaan, penalaran kritis, kreativitas, kolaborasi, kemandirian, kesehatan, komunikasi)

**B. Desain Pembelajaran**
- Tujuan Pembelajaran (+ pertemuan ke berapa)
- Topik pembelajaran
- Praktik pedagogis (model/pendekatan + SINTAKS lengkap vertikal)
- Kemitraan pembelajaran (kolaborasi orang tua/komunitas/DUDI bila relevan)
- Lingkungan pembelajaran (virtual/fisik/budaya)
- Pemanfaatan digital

**C. Pengalaman Belajar per pertemuan** — 3 tahap wajib:
- **Memahami** (AWAL + inti bagian konsep)
- **Mengaplikasi** (praktik/diskusi/proyek)
- **Merefleksi** (PENUTUP + refleksi)
Tiap tahap berlabel prinsip yang disentuh: *mindful / meaningful / joyful*. Alokasi menit per tahap harus menjumlah pas (`Σ = JP × menit_per_JP`; contoh pola seimbang: AWAL 15' / Memahami 40' / Mengaplikasi 80' / Merefleksi 30' / PENUTUP 15').

**D. Asesmen**: awal (diagnostik), proses (formatif), akhir (sumatif) + tindak lanjut remedial-pengayaan (rujuk `pa-soal`).

**TTD**: blok `kotak-ttd` dua kolom (Kepala Sekolah | Guru) + NIP bila diberikan.

## Fallback: Modul Ajar KM
Informasi Umum (kompetensi awal, dimensi profil/pelajar, sarana) → Komponen Inti (TP, pemahaman bermakna, pertanyaan pemantik, kegiatan AWAL-INTI-PENUTUP, asesmen, pengayaan-remedial, refleksi) → Lampiran (LKPD via `pa-lkpd`, bahan bacaan, glosarium, pustaka).

## Fallback: RPP K13
Identitas → KD/IPK → TP → indikator → langkah pembelajaran → penilaian.

## Aturan angka yang sering salah
- **Alokasi waktu wajib tulis jumlah pertemuan**: `4 × 45 Menit (180 Menit) — 1 Pertemuan`; `pertemuan = JP ÷ jp_per_minggu`.
- Verifikasi `Σ menit tahap == JP × menit_per_JP`. Guru bilang "salah"? HITUNG dulu.
- Konsisten dengan Prota/Prosem (audit silang aturan #4 `pa-core`).

## Sumber isi
- Studi kasus & materi ambil dari **LKPD resmi guru** (`pa-lkpd`) — jangan karang sendiri.
- Versi sederhana 3 komponen (tujuan-langkah-asesmen) sah sesuai arah penyederhanaan — tanya sekolah mau versi mana.
- Tanda prinsip MMJ ditulis italic singkat, bukan paragraf teori panjang.

## Pitfall
- Dokumen rawan halaman sepi → jangan `page-break-inside: avoid` pada blok besar; pakai `h2/h4 { page-break-after: avoid }`.
- Konten LKPD tidak dicampur ke PPM — dua dokumen beda.
- Setelah revisi besar: grep keyword materi lama di SELURUH MD.

## Verifikasi (pymupdf)
- Σ menit per pertemuan benar; jumlah pertemuan = JP ÷ JP/minggu.
- Keyword struktur ada ("Dimensi Profil Lulusan", "Memahami/Mengaplikasi/Merefleksi" untuk PPM).
- TTD utuh satu halaman, tidak jatuh ke halaman sepi.
