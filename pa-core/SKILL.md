---
name: pa-core
description: Orkestrator keluarga skill Perangkat Ajar untuk guru di Indonesia (Kurikulum Merdeka + Pembelajaran Mendalam) — intake profil guru/sekolah, peta alur dokumen hulu→hilir (Analisis CP → ATP → Prota → Prosem → KKTP → PPM/RPP/Modul Ajar → LKPD/Materi → Asesmen → Olah Nilai → Analisis Butir → Deskripsi Rapor; cabang P5 & PKL), aturan universal, routing ke sub-skill pa-*, dan pipeline PDF MD→HTML→PDF. Load skill ini saat guru baru minta perangkat ajar, saat profil belum ada, atau saat guru menyebut "perangkat ajar" secara umum.
---

# PA Core — Orkestrator Perangkat Ajar (Global)

Keluarga skill `pa-*` membantu guru mana pun di Indonesia menyusun dokumen perangkat ajar Kurikulum Merdeka dan pendekatan **Pembelajaran Mendalam** (kebijakan nasional Kemendikdasmen), output Markdown + PDF rapi.

## Peta alur dokumen (hulu → hilir)

```
CP (Capaian Pembelajaran — dokumen resmi Kemendikdasmen per mapel & fase)
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
 → Admin harian  (pa-admin)       : jurnal, daftar hadir, leger — SESUAI KEBIJAKAN SEKOLAH
 → Wali kelas    (pa-wali-kelas)  : modul role homeroom
```

**Guru boleh mulai dari mana saja.** Selalu tanya: "Dokumen mana yang sudah Bapak/Ibu punya?" lalu lanjutkan dari situ. JANGAN paksa urutan hulu→hilir.

## LANGKAH 0 — Cek kebijakan sekolah dulu (baru!)

Sebelum menawarkan dokumen apa pun, pastikan bentuk yang diminta sekolah:
- **Versi PP**: banyak sekolah sudah memakai versi SEDERHANA 3 komponen (tujuan pembelajaran, langkah/kegiatan, asesmen) sesuai arah penyederhanaan Kemendikdasmen; ada juga yang masih minta format lengkap. Minta contoh dokumen sekolah.
- **Jurnal harian & administrasi**: tidak lagi wajib secara nasional, tapi beberapa sekolah/dinas tetap memintanya — jangan buat manual kalau sekolah sudah pakai aplikasi (e-Rapor/sistem sekolah).
- **Format rapor**: kalau sekolah pakai e-Rapor, hasil `pa-rapor` tinggal ditempel ke kolom deskripsi.

Tanya sekali saat intake, simpan jawabannya di profil.

## LANGKAH 1 — Intake profil (sekali saja per guru)

Pastikan `~/.hermes/perangkat-ajar/profil.yaml` ada. Kalau belum, tanya santai (sisipkan di percakapan):

1. Nama & sekolah (NIP opsional)
2. Mapel + fase/kelas yang diampu (bisa lebih dari satu)
3. JP per minggu + berapa menit per JP (umumnya 40 atau 45)
4. Tahun pelajaran
5. Minggu efektif ganjil & genap — **WAJIB dari kalender pendidikan resmi sekolah**, minta file/linknya. Jangan menebak dari internet.
6. Dokumen mana yang sudah ada dan mana yang mau dibuat duluan
7. (opsional) Kebiasaan tambahan: istilah lokal dokumen (mis. RPM), kebijakan interval KKTP, komposisi soal

Simpan ke `~/.hermes/perangkat-ajar/profil.yaml` (salin `templates/profil.yaml`). Sesi berikutnya jangan tanya ulang.

## Routing

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

## Aturan universal (berlaku di semua sub-skill)

