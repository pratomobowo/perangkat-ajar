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
- Format sekolah: belum tersedia, gunakan mode ringkas dan tandai sebagai draf

## CP sintetis

Pada akhir fase, peserta didik mampu menganalisis kebutuhan data, merancang basis data relasional sederhana, menerapkan normalisasi dasar, membuat query SQL untuk pengolahan data, dan menjelaskan hasilnya secara tertib serta bertanggung jawab.

## Ruang lingkup uji

Gunakan satu unit kecil agar alur cepat:

- TP1: Peserta didik mampu menjelaskan entitas, atribut, relasi, dan kunci utama pada kasus data perpustakaan.
- TP2: Peserta didik mampu merancang skema tabel relasional sederhana dari kasus data perpustakaan.
- Total unit: 8 JP dalam 2 pertemuan.

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
| CP -> TP | Belum diuji | |
| TP -> ATP | Belum diuji | |
| ATP -> Prota | Belum diuji | |
| Prota -> Prosem | Belum diuji | |
| TP -> KKTP | Belum diuji | |
| KKTP -> Rencana | Belum diuji | |
| Rencana -> LKPD/asesmen | Belum diuji | |
| Nilai -> Rapor | Lulus terbatas | Mapping siswa dan TP benar; kata evaluatif tanpa interval KKTP menjadi catatan |
| Gate lintas dokumen | Lulus terbatas | Alur dan angka konsisten; rapor final tertahan sampai KKTP resmi tersedia |

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
