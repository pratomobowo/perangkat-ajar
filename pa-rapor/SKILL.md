---
name: pa-rapor
description: "Use when a teacher asks to generate or review student report descriptions from criteria and scores. Verify student identity and keep the output private."
---

# Deskripsi Capaian Kompetensi (Kalimat Rapor)

## Prasyarat
- KKTP (`pa-kktp`): deskripsi interval per TP.
- Daftar nilai siswa per TP (export e-Rapor / rekap guru). Kalau belum ada nilai → tanya dulu; JANGAN mengarang angka.

## Langkah
1. **Konfirmasi sumber & bobot**: nilai rapor = gabungan formatif+sumatif? Bobotnya? Ikuti kebijakan sekolah/e-Rapor.
2. Tentukan predikat tiap siswa dari interval KKTP (Perlu Bimbingan/Cukup/Baik/Sangat Baik).
3. Susun deskripsi per siswa dengan pola konsisten:
   - Buka dengan penguasaan umum: "**Ananda <nama>** menunjukkan penguasaan yang sangat baik dalam ..." (sesuaikan panggilan konvensi sekolah: Ananda/Saudara/i)
   - Sebut **TP yang tercapai secara spesifik** (pakai kata kerja TP-nya, bukan generik): "...dalam merancang basis data relasional dan menerapkan normalisasi..."
   - Untuk TP belum tuntas → kalimat pembina, bukan label negatif: "perlu penguatan pada ..." / "sedang mengembangkan kemampuan ...", diikuti saran konkret.
4. Output: tabel `No | Nama | Predikat | Deskripsi Rapor` + file teks per kelas siap tempel e-Rapor.

## Verifikasi WAJIB (fatal kalau salah)
1. **Nama ↔ deskripsi tidak tertukar** - cocokkan mapping NIS→nama→deskripsi dua kali; salah pasang nama = masalah serius ke ortu.
2. Semua siswa punya deskripsi (jumlah baris = jumlah murid kelas).
3. Deskripsi spesifik: grep kata generik ("materi", "pelajaran") harus minim; tiap deskripsi menyebut ≥2 konten TP nyata.
4. Panjang wajar 2-4 kalimat (~40-80 kata); tidak ada predikat bertentangan dengan isi kalimat.
5. Konsistensi antar siswa selevel: dua siswa "Baik" boleh beda konten tapi setara bobot pujian.

## Pitfall
- Copy-paste generik ganti nama saja → langsung ketahuan guru/ortu; variasikan berdasarkan nilai per TP yang membedakan mereka.
- Kalimat untuk "Perlu Bimbingan" tetap hormat & konstruktif (aturan #9 `pa-core`: data sensitif).
- e-Rapor punya batas karakter kolom - cek dulu panjang maksimalnya.
