#!/usr/bin/env python3
import argparse, json, os, re
from pathlib import Path

RISK_PATTERNS = {
    "prompt_injection": [r"ignore (all )?(previous|prior) instructions", r"override (system|safety)", r"reveal (secrets|tokens|keys)", r"bypass (safeguards|policy)", r"act as (system|developer)"] ,
    "destructive": [r"rm\s+-rf", r"mkfs", r"dd\s+if=", r"curl\s+.*\|\s*(sh|bash)", r"chmod\s+777"],
    "exfiltration": [r"send .* to (discord|telegram|slack|webhook)", r"post .* secret", r"upload .* credentials"],
    "privilege": [r"sudo\s+", r"NOPASSWD: ALL", r"systemctl\s+enable"],
    "secrets": [r"sk-[A-Za-z0-9_-]{20,}", r"OPENAI_API_KEY=", r"TOKEN=", r"PASSWORD="]
}

TEXT_EXT = {".md", ".txt", ".sh", ".py", ".json", ".yaml", ".yml"}


def scan_file(path: Path):
    findings = []
    try:
        txt = path.read_text(errors="ignore")
    except Exception:
        return findings
    for category, patterns in RISK_PATTERNS.items():
        for pat in patterns:
            for m in re.finditer(pat, txt, flags=re.IGNORECASE):
                line = txt.count("\n", 0, m.start()) + 1
                findings.append({"category": category, "pattern": pat, "line": line, "file": str(path)})
    return findings


def list_files(root: Path, recursive: bool):
    if root.is_file():
        return [root]
    globber = root.rglob("*") if recursive else root.glob("*")
    files = []
    for p in globber:
        if p.is_file() and p.suffix.lower() in TEXT_EXT:
            files.append(p)
    return files


def classify(findings):
    cats = {f["category"] for f in findings}
    if "destructive" in cats or "prompt_injection" in cats or "secrets" in cats:
        return "FAIL"
    if "privilege" in cats or "exfiltration" in cats:
        return "WARN"
    return "PASS"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", required=True)
    ap.add_argument("--recursive", action="store_true")
    args = ap.parse_args()

    root = Path(args.path).expanduser().resolve()
    files = list_files(root, args.recursive)
    findings = []
    for f in files:
        findings.extend(scan_file(f))

    status = classify(findings)
    out = {
        "target": str(root),
        "status": status,
        "findingCount": len(findings),
        "findings": findings[:200]
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
