#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

PATTERNS = [
    ("override_instructions", r"(?i)ignore (all |any |previous |prior )?(instructions|rules|guidance|system prompt)"),
    ("reveal_hidden", r"(?i)(reveal|show|print|dump|expose).{0,40}(system prompt|hidden prompt|instructions|policy|secrets?)"),
    ("tool_exfil", r"(?i)(use|call|invoke).{0,40}(tool|browser|api|function).{0,40}(send|post|upload|exfiltrate|export)"),
    ("credential_request", r"(?i)(api key|token|password|secret|credential|vault).{0,30}(show|print|give|reveal|send)"),
    ("authority_claim", r"(?i)(you are now|new instructions|administrator note|developer note|system message)"),
    ("disable_safety", r"(?i)(disable|bypass|ignore).{0,30}(safety|policy|guardrails?|restrictions?)"),
    ("data_exfil", r"(?i)(copy|extract|collect|gather).{0,40}(all|every|entire).{0,40}(data|documents|files|messages)"),
    ("prompt_leak", r"(?i)(repeat|recite|output).{0,30}(your prompt|the prompt|system instructions)"),
    ("encoded_payload", r"(?i)(base64|rot13|hex-encoded|decode this hidden instruction)"),
    ("html_hidden", r"(?is)<(script|iframe|object|embed|meta)[^>]*>|display\s*:\s*none|visibility\s*:\s*hidden"),
]

SAFE_EXTENSIONS = {'.md', '.txt', '.html', '.htm', '.json', '.yaml', '.yml', '.csv', '.xml', '.log'}


def scan_text(text: str) -> dict:
    findings = []
    score = 0
    for name, pattern in PATTERNS:
        matches = list(re.finditer(pattern, text))
        if matches:
            score += len(matches)
            findings.append({
                'type': name,
                'count': len(matches),
                'examples': [m.group(0)[:180] for m in matches[:3]],
            })
    risk = 'low'
    if score >= 6:
        risk = 'high'
    elif score >= 2:
        risk = 'medium'
    return {'risk': risk, 'score': score, 'findings': findings}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--file')
    p.add_argument('--text')
    p.add_argument('--json-out')
    args = p.parse_args()

    if args.file:
        path = Path(args.file)
        text = path.read_text(errors='ignore')
        result = scan_text(text)
        result['source'] = str(path)
        result['extension'] = path.suffix.lower()
    elif args.text is not None:
        result = scan_text(args.text)
        result['source'] = 'inline'
    else:
        raise SystemExit('Provide --file or --text')

    if args.json_out:
        Path(args.json_out).write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['risk'] in {'low', 'medium'} else 2)


if __name__ == '__main__':
    main()
