---
name: pa-prota
description: Membuat dokumen Prota (Program Tahunan) — memetakan ATP ke minggu efektif satu tahun ajaran beserta alokasi JP per TP per semester. Input dari pa-atp + kalender pendidikan resmi sekolah; output jadi input Prosem.
---

# Prota (Program Tahunan)

## Prasyarat
- ATP (`pa-atp`) + **kalender pendidikan resmi sekolah** (SK/edaran — biasanya lampiran SK pembagian tugas). Minggu efektif TIDAK BOLEH ditebak dari internet.
- Dari kalender ambil: minggu efektif ganjil & genap, hari libur besar, jadwal asesmen (STS/SAS/pengolahan nilai).

## Mengolah kalender pendidikan (pitfall terbukti)
1. Ekstrak teks PDF kalender (halaman lampiran, sering bukan hal. 1): `import fitz; ''.join(p.get_text() for p in fitz.open(f))`.
2. **Verifikasi label dengan MENJUMLAHKAN per bulan** — baris rekap di dokumen sering salah ketik/label Ganjil-Genap tertukar. Contoh nyata: label tertulis tertukar; jumlah per bulan-lah yang benar.
3. Semester: Jul–Des = Ganjil, Jan–Jun = Genap.
4. Simpan ringkasan angka (ME/HE/libur per bulan) supaya Prosem tinggal pakai.

## Langkah menyusun
1. Template resmi guru dulu.
2. Hitung JP total per semester: `JP_total = minggu_efektif × jp_per_minggu`.
3. Alokasikan JP per TP **bersama guru** (usulan proporsional bobot materi → guru memangkas/menambah). Aturan:
   - Total per semester HARUS tepat sama dengan hitungan di atas.
   - Guru memangkas JP satu TP → **jangan asumsikan sendiri sisanya ke mana** — tanya guru; total harus tetap.
   - Revisi alokasi satu TP → sinkronkan pertemuan di Prosem (audit silang, aturan #4 `pa-core`).
4. Format tabel:

   | No | Bab/ATP | Tujuan Pembelajaran | Materi | Alokasi Waktu | Semester |

   + baris terakhir **"Jumlah Total Alokasi Waktu"** (jumlahkan & cocokkan dengan langkah 2).
5. Header: Satuan Pendidikan, Mapel, Kelas/Fase, Tahun Pelajaran.
6. Generate PDF, verifikasi jumlah & keyword.

## Verifikasi (WAJIB)
- `Σ alokasi per semester == ME_semester × jp_per_minggu` — hitung terprogram, bukan manual.
- Setiap TP dari ATP muncul sekali, urutannya sama.
- Alokasi kelipatan JP per minggu (tiap pertemuan utuh).

## Pitfall
- Minggu efektif genap biasanya lebih sedikit dari ganjil (libur akhir tahun ajaran) — kalau angkanya kebalikan, kemungkinan label tertukar (lihat atas).
- Jangan lupa baris total; banyak format resmi mensyaratkannya.
