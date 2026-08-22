# Perangkat Ajar

### Perangkat ajar yang lebih mudah disiapkan

Guru menghabiskan banyak waktu untuk menyusun dokumen, menghitung alokasi, memeriksa nilai, dan menyesuaikan format sekolah. Proyek ini membantu meringankan pekerjaan tersebut.

`perangkat-ajar` menyediakan alat bantu untuk menyusun perangkat ajar secara lebih teratur, mulai dari Capaian Pembelajaran, tujuan pembelajaran, dan rencana pembelajaran hingga asesmen, pengolahan nilai, dan deskripsi rapor.

Tujuannya sederhana: **mengurangi beban administratif agar guru dapat lebih fokus pada proses belajar murid.**

AI membantu membuat draf, merapikan alur, menghitung, dan memeriksa konsistensi. Guru tetap menentukan tujuan, strategi, penilaian, dan keputusan yang sesuai dengan murid serta kebijakan sekolah.

## Mengapa proyek ini dibuat?

Menyusun perangkat ajar sering berarti menghubungkan banyak dokumen, angka, dan keputusan:

- Capaian Pembelajaran perlu diterjemahkan menjadi tujuan dan alur belajar.
- Alokasi waktu harus selaras dengan minggu efektif dan kalender sekolah.
- Rencana pembelajaran perlu terhubung dengan LKPD, materi, dan asesmen.
- Nilai harus diolah secara konsisten dan dapat dijelaskan.
- Format akhir harus mengikuti kebutuhan satuan pendidikan.

Proyek ini membantu menghubungkan pekerjaan tersebut dalam satu alur yang fleksibel. Setiap sekolah tetap dapat menggunakan format dan kebijakannya sendiri.

## Prinsip utama

- **Guru memegang kendali.** AI menyusun dan memeriksa. Guru mengambil keputusan.
- **Konteks sekolah menjadi rujukan.** Format resmi, kalender pendidikan, dan kebijakan sekolah didahulukan daripada template generik.
- **Mulai dari kebutuhan nyata.** Guru dapat membuat ATP, modul ajar, soal, atau dokumen lain tanpa harus memulai dari awal.
- **Konsistensi dapat diverifikasi.** Alokasi JP, komposisi soal, nomor jawaban, dan hasil PDF dibantu pemeriksa otomatis.
- **Data murid diperlakukan sebagai data sensitif.** Nilai, kehadiran, dan catatan kasus tetap berada dalam kendali guru atau sekolah.
- **Markdown menjadi sumber utama.** Revisi dilakukan pada dokumen sumber, lalu output dapat dibuat ulang.

## Cakupan skill

| Skill | Kegunaan |
| --- | --- |
| `pa-core` | Intake profil, orkestrasi alur, aturan universal, dan pipeline PDF |
| `pa-analisis-cp` | Mengurai CP menjadi tujuan pembelajaran per elemen |
| `pa-atp` | Menyusun Alur Tujuan Pembelajaran |
| `pa-prota` | Memetakan tujuan dan alokasi JP dalam Program Tahunan |
| `pa-prosem` | Menyusun Program Semester berdasarkan minggu efektif |
| `pa-kktp` | Menyusun Kriteria Ketercapaian Tujuan Pembelajaran |
| `pa-rpp` | Membuat RPP, Modul Ajar, atau format lokal sekolah |
| `pa-lkpd` | Menyusun LKPD berbasis aktivitas dan rubrik |
| `pa-media` | Membuat materi ajar, slide, dan pertanyaan interaktif |
| `pa-soal` | Membuat asesmen, kisi-kisi, SAS, remedial, pengayaan, dan analisis butir |
| `pa-nilai` | Mengolah nilai, statistik kelas, ketuntasan, dan leger |
| `pa-rapor` | Menghasilkan deskripsi capaian kompetensi siswa |
| `pa-p5` | Menyusun modul projek, jurnal fasilitasi, dan rapor projek |
| `pa-pkl` | Menyusun perangkat PKL/Prakerin SMK dan instrumen penilaian |
| `pa-riset` | Mengkurasi sumber internet menjadi bahan ajar terverifikasi |
| `pa-admin` | Membantu jurnal mengajar, daftar hadir, dan administrasi pilihan |
| `pa-wali-kelas` | Membantu proker, denah duduk, buku kasus, dan analisis kelas |

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
2. Sebutkan dokumen mana yang mau dibuat - mulai dari mana saja (guru sering sudah punya sebagian): *"Bikin ATP"* / *"Susun prosem"* / *"Buatkan modul ajar TP1"*.
3. Semua dokumen tersimpan `.md` + `.pdf` di `~/.hermes/perangkat-ajar/output/<paket>/`; revisi cukup edit `.md` lalu minta regenerate.

## Filosofi desain

- **Hulu → hilir**: CP dianalisis → ATP → Prota → Prosem → KKTP → RPP/Modul Ajar → LKPD → Soal/Asesmen. Guru boleh masuk di titik mana pun.
- **Data ≠ proses**: semua data spesifik guru/sekolah hidup di `profil.yaml` + dokumen sumber guru; skill hanya berisi proses. Satu keluarga skill melayani semua guru.
- **Template dulu**: dokumen mengikuti format resmi sekolah masing-masing, bukan format bawaan skill.
- **Terprogram**: setiap dokumen diverifikasi otomatis (pymupdf + `verify_soal.py`) - bukan dicek dengan mata.

Dikembangkan dari kebutuhan nyata guru dan terus disempurnakan melalui penggunaan serta masukan komunitas.
