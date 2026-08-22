---
name: pa-p5
description: "Use when a teacher asks for a P5 project document, project module, facilitator journal, reflection sheet, or project report. Check whether the school uses P5 terminology or a newer cocurricular format."
version: 1.4.0
author: Hermes Agent
license: MIT
---

# P5 - Projek Penguatan Profil Pelajar Pancasila

Skill ini menghasilkan dokumen projek atau kokurikuler sesuai format sekolah: **modul projek**, **jurnal fasilitasi**, **lembar refleksi**, dan **rapor projek**. Jangan menyebut satu format sebagai dokumen wajib untuk semua sekolah.

## LANGKAH 0 - Cek dulu (pitfall #1)
1. Minta **template modul projek & format rapor projek resmi sekolah** dulu - tiap sekolah/dinas punya varian (perintah download di `pa-core`).
2. Era Pembelajaran Mendalam: beberapa sekolah menyebutnya "Projek Profil Pelajar Pancasila" atau mengintegrasikannya ke DPL (8 dimensi profil lulusan, lihat `pa-rpp`). Ikuti istilah sekolah; bawaan panduan nasional memakai **6 dimensi Profil Pelajar Pancasila**.
3. Alokasi waktu & jenis projek (ko-kurikuler / intra-kurikuler) ambil dari struktur kurikulum (KOSP) sekolah - JANGAN tebak angka dari internet.

## Bahan mentah yang dibutuhkan
- Tema & topik projek (kalau guru belum punya, tawarkan dari daftar tema di bawah sesuai konteks lokal sekolah)
- Kelompok kelas/fase + jumlah murid
- Alokasi waktu (jumlah pertemuan × menit)
- Tim pengampu (nama + peran)

## Output minimum

Buat hanya modul, jurnal, refleksi, atau rapor yang diminta. Tujuan projek, aktivitas, produk, dan asesmen harus dapat ditelusuri ke konteks sekolah dan dimensi atau profil yang dipilih.

## 7 Tema P5
Kearifan Lokal · Bangunlah Jiwa dan Raganya · Gaya Hidup Berkelanjutan · Bhinneka Tunggal Ika · Suara Demokrasi · Rekayasa dan Teknologi · Kewirausahaan dan Ekonomi Kreatif

## 6 Dimensi Profil Pelajar Pancasila (+ elemen)
1. **Beriman, bertakwa kepada Tuhan YME, dan berakhlak mulia** - akhlak beribadah · akhlak pergaulan · akhlak terhadap sesama manusia · akhlak terhadap alam
2. **Berkebinekaan global** - mengenal & menghargai budaya · komunikasi/interaksi lintas budaya · refleksi & tanggung jawab atas keberagaman
3. **Bergotong royong** - kolaborasi · kepedulian · berbagi
4. **Mandiri** - regulasi diri · refleksi diri
5. **Bernalar kritis** - memperoleh & memproses informasi/gagasan · menganalisis & mengevaluasi penalaran · mengambil kesimpulan
6. **Kreatif** - menghasilkan gagasan orisinal · menghasilkan karya orisinal

Modul projek umumnya memilih 2-3 dimensi saja - jangan pakai semuanya.

## Format Modul Projek

**A. Informasi Umum**: nama projek · tema · topik · kelompok kelas · alokasi waktu · jenis projek (ko/intra-kurikuler) · sekolah · tahun pelajaran · tim pengampu (tabel nama-peran-deskripsi tugas).

**B. Komponen Inti**
1. **Dimensi & elemen terpilih** (dari daftar di atas)
2. **Tujuan pembelajaran** per dimensi (rumusan perilaku teramati, bukan TP mapel)
3. **Langkah aktivitas** - 3 tahap wajib:
   - **Memulai**: pengenalan konteks/masalah, pemetaan minat murid, pembagian kelompok
   - **Pengembangan**: aksi nyata - riset lapangan, eksperimen, wawancara, produksi produk; sertakan jadwal per pertemuan
   - **Penutup**: demonstrasi/pameran karya, presentasi, refleksi & perayaan
4. **Produk** (karya konkret yang dihasilkan kelompok)
5. **Asesmen** - instrumen per jenis: observasi · jurnal · refleksi · penilaian diri · antarteman · portofolio · presentasi → rubrik 4 level (lihat Rapor)

**C. Lampiran**: jurnal proses belajar · lembar refleksi guru & murid · rencana dokumentasi

## Jurnal Fasilitasi
Tabel per pertemuan: `No · Tanggal · Kelompok/Kelas · Dimensi yang difasilitasi · Uraian kegiatan (apa yang dilakukan murid, apa yang dilakukan fasilitator) · Catatan/refleksi`. Isi otomatis dari catatan pelaksanaan yang guru ceritakan di chat - jangan biarkan kolom kosong, kalau data kurang TANYA.

## Rapor Projek (paling sering ditunggu wali murid!)
- Per murid, per dimensi-elemen: **narasi deskriptif + predikat**.
- 4 kategori capaian: **Baru berkembang → Sedang berkembang → Berkembang sesuai harapan → Sangat berkembang**.
- Narasi = bukti perilaku konkret selama projek (dari jurnal fasilitasi), bukan klaim kosong. Pola: *"[Nama] menunjukkan [elemen] melalui [bukti konkret]; [saran pengembangan]."*
- Verifikasi nama-tidak-tertukar WAJIB (aturan universal `pa-core`) - kesalahan rapor projek fatal secara sosial.
- Kalau sekolah pakai e-Rapor P5, hasil tinggal ditempel ke aplikasi.

## Output
MD → HTML → PDF via pipeline `pa-core`. Blok tanda tangan: Kepala Sekolah | Koordinator/tim pengampu.

## Pitfall
- Tujuan projek ≠ tujuan mapel: tulis perilaku teramati ("murid mampu berkolaborasi dalam..."), bukan materi pelajaran
- Rubrik 4 level harus punya deskripsi beda-tajam antarlevel (level 1 vs level 2 harus jelas bedanya) - pakai pola rubrik `pa-lkpd`
- Raport projek sering minta per-elemen, bukan per-dimensi - cek template sekolah sebelum generate massal

## Verifikasi

- Istilah P5, kokurikuler, dan Profil Lulusan sesuai kebijakan sekolah.
- Alokasi waktu berasal dari KOSP atau dokumen resmi sekolah.
- Rubrik memiliki bukti perilaku atau produk yang dapat diamati.
- Rapor hanya dibuat dari jurnal atau bukti projek yang tersedia.
- Mapping nama murid diperiksa ulang dan data lengkap tetap lokal.
