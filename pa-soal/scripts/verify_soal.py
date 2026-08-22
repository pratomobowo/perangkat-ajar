#!/usr/bin/env python3
"""
Verifikasi naskah soal sebelum generate PDF (portable, tanpa dependensi eksternal).
Pemakaian:
    python3 verify_soal.py naskah.md --jumlah 50 --target 10,20,20 --kisi kisi.md
    python3 verify_soal.py naskah.md --jumlah 30            # latihan tanpa kisi
Cek:
    1. Nomor soal 1..N lengkap di naskah (format MD "**N.**" atau "N.")
    2. Kunci jawaban lengkap 1..N + distribusi A-D seimbang (toleransi ±2)
    3. (bila --kisi) komposisi level L1/L2/L3 = --target, tiap TP >=1 L1
    4. (bila --kisi) pembahasan mencakup semua nomor L3
Exit code 0 = lolos semua; 1 = ada kegagalan.
"""
import argparse, re, sys
from collections import Counter, defaultdict


def baca(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def nomor_soal(naskah):
    nums = set(int(n) for n in re.findall(r"^\s*(?:\*\*)?(\d{1,3})\.(?:\*\*)?\s", naskah, re.M))
    # buang angka yang bukan penanda soal (mis. tahun di petunjuk): soal biasanya berurutan dari 1
    urut = []
    n = 1
    while n in nums:
        urut.append(n)
        n += 1
    return urut


def pasangan_kunci(naskah):
    """Ambil bagian KUNCI JAWABAN, parse tabel per-baris (bukan regex lintas baris)."""
    idx = naskah.find("KUNCI JAWABAN")
    if idx == -1:
        return []
    bagian = naskah[idx:]
    pairs = []
    for line in bagian.splitlines():
        if "|" not in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2 or cells[0] in ("", "No", "---"):
            continue
        for a, b in zip(cells[0::2], cells[1::2]):
            if a.isdigit() and b.upper() in "ABCD" and len(b) == 1:
                pairs.append((int(a), b.upper()))
    return pairs


def baris_kisi(kisi):
    """Parse baris kisi-kisi: | No | TP | Materi | Indikator | Level | NoSoal |"""
    rows = []
    for line in kisi.splitlines():
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) >= 6 and re.fullmatch(r"\d{1,3}", cells[0]) and re.fullmatch(r"L[123]", cells[4]):
            rows.append({"tp": cells[1], "level": cells[4], "soal": cells[5]})
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("naskah")
    ap.add_argument("--jumlah", type=int, required=True, help="jumlah total soal")
    ap.add_argument("--target", default="", help="komposisi L1,L2,L3 mis. 10,20,20")
    ap.add_argument("--kisi", default="", help="file kisi-kisi (opsional)")
    args = ap.parse_args()

    gagal = []
    naskah = baca(args.naskah)

    # 1. nomor soal lengkap
    nums = nomor_soal(naskah)
    if nums != list(range(1, args.jumlah + 1)):
        hilang = sorted(set(range(1, args.jumlah + 1)) - set(nums))
        gagal.append(f"Nomor soal tidak lengkap: ada {len(nums)}, hilang {hilang[:10]}")

    # 2. kunci lengkap + distribusi
    pairs = pasangan_kunci(naskah)
    if sorted(n for n, _ in pairs) != list(range(1, args.jumlah + 1)):
        gagal.append(f"Kunci tidak lengkap: {len(pairs)}/{args.jumlah}")
    dist = Counter(h for _, h in pairs)
    counts = [dist.get(h, 0) for h in "ABCD"]  # sertakan huruf bernilai 0
    if pairs and max(counts) - min(counts) > 2:
        gagal.append(f"Distribusi kunci timpang: {dict(dist)}")
    else:
        print(f"Kunci OK: {len(pairs)} pasangan, distribusi {dict(dist)}")

    # 3-4. kisi-kisi
    if args.kisi:
        rows = baris_kisi(baca(args.kisi))
        lvl = Counter(r["level"] for r in rows)
        if args.target:
            target = [int(x) for x in args.target.split(",")]
            if [lvl.get("L1", 0), lvl.get("L2", 0), lvl.get("L3", 0)] != target:
                gagal.append(f"Komposisi level {dict(lvl)} != target {target}")
        per_tp = defaultdict(list)
        for r in rows:
            per_tp[r["tp"]].append(r["level"])
        tanpa_mudah = [tp for tp, ls in per_tp.items() if "L1" not in ls]
        if tanpa_mudah:
            gagal.append(f"TP tanpa soal mudah (L1): {tanpa_mudah}")
        else:
            print(f"Kisi OK: {len(rows)} baris, tiap TP punya L1 ({len(per_tp)} TP)")
        # pembahasan mencakup semua L3
        l3_nums = set()
        for r in rows:
            if r["level"] == "L3":
                l3_nums.update(int(x) for x in re.findall(r"\d+", r["soal"]))
        idx = naskah.find("PEMBAHASAN")
        pembahasan = set(int(x) for x in re.findall(r"^\s*(?:\*\*)?(\d{1,3})\.", naskah[idx:], re.M)) if idx != -1 else set()
        if l3_nums - pembahasan:
            gagal.append(f"Pembahasan kurang nomor L3: {sorted(l3_nums - pembahasan)}")
        else:
            print(f"Pembahasan OK: mencakup {len(l3_nums)} soal L3")

    if gagal:
        print("GAGAL:")
        for g in gagal:
            print(f"  - {g}")
        sys.exit(1)
    print("SEMUA CEK LOLOS ✔")


if __name__ == "__main__":
    main()
