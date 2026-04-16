"""Create a plain-text zone report from a BOM-style configuration.

This helper exists to make design reviews readable by non-programmers.
It intentionally performs formatting only.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_report(data: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append(f"Repository: {data.get('repo', 'IX-GCR-SPE')}")
    lines.append(f"Configuration: {data.get('configuration', 'unknown')}")
    lines.append("")

    for zone in data.get("zones", []):
        lines.append(f"Zone: {zone['name']}")
        description = zone.get("description", "")
        if description:
            lines.append(f"  Description: {description}")

        total = 0.0
        for layer in zone.get("layers", []):
            value = float(layer["g_cm2"])
            total += value
            role = layer.get("role", "unspecified")
            lines.append(f"  - {layer['name']}: {value:.3f} g/cm^2 [{role}]")
            notes = layer.get("notes", "")
            if notes:
                lines.append(f"      notes: {notes}")

        lines.append(f"  Total: {total:.3f} g/cm^2")
        lines.append("")

    if data.get("notes"):
        lines.append("Notes:")
        for note in data["notes"]:
            lines.append(f"  - {note}")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a human-readable zone report.")
    parser.add_argument("config", type=Path, help="Path to the JSON config file.")
    parser.add_argument("--output", type=Path, default=None, help="Optional output text file.")
    args = parser.parse_args()

    config = load_json(args.config)
    report = build_report(config)

    if args.output:
        args.output.write_text(report, encoding="utf-8")
    else:
        print(report)


if __name__ == "__main__":
    main()
