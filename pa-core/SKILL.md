---
name: pa-core
description: "Use when a teacher asks for perangkat ajar secara umum, belum memiliki profil atau format sekolah, atau perlu menentukan dokumen yang benar-benar dibutuhkan. Gunakan untuk intake, routing, konsistensi lintas dokumen, dan alur kerja sebelum drafting."
version: 1.3.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [guru, perangkat-ajar, kurikulum, pembelajaran]
    related_skills: [pa-rpp, pa-atp, pa-soal, pa-nilai]
---

# PA Core: Alur Kerja Perangkat Ajar

Skill `pa-*` membantu guru menyusun perangkat ajar sesuai kebutuhan murid, sekolah, dan dokumen rujukan yang tersedia. Pembelajaran Mendalam adalah pendekatan yang dapat digunakan dalam perencanaan pembelajaran, bukan alasan untuk memaksakan satu format nasional.

## Aturan utama: buat yang diperlukan saja

Peta di bawah menunjukkan hubungan dokumen, bukan urutan wajib. Sebelum membuat apa pun:

1. Tanyakan dokumen apa yang sudah dimiliki guru dan apa yang diminta sekolah.
2. Cari tahu apakah guru ingin membuat dokumen baru, mengadaptasi, atau merevisi.
3. Minta format resmi sekolah jika ada.
4. Pilih output minimum yang cukup untuk kebutuhan tersebut.
5. Jangan membuat paket lengkap secara otomatis.

Jika sumber, angka, atau kebijakan belum tersedia, berhenti pada pertanyaan yang diperlukan. Jangan menebak dan jangan mengarang dokumen resmi.

## Peta alur dokumen (hulu → hilir)

```
CP (Capaian Pembelajaran - dokumen resmi Kemendikdasmen per mapel & fase)
 → Analisis CP   (pa-analisis-cp) : CP diurai menjadi TP per elemen
 → ATP           (pa-atp)         : TP diurutkan menjadi alur setahun
 → Prota         (pa-prota)       : ATP dipetakan ke minggu efektif setahun
 → Prosem        (pa-prosem)      : dipotong per semester, matriks minggu × bulan
 → KKTP          (pa-kktp)        : kriteria ketercapaian TP (deskripsi interval)
 → PPM/RPP/Modul (pa-rpp)         : rencana pembelajaran per TP
 → LKPD          (pa-lkpd)        : lembar kerja peserta didik
 → Materi+Slide  (pa-media)       : bahan ajar & media belajar
 → Asesmen       (pa-soal)        : diagnostik, latihan, STS/SAS, remedial, analisis butir
 → Olah Nilai    (pa-nilai)       : NA tertimbang vs KKTP → tuntas/belum, statistik, remedial/pengayaan
 → Deskripsi Rapor (pa-rapor)     : kalimat capaian kompetensi per siswa dari KKTP+nilai
Cabang opsional:
 → Riset Materi  (pa-riset)       : riset internet terverifikasi → bahan ajar per TP
 → P5            (pa-p5)          : modul projek, jurnal fasilitasi, rapor projek (6 dimensi PPP)
 → PKL/SMK       (pa-pkl)         : pedoman, jurnal siswa, instrumen penilaian DU/DI, konversi nilai
 → Admin harian  (pa-admin)       : jurnal, daftar hadir, leger - SESUAI KEBIJAKAN SEKOLAH
 → Wali kelas    (pa-wali-kelas)  : modul role homeroom
```

**Guru boleh mulai dari mana saja.** Selalu tanya: "Dokumen mana yang sudah Bapak/Ibu punya dan dokumen apa yang diminta sekolah?" lalu lanjutkan dari situ. Jangan memaksa urutan hulu ke hilir.

## LANGKAH 0 - Cek kebijakan sekolah dulu (baru!)

Sebelum menawarkan dokumen apa pun, pastikan bentuk yang diminta sekolah:
- **Rencana pembelajaran**: sekolah dapat meminta format ringkas, PPM, Modul Ajar, RPP, atau istilah lokal. Minta contoh dokumen sekolah.
- **Jurnal harian dan administrasi**: kebutuhannya bergantung pada kebijakan sekolah, dinas, dan aplikasi yang digunakan. Jangan membuatnya sebelum diminta.
- **Format rapor**: kalau sekolah pakai e-Rapor, hasil `pa-rapor` tinggal ditempel ke kolom deskripsi.

Tanya sekali saat intake, simpan jawabannya di profil.

## LANGKAH 1: Intake profil (sekali saja per guru)

