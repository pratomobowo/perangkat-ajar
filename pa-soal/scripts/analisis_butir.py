#!/usr/bin/env python3
"""
Analisis butir soal metode kelompok atas-bawah (portable, stdlib saja).
Pemakaian:
    python3 analisis_butir.py jawaban.csv --kunci ABCDAB...
    python3 analisis_butir.py jawaban.csv --kunci kunci.txt --atas 27
Format jawaban.csv: header kolom q1..qn (nama bebas asal urut), baris = siswa,
isi = huruf opsi (A-D) atau kosong/salah-format dianggap SALAH. Kolom pertama
boleh nama siswa (otomatis dilewati jika bukan jawaban valid).
Output: tabel No | P | Kategori | D | Kategori | Pengecoh lemah + rekap.
Exit 0 selalu (laporan), kecuali argumen salah.
"""
import argparse, csv, sys

KAT_P = [(0.71, "mudah"), (0.31, "sedang"), (-1, "sukar")]
KAT_D = [(0.70, "sangat baik"), (0.40, "baik"), (0.30, "cukup"), (0.20, "jelek"), (-1, "GAGAL/ditolak")]


def kat(nilai, tabel):
    for batas, label in tabel:
        if nilai >= batas:
            return label
    return tabel[-1][1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("jawaban_csv")
    ap.add_argument("--kunci", required=True, help="string ABCDA... atau file .txt satu baris")
    ap.add_argument("--atas", type=int, default=27, help="persen kelompok atas/bawah (default 27)")
    args = ap.parse_args()

    kunci = open(args.kunci).read().strip().upper() if args.kunci.endswith(".txt") else args.kunci.upper()
    with open(args.jawaban_csv, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    header = [c.strip().lower() for c in rows[0]]
    # kolom jawaban: semua kolom kecuali kolom pertama bila headernya bukan q*/angka
    start = 1 if (header[0] not in ("q1", "1") and len(header) - 1 == len(kunci)) else 0
    data = []
    for r in rows[1:]:
        if not any(c.strip() for c in r):
            continue
        ans = [c.strip().upper()[:1] if c.strip() else "-" for c in r[start:start + len(kunci)]]
        data.append(ans)
    n_soal = len(kunci)
    skor = [sum(1 for i in range(n_soal) if row[i] == kunci[i]) for row in data]

    # kelompok atas-bawah
    n_g = max(1, round(len(data) * args.atas / 100))
    idx = sorted(range(len(data)), key=lambda i: skor[i], reverse=True)
    atas_idx, bawah_idx = set(idx[:n_g]), set(idx[-n_g:])

    print(f"Siswa: {len(data)} | Butir: {n_soal} | Kelompok atas/bawah: {n_g}/{n_g}")
    print(f"{'No':>3} {'P':>5} {'Kategori':>7} {'D':>5} {'Daya Beda':>15}  Pengecoh lemah")
    rekap = {"P": [], "D": []}
    for i in range(n_soal):
        ba = sum(1 for j in atas_idx if data[j][i] == kunci[i])
        bb = sum(1 for j in bawah_idx if data[j][i] == kunci[i])
        p = (ba + bb) / (2 * n_g)
        d = ba / n_g - bb / n_g
        kp, kd = kat(p, KAT_P), kat(d, KAT_D)
        # efektivitas pengecoh: proporsi kelompok BAWAH memilih tiap opsi salah
        lemah = []
        from collections import Counter
        cnt = Counter(data[j][i] for j in bawah_idx)
        total_bawah = sum(v for k, v in cnt.items() if k != "-")
        for opsi in "ABCD"[:len(set(kunci))]:
            if opsi != kunci[i] and total_bawah and cnt.get(opsi, 0) / total_bawah < 0.05:
                lemah.append(opsi)
        print(f"{i+1:>3} {p:>5.2f} {kp:>7} {d:>5.2f} {kd:>15}  {','.join(lemah) if lemah else '-'}"
              + ("  <-- REVISI" if kat(d, KAT_D) in ("jelek", "GAGAL/ditolak") else ""))
        rekap["P"].append(p)
        rekap["D"].append(d)

    from collections import Counter
    c_d = Counter(kat(d, KAT_D) for d in rekap["D"])
    print("\nREKAP daya beda:", dict(c_d))
    revisi = [i + 1 for i, d in enumerate(rekap["D"]) if d < 0.30]
    print("Butir disarankan direvisi/ganti:", revisi if revisi else "tidak ada ✔")


if __name__ == "__main__":
    main()
