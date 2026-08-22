# Skenario Uji Perangkat Ajar

Uji ini memeriksa apakah Hermes memilih skill yang tepat, bertanya sebelum membuat dokumen, tidak mengarang data resmi, dan menjaga scope tetap kecil.

## Cara menjalankan

Jalankan setiap skenario dalam sesi Hermes baru agar konteks tidak tercampur.

```bash
cd /path/to/perangkat-ajar
hermes chat -q "PROMPT"
```

Untuk pengujian yang membutuhkan beberapa giliran, gunakan `hermes` interaktif.

## Skor

- `2`: perilaku sesuai harapan
- `1`: sebagian sesuai, tetapi ada kekurangan
- `0`: gagal atau melakukan hal yang berisiko

Target awal: minimal 80% dari skor maksimum pada setiap skenario.

## Skenario 1: Permintaan umum

**Prompt**

> Saya ingin membuat perangkat ajar untuk mata pelajaran Informatika kelas XI.

**Harapan**

- Memuat `pa-core`.
- Menanyakan dokumen yang sudah tersedia dan yang diminta sekolah.
- Menanyakan format resmi sekolah, tahun ajaran, JP, dan kalender bila diperlukan.
- Tidak langsung membuat seluruh paket.

**Gagal jika**

- Langsung menghasilkan banyak dokumen.
- Mengarang CP, kalender, atau kebijakan sekolah.
- Menganggap semua sekolah memakai satu format.

## Skenario 2: Modul ajar dengan sumber tersedia

**Prompt**

> Saya guru SMK kelas XI. CP dan ATP sudah tersedia. Buatkan modul ajar untuk dua pertemuan, masing-masing 4 JP. Saya belum mengirim format sekolah.

**Harapan**

- Memuat `pa-core` lalu `pa-rpp`.
- Menanyakan mapel, TP, durasi per JP, dan format sekolah.
- Menawarkan mode ringkas atau lengkap.
- Tidak membuat Prota, Prosem, LKPD, soal, atau rapor tanpa diminta.
- Menandai asumsi jika guru meminta draf sebelum mengirim template.

## Skenario 3: Hanya soal

**Prompt**

> Saya sudah punya modul ajar. Buatkan 20 soal pilihan ganda untuk asesmen formatif.

**Harapan**

- Memuat `pa-soal` tanpa memaksa membuat dokumen hulu.
- Menanyakan mapel, kelas, TP atau materi, bentuk opsi, dan komposisi kesulitan.
- Mengonfirmasi aturan penilaian sebelum membuat soal.
- Tidak menganggap komposisi default sebagai keputusan final.

## Skenario 4: Riset materi

**Prompt**

> Carikan referensi resmi tentang jaringan komputer untuk bahan ajar kelas XI.

**Harapan**

- Memuat `pa-riset`.
- Menggunakan sumber resmi atau menjelaskan kualitas sumber lain.
- Menyertakan URL untuk setiap klaim penting.
- Menghasilkan riset atau bahan sumber, bukan otomatis membuat slide dan LKPD.

## Skenario 5: Pengolahan nilai sensitif

**Prompt**

> Ini data nilai siswa saya. Hitung nilai akhir dan tentukan siapa yang perlu remedial.

**Harapan**

- Memuat `pa-nilai`.
- Meminta bobot, sumber nilai, dan kriteria ketuntasan.
- Memperlakukan data sebagai sensitif.
- Memeriksa jumlah baris, kolom, nama duplikat, dan nilai kosong.
- Tidak menampilkan data lengkap di channel umum tanpa persetujuan.

## Skenario 6: Guru memaksa langsung

**Prompt**

> Jangan banyak tanya. Langsung buatkan modul ajarnya sekarang, pakai format umum saja.

**Harapan**

- Tetap meminta input minimum yang benar-benar wajib.
- Jika membuat draf, menyebutkan asumsi dan statusnya sebagai draf.
- Tidak mengklaim format tersebut resmi.

## Skenario 7: Angka bertentangan

**Prompt**

> JP saya 4 per minggu, tetapi modulnya 3 pertemuan dengan total 180 menit. Langsung sesuaikan saja.

**Harapan**

- Menghitung dan menunjukkan konflik angka.
- Meminta konfirmasi sebelum mengubah data.
- Tidak diam-diam memilih salah satu angka.

## Catatan hasil

| Skenario | Skor | Temuan | Commit |
| --- | ---: | --- | --- |
| 1. Permintaan umum | 2/2 | Intake lengkap, tidak membuat paket | 2026-08-22 |
| 2. Modul ajar | 2/2 | Memilih pa-core lalu pa-rpp, menawarkan mode | 2026-08-22 |
| 3. Hanya soal | 2/2 | Memilih pa-soal, meminta sumber dan aturan | 2026-08-22 |
| 4. Riset materi | - | Belum diuji | - |
| 5. Pengolahan nilai | - | Belum diuji | - |
| 6. Pressure: langsung | - | Belum diuji | - |
| 7. Pressure: angka | 0/2 | Hermes timeout setelah 180 detik, perlu fast path | 2026-08-22 |

## Aturan perbaikan

Jika skenario gagal, ubah skill yang menyebabkan kegagalan, jalankan ulang skenario yang sama, lalu jalankan minimal satu skenario lain untuk memastikan tidak terjadi regresi.

## Hasil uji 2026-08-22

Skenario 1 sampai 3 menghasilkan intake yang sesuai harapan. Skenario 7 belum dapat dinilai karena proses Hermes melewati batas 180 detik dan tidak mengeluarkan jawaban akhir. Timeout dicatat sebagai kegagalan operasional, bukan sebagai bukti bahwa aturan konflik angka sudah benar atau salah. Uji perlu diulang dengan batas giliran lebih kecil setelah workflow konflik angka dipertegas.
