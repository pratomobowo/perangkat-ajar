# Perangkat Ajar — Skill AI untuk Guru Indonesia

Keluarga skill Hermes yang dirancang untuk membantu guru menyusun, memeriksa, dan mengembangkan perangkat ajar secara lebih cepat, konsisten, dan tetap mengikuti konteks sekolah masing-masing.

Proyek ini lahir dari kebutuhan nyata guru: bukan sekadar menghasilkan dokumen, tetapi membantu menerjemahkan capaian pembelajaran menjadi perangkat ajar yang runtut — dari analisis CP sampai asesmen, pengolahan nilai, dan deskripsi rapor.

> **Tujuan utama:** membantu guru mengurangi beban administratif agar lebih banyak waktu dapat digunakan untuk merancang pengalaman belajar yang bermakna bagi murid.

## Prinsip proyek

- **Guru tetap pengambil keputusan.** AI membantu menyusun dan memeriksa, bukan menggantikan pertimbangan profesional guru.
- **Konteks sekolah lebih penting daripada template generik.** Format resmi sekolah, kalender pendidikan, dan kebijakan satuan pendidikan menjadi rujukan utama.
- **Dari hulu ke hilir, tetapi fleksibel.** Guru dapat memulai dari dokumen yang belum tersedia tanpa dipaksa mengikuti urutan tertentu.
- **Angka dan konsistensi dapat diverifikasi.** Alokasi JP, minggu efektif, komposisi asesmen, dan output PDF diperiksa dengan bantuan skrip.
- **Privasi murid dijaga.** Data nilai, kasus, kehadiran, dan informasi pribadi diproses secara hati-hati dan tidak dibagikan tanpa persetujuan.

## Siapa yang dapat menggunakan?

- Guru SD, SMP, SMA, dan SMK di Indonesia
- Wali kelas dan koordinator projek
- Tim kurikulum atau komunitas belajar guru
- Pengembang asisten AI pendidikan berbasis Hermes Agent

## Status

**Versi:** 1.2 · **Status:** usable untuk pengembangan dan uji lapangan

Keluarga skill ini terus dikembangkan berdasarkan kebutuhan guru, perubahan kebijakan pendidikan, dan masukan dari penggunaan nyata. Kontribusi berupa contoh format sekolah, koreksi alur, dan laporan masalah sangat disambut.

## Yang dibantu

Keluarga skill Hermes untuk membantu guru mana pun di Indonesia menyusun dokumen perangkat ajar Kurikulum Merdeka, **dari hulu ke hilir**, output Markdown + PDF rapi.

## Isi paket

| Skill | Dokumen |
|---|---|
| `pa-core` | Orkestrator: intake profil guru, peta alur, aturan universal, pipeline PDF |
| `pa-analisis-cp` | Analisis Capaian Pembelajaran (CP → TP per elemen) |
| `pa-atp` | Alur Tujuan Pembelajaran (taksonomi SOLO + dimensi profil lulusan) |
| `pa-prota` | Program Tahunan (alokasi JP per TP vs minggu efektif) |
| `pa-prosem` | Program Semestre (matriks minggu × bulan, landscape) |
| `pa-kktp` | Kriteria Ketercapaian TP (deskripsi interval) |
| `pa-rpp` | RPP / Modul Ajar / varian lokal sekolah |
| `pa-lkpd` | Lembar Kerja Peserta Didik (kasus, rubrik 100, kriteria A-D) |
| `pa-soal` | Asesmen lengkap: diagnostik, latihan soal, kisi-kisi + naskah SAS, mode TKA, remedial & pengayaan, analisis butir soal |
| `pa-rapor` | Deskripsi capaian kompetensi (kalimat rapor) massal dari KKTP + nilai |
| `pa-nilai` | Pengolahan nilai: NA tertimbang vs KKTP, statistik kelas, remedial/pengayaan, leger (script `olah_nilai.py`) |
| `pa-p5` | P5: modul projek, jurnal fasilitasi, refleksi, rapor projek 6 dimensi Profil Pelajar Pancasila |
| `pa-pkl` | PKL/Prakerin SMK: pedoman, jurnal siswa, instrumen penilaian DU/DI & pembimbing, konversi nilai |
| `pa-media` | Materi ajar per TP + slide pembelajaran + bank pertanyaan interaktif |
| `pa-riset` | Riset internet → bahan ajar terverifikasi multi-sumber (prioritas resmi), feed ke materi/LKPD/soal |
| `pa-admin` | Jurnal mengajar, daftar hadir, leger nilai (opsional per kebijakan sekolah) |
| `pa-wali-kelas` | Modul homeroom: data siswa, proker, denah duduk, buku kasus, analisis kenaikan |

## Instalasi

```bash
# salin folder ini ke direktori skills Hermes kamu
cp -r perangkat-ajar ~/.hermes/skills/

# dependensi pipeline PDF (sekali saja)
pip install markdown-it-py weasyprint
```

Verifikasi: jalankan `hermes` lalu cek `skills_list` memuat skill `pa-*`.

## Mulai cepat

1. Bilang ke agent-mu: *"Bantu aku bikin perangkat ajar"* → agent melakukan intake profil (nama, sekolah, mapel, JP/minggu, tahun pelajaran, minggu efektif dari kalender resmi) dan menyimpannya di `~/.hermes/perangkat-ajar/profil.yaml`.
2. Sebutkan dokumen mana yang mau dibuat — mulai dari mana saja (guru sering sudah punya sebagian): *"Bikin ATP"* / *"Susun prosem"* / *"Buatkan modul ajar TP1"*.
3. Semua dokumen tersimpan `.md` + `.pdf` di `~/.hermes/perangkat-ajar/output/<paket>/`; revisi cukup edit `.md` lalu minta regenerate.

## Filosofi desain

- **Hulu → hilir**: CP dianalisis → ATP → Prota → Prosem → KKTP → RPP/Modul Ajar → LKPD → Soal/Asesmen. Guru boleh masuk di titik mana pun.
- **Data ≠ proses**: semua data spesifik guru/sekolah hidup di `profil.yaml` + dokumen sumber guru; skill hanya berisi proses. Satu keluarga skill melayani semua guru.
- **Template dulu**: dokumen mengikuti format resmi sekolah masing-masing, bukan format bawaan skill.
- **Terprogram**: setiap dokumen diverifikasi otomatis (pymupdf + `verify_soal.py`) — bukan dicek dengan mata.

Diturunkan dari praktik nyata penyusunan perangkat ajar Basis Data SMKN 7 Baleendah (2026/2027).
