---
name: pa-nilai
description: Pengolahan nilai guru — input skor per TP/komponen (ketikan, CSV, atau Excel), hitung nilai akhir tertimbang, bandingkan dengan interval KKTP (tuntas/belum), statistik kelas, mapping remedial & pengayaan, rekap leger siap e-Rapor. Feed langsung ke pa-rapor.
---

# Pengolahan Nilai → Ketuntasan → Leger

Hilir dari `pa-soal` (skor asesmen) dan jembatan menuju `pa-rapor` (deskripsi) & leger. Skill ini = *tool* olah data, bukan generator dokumen.

## LANGKAH 0 — Tentukan parameter
1. **Bobot komponen** — WAJIB dari kebijakan sekolah/profil (`~/.hermes/perangkat-ajar/profil.yaml`), contoh lazim: Tugas 30% · STS 30% · SAS 40%. Kalau profil kosong, tanya sekali lalu simpan ke profil.
2. **Interval KKTP** — ambil dari dokumen `pa-kktp` guru (mis. A ≥ 90, B 80–89, C 70–79, D < 70; atau KKM/tuntas ≥ 70). Jangan mengarang angka.
3. Sumber skor: ketik manual di chat · file CSV/Excel (baca pakai script di bawah atau pandas bila tersedia).

## Script cepat: `scripts/olah_nilai.py`
```bash
# format CSV: nis,nama,tp1,tp2,... (header wajib; kolom selain nis/nama = komponen skor)
python3 olah_nilai.py nilai.csv --bobot "tp1=0.3,tp2=0.3,tp3=0.4" --kktp 70
# output: tabel MD per siswa (NA tertimbang + status) + statistik kelas + daftar remedial/pengayaan
python3 olah_nilai.py nilai.csv --selftest   # cek integritas rumus
```

## Alur kerja
1. **Validasi input dulu**: nama ganda/duplikat NIS, skor di luar rentang 0–100, kolom bobot ≠ kolom file → STOP dan tanya, JANGAN menebak (kesalahan nilai = komplain).
2. Hitung NA tertimbang per murid; bulatkan sesuai kebiasaan sekolah (umumnya 0 desimal atau 2).
3. Bandingkan dengan interval KKTP → status per TP (untuk rapor per-TP) dan per mapel (untuk leger).
4. Statistik kelas: mean, min, max, distribusi predikat, % ketuntasan per TP.
5. **Mapping tindak lanjut**: belum tuntas → remedial (rujuk bagian Remedial & Pengayaan di `pa-soal`); melampaui KKTP tinggi → pengayaan.
6. Output: rekap MD di chat + XLSX/DOCX leger kalau diminta (openpyxl/python-docx).
7. **Feed ke `pa-rapor`**: hasil per-TP + status + narasi KKTP → generate deskripsi massal.

## Format output rekap
```
NIS | Nama | TP1 | TP2 | TP3 | NA | Predikat | Status | Tindak lanjut
```
+ blok statistik kelas + blok remedial/pengayaan.

## Pitfall
- Sel kosong ≠ nol: tanya dulu (belum dinilai? memang absen? remidi belum masuk?)
- Excel sering punya baris kosong/merged cells di atas header — bersihkan sebelum parse
- Nilai rata-rata sederhana ≠ nilai akhir berbobot — pastikan bobot disetujui guru SEBELUM hitung massal
- Data murid sensitif (aturan universal `pa-core`): jangan sebar rekap lengkap ke chat grup; kirim ke guru pribadi
