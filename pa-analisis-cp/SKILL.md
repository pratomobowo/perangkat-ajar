---
name: pa-analisis-cp
description: "Use when a teacher asks to analyze an official Capaian Pembelajaran and derive learning objectives per element or phase. Require the source CP before drafting."
---

# Analisis CP

## Prasyarat
- Profil guru ada (skill `pa-core`).
- **Dokumen CP resmi** mapel & fase terkait — minta dari guru atau file/teksnya. JANGAN mengarang/mengingat CP dari kepala; versi CP berbeda antar tahun.
- Untuk SMK: tanya apakah sekolah punya **CP hasil sinkronisasi industri/DUDI** — kalau ada, itu yang jadi acuan tambahan (sering menambah TP praktik yang tidak ada di CP nasional).

## Langkah
1. Ambil template format resmi guru dulu (aturan universal #1 di `pa-core`).
2. Diskusikan pembagian elemen & draf TP di chat → setuju → baru tulis dokumen.
3. Susun MD dengan struktur:
   - `# ANALISIS CAPAIAN PEMBELAJARAN` + `<p class="sub">Sekolah — Mapel | Fase X | Kelas | TP ...</p>`
   - Kotak CP nasional (blockquote) + kotak CP hasil sinkronisasi bila ada
   - Tabel penguraian: **No | Kode/Elemen | Elemen | Tujuan Pembelajaran**
   - Catatan analisis: KKO (kata kerja operasional yang dipakai), cakupan konten, konteks/situasi belajar, dimensi profil lulusan yang tersentuh, keterkaitan dengan mapel lain
4. Generate PDF via pipeline `pa-core`, verifikasi pymupdf.

## Format tabel penguraian (contoh)

| No | Elemen | Tujuan Pembelajaran |
|----|--------|---------------------|
| 1 | Pemahaman Konsep | Peserta didik mampu menjelaskan ... |
| 2 | Perancangan | Peserta didik mampu merancang ... |

## Pitfall
- TP harus **terukur** (ada kata kerja operasional + objek + konteks), bukan restatement materi.
- Urutan TP sebaiknya mengikuti **alur logika nyata bidang ilmunya** (mis. konsep → rancang → bangun → operasikan → kelola), bukan sekadar urutan teks CP — diskusikan dengan guru.
- Kalau guru bilang "sepertinya saya sudah punya analisisnya" → tunggu dulu draft gurunya, sesuaikan, jangan paksa dokumen buatan sendiri.

## Verifikasi
- Jumlah TP wajar untuk alokasi setahun (± 10–20 TP per fase-kelas; tanya guru).
- Semua elemen CP nasional terwakili di tabel.
- PDF: header center, tabel tidak terpotong.
