#!/usr/bin/env python3
"""
Excel Formula Generator (offline)
Usage:
  python main.py --input "Sum column A when B is 'Paid'"
"""
import argparse, requests, os, sys

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/generate")
MODEL = "llama3.2:4b"
TIMEOUT = 120

def run_llama(prompt):
    r = requests.post(OLLAMA_URL, json={"model": MODEL, "prompt": prompt, "stream": False}, timeout=TIMEOUT)
    r.raise_for_status()
    return r.json().get("response","").strip()

def build_prompt(task):
    return (
        "Return ONLY the Excel or Google Sheets formula that accomplishes the task described.\n"
        "Do not include explanation, code fences, or other text.\n\n"
        f"Task: {task}"
    )

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", "-i", required=True, help="Plain-English description")
    args = p.parse_args()
    print(run_llama(build_prompt(args.input)))

if __name__ == "__main__":
    main()
