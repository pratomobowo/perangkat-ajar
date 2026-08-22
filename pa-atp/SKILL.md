---
name: pa-atp
description: Membuat dokumen ATP (Alur Tujuan Pembelajaran) — mengurutkan TP hasil analisis CP menjadi rangkaian setahun beserta taksonomi SOLO, materi pokok, dan dimensi profil lulusan. Input dari pa-analisis-cp; output jadi input Prota.
---

# ATP (Alur Tujuan Pembelajaran)

## Prasyarat
- Hasil Analisis CP (`pa-analisis-cp`): daftar TP per elemen.

## Langkah
1. Template resmi guru dulu.
2. Diskusikan **urutan TP** di chat — urutan harus masuk akal sebagai alur belajar setahun (umumnya: konsep → perancangan → implementasi → operasional → tata kelola/proyek), boleh beda dari urutan tabel CP. Guru yang memutuskan.
3. Format kolom standar:

   | No | CP | Tujuan Pembelajaran | Taksonomi SOLO | Materi Pokok | Dimensi Profil Lulusan |

4. Isi taksonomi SOLO per TP: `Unistructural / Multistructural / Relational / Extended Abstract` (naik bertahap; TP akhir semester biasanya Relational/Extended Abstract).
5. Daftar dimensi profil lulusan sesuaikan dengan kurikulum sekolah (Kurikulum Merdeka umum: penalaran kritis, komunikasi, kolaborasi, kemandirian, kreativitas, kewargaan; beberapa sekolah memakai 8 dimensi termasuk keimanan & kesehatan) — **pakai daftar yang resmi di sekolah guru tsb**.
6. Boleh dibuat per semester lalu digabung jadi satu dokumen:
   - Header semester = "Ganjil & Genap"
   - Sub-heading `## SEMESTER GANJIL (TP1–TPn)` / `## SEMESTER GENAP (TPn+1–TPm)`
   - Catatan urutan singkat per semester (paragraf italic)
7. Generate PDF via pipeline `pa-core`.

## Pitfall
- Judul dokumen rapi: `# JUDUL` saja + 2 baris `<p class="sub">` pendek centered ("Mapel · Fase (Kelas)" lalu "Semester ... — Sekolah — TP xxx/xxx"). JANGAN baris info panjang ber-pemisah `|`.
- Nomor TP lanjut menyambung antar semester (Ganjil TP1–9 → Genap mulai TP10) — konfirmasi konvensi penomoran ke guru.
- Jangan isi alokasi JP di ATP — itu tugas Prota (pemisahan tanggung jawab dokumen).

## Verifikasi
- Semua TP dari analisis CP ada & tidak ada duplikat.
- SOLO naik secara wajar (tidak semua Extended Abstract di awal tahun).
- PDF: tabel utuh, header center.
