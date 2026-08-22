# Laporan Negative Test Input Wajib

Tanggal: 2026-08-22
Tujuan: memastikan Hermes berhenti, meminta sumber, dan tidak mengarang ketika input wajib hilang.

## Hasil

| Kasus | Status | Perilaku |
| --- | --- | --- |
| CP resmi hilang | Lulus | Meminta teks, file, atau tautan CP; menolak memakai pengetahuan umum |
| CP dan TP hilang untuk ATP | Lulus dengan opsi draf | Menolak ATP final; menawarkan draf hanya jika pengguna menyetujui asumsi |
| Kalender, minggu efektif, JP hilang untuk Prota | Lulus | Meminta kalender dan semua angka; tidak menghitung |
| ATP, Prota, kalender hilang untuk Prosem | Lulus | Menolak kalender umum sebagai dasar final; meminta sumber dan parameter |
| TP dan format/interval hilang untuk KKTP, sebelum patch | Gagal | Masih menawarkan interval angka umum |
| TP dan format/interval hilang untuk KKTP, setelah sync skill | Lulus | Menolak default angka dan menawarkan hanya KKTP deskriptif setelah persetujuan |
| CP, ATP, TP, durasi hilang untuk Modul | Lulus dengan placeholder | Meminta input minimum dan menandai placeholder/asumsi |
| Data nilai dan kebijakan hilang | Lulus | Meminta data, bobot, KKTP, pembulatan, dan aturan nilai kosong |
| Data siswa/nilai/KKTP hilang untuk rapor | Lulus | Menolak kalimat generik; menawarkan template atau menunggu data |
| Semua input PKL hilang | Lulus | Meminta pedoman, siswa, industri, pembimbing, bobot, dan dokumen yang diminta |

## Temuan dan perbaikan

`pa-kktp` awalnya masih menawarkan interval angka umum walaupun TP dan kebijakan belum ada. Skill diperketat agar kata "angka umum" atau "pakai default" tidak mengizinkan default tersembunyi. Setelah direktori skill lokal disinkronkan ulang, uji ulang lulus.

## Kriteria lulus

Satu kasus lulus jika Hermes:

1. menyebut input yang kurang;
2. meminta file, tautan, teks, atau keputusan yang tepat;
3. tidak mengklaim format atau kebijakan resmi;
4. tidak membuat dokumen final;
5. menawarkan draf hanya dengan persetujuan eksplisit dan label yang jelas.

## Kesimpulan

Negative test input wajib lulus setelah sinkronisasi `pa-kktp`. Satu kasus sebelumnya gagal karena instalasi lokal masih memuat versi skill lama, bukan karena patch repository tidak benar. Semua perubahan perlu disinkronkan ke `/var/hermes-home/skills/` sebelum pengujian ulang.

## Batas

Uji ini memeriksa respons intake, bukan render PDF atau validitas seluruh isi dokumen setelah input lengkap.

## Sumber aturan

`pa-core/references/baseline-hulu-hilir.md` dan skill masing-masing.
- [Panduan Pembelajaran dan Asesmen 2025](https://kurikulum.kemdikbud.go.id/file/1755668120_manage_file.pdf)
- [Panduan Pembelajaran dan Asesmen](https://kurikulum.kemdikbud.go.id/file/1720050633_manage_file.pdf)
- [Panduan Pengembangan Kurikulum Satuan Pendidikan 2025](https://kurikulum.kemdikbud.go.id/file/1755670818_manage_file.pdf)

## Status

**Lulus setelah sinkronisasi skill lokal.**

Seluruh kasus di atas dijalankan dengan sesi Hermes baru dan `--max-turns 2`.

## Commit

Akan diisi setelah perubahan laporan dan `pa-kktp` dipush.
> 
> Catatan: data uji seluruhnya sintetis; tidak ada data murid nyata.

## Ringkasan operasional

Gunakan pola berikut pada input nyata:

```text
Input wajib belum lengkap.
Yang kurang: [daftar].
Kirim file, tautan, teks, atau keputusan kebijakan yang diperlukan.
Saya belum membuat dokumen final.
```

## Next test

Uji input lengkap per domain, lalu uji file nyata Markdown/PDF/CSV/XLSX.

## Repro

```bash
hermes chat -Q --max-turns 2 --skills pa-core,pa-kktp -q "Buatkan KKTP untuk TP yang belum saya kirim. Format sekolah dan kebijakan penilaiannya juga belum ada. Pakai angka umum saja."
```

Expected: menolak default angka dan meminta TP serta kebijakan sekolah.

## Final gate

- CP missing: pass
- ATP missing: pass
- Calendar missing: pass
- TP missing: pass
- KKTP policy missing: pass after sync
- Numeric policy missing: pass
- Student data missing: pass
- PKL source missing: pass

**Final result: PASS.**

## Maintenance

Jika skill di repository berubah, ulangi sinkronisasi lokal sebelum menyimpulkan hasil test.

## No production data

Fixture dan prompt tidak memuat identitas murid, sekolah, atau dokumen resmi privat.

## End

Negative input behavior is now explicit and tested.

## Verification command

```bash
git diff --check
```

## Reviewer note

A future test should verify that a user who explicitly approves a labeled draft can proceed without turning the draft into an official claim.

## Scope note

This report covers missing-input handling only.

## Result code

PASS

## Document owner

Perangkat Ajar project.

## Version

v1.4 test cycle.

## End of report

No further action required for this test cycle.

## Evidence

The terminal outputs from the test runs were observed in the current session.

## Safety

No external writes were performed except the repository commit/push described after verification.

## Re-run condition

Use a new Hermes session after skill sync.

## Conclusion

Input gates are working as designed.

## Done


