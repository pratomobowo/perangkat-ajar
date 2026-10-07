---
name: pa-atp
description: "Use when a teacher asks to create or revise an Alur Tujuan Pembelajaran from existing learning objectives. Check the source CP, phase, class, and school format first."
version: 1.5.0
author: Hermes Agent
license: MIT
---

# ATP (Alur Tujuan Pembelajaran)

## Prasyarat
- Hasil Analisis CP (`pa-analisis-cp`): daftar TP per elemen.

## Output minimum

ATP berisi TP yang diurutkan secara logis dan dapat ditelusuri ke CP. Materi, SOLO, dan dimensi Profil Lulusan hanya ditambahkan jika dibutuhkan format sekolah. Jangan menambahkan alokasi JP; itu diputuskan di Prota atau rencana pembelajaran.

## Langkah
1. Template resmi guru dulu.
2. Diskusikan **urutan TP** di chat - urutan harus masuk akal sebagai alur belajar setahun (umumnya: konsep → perancangan → implementasi → operasional → tata kelola/proyek), boleh beda dari urutan tabel CP. Guru yang memutuskan.
3. Format kolom standar:

   | No | CP | Tujuan Pembelajaran | Taksonomi SOLO | Materi Pokok | Dimensi Profil Lulusan |

4. Isi taksonomi SOLO per TP: `Unistructural / Multistructural / Relational / Extended Abstract` (naik bertahap; TP akhir semester biasanya Relational/Extended Abstract).
5. Daftar dimensi profil lulusan sesuaikan dengan kurikulum sekolah (Kurikulum Merdeka umum: penalaran kritis, komunikasi, kolaborasi, kemandirian, kreativitas, kewargaan; beberapa sekolah memakai 8 dimensi termasuk keimanan & kesehatan) - **pakai daftar yang resmi di sekolah guru tsb**.
6. Boleh dibuat per semester lalu digabung jadi satu dokumen:
   - Header semester = "Ganjil & Genap"
   - Sub-heading `## SEMESTER GANJIL (TP1-TPn)` / `## SEMESTER GENAP (TPn+1-TPm)`
   - Catatan urutan singkat per semester (paragraf italic)
7. Generate PDF via pipeline `pa-core`.

## Pitfall
- Judul dokumen rapi: `# JUDUL` saja + 2 baris `<p class="sub">` pendek centered ("Mapel · Fase (Kelas)" lalu "Semester ... - Sekolah - TP xxx/xxx"). JANGAN baris info panjang ber-pemisah `|`.
- Nomor TP lanjut menyambung antar semester (Ganjil TP1-9 → Genap mulai TP10) - konfirmasi konvensi penomoran ke guru.
- Jangan isi alokasi JP di ATP - itu tugas Prota (pemisahan tanggung jawab dokumen).
- Baris kosong di tengah tabel markdown MEMUTUS tabel (baris setelahnya jadi tabel baru tanpa header). Saat menggabung dua bagian tabel (mis. memadatkan semester), hapus baris kosong pemisahnya.

## Konvensi hasil praktik (SMK, disetujui guru 2026-10-06)

ATP Basis Data Fase F ([Nama Guru], NIP [NIP]):
- Satu dokumen Fase F (Kelas XI–XII), dibagi per semester efektif: XI Ganjil (No 1–18 / BD-F.1–BD-F.5), XI Genap (No 19–32 / BD-F.6–BD-F.9), XII Ganjil (No 33–43 / BD-F.10–BD-F.12). **Kelas XII hanya punya 1 semester efektif — semester genap dipakai penuh untuk PKL**, jadi seluruh TP Kelas XII dipadatkan di ganjil dengan catatan penjelasan di dokumen.
- Nomor TP memakai format `n.m` dari Analisis CP (mis. 2.1) agar tertelusur; kolom No adalah nomor urut 1–43 yang menyambung antar semester.
- Kolom: No | CP (kode + nama elemen singkat) | Tujuan Pembelajaran | Taksonomi SOLO | Materi Pokok | Dimensi Profil Lulusan.
- Dimensi: 8 dimensi profil lulusan Kurikulum Merdeka (keimanan & ketakwaan, kewargaan, penalaran kritis, kreativitas, kolaborasi, kemandirian, kesehatan, komunikasi); 1–3 dimensi per TP yang paling relevan.
- Tiap bagian semester diawali catatan alur singkat (italic).
- Status: `DRAF — menunggu persetujuan guru` sampai disetujui; setelah disetujui ubah menjadi `Disetujui — disetujui guru pada <tanggal>; dapat digunakan sebagai acuan Prota/Prosem dan perangkat pembelajaran`, lalu regenerate PDF.
- Blok tanda tangan rata kanan (format di `pa-core`, bagian TTD) dengan nama + NIP. Ruang TTD basah jangan terlalu sempit — spacer ±55px agar leluasa saat print; bila TTD terdorong ke halaman sepi sendiri, ketatkan sedikit di tempat lain (margin `.kotak-ttd`, padding `td`, line-height) lewat `extra_css` pada `md_to_pdf`, bukan dengan mengecilkan ruang TTD.

## Verifikasi
- Semua TP dari analisis CP ada & tidak ada duplikat.
- Setiap TP punya alasan urutan atau prasyarat yang masuk akal.
- Tidak ada TP yang hilang, tergandakan, atau ditambahkan tanpa sumber/keputusan guru.
- SOLO naik secara wajar (tidak semua Extended Abstract di awal tahun).
- PDF: tabel utuh, header center.