1. **Template resmi guru DULU sebelum menulis draf.** Hampir semua sekolah punya format resmi (sering Google Docs). Download dulu, ikuti persis.
   ```bash
   # Google Docs (publik): FILE_ID = bagian antara /d/ dan /edit
   curl -sL -A "Mozilla/5.0" "https://docs.google.com/document/d/${FILE_ID}/export?format=txt" -o template.txt
   # Google Drive: tambah &confirm=t agar file besar tidak berhenti di halaman virus-scan
   curl -sL "https://docs.google.com/uc?export=download&id=${FILE_ID}&confirm=t" -o file.pdf
   ```
   Output HTML / redirect ke `accounts.google.com` = file privat → minta guru ubah sharing atau kirim file langsung. Jangan bypass.
2. **Diskusikan dulu di chat, baru tulis dokumen.** Keputusan berdampak (komposisi soal, interval KKTP, alokasi JP, kebijakan remedial): sajikan usulan, tunggu persetujuan, baru generate. Yang belum final ditandai `> Catatan (sementara — dibedah bersama)`.
3. **Dokumen resmi = satu-satunya sumber angka.** Minggu efektif, libur, jadwal STS/SAS dari kalender resmi. Verifikasi label dengan MENJUMLAHKAN per bulan — label Ganjil/Genap sering tertukar.
4. **Konsistensi angka lintas dokumen.** JP per TP di Prota = pertemuan di Prosem = alokasi di RPP. `pertemuan = JP ÷ jp_per_minggu`, `total menit = JP × menit_per_JP`. Kalau guru bilang angka "salah", HITUNG dulu sebelum mengubah.
5. **MD = single source of truth.** Revisi = edit MD → regenerate. Versi lama pindah ke `Arsip/`, jangan dihapus.
6. **Verifikasi PDF terprogram** (pymupdf), bukan dengan mata: jumlah halaman, keyword, tidak ada halaman sepi (<300 chars body), TTD utuh 1 halaman, header center. Normalisasi teks dulu: `re.sub(r'\s+', ' ', text)`.
7. **Komposisi & kebijakan penilaian milik guru.** Konfirmasi angka dulu; angka komposisi harus menjumlah 100%.
8. **Jangan mengarang konten resmi.** CP, studi kasus, rubrik resmi: minta dokumennya. Belum ada? Placeholder + catat "resmi menyusul".
9. **Data pribadi murid sensitif** (nilai, absen, kasus, deskripsi rapor): simpan lokal di folder output, jangan dikirim ke grup/chat lain tanpa diminta guru pemiliknya.

## Prinsip pengembangan keluarga skill ini
- Keluarga `pa-*` HANYA ditambah/direvisi setelah **breakdown kebutuhan nyata**: riset lapangan & kebijakan dulu (baseline: `references/konteks-kebijakan-2026.md`), sajikan breakdown di chat, tunggu persetujuan pemilik, baru bangun. Kasus nyata: v1.0 dibangun langsung dari pengalaman satu mapel tanpa riset kebutuhan → revisi besar jadi v1.1 (13 skill) setelah riset.
- **Pemilik sering menyempitkan scope setelah lihat usulan** — hormati penyempitan itu dan catat batch yang ditunda/ditolak secara eksplisit; jangan dibangun tanpa persetujuan ulang. Kasus nyata (Agu-2026): dari usulan 3 tier, pemilik menunda otomasi (cron/vision/webhook) DAN administrasi dinas (surat/PAK/LPJ), memilih keluarga dokumen pembelajaran "RPP dan kawan-kawan" → jadi v1.2 (16 skill).
- Referensi konteks kebijakan nasional (framework Pembelajaran Mendalam, penyederhanaan administrasi, TKA, rumus analisis butir): `references/konteks-kebijakan-2026.md`.

## Pipeline PDF (MD → HTML → PDF)

Script: `scripts/gen_pdf_from_md.py`. Dependensi: `pip install markdown-it-py weasyprint`.

```bash
python3 gen_pdf_from_md.py input.md output.pdf "HEADER — Nama Sekolah | Topik"          # portrait
python3 gen_pdf_from_md.py input.md output.pdf "HEADER" landscape                       # tabel lebar
```

Aturan MD (data saja, tanpa styling):
- Baris pertama BUKAN teks header — header dari CSS `@top-center`; sub-judul pakai `<p class="sub">`.
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
