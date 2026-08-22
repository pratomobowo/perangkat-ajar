# Expanded QA Report

Tanggal: 2026-08-22
Data: sintetis, bukan data sekolah atau murid nyata.

## Ringkasan

| Area | Status | Catatan |
| --- | --- | --- |
| PDF dan artefak file | Not verified | Generator PDF berhenti karena `weasyprint` belum tersedia |
| Excel/CSV | Partial | CSV nilai valid diuji; sel kosong awalnya dihitung nol, sudah diperbaiki dan kini ditolak |
| P5/kokurikuler | Intake pass | Input wajib diminta, tidak membuat dokumen |
| PKL | Intake pass | Pedoman, peserta, industri, pembimbing, bobot, dan format diminta |
| Wali kelas | Intake pass | Sumber daftar siswa, kebijakan akses, periode, dan jenis dokumen diminta |
| Riset -> materi -> LKPD -> soal | Gate pass | Rantai berhenti sebelum riset karena input dan kebijakan belum lengkap |
| Template sekolah | Not verified | Fixture template sintetis tersedia; template resmi nyata belum diberikan |

## 1. PDF dan artefak file

Command generator PDF dijalankan terhadap template sintetis:

```bash
python3 pa-core/scripts/gen_pdf_from_md.py tests/fixtures/template-sekolah-sintetis.md /tmp/template-uji.pdf 'Template Uji'
```

Hasil: **NOT VERIFIED**.

```text
Dependensi kurang: No module named 'weasyprint'
```

Tidak ada klaim PDF lulus. PDF perlu diuji ulang setelah dependensi disiapkan atau dengan fallback renderer yang disepakati.

## 2. CSV dan nilai

CSV fixture:

```text
tests/fixtures/nilai-sintetis.csv
```

`--selftest` script nilai lulus.

Temuan awal: baris kosong pada Siswa Empat dihitung sebagai nol walaupun skill menyatakan sel kosong bukan nol. Script diperbaiki.

Setelah perbaikan, fixture dengan nilai kosong ditolak:

```text
ERROR: missing scores for Siswa Empat: tp1
```

Ini adalah perilaku yang benar. Nilai kosong harus dikonfirmasi sebelum kalkulasi.

## 3. P5/kokurikuler

Intake pass. Hermes meminta istilah sekolah, template, jenis kegiatan, tema, jumlah murid, dimensi, elemen, alokasi resmi, tim, produk, asesmen, dan bukti pelaksanaan. Tidak membuat dokumen dengan input yang tidak cukup.

## 4. PKL

Intake pass. Hermes meminta pedoman resmi, periode, durasi, siswa, industri, pembimbing, bobot, skala, kompetensi, dan format jurnal/laporan. Tidak membuat dokumen.

## 5. Wali kelas

Intake pass. Hermes meminta daftar siswa resmi, template, periode, jenis dokumen, kebijakan akses, agenda, data kontak, denah, dan prosedur buku kasus. Tidak merekonstruksi data siswa dari chat.

## 6. Riset -> materi -> LKPD -> soal

Gate behavior pass. Hermes menahan rantai ketika hanya TP sintetis tersedia. Gate yang disebut:

1. konteks pembelajaran;
2. kebijakan dan format;
3. TP dan indikator;
4. riset sumber;
5. persetujuan riset;
6. materi;
7. persetujuan materi;
8. LKPD;
9. rubrik;
10. persetujuan LKPD;
11. blueprint asesmen;
12. soal dan validasi;
13. konsistensi lintas artefak;
14. persetujuan akhir.

Tidak ada materi, LKPD, atau soal yang dibuat sebelum gate sebelumnya disetujui.

## 7. Template sekolah

Fixture tersedia:

```text
tests/fixtures/template-sekolah-sintetis.md
```

Isinya sengaja sederhana dan diberi label bukan format resmi. Template nyata belum tersedia, jadi area ini **NOT VERIFIED** untuk kondisi produksi.

## Perbaikan yang masuk

- `pa-nilai/scripts/olah_nilai.py` kini menolak nilai kosong ketika bobot komponen digunakan.
- Error dikembalikan sebagai pesan CLI, bukan traceback.
- Fixture CSV tetap menyimpan satu nilai kosong sebagai negative test.

## Kesimpulan

Expanded QA belum seluruhnya PASS karena PDF dan template sekolah nyata belum dapat diverifikasi tanpa dependensi dan sumber nyata. Semua area yang bisa diuji tanpa input eksternal sudah diuji, dan temuan nilai kosong sudah diperbaiki.

Status keseluruhan: **PARTIAL PASS, dengan blocker eksternal untuk PDF dan template nyata.**

## Next steps

1. Siapkan `weasyprint` atau renderer PDF yang disepakati.
2. Uji ulang generator PDF dan baca kembali PDF dengan PyMuPDF.
3. Kirim satu template sekolah nyata untuk uji format.
4. Tambahkan fixture CSV lengkap dan XLSX untuk uji nilai.
5. Jalankan chain riset dengan sumber resmi yang disetujui.

## Repro

```bash
python3 pa-nilai/scripts/olah_nilai.py --selftest
python3 pa-nilai/scripts/olah_nilai.py tests/fixtures/nilai-sintetis.csv --bobot 'tp1=0.4,tp2=0.6' --kktp 70
python3 pa-core/scripts/gen_pdf_from_md.py tests/fixtures/template-sekolah-sintetis.md /tmp/template-uji.pdf 'Template Uji'
```

Expected: selftest pass; CSV fixture rejected due to missing score; PDF reports missing dependency until installed.

## Data safety

No real student, school, contact, or official private template data was used.

## End

This report records observed results, not assumed success.

## Commit

Filled after implementation verification.

## Owner

Perangkat Ajar project.

## Version

Expanded QA cycle 1.

## Final note

A test marked Not verified must not be reported as passed.

## Status code

PARTIAL_PASS

## Future evidence

Attach PyMuPDF page count and extracted text after PDF dependency setup.

## Scope

Seven requested QA areas are covered at intake or artifact level according to available evidence.

## Done



## Reviewer checklist

- [x] Commands actually run
- [x] Negative CSV behavior observed
- [x] PDF blocker observed
- [x] External template limitation stated
- [x] No fabricated output

## Final

PARTIAL PASS