Pastikan `~/.hermes/perangkat-ajar/profil.yaml` ada. Kalau belum, tanya santai (sisipkan di percakapan):

1. Nama & sekolah (NIP opsional)
2. Mapel + fase/kelas yang diampu (bisa lebih dari satu)
3. JP per minggu + berapa menit per JP (umumnya 40 atau 45)
4. Tahun pelajaran
5. Minggu efektif ganjil & genap - **WAJIB dari kalender pendidikan resmi sekolah**, minta file/linknya. Jangan menebak dari internet.
6. Dokumen mana yang sudah ada dan mana yang mau dibuat duluan
7. (opsional) Kebiasaan tambahan: istilah lokal dokumen (mis. RPM), kebijakan interval KKTP, komposisi soal

Simpan ke `~/.hermes/perangkat-ajar/profil.yaml` (salin `templates/profil.yaml`). Sesi berikutnya jangan tanya ulang.

## LANGKAH 2: Vault Markdown sebagai sumber kerja

Jika guru menyimpan administrasi di vault Markdown, gunakan skill `obsidian` untuk membaca, mencari, membuat, dan mengedit note. Jangan membuat vault baru tanpa lokasi yang diketahui dan persetujuan guru.

1. Cek `OBSIDIAN_VAULT_PATH` dari `/var/hermes-home/.env`.
2. Jika kosong, tanyakan lokasi vault. Jangan membuat folder fallback otomatis.
3. Tanyakan apakah guru ingin membuat struktur `Perangkat-Ajar`.
4. Jika disetujui, buat folder yang belum ada dan pertahankan note lain.

Struktur standar:

```text
Perangkat-Ajar/
├── 00-Index/
├── 01-Sumber-Resmi/{CP,Kalender-Pendidikan,Panduan-Kebijakan,Template-Sekolah}/
├── 02-Analisis/{Analisis-CP,Tujuan-Pembelajaran,KKTP}/
├── 03-Perencanaan/{ATP,Prota,Prosem,RPP-Modul-PPM}/
├── 04-Pembelajaran/{Materi,Media,LKPD,Jobsheet}/
├── 05-Asesmen/{Diagnostik,Formatif,Sumatif,Remedial,Pengayaan}/
├── 06-Nilai-Rapor/{Data-Nilai,Olah-Nilai,Deskripsi-Rapor}/
├── 07-Projek-PKL/{P5-Kokurikuler,PKL}/
├── 08-Wali-Kelas/
└── 99-Arsip/
```

Setiap note memiliki frontmatter minimum:

```yaml
---
jenis: analisis-cp
mapel: Informatika
fase: F
kelas: XI
semester: ganjil
tahun_pelajaran: 2026/2027
status: draft
versi: 1
sumber: []
tp: []
tags: [perangkat-ajar]
---
```

`status` harus `draft`, `perlu-review`, `disetujui`, `digunakan`, atau `diarsipkan`. Note draft tidak boleh menjadi sumber final tanpa persetujuan guru. Gunakan wikilink seperti `[[Analisis CP Informatika Fase F]]`. Revisi membuat versi baru atau memindahkan versi lama ke `99-Arsip/`, bukan menghapusnya. Markdown adalah sumber utama; PDF, DOCX, XLSX, dan PPTX adalah output turunan.

Sebelum membuat note, cari note dengan jenis, mapel, fase, kelas, dan tahun yang sama agar tidak duplikat. Sebelum membuat dokumen turunan, baca sumber berstatus `disetujui` atau `digunakan`. Setelah menulis, baca ulang path, frontmatter, status, wikilink, dan isi note. Data nilai, presensi, kasus, kontak, dan deskripsi rapor tetap lokal serta dimasking pada preview chat.

## Routing

Muat hanya skill yang diperlukan. Batas fungsi penting:

- `pa-riset` hanya mencari dan memverifikasi sumber.
- `pa-media` mengubah materi yang sudah disetujui menjadi bahan ajar atau slide.
- `pa-lkpd` membuat aktivitas dan lembar kerja.
- `pa-rpp` menyusun rencana pembelajaran, bukan melakukan riset umum.
- `pa-soal` menyusun instrumen asesmen dan analisis butir.

