# Konteks Kebijakan Pendidikan Nasional

Baseline hasil riset SearXNG saat menyusun keluarga `pa-*`. Sumber primer tercantum di bawah - verifikasi ulang angka/jadwal bila sudah lebih dari 1 tahun.

## Pembelajaran Mendalam (PM) - arah nasional
- Portal resmi: `https://kurikulum.kemendikdasmen.go.id/pembelajaran-mendalam`; ada Permendikdasmen yang mengatur kerangkanya ("kerangka kerja pembelajaran mendalam terdiri atas empat komponen").
- Definisi resmi: pendekatan yang memuliakan, menciptakan suasana belajar **berkesadaran (mindful)**, **bermakna (meaningful)**, **menggembirakan (joyful)** melalui olah pikir, olah hati, olah rasa, olah raga secara holistik dan terpadu.
- Kerangka kerja 4 komponen: (1) Dimensi Profil Lulusan, (2) Prinsip pembelajaran (mindful/meaningful/joyful), (3) Proses pembelajaran (**memahami - mengaplikasi - merefleksi**), (4) Kerangka pembelajaran: praktik pedagogis + kemitraan + lingkungan belajar + pemanfaatan digital.
- **8 DPL**: keimanan & ketakwaan, kewargaan, penalaran kritis, kreativitas, kolaborasi, kemandirian, kesehatan, komunikasi.
- Karakteristik pedagogis versi portal: keterlibatan murid sebagai subjek, berkesadaran, memuliakan, guru sebagai pengembang budaya belajar, pemanfaatan teknologi digital, multi/interdisiplin ilmu.
- Implikasi keluarga `pa-*`: format rencana pembelajaran primer = PPM (`pa-rpp`); kolom identifikasi murid diisi dari asesmen diagnostik (`pa-soal`).

## Perencanaan pembelajaran dan penyederhanaan administrasi
- [Panduan Pembelajaran dan Asesmen](https://kurikulum.kemdikbud.go.id/file/1720050633_manage_file.pdf) menyatakan bahwa RPP dapat dibuat sederhana. Komponen minimumnya adalah tujuan pembelajaran, langkah-langkah pembelajaran, dan asesmen pembelajaran.
- Modul ajar merupakan bentuk perencanaan yang lebih lengkap. Jika guru menggunakan modul ajar yang sudah memuat komponen RPP, guru tidak perlu membuat RPP terpisah.
- Guru dapat menggunakan, mengadaptasi, atau memodifikasi contoh perangkat ajar sesuai kebutuhan peserta didik dan konteks sekolah. Tidak semua komponen tambahan modul ajar wajib dicantumkan.
- [Panduan Pembelajaran dan Asesmen versi terbaru](https://kurikulum.kemdikbud.go.id/file/1755668120_manage_file.pdf) menempatkan perencanaan sebagai proses merumuskan tujuan belajar, menentukan bukti asesmen, lalu memilih langkah pembelajaran yang membantu murid mencapai tujuan tersebut.
- Kebutuhan jurnal kelas, daftar hadir, dan administrasi lain tetap harus dicek berdasarkan kebijakan sekolah, dinas, dan aplikasi yang digunakan. Jangan menyimpulkan bahwa satu dokumen selalu wajib atau selalu tidak diperlukan.
- Pengelolaan kinerja baru berlaku 1 Jan 2025, terintegrasi BKN - bukan dokumen yang digenerate keluarga ini.

## TKA (Tes Kemampuan Akademik)
- `https://tka.kemendikdasmen.go.id` / pusmendik: pelaporan capaian akademik individu murid dari penilaian terstandar.
- 2026: pendaftaran TKA+AN jenjang SMA/MA/sederajat & SMK/MAK dibuka ~Juli 2026; hasil TKA SD/sederajat dirilis ~Mei 2026. Jadwal tahunan - pastikan ulang tiap tahun.
- Implikasi `pa-soal`: mode soal berbasis stimulus (teks/tabel/grafik kasus) gaya literasi-numerasi.

## Asesmen Kurikulum Merdeka (ringkas)
Diagnostik (awal semester/TP; non-kognitif + kognitif; BUKAN nilai rapor) → Formatif (proses belajar) → Sumatif (STS/SAS). Interval nilai & deskripsi mengacu KKTP sekolah masing-masing.

## RPP dan modul ajar: aturan praktis untuk skill

1. Tanyakan apakah sekolah meminta RPP, modul ajar, PPM, atau istilah lokal lainnya.
2. Tanyakan apakah guru sudah memiliki perangkat yang dapat digunakan atau diadaptasi.
3. Jika kebutuhan hanya perencanaan inti, gunakan mode ringkas: tujuan, langkah, asesmen.
4. Tambahkan media, bahan ajar, LKPD, jobsheet, diferensiasi, refleksi, dan lampiran hanya jika relevan.
5. Jangan membuat RPP dan modul ajar sebagai dua dokumen terpisah jika modul ajar sudah mencakup komponen RPP.
6. Rancang dari tujuan dan bukti belajar. Jangan memulai dari daftar komponen atau template kosong.

## Konteks SMK

Pada mata pelajaran kejuruan, terutama Dasar-dasar Program Keahlian dan Konsentrasi Keahlian, modul ajar dapat dilengkapi buku pelajaran, handout, media visual, media interaktif, lembar kerja, atau jobsheet. Materi dapat disusun dengan mempertimbangkan SKKNI dan/atau bersama mitra dunia kerja jika relevan. Rujukan: [Pembelajaran dan Asesmen](https://kurikulum.kemdikbud.go.id/file/1755668120_manage_file.pdf).

## Analisis butir soal (metode kelompok atas-bawah)
- Kelompok atas/bawah = ±27% berdasar skor total.
- Tingkat kesukaran `P = (BA+BB)/(N_atas+N_bawah)`: ≥0.71 mudah · 0.31-0.70 sedang · ≤0.30 sukar.
- Daya beda `D = BA/N_atas − BB/N_bawah`: ≥0.70 sangat baik · 0.40-0.69 baik · 0.30-0.39 cukup · 0.20-0.29 jelek · <0.20 gagal (butir ditolak/revisi).
- Pengecoh efektif bila dipilih ≥5% kelompok bawah; di bawah itu = pengecoh mati.
- Implementasi teruji: `pa-soal/scripts/analisis_butir.py`.

## Dokumen wali kelas (praktik umum lapangan)
Data siswa · program kerja wali kelas · jadwal pelajaran & piket · struktur organisasi kelas · denah duduk · leger · buku kasus pembinaan · analisis ketuntasan/kenaikan.

## Sumber utama

- [Panduan Pembelajaran dan Asesmen](https://kurikulum.kemdikbud.go.id/file/1720050633_manage_file.pdf)
- [Pembelajaran dan Asesmen versi terbaru](https://kurikulum.kemdikbud.go.id/file/1755668120_manage_file.pdf)
- [Panduan Pengembangan Kurikulum Satuan Pendidikan](https://kurikulum.kemdikbud.go.id/file/1755670818_manage_file.pdf)
- [Pembelajaran Mendalam dan Permendikdasmen Nomor 13 Tahun 2025](https://gtk.kemendikdasmen.go.id/news/siaran-pers/c034d26f-83b6-4b4b-926c-b572e665e477)
- [Regulasi TKA, Pusat Asesmen Pendidikan](https://pusmendik.kemdikbud.go.id/regulasi)

Gunakan portal dan dokumen resmi sebagai sumber utama. Sumber media atau blog hanya dipakai untuk konteks tambahan dan tidak boleh menjadi dasar tunggal klaim kebijakan.
