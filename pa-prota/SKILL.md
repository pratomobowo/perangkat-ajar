---
name: pa-prota
description: "Use when a teacher asks to map learning objectives across an academic year with effective weeks and lesson-hour allocations. Require the existing ATP and official school calendar before calculating."
version: 1.5.0
author: Hermes Agent
license: MIT
---

# Prota (Program Tahunan)

## Prasyarat
- ATP (`pa-atp`) + **kalender pendidikan resmi sekolah** (SK/edaran - biasanya lampiran SK pembagian tugas). Minggu efektif TIDAK BOLEH ditebak dari internet.
- Dari kalender ambil: minggu efektif ganjil & genap, hari libur besar, jadwal asesmen (STS/SAS/pengolahan nilai).

## Output minimum

Prota hanya memetakan TP atau unit belajar, semester, dan alokasi waktu. Jangan membuat kalender sekolah atau menebak minggu efektif. Jika sekolah tidak meminta Prota, gunakan hasil pemetaan internal tanpa memaksa membuat PDF.

## Mengolah kalender pendidikan (pitfall terbukti)
1. Ekstrak teks PDF kalender (halaman lampiran, sering bukan hal. 1): `import fitz; ''.join(p.get_text() for p in fitz.open(f))`.
2. **Verifikasi label dengan MENJUMLAHKAN per bulan** - baris rekap di dokumen sering salah ketik/label Ganjil-Genap tertukar. Contoh nyata: label tertulis tertukar; jumlah per bulan-lah yang benar.
3. Semester: Jul-Des = Ganjil, Jan-Jun = Genap.
4. Simpan ringkasan angka (ME/HE/libur per bulan) supaya Prosem tinggal pakai.

## Langkah menyusun
1. Template resmi guru dulu.
2. Hitung JP total per semester: `JP_total = minggu_efektif × jp_per_minggu`.
3. Alokasikan JP per TP **bersama guru** (usulan proporsional bobot materi → guru memangkas/menambah). Aturan:
   - Total per semester HARUS tepat sama dengan hitungan di atas.
   - Guru memangkas JP satu TP → **jangan asumsikan sendiri sisanya ke mana** - tanya guru; total harus tetap.
   - Revisi alokasi satu TP → sinkronkan pertemuan di Prosem (audit silang, aturan #4 `pa-core`).
4. Format tabel:

   | No | Bab/ATP | Tujuan Pembelajaran | Materi | Alokasi Waktu | Semester |

   + baris terakhir **"Jumlah Total Alokasi Waktu"** (jumlahkan & cocokkan dengan langkah 2).
5. Header: Satuan Pendidikan, Mapel, Kelas/Fase, Tahun Pelajaran.
6. Generate PDF, verifikasi jumlah & keyword.

## Verifikasi (WAJIB)
- `Σ alokasi per semester == ME_semester × jp_per_minggu` - hitung terprogram, bukan manual.
- Setiap TP dari ATP muncul sekali, urutannya sama.
- Alokasi kelipatan JP per minggu (tiap pertemuan utuh).
- Tidak ada minggu libur atau agenda sekolah yang dihitung sebagai minggu pembelajaran tanpa konfirmasi.

## Pitfall
- Minggu efektif genap biasanya lebih sedikit dari ganjil (libur akhir tahun ajaran) - kalau angkanya kebalikan, kemungkinan label tertukar (lihat atas).
- Jangan lupa baris total; banyak format resmi mensyaratkannya.
- Revisi alokasi JP guru sering membuat total meleset dari target - hitung ulang terprogram setiap revisi; selisihnya sesuaikan ke TP yang materinya paling ringan/berat sesuai arahan guru, lalu laporkan transparan agar guru bisa veto.

## Konvensi hasil praktik (SMK, disetujui guru 2026-10-06)

Prota Basis Data Fase F ([Nama Guru], NIP [NIP]):
- Satu dokumen Fase F (Kelas XI–XII), 3 semester efektif: XI Ganjil 76 JP (19 ME × 4), XI Genap 68 JP (17 ME × 4), XII Ganjil 76 JP (19 ME × 4); XII Genap = PKL (tanpa alokasi, cukup catatan).
- Alokasi JP per TP disepakati bersama guru (usulan proporsional → guru merevisi manual). Alokasi akhir: No 1,2,4,9,10 = 2 JP; No 3,11,12,13,17,18,25,26 = 2–4 JP; No 7 (normalisasi) & No 16 (SELECT) = 12 JP; No 22 (subquery), No 38,42 (bangun API) = 8–12 JP; sisanya 4–8 JP sesuai bobot.
- Tabel: No | Bab/ATP (kode + nama elemen) | Tujuan Pembelajaran (`n.m` + teks TP) | Materi | Alokasi Waktu | Semester; tiap semester diakhiri baris **"Jumlah Total Alokasi Waktu"** yang dicocokkan terprogram dengan ME × JP/minggu.
- Header: Satuan Pendidikan, Mapel, Kelas/Fase, Tahun Pelajaran (via 2 baris `<p class="sub">`).
- Status: `DRAF` sampai disetujui guru, lalu `Disetujui — disetujui guru pada <tanggal>; dapat digunakan sebagai acuan Prosem`, regenerate PDF.
- Blok tanda tangan rata kanan + NIP (format di `pa-core`); ruang TTD basah ±55px.
