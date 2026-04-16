"""Validate IX-GCR-SPE BOM-style configuration files.

Purpose:
    Perform transparent structural and semantic checks on concept-stage
    configuration JSON files.

Important:
    This script does not perform radiation transport or dose estimation.
    It only checks whether a configuration is internally well-formed enough
    for bookkeeping, comparison, and review workflows.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


ALLOWED_ROLES = {
    "baseline_candidate",
    "aggressive_branch",
    "speculative_branch",
    "instrumentation",
}

ALLOWED_ORIENTATIONS = {
    "sidewall",
    "endcap",
    "hatch_path",
    "general_envelope",
    "ceiling",
    "floor",
    "unknown",
}

ALLOWED_THREAT_CLASSES = {
    "GCR",
    "SPE",
    "GCR+SPE",
    "monitoring",
    "mixed",
}

ALLOWED_MATERIAL_FAMILIES = {
    "water_equivalent",
    "polyethylene_family",
    "hydride",
    "cryogenic_hydrogen",
    "boron_nitrogen_composite",
    "structural_shell",
    "instrumentation",
    "other",
}


@dataclass
class ValidationIssue:
    severity: str
    location: str
    message: str


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("Top-level JSON value must be an object.")
    return data


def _add(issues: list[ValidationIssue], severity: str, location: str, message: str) -> None:
    issues.append(ValidationIssue(severity=severity, location=location, message=message))


def validate_config(data: dict[str, Any]) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []

    repo = data.get("repo")
    if repo != "IX-GCR-SPE":
        _add(issues, "error", "repo", "Expected repo to equal 'IX-GCR-SPE'.")

    configuration = data.get("configuration")
    if not isinstance(configuration, str) or not configuration.strip():
        _add(issues, "error", "configuration", "Configuration must be a non-empty string.")

    schema_version = data.get("schema_version")
    if schema_version is None:
        _add(
            issues,
            "warning",
            "schema_version",
            "Missing schema_version. Recommended value is '1.0.0'.",
        )
    elif schema_version != "1.0.0":
        _add(
            issues,
            "warning",
            "schema_version",
            "Unrecognized schema_version. Expected '1.0.0'.",
        )

    notes = data.get("notes")
    if not isinstance(notes, list):
        _add(issues, "error", "notes", "Notes must be a list of strings.")
    else:
        for index, note in enumerate(notes):
            if not isinstance(note, str) or not note.strip():
                _add(issues, "error", f"notes[{index}]", "Each note must be a non-empty string.")

    zones = data.get("zones")
    if not isinstance(zones, list) or not zones:
        _add(issues, "error", "zones", "Zones must be a non-empty list.")
        return issues

    seen_zone_names: set[str] = set()

    for zone_index, zone in enumerate(zones):
        zone_loc = f"zones[{zone_index}]"
        if not isinstance(zone, dict):
            _add(issues, "error", zone_loc, "Each zone must be an object.")
            continue

        name = zone.get("name")
        if not isinstance(name, str) or not name.strip():
            _add(issues, "error", f"{zone_loc}.name", "Zone name must be a non-empty string.")
            zone_name = f"<unnamed:{zone_index}>"
        else:
            zone_name = name.strip()
            if zone_name in seen_zone_names:
                _add(issues, "error", f"{zone_loc}.name", f"Duplicate zone name '{zone_name}'.")
            seen_zone_names.add(zone_name)

        description = zone.get("description")
        if not isinstance(description, str) or not description.strip():
            _add(
                issues,
                "error",
                f"{zone_loc}.description",
                "Zone description must be a non-empty string.",
            )

        orientation = zone.get("orientation")
        if orientation is not None and orientation not in ALLOWED_ORIENTATIONS:
            _add(
                issues,
                "error",
                f"{zone_loc}.orientation",
                f"Orientation must be one of: {sorted(ALLOWED_ORIENTATIONS)}.",
            )

        occupancy_weight = zone.get("occupancy_weight")
        if occupancy_weight is not None:
            if not isinstance(occupancy_weight, (int, float)) or occupancy_weight < 0:
                _add(
                    issues,
                    "error",
                    f"{zone_loc}.occupancy_weight",
                    "occupancy_weight must be a number greater than or equal to 0.",
                )

        layers = zone.get("layers")
        if not isinstance(layers, list) or not layers:
            _add(issues, "error", f"{zone_loc}.layers", "Layers must be a non-empty list.")
            continue

        seen_layer_names: set[str] = set()

        for layer_index, layer in enumerate(layers):
            layer_loc = f"{zone_loc}.layers[{layer_index}]"
            if not isinstance(layer, dict):
                _add(issues, "error", layer_loc, "Each layer must be an object.")
                continue

            layer_name = layer.get("name")
            if not isinstance(layer_name, str) or not layer_name.strip():
                _add(issues, "error", f"{layer_loc}.name", "Layer name must be a non-empty string.")
            else:
                normalized_layer_name = layer_name.strip()
                if normalized_layer_name in seen_layer_names:
                    _add(
                        issues,
                        "warning",
                        f"{layer_loc}.name",
                        f"Duplicate layer name '{normalized_layer_name}' within zone '{zone_name}'.",
                    )
                seen_layer_names.add(normalized_layer_name)

            role = layer.get("role")
            if role not in ALLOWED_ROLES:
                _add(
                    issues,
                    "error",
                    f"{layer_loc}.role",
                    f"Role must be one of: {sorted(ALLOWED_ROLES)}.",
                )

            if "g_cm2" not in layer:
                _add(issues, "error", f"{layer_loc}.g_cm2", "Missing g_cm2.")
            else:
                g_cm2 = layer["g_cm2"]
                if not isinstance(g_cm2, (int, float)):
                    _add(issues, "error", f"{layer_loc}.g_cm2", "g_cm2 must be numeric.")
                elif g_cm2 <= 0:
                    _add(issues, "error", f"{layer_loc}.g_cm2", "g_cm2 must be greater than 0.")

            notes_value = layer.get("notes")
            if not isinstance(notes_value, str):
                _add(issues, "error", f"{layer_loc}.notes", "notes must be a string.")

            source_ids = layer.get("source_ids")
            if source_ids is not None:
                if not isinstance(source_ids, list):
                    _add(issues, "error", f"{layer_loc}.source_ids", "source_ids must be a list.")
                else:
                    seen_source_ids: set[str] = set()
                    for source_index, source_id in enumerate(source_ids):
                        src_loc = f"{layer_loc}.source_ids[{source_index}]"
                        if not isinstance(source_id, str) or not source_id.startswith("S-"):
                            _add(
                                issues,
                                "error",
                                src_loc,
                                "Each source_id must be a string like 'S-07'.",
                            )
                        elif source_id in seen_source_ids:
                            _add(
                                issues,
                                "warning",
                                src_loc,
                                f"Duplicate source_id '{source_id}' within the same layer.",
                            )
                        else:
                            seen_source_ids.add(source_id)

            threat_class = layer.get("threat_class")
            if threat_class is not None and threat_class not in ALLOWED_THREAT_CLASSES:
                _add(
                    issues,
                    "error",
                    f"{layer_loc}.threat_class",
                    f"threat_class must be one of: {sorted(ALLOWED_THREAT_CLASSES)}.",
                )

            material_family = layer.get("material_family")
            if material_family is not None and material_family not in ALLOWED_MATERIAL_FAMILIES:
                _add(
                    issues,
                    "error",
                    f"{layer_loc}.material_family",
                    f"material_family must be one of: {sorted(ALLOWED_MATERIAL_FAMILIES)}.",
                )

    return issues


def render_text(issues: list[ValidationIssue], source_path: Path) -> str:
    errors = [issue for issue in issues if issue.severity == "error"]
    warnings = [issue for issue in issues if issue.severity == "warning"]

    lines: list[str] = []
    lines.append(f"Validation target: {source_path}")
    lines.append(f"Errors: {len(errors)}")
    lines.append(f"Warnings: {len(warnings)}")
    lines.append("")

    if not issues:
        lines.append("No validation issues found.")
        return "\n".join(lines) + "\n"

    for issue in issues:
        lines.append(f"[{issue.severity.upper()}] {issue.location} — {issue.message}")

    return "\n".join(lines) + "\n"


def render_json(issues: list[ValidationIssue], source_path: Path) -> str:
    payload = {
        "source": str(source_path),
        "error_count": sum(1 for issue in issues if issue.severity == "error"),
        "warning_count": sum(1 for issue in issues if issue.severity == "warning"),
        "issues": [asdict(issue) for issue in issues],
    }
    return json.dumps(payload, indent=2) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate an IX-GCR-SPE config file.")
    parser.add_argument("config", type=Path, help="Path to the JSON config file.")
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Output format for the validation report.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Optional path to write the validation report.",
    )
    args = parser.parse_args()

    try:
        data = load_json(args.config)
        issues = validate_config(data)
    except Exception as exc:  # pragma: no cover - catastrophic parse path
        message = f"Validation failed before semantic checks: {exc}\n"
        if args.output:
            args.output.write_text(message, encoding="utf-8")
        else:
            sys.stderr.write(message)
        raise SystemExit(2) from exc

    rendered = render_json(issues, args.config) if args.format == "json" else render_text(issues, args.config)

    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")

    has_errors = any(issue.severity == "error" for issue in issues)
    raise SystemExit(1 if has_errors else 0)


if __name__ == "__main__":
    main()
