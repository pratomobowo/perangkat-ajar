---
name: pa-lkpd
description: "Use when a teacher asks to create or revise a student worksheet, activity sheet, practical case, or its assessment rubric. Use approved content and keep the worksheet separate from the lesson plan."
version: 1.4.0
author: Hermes Agent
license: MIT
---

# LKPD (Lembar Kerja Peserta Didik)

## Peran penting: LKPD = sumber isi
Saat membuat RPP/modul ajar (`pa-rpp`), **minta dulu LKPD resmi gurunya** - LKPD mendefinisikan studi kasus, materi singkat, soal praktik, rubrik, dan kriteria penguasaan. Menulis RPP dengan kasus karangan sendiri padahal LKPD resmi ada = revisi total. Skill ini untuk MEMBUAT LKPD baru saat guru memang belum punya.

## Struktur LKPD yang teruji
1. **Identitas** (judul/topik, mapel, kelas/fase, alokasi waktu, nama kelompok kosong)
2. **Petunjuk pengerjaan** (langkah kerja, bentuk output, tenggat)
3. **Studi kasus** - konkret, kontekstual, disepakati guru (jangan mengarang sendiri kalau guru punya preferensi)
4. **Materi singkat** + referensi (buku/jurnal) - bullet list, bukan wall of text
5. **Soal/tugas praktik** bertahap (tiap tahap jelas outputnya)
6. **Rubrik penilaian skor 100**: tabel langkah/aspek × skor maks × kriteria per skor
7. **Kriteria penguasaan**: A/B/C/D dengan rentang nilai (konfirmasi rentang ke guru; lazim 91-100/80-90/65-79/<64)
8. **Panduan pengumpulan** (format nama file, kanal pengumpulan)

## Output minimum

LKPD minimum berisi tujuan atau kompetensi, instruksi aktivitas, ruang atau format bukti kerja, dan kriteria penilaian. Studi kasus, materi, rubrik, dan lampiran ditambahkan sesuai kebutuhan. Jangan membuat kasus atau data industri seolah-olah resmi tanpa sumber atau persetujuan guru.

## Format agar enak dipandang (hasil uji revisi nyata)
- Paragraf panjang → **bullet/numbered list**
- Kode/perintah terminal → **block code** (terpisah dari teks penjelasan)
- Tabel perbandingan → bungkus `<div>` dengan `page-break-inside: avoid`; padding sel cukup
- Kalau tabel kecil didorong halaman berikutnya menyisakan halaman sepi → kecilkan margin/line-height sedikit sampai muat
- Versi Word (.docx) bisa dibuat bila diminta (`python-docx`; heading berwarna, tabel grid, block code monospace + shading abu)

## Pitfall
- Rubrik skor maks harus menjumlah tepat 100 - hitung terprogram.
- Satu LKPD per TP (atau per pertemuan bila materi banyak) - tanya konvensi guru.
- Setelah LKPD final, selaraskan ringkasan materi di RPP bila guru minta (eksplisit).

## Verifikasi
- Σ skor rubrik = 100.
- Rentang A/B/C/D tidak tumpang-tindih & mencakup 0-100.
- PDF: tiap halaman >300 chars body (tidak ada halaman sepi), block code tidak terpotong antar halaman.
- Aktivitas menghasilkan bukti yang dapat dinilai dan selaras dengan tujuan.
- Instruksi dapat diikuti tanpa penjelasan lisan yang tidak tersedia di dokumen.
- Data murid atau data mitra yang sensitif tidak masuk contoh publik.