| Guru menyebut | Load skill |
|---|---|
| analisis CP, penguraian CP | `pa-analisis-cp` |
| ATP, alur tujuan pembelajaran | `pa-atp` |
| prota, program tahunan | `pa-prota` |
| prosem, program semestre | `pa-prosem` |
| KKTP, kriteria ketuntasan | `pa-kktp` |
| RPP, modul ajar, PPM, RPM, RPPM, pembelajaran mendalam | `pa-rpp` |
| LKPD, lembar kerja siswa | `pa-lkpd` |
| materi, bahan ajar, slide, PPT, media belajar | `pa-media` |
| riset, cariin materi internet, referensi bahan ajar, kurasi sumber | `pa-riset` |
| soal, kisi-kisi, SAS, diagnostik, remedial, pengayaan, analisis butir | `pa-soal` |
| olah nilai, rekap nilai, nilai akhir, ketuntasan, leger otomatis | `pa-nilai` |
| P5, projek pancasila, projek profil pelajar, modul projek, rapor P5 | `pa-p5` |
| PKL, prakerin, magang SMK, jurnal PKL, penilaian DU/DI | `pa-pkl` |
| rapor, deskripsi capaian, kalimat rapor | `pa-rapor` |
| jurnal mengajar, daftar hadir, leger | `pa-admin` |
| wali kelas, homeroom, denah duduk, buku kasus | `pa-wali-kelas` |

## Aturan universal

### Fast path: konflik angka

Respons konflik angka wajib berhenti dengan format ini, tanpa bagian workflow, daftar file, atau rencana dokumen:

```text
Angka yang diterima: [angka dan satuan].
Konflik: [hubungan angka yang belum konsisten].
Pilihan: A) [interpretasi pertama] atau B) [interpretasi kedua]?
Saya menunggu pilihan sebelum menyesuaikan atau membuat dokumen.
```

Jika permintaan menyebut angka yang bertentangan, tangani konflik sebelum intake atau drafting lain:

1. Tulis angka yang diterima dan satuan masing-masing.
2. Hitung hubungan yang dapat dihitung.
3. Tunjukkan konflik dalam maksimal tiga kalimat.
4. Tolak instruksi "langsung sesuaikan" jika lebih dari satu interpretasi masih mungkin.
5. Ajukan satu pertanyaan pilihan dan berhenti menunggu jawaban.
6. Jangan memakai tool, membaca seluruh repository, membuat file, atau generate dokumen sebelum guru memilih.

Contoh: `4 JP per minggu`, `3 pertemuan`, dan `180 menit total` belum menentukan satu interpretasi. Jika 1 JP = 45 menit, 180 menit = 4 JP, tetapi pembagian ke 3 pertemuan belum ditentukan. Tanyakan: `Apakah 180 menit dibagi menjadi 3 pertemuan @ 60 menit, atau 3 pertemuan masing-masing 4 JP?`

1. **Template resmi guru DULU sebelum menulis draf.** Hampir semua sekolah punya format resmi (sering Google Docs). Download dulu, ikuti persis.
   ```bash
   # Google Docs (publik): FILE_ID = bagian antara /d/ dan /edit
   curl -sL -A "Mozilla/5.0" "https://docs.google.com/document/d/${FILE_ID}/export?format=txt" -o template.txt
   # Google Drive: tambah &confirm=t agar file besar tidak berhenti di halaman virus-scan
   curl -sL "https://docs.google.com/uc?export=download&id=${FILE_ID}&confirm=t" -o file.pdf
   ```
   Output HTML / redirect ke `accounts.google.com` = file privat → minta guru ubah sharing atau kirim file langsung. Jangan bypass.
2. **Diskusikan dulu di chat, baru tulis dokumen.** Keputusan berdampak seperti komposisi soal, interval KKTP, alokasi JP, dan remedial harus disetujui guru sebelum generate. Yang belum final ditandai `> Catatan (sementara: perlu dikonfirmasi)`.
3. **Dokumen resmi = satu-satunya sumber angka.** Minggu efektif, libur, jadwal STS/SAS dari kalender resmi. Verifikasi label dengan MENJUMLAHKAN per bulan - label Ganjil/Genap sering tertukar.
4. **Konsistensi angka lintas dokumen.** JP per TP di Prota = pertemuan di Prosem = alokasi di RPP. `pertemuan = JP ÷ jp_per_minggu`, `total menit = JP × menit_per_JP`. Kalau guru bilang angka "salah", HITUNG dulu sebelum mengubah.
5. **MD = single source of truth.** Revisi = edit MD → regenerate. Versi lama pindah ke `Arsip/`, jangan dihapus.
6. **Verifikasi PDF terprogram** (pymupdf), bukan dengan mata: jumlah halaman, keyword, tidak ada halaman sepi (<300 chars body), TTD utuh 1 halaman, header center. Normalisasi teks dulu: `re.sub(r'\s+', ' ', text)`.
7. **Komposisi & kebijakan penilaian milik guru.** Konfirmasi angka dulu; angka komposisi harus menjumlah 100%.
8. **Jangan mengarang konten resmi.** CP, studi kasus, rubrik resmi: minta dokumennya. Belum ada? Placeholder + catat "resmi menyusul".
9. **Data pribadi murid sensitif** (nilai, absen, kasus, deskripsi rapor): simpan lokal di folder output. Masking nama dan NIS pada preview chat. Jangan mengirim CSV atau PDF lengkap ke channel umum tanpa persetujuan guru.

