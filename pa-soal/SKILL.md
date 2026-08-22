---
name: pa-soal
description: "Use when a teacher asks for diagnostic tests, practice questions, blueprints, SAS instruments, TKA-style items, remedial or enrichment assessments, or post-test item analysis. Confirm assessment rules before drafting."
version: 1.4.0
author: Hermes Agent
license: MIT
---

# Soal & Asesmen (Latihan · Kisi-kisi · SAS · Remedial)

## Prasyarat
- Daftar TP + alokasi JP (Prota) + materi per pertemuan (RPP/LKPD).
- **Konfirmasi dulu ke guru** (aturan #2 & #7 `pa-core`): jumlah soal, komposisi tingkat kesulitan, batas tuntas. Jangan menyusun sebelum angka disetujui.

## Output minimum

Buat hanya instrumen yang diminta: diagnostik, formatif, sumatif, remedial, pengayaan, kisi-kisi, atau analisis butir. Jangan otomatis membuat semua jenis asesmen. Setiap instrumen harus terhubung ke TP, bukti belajar, dan KKTP.

## Komposisi default (selalu konfirmasi - angka harus menjumlah 100%)
- **Latihan per TP**: 10% mudah / 50% sedang / 40% susah, urut mudah → susah.
- **SAS**: 20% / 40% / 40%, dan **setiap TP wajib ≥1 soal mudah** (cek per TP, bukan hanya total).
- Jumlah soal lazim: ±10 per pertemuan; untuk SAS proporsional JP per TP (`soal_TP = round(N × JP_TP / JP_semester)` - pastikan Σ tepat N).
- Kalau guru menyebut komposisi yang tidak menjumlah 100% → tanyakan maksudnya dulu (kasus nyata: "30/50/10" ternyata typo).

## Struktur naskah latihan/SAS
1. Judul + `<p class="sub">` identitas.
2. **Petunjuk Pengerjaan** (jumlah soal, urutan mudah→susah, kunci di halaman terakhir).
3. Soal PG A-D. TP multi-pertemuan → heading per pertemuan, nomor soal **berlanjut** (P1: 1-10, P2: 11-20, ...).
4. `<div class="pagebreak"></div>` lalu `## KUNCI JAWABAN` - tabel No|Kunci (bisa kolom ganda) + **pembahasan singkat semua soal susah/L3**.
5. Kisi-kisi (untuk SAS): tabel No|TP|Materi Pokok|Indikator Soal|Level (L1/L2/L3)|No Soal + rekap distribusi per TP.

## Distribusi kunci A-D seimbang (wajib)
- Target tiap huruf ± sama banyak (30 soal → ±7-8/huruf). Hindari pola tebakable.
- Kalau timpang: **JANGAN ubah isi soal** - cukup acak ulang urutan opsi (teks opsi tetap, posisi jawaban benar digeser ke huruf yang kurang), regenerate, verifikasi ulang.
- Verifikasi SEBELUM generate PDF: parse tabel kunci di MD per-baris:
  ```python
  pairs = []
  for line in md.splitlines():
      if '|' in line and 'Kunci' not in line:
          cells = [c.strip() for c in line.strip('|').split('|')]
          pairs += list(zip(cells[0::2], cells[1::2]))
  ```
  ⚠️ Jangan pakai satu regex pipe lintas baris (`\s*` menelan newline) - pasangan bisa terlewat.

## Verifikasi otomatis sebelum PDF
```bash
python3 scripts/verify_soal.py naskah.md --kunci-in-naskah --jumlah 50 \
    [--kisi kisi.md --target 10,20,20]
```
Script mengecek: nomor 1..N lengkap, kunci lengkap + distribusi A-D, (bila ada kisi) komposisi level = target & tiap TP ≥1 L1 & pembahasan mencakup semua L3. Setelah PDF jadi: pymupdf cek "KUNCI JAWABAN" hanya di halaman terakhir, halaman 1 bebas kata "Kunci:", nomor soal dicek regex `^N\.` pada teks (di MD formatnya `**N.**`, di PDF asterisk hilang - jangan grep literal).

Jika script atau dependensi tidak tersedia, tandai verifikasi sebagai belum dijalankan. Jangan mengklaim soal sudah tervalidasi.

## Asesmen Diagnostik (awal semester / awal TP)
Input untuk kolom "Identifikasi Murid" di PPM (`pa-rpp`). Dua bagian:
1. **Non-kognitif**: minat, motivasi, gaya/persiapan belajar - 8-15 pertanyaan skala/pilihan singkat.
2. **Kognitif**: prasyarat mapel dari fase/kelas sebelumnya (mis. TP akhir semester lalu) - 5-10 soal PG/isian singkat, level L1-L2.
Output ringkas: hasil per murid → kategori (Perlu Penguatan / Cukup / Siap) → rekomendasi pengelompokan & penguatan awal. Jangan beri nilai rapor dari sini.

## Mode soal gaya TKA (literasi-numerasi)
Untuk persiapan Tes Kemampuan Akademik (agenda nasional mulai 2026): soal berbasis teks/stimulus nyata (bacaan pendek, tabel, grafik, kasus) yang menguji penalaran, bukan hafalan. Konvensi: 1 stimulus bisa dipakai 2-3 soal; tetap pakai struktur & verifikasi standar skill ini.

## Analisis Butir Soal (pasca STS/SAS)
Hitung kualitas butir dengan metode kelompok atas-bawah:
```bash
python3 scripts/analisis_butir.py jawaban.csv --kunci ABCDA... [--atas 27]
# jawaban.csv: baris = siswa, kolom = q1,q2,... isi huruf opsi / kosong utk salah
```
- **Tingkat kesukaran** `P = (BA+BB)/(N_atas+N_bawah)` → ≥0.71 mudah · 0.31-0.70 sedang · ≤0.30 sukar
- **Daya beda** `D = BA/N_atas − BB/N_bawah` → ≥0.70 sangat baik · 0.40-0.69 baik · 0.30-0.39 cukup · 0.20-0.29 jelek · <0.20 gagal (butir ditolak/revisi)
- **Efektivitas pengecoh**: tiap opsi salah harus dipilih ≥5% kelompok bawah; kalau tidak, pengecoh mati.
Laporkan rekap: jumlah butir baik/cukup/jelek/gagal + daftar butir untuk direvisi. Sajikan analisis di chat dulu sebelum jadi dokumen PDF.

## Program Remedial & Pengayaan
⚠️ **DISKUSI DULU** - dokumen administratif sensitif. Tanya 7 keputusan: (1) batas tuntas, (2) cakupan (per TP/semester), (3) sumber nilai, (4) jadwal, (5) kesempatan & nilai akhir, (6) bentuk remedial, (7) bentuk pengayaan. Sajikan usulan di chat; yang belum final tulis + tandai `> Catatan (sementara - dibedah bersama)`. Struktur teruji: Dasar & Tujuan → Kriteria Ketuntasan → Pelaksanaan Remedial → Butir Soal Remedial (3 per TP, mudah→sedang, kunci terpisah) → Program Pengayaan (tabel TP|Kegiatan|Output + tutor sebaya) → Jadwal & Tindak Lanjut → TTD.

## Pitfall
- **Uji script verifikasi dengan kasus NEGATIF sebelum dipercaya** (minimal: satu kunci dihapus + distribusi timpang ekstrem semua-A). Negative test menemukan bug nyata saat pembuatan: cek `max(dist.values()) - min(dist.values())` menganggap 30/0/0/0 "seimbang" karena huruf berjumlah 0 tidak masuk values() - hitung dari `[dist.get(h, 0) for h in "ABCD"]` (sudah difix di verify_soal.py).
- Bangun fixture test secara **programatik dari target komposisi** (loop dari Counter target), jangan tulis baris kisi/kunci manual - salah hitung 2x berturut-turut saat pembuatan.
- Halaman terakhir sepi karena TTD/kunci loncat → kompaksi (tabel kunci 4 kolom + class small, ringkas sel 1 baris, spacer TTD ≤8mm).
- f-string Python vs kurung kurawal materi (`{X, Y}`) → NameError saat render; pakai placeholder + `.replace()`.
- Soal menguji **baris program/konsep** untuk mapel praktik (bukan hafalan definisi) bila guru minta level HOTS.
- Cek keseimbangan kunci WAJIB menyertakan huruf bernilai 0 (hitung `dist.get(h,0) for h in "ABCD"` sebelum min/max). Bug nyata v1.0 `verify_soal.py`: kunci 30×A dianggap "seimbang" karena min/max hanya dihitung atas huruf yang muncul (30/30 → selisih 0).

## Verifikasi lintas asesmen

- Setiap butir memiliki TP atau indikator yang jelas.
- Bentuk asesmen sesuai kompetensi yang diukur; praktik tidak dipaksa menjadi pilihan ganda.
- Diagnostik tidak dimasukkan sebagai nilai rapor tanpa kebijakan eksplisit.
- Remedial merespons kesulitan yang ditemukan, bukan sekadar mengulang naskah lama.
