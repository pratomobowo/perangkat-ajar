# Konteks Kebijakan Pendidikan Nasional (riset Agu 2026)

Baseline hasil riset SearXNG saat menyusun keluarga `pa-*`. Sumber primer tercantum di bawah — verifikasi ulang angka/jadwal bila sudah lebih dari 1 tahun.

## Pembelajaran Mendalam (PM) — arah nasional
- Portal resmi: `https://kurikulum.kemendikdasmen.go.id/pembelajaran-mendalam`; ada Permendikdasmen yang mengatur kerangkanya ("kerangka kerja pembelajaran mendalam terdiri atas empat komponen").
- Definisi resmi: pendekatan yang memuliakan, menciptakan suasana belajar **berkesadaran (mindful)**, **bermakna (meaningful)**, **menggembirakan (joyful)** melalui olah pikir, olah hati, olah rasa, olah raga secara holistik dan terpadu.
- Kerangka kerja 4 komponen: (1) Dimensi Profil Lulusan, (2) Prinsip pembelajaran (mindful/meaningful/joyful), (3) Proses pembelajaran (**memahami – mengaplikasi – merefleksi**), (4) Kerangka pembelajaran: praktik pedagogis + kemitraan + lingkungan belajar + pemanfaatan digital.
- **8 DPL**: keimanan & ketakwaan, kewargaan, penalaran kritis, kreativitas, kolaborasi, kemandirian, kesehatan, komunikasi.
- Karakteristik pedagogis versi portal: keterlibatan murid sebagai subjek, berkesadaran, memuliakan, guru sebagai pengembang budaya belajar, pemanfaatan teknologi digital, multi/interdisiplin ilmu.
- Implikasi keluarga `pa-*`: format rencana pembelajaran primer = PPM (`pa-rpp`); kolom identifikasi murid diisi dari asesmen diagnostik (`pa-soal`).

## Penyederhanaan administrasi guru
- Mendikdasmen Mu'ti (Nov 2025): beban administrasi guru dikurangi; tidak lagi mutlak mengejar 24 jam tatap muka; ada hari ruang belajar bagi guru.
- Perencanaan Pembelajaran cukup **3 komponen sederhana** (tujuan pembelajaran, langkah/kegiatan, asesmen) — tapi banyak sekolah masih mensyaratkan format lengkap → selalu tanya dulu (`pa-core` LANGKAH 0).
- Jurnal kelas harian: tidak wajib dalam Kurikulum Merdeka, "alangkah baiknya tetap dibuat"; sebagian sekolah/dinas tetap meminta → `pa-admin` selalu OPSIONAL dan jangan bikin manual dobel bila sekolah pakai aplikasi.
- Pengelolaan kinerja baru berlaku 1 Jan 2025, terintegrasi BKN — bukan dokumen yang digenerate keluarga ini.

## TKA (Tes Kemampuan Akademik)
- `https://tka.kemendikdasmen.go.id` / pusmendik: pelaporan capaian akademik individu murid dari penilaian terstandar.
- 2026: pendaftaran TKA+AN jenjang SMA/MA/sederajat & SMK/MAK dibuka ~Juli 2026; hasil TKA SD/sederajat dirilis ~Mei 2026. Jadwal tahunan — pastikan ulang tiap tahun.
- Implikasi `pa-soal`: mode soal berbasis stimulus (teks/tabel/grafik kasus) gaya literasi-numerasi.

## Asesmen Kurikulum Merdeka (ringkas)
Diagnostik (awal semester/TP; non-kognitif + kognitif; BUKAN nilai rapor) → Formatif (proses belajar) → Sumatif (STS/SAS). Interval nilai & deskripsi mengacu KKTP sekolah masing-masing.

## Analisis butir soal (metode kelompok atas-bawah)
- Kelompok atas/bawah = ±27% berdasar skor total.
- Tingkat kesukaran `P = (BA+BB)/(N_atas+N_bawah)`: ≥0.71 mudah · 0.31–0.70 sedang · ≤0.30 sukar.
- Daya beda `D = BA/N_atas − BB/N_bawah`: ≥0.70 sangat baik · 0.40–0.69 baik · 0.30–0.39 cukup · 0.20–0.29 jelek · <0.20 gagal (butir ditolak/revisi).
- Pengecoh efektif bila dipilih ≥5% kelompok bawah; di bawah itu = pengecoh mati.
- Implementasi teruji: `pa-soal/scripts/analisis_butir.py`.

## Dokumen wali kelas (praktik umum lapangan)
Data siswa · program kerja wali kelas · jadwal pelajaran & piket · struktur organisasi kelas · denah duduk · leger · buku kasus pembinaan · analisis ketuntasan/kenaikan.

## Sumber utama
kurikulum.kemendikdasmen.go.id · pusatinformasi.rumahpendidikan.kemendikdasmen.go.id · tka.kemendikdasmen.go.id · kemendikdasmen.go.id/siaran-pers · kumparan/Kompas (kebijakan Mu'ti Nov 2025) · blog.kejarcita.id (komponen PPM).
