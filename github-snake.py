#!/usr/bin/env python3
import sys
from datetime import datetime
import os

def main():
    username = None
    out = "output/github-contribution-grid-snake.svg"
    # parse args --username and --output
    args = sys.argv[1:]
    for i, a in enumerate(args):
        if a in ("--username", "-u") and i+1 < len(args):
            username = args[i+1]
        if a in ("--output", "-o") and i+1 < len(args):
            out = args[i+1]

    if username is None:
        username = os.environ.get("GITHUB_ACTOR", "unknown")

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="120" viewBox="0 0 800 120">
  <rect width="800" height="120" fill="#0b0f14"/>
  <text x="20" y="40" fill="#00FF7F" font-family="monospace" font-size="20">Snake contributions - user: {username}</text>
  <text x="20" y="75" fill="#8fb3ff" font-family="monospace" font-size="14">Generated: {datetime.utcnow().isoformat()} UTC</text>
  <g transform="translate(20,90)">
'''

    # fake "blocks" representing contributions
    for i in range(30):
        color = "#213241" if i % 5 == 0 else "#2a6f3b"
        x = i * 24
        svg += f'<rect x="{x}" y="0" width="18" height="18" rx="3" fill="{color}" />'

    svg += "\n  </g>\n</svg>"

    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        f.write(svg)
    print(f"Wrote {out}")

if __name__ == "__main__":
    main()

