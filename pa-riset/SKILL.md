---
name: pa-riset
description: "Use when a teacher asks to find and verify web sources for a topic, learning objective, teaching material, case, or assessment context. Return sourced research for another skill to transform."
---

# Riset Materi → Bahan Ajar

Guru: *"cariin materi X"*, *"ada nggak referensi Y"*, *"bikinin bahan ajar tentang Z"* → skill ini mencari, memverifikasi, merangkum, dan menghasilkan dokumen bahan ajar.

## LANGKAH 0 - Pakai tool pencarian yang ADA di Hermes guru
- Prioritas: tool web-search bawaan Hermes → kalau host punya SearXNG lokal (`http://127.0.0.1:8080/search?q=<query>&format=json`) pakai itu → terakhir fallback browser.
- Jangan anggap satu tool tertentu selalu ada; cek dulu, gagal → turun ke alternatif.

## Alur kerja
1. **Kaitkan ke TP dulu**: tanya/cocokkan topik dengan mapel & TP aktif dari `profil.yaml`/Prosem (`pa-prosem`) supaya hasil riset nyambung dengan perangkat ajar - bukan materi lepas.
2. **Cari dengan 2-3 variasi query**: bahasa Indonesia + Inggris; pola: `materi <topik> SMK`, `<topik> kurikulum merdeka`, `<topic> tutorial/documentation`.
3. **Filter hasil**: buang spam/duplikat (dedupe by URL); **prioritaskan sumber resmi** - kemendikdasmen.go.id, dokumentasi resmi framework/teknologi, media akademik. Klaim dari 1 sumber saja = tandai belum terverifikasi.
4. **Verifikasi silang**: fakta inti butuh minimal 2-3 sumber independen. Bedakan FAKTA vs OPINI vs HIPOTESIS di hasil akhir.
5. **Baca isi halaman terbaik** (fetch + extract teks; foto/scan pakai vision sesuai `pa-core`).
6. **Ringkas jadi bahan ajar** - struktur standar: *pengertian → konsep/prinsip → contoh (kontekstual Indonesia/industri) → latihan*. Bahasa sesuai jenjang (SMK ≠ SD).
7. **Tuangkan ke dokumen keluarga** (ini nilai utamanya - riset tanpa dokumen = hilang):
   - Materi lengkap per TP → format `pa-media`
   - Poin penting → slide + bank pertanyaan interaktif (`pa-media`)
   - Studi kasus/kasus dunia kerja → `pa-lkpd`
   - Fakta & konsep kunci → konteks soal `pa-soal`
8. Simpan MD di folder output guru (aturan `pa-core`: MD = single source of truth), sajikan ringkasan di chat dulu, PDF kalau diminta.

## Format jawaban riset di chat
```
📌 <Topik> - kaitan: TP<x> <mapel>
Sumber utama: [judul](url) × n sumber
Ringkasan: ...
⚠️ Yang belum terverifikasi: ...
Lanjut dibuatkan: materi lengkap / slide / studi kasus LKPD?
```

## Pitfall
- Situs menolak curl polos (406/bot-check) → ulangi dengan UA browser: `curl -sL -A 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' '<url>' --max-time 25`. Situs pemerintah umumnya lolos; komersial tertentu tetap blok → pakai snippet hasil pencarian sebagai gantinya.
- Engine pencarian bisa kena rate-limit/lambat → retry query berbeda, jangan loop tanpa henti.
- Field konten kadang kosong → pakai judul+URL sebagai petunjuk, fetch halaman untuk detail.
- JANGAN copy-paste mentah artikel orang lain jadi materi - rangkum ulang + sebut sumber (hak cipta & ketelitian).
- Konten teknologi cepat basi - cek tanggal sumber; dokumentasi versi lama bisa menyesatkan.
