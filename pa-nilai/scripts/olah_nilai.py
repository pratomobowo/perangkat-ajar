#!/usr/bin/env python3
"""olah_nilai.py — rekap nilai tertimbang per murid + status KKTP + statistik kelas.
CSV: nis,nama,komponen1,komponen2,...  (kolom selain nis/nama = komponen skor 0-100)
Usage:
  python3 olah_nilai.py nilai.csv --bobot "tp1=0.3,tp2=0.3,tp3=0.4" --kktp 70
  python3 olah_nilai.py --selftest
"""
import argparse, csv, sys
from statistics import mean

def parse_bobot(s):
    bobot = {}
    for part in s.split(","):
        k, v = part.split("=")
        bobot[k.strip().lower()] = float(v)
    total = sum(bobot.values())
    if abs(total - 1.0) > 1e-9:
        sys.exit(f"ERROR: total bobot = {total}, harus 1.0")
    return bobot

def load(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        sys.exit("ERROR: CSV kosong")
    seen, siswa = set(), []
    for i, r in enumerate(rows, 2):
        nis = (r.get("nis") or "").strip()
        nama = (r.get("nama") or "").strip()
        if not nama:
            sys.exit(f"ERROR baris {i}: nama kosong")
        if nis and nis in seen:
            sys.exit(f"ERROR baris {i}: NIS {nis} duplikat ({nama})")
        seen.add(nis)
        skor = {}
        for k, v in r.items():
            if k in ("nis", "nama") or v is None or str(v).strip() == "":
                continue
            try:
                s = float(str(v).replace(",", "."))
            except ValueError:
                sys.exit(f"ERROR baris {i}: skor '{k}={v}' bukan angka")
            if not 0 <= s <= 100:
                sys.exit(f"ERROR baris {i} ({nama}): skor {k}={s} di luar 0-100")
            skor[k.strip().lower()] = s
        siswa.append({"nis": nis, "nama": nama, "skor": skor})
    return siswa

def hitung(siswa, bobot, kktp, warn=True):
    out = []
    for s in siswa:
        if warn:
            for k in bobot:
                if k not in s["skor"]:
                    print(f"⚠ {s['nama']}: tidak ada skor {k} — dihitung 0, CEK DULU (sel kosong ≠ nol)", file=sys.stderr)
        na = sum(s["skor"].get(k, 0) * w for k, w in bobot.items())
        na = round(na, 2)
        out.append({**s, "na": na, "status": "TUNTAS" if na >= kktp else "BELUM"})
    return out

def rekap(rows, kktp):
    na_all = [r["na"] for r in rows]
    tuntas = [r for r in rows if r["status"] == "TUNTAS"]
    lines = ["| NIS | Nama | NA | Status |", "|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r['nis']} | {r['nama']} | {r['na']} | {r['status']} |")
    pct = 100 * len(tuntas) / len(rows)
    lines += ["",
        f"**Statistik kelas**: n={len(rows)} · mean={mean(na_all):.2f} · min={min(na_all)} · max={max(na_all)} · ketuntasan={pct:.0f}%",
        "", f"**Remedial** ({len(rows)-len(tuntas)}): " + (", ".join(r["nama"] for r in rows if r["status"] == "BELUM") or "-"),
        f"**Pengayaan** (NA >= {kktp+20}): " + (", ".join(r["nama"] for r in rows if r["na"] >= kktp + 20) or "-")]
    return "\n".join(lines)

def selftest():
    b = parse_bobot("tp1=0.3,tp2=0.3,tp3=0.4")
    assert abs(sum(b.values()) - 1.0) < 1e-9
    siswa = [
        {"nis": "1", "nama": "Ana", "skor": {"tp1": 80, "tp2": 90, "tp3": 70}},
        {"nis": "2", "nama": "Beni", "skor": {"tp1": 60, "tp2": 65, "tp3": 55}},
        {"nis": "3", "nama": "Cici", "skor": {"tp1": 95, "tp2": 95, "tp3": 95}},
    ]
    rows = hitung(siswa, b, 70)
    assert rows[0]["na"] == 79.0 and rows[0]["status"] == "TUNTAS"   # 24+27+28
    assert rows[1]["na"] == 59.5 and rows[1]["status"] == "BELUM"
    assert rows[2]["na"] == 95.0
    txt = rekap(rows, 70)
    assert "ketuntasan=67%" in txt and "Remedial** (1): Beni" in txt and "Pengayaan" in txt
    try:
        parse_bobot("tp1=0.5,tp2=0.4"); assert False
    except SystemExit:
        pass
    print("SELFTEST OK — rumus bobot, status KKTP, statistik terverifikasi")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", nargs="?", help="file CSV nilai")
    ap.add_argument("--bobot", default="", help='mis. "tp1=0.3,tp2=0.3,tp3=0.4" (default: rata-rata sederhana)')
    ap.add_argument("--kktp", type=float, default=70)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest(); sys.exit(0)
    if not a.csv:
        ap.error("butuh file CSV atau --selftest")
    bobot = parse_bobot(a.bobot) if a.bobot else None
    siswa = load(a.csv)
    komponen = {k for s in siswa for k in s["skor"]}
    if bobot is None:
        # rata-rata sederhana dari skor yang ADA per murid (sel kosong di-skip)
        for s in siswa:
            s["na"] = round(mean(s["skor"].values()), 2) if s["skor"] else 0.0
        rows = [{**s, "status": "TUNTAS" if s["na"] >= a.kktp else "BELUM"} for s in siswa]
    else:
        missing = bobot.keys() - komponen
        if missing:
            sys.exit(f"ERROR: kolom bobot {sorted(missing)} tidak ada di CSV (kolom: {sorted(komponen)})")
        rows = hitung(siswa, bobot, a.kktp)
    print(rekap(rows, a.kktp))
