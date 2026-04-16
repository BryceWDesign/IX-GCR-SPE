"""IX-GCR-SPE areal-density bookkeeping helper.

Purpose:
    Read a BOM-style JSON configuration and compute zone-level and repository-level
    areal-density totals.

Important:
    This script does not estimate radiation dose. It only performs transparent
    mass-per-area bookkeeping from user-provided inputs.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class Layer:
    name: str
    role: str
    g_cm2: float
    notes: str = ""

    @classmethod
    def from_mapping(cls, raw: dict[str, Any]) -> "Layer":
        return cls(
            name=str(raw["name"]),
            role=str(raw.get("role", "unspecified")),
            g_cm2=float(raw["g_cm2"]),
            notes=str(raw.get("notes", "")),
        )


def load_config(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def summarize(config: dict[str, Any]) -> dict[str, Any]:
    zones_out: list[dict[str, Any]] = []
    total = 0.0

    for zone in config.get("zones", []):
        layers = [Layer.from_mapping(item) for item in zone.get("layers", [])]
        zone_total = sum(layer.g_cm2 for layer in layers)
        total += zone_total
        zones_out.append(
            {
                "zone": zone["name"],
                "description": zone.get("description", ""),
                "total_g_cm2": round(zone_total, 3),
                "layers": [
                    {
                        "name": layer.name,
                        "role": layer.role,
                        "g_cm2": layer.g_cm2,
                        "notes": layer.notes,
                    }
                    for layer in layers
                ],
            }
        )

    return {
        "repo": config.get("repo", "IX-GCR-SPE"),
        "configuration": config.get("configuration", "unknown"),
        "zone_count": len(zones_out),
        "zones": zones_out,
        "sum_of_zone_totals_g_cm2": round(total, 3),
        "notes": config.get("notes", []),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize areal-density budgets by zone.")
    parser.add_argument("config", type=Path, help="Path to a JSON configuration file.")
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Optional path to write the JSON summary.",
    )
    args = parser.parse_args()

    config = load_config(args.config)
    summary = summarize(config)
    rendered = json.dumps(summary, indent=2)

    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
