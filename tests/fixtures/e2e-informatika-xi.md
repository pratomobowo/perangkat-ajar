# Fixture E2E Perangkat Ajar

Data ini sintetis untuk pengujian. Bukan dokumen resmi sekolah.

## Profil

- Jenjang: SMK
- Mata pelajaran: Informatika
- Fase/Kelas: F / XI
- Tahun pelajaran: 2026/2027
- JP per minggu: 4
- Durasi 1 JP: 45 menit
- Minggu efektif semester ganjil: 18
- Format sekolah: format ringkas sintetis disepakati untuk pengujian
- KKTP uji: TP1 dan TP2 menggunakan interval deskriptif yang disepakati di bawah

## CP sintetis

Pada akhir fase, peserta didik mampu menganalisis kebutuhan data, merancang basis data relasional sederhana, menerapkan normalisasi dasar, membuat query SQL untuk pengolahan data, dan menjelaskan hasilnya secara tertib serta bertanggung jawab.

## Ruang lingkup uji

Gunakan satu unit kecil agar alur cepat:

- TP1: Peserta didik mampu menjelaskan entitas, atribut, relasi, dan kunci utama pada kasus data perpustakaan.
- TP2: Peserta didik mampu merancang skema tabel relasional sederhana dari kasus data perpustakaan.
- Total unit: 8 JP dalam 2 pertemuan.

## Kalender sintetis untuk Prosem

Semester ganjil memiliki 18 minggu efektif:

| Bulan | Minggu efektif | Kegiatan unit |
| --- | ---: | --- |
| Juli | 3 | TP1 minggu 1-2, TP2 mulai minggu 3 |
| Agustus | 4 | TP2 |
| September | 4 | TP2 dan latihan |
| Oktober | 3 | asesmen unit dan penguatan |
| November | 2 | unit lain |
| Desember | 2 | unit lain dan penutup semester |

Unit uji memakai Juli minggu 1-3 dan Agustus minggu 1-2. Total alokasi unit tetap 8 JP.

## KKTP uji yang disepakati

- TP1 tercapai jika murid mengidentifikasi entitas, atribut, relasi, dan kunci utama dengan benar pada kasus perpustakaan.
- TP2 tercapai jika murid menghasilkan skema tabel dengan tabel relevan, kunci utama, dan hubungan antartabel yang konsisten.
- Predikat uji: Belum tercapai, Tercapai, Tercapai dengan penguasaan kuat.
- Pemetaan skor uji: 0-69 Belum tercapai, 70-89 Tercapai, 90-100 Tercapai dengan penguasaan kuat.

## Kesepakatan pengujian

- ATP hanya untuk TP1 dan TP2.
- Prota hanya memetakan unit 8 JP pada semester ganjil.
- Prosem hanya memakai minggu efektif sintetis yang tersedia.
- KKTP memakai bukti deskriptif, bukan angka default.
- Rencana pembelajaran memakai mode ringkas.
- LKPD, asesmen formatif 4 soal, pengolahan nilai, dan deskripsi rapor dibuat hanya setelah tahap sebelumnya konsisten.
- Bobot uji nilai: TP1 40%, TP2 60%.
- Data nilai sintetis: S01=80,85; S02=60,70; S03=95,90.

## Larangan pengujian

- Jangan mengklaim CP sintetis sebagai CP resmi.
- Jangan membuat dokumen di luar ruang lingkup.
- Jangan memakai data siswa nyata.
- Jika ada angka atau format yang ambigu, berhenti dan catat konflik.

## Gate kelulusan

Satu tahap lulus jika:

1. input tahap disebutkan;
2. output hanya mencakup scope yang diminta;
3. hubungan ke tahap sebelumnya dapat ditelusuri;
4. tidak ada angka atau kebijakan yang diarang;
5. ada verifikasi sebelum lanjut.

Alur target:

`CP -> TP -> ATP -> Prota -> Prosem -> KKTP -> Rencana ringkas -> LKPD/asesmen -> Nilai -> Rapor`

TKA, P5, PKL, admin, dan wali kelas tidak termasuk uji ini.

## Catatan hasil

| Tahap | Status | Temuan |
| --- | --- | --- |
| CP -> TP | Lulus | TP1 dan TP2 konsisten dengan CP sintetis |
| TP -> ATP | Lulus | Urutan konsep ke rancangan, tanpa TP tambahan |
| ATP -> Prota | Lulus | TP lengkap, alokasi unit 8 JP |
| Prota -> Prosem | Lulus | 18 minggu, 8 JP, semua bulan dan penempatan unit konsisten |
| TP -> KKTP | Lulus | Kriteria dan interval uji disepakati |
| KKTP -> Rencana | Lulus | Tujuan, kegiatan, dan bukti asesmen terhubung |
| Rencana -> LKPD/asesmen | Lulus | Asesmen mengukur TP1 dan TP2 |
| Nilai -> Rapor | Lulus | Predikat mengikuti KKTP dan mapping siswa benar |
| Gate lintas dokumen | Lulus | Semua gate uji terpenuhi pada fixture sintetis |

## Kriteria akhir

- Tidak ada TP yang hilang atau berubah tanpa dicatat.
- Total unit tetap 8 JP.
- KKTP dan asesmen mengukur TP yang sama.
- Bobot nilai tepat 100%.
- Deskripsi rapor bersumber dari nilai TP dan tidak tertukar.
- Semua output diberi label sintetis/draf.

## Perintah uji

Jalankan tiap tahap dalam sesi baru dengan skill yang relevan. Simpan hasil jawaban ke laporan uji, bukan ke folder output guru.

```bash
hermes chat -Q --max-turns 4 --skills pa-core,pa-analisis-cp -q "..."
```

Jangan meneruskan tahap berikutnya jika gate tahap sebelumnya gagal.

## Sumber aturan

Baseline internal: `pa-core/references/baseline-hulu-hilir.md`.
Sumber kebijakan resmi dipakai sebagai referensi prinsip, sedangkan CP dan angka pada fixture ini sengaja sintetis.