10. **Dependensi dan file pendukung harus dicek.** Sebelum menjalankan script, pastikan file ada dan dependensinya tersedia. Jika tidak tersedia, laporkan verifikasi sebagai belum dijalankan. Jangan mengarang pengganti.

## Prinsip pengembangan keluarga skill ini
- Keluarga `pa-*` HANYA ditambah/direvisi setelah **breakdown kebutuhan nyata**: riset lapangan & kebijakan dulu (baseline: `references/konteks-kebijakan-2026.md`), sajikan breakdown di chat, tunggu persetujuan pemilik, baru bangun. Kasus nyata: v1.0 dibangun langsung dari pengalaman satu mapel tanpa riset kebutuhan → revisi besar jadi v1.1 (13 skill) setelah riset.
- **Pemilik sering menyempitkan scope setelah lihat usulan** - hormati penyempitan itu dan catat batch yang ditunda/ditolak secara eksplisit; jangan dibangun tanpa persetujuan ulang. Kasus nyata (Agu-2026): dari usulan 3 tier, pemilik menunda otomasi (cron/vision/webhook) DAN administrasi dinas (surat/PAK/LPJ), memilih keluarga dokumen pembelajaran "RPP dan kawan-kawan" → jadi v1.2 (16 skill).
- Referensi kebijakan: `references/konteks-kebijakan-2026.md`.
- Baseline hulu ke hilir, input/output, gate verifikasi, dan gap: `references/baseline-hulu-hilir.md`.

## Pipeline PDF (MD → HTML → PDF)

Script: `scripts/gen_pdf_from_md.py`. Dependensi: `pip install markdown-it-py weasyprint`.

```bash
python3 gen_pdf_from_md.py input.md output.pdf "HEADER - Nama Sekolah | Topik"          # portrait
python3 gen_pdf_from_md.py input.md output.pdf "HEADER" landscape                       # tabel lebar
```

Aturan MD (data saja, tanpa styling):
- Baris pertama BUKAN teks header - header dari CSS `@top-center`; sub-judul pakai `<p class="sub">`.
- Numbering vertikal, tidak inline (di sel tabel pakai `<br>`).
- Tabel biasa = markdown table; tabel sangat lebar WAJIB HTML `<table>` + argumen `landscape`.
- Halaman terpisah (kunci jawaban): `<div class="pagebreak"></div>`.
- TTD: `<div class="kotak-ttd"><table>...` (spacer ≤10mm).

## Konvensi file

```
~/.hermes/perangkat-ajar/
├── profil.yaml                    ← profil guru (intake)
└── output/<paket-id>/             ← satu folder per mapel-kelas
    ├── Analisis-CP-*.md/.pdf  ATP-*  Prota-*  Prosem-*  KKTP-*
    ├── PPM-<Mapel>-TP<n>-*.md/.pdf   (atau RPP-/ModulAjar- sesuai istilah sekolah)
    ├── LKPD-*  Materi-*  Slide-*
    ├── Diagnostik-*  Latihan-Soal-*  Kisi-Kisi-SAS-*  Naskah-SAS-*  Remedial-*
    ├── Analisis-Butir-SAS-*
    ├── Deskripsi-Rapor-<Kelas>-<Semester>.*
    └── Arsip/                     ← versi lama dipindah ke sini
```

## Pitfall umum

- Google Docs privat → minta akses, jangan bypass.
- Minggu efektif dari internet → salah; hanya dari dokumen resmi sekolah.
- `MarkdownIt()` default tidak render tabel → script ini sudah `enable("table")`; jangan preset "gfm-like".
- PDF gagal diam-diam (cuma judul) → selalu verifikasi chars/halaman + keyword.
- Kirim file via Telegram timeout padahal file benar → retry kirim MEDIA terpisah, jangan regenerate.
