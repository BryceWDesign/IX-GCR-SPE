import json
from pathlib import Path

from src.analysis.validate_config import load_json, validate_config


def _write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def _base_config() -> dict:
    return {
        "repo": "IX-GCR-SPE",
        "configuration": "test_config",
        "schema_version": "1.0.0",
        "notes": ["Concept-stage test config."],
        "zones": [
            {
                "name": "Shadow Vault sidewall",
                "description": "High-occupancy refuge zone.",
                "orientation": "sidewall",
                "occupancy_weight": 1.0,
                "layers": [
                    {
                        "name": "Outer survivability shell",
                        "role": "baseline_candidate",
                        "g_cm2": 2.0,
                        "notes": "Placeholder.",
                        "source_ids": ["S-07"],
                        "threat_class": "GCR+SPE",
                        "material_family": "structural_shell",
                    },
                    {
                        "name": "Water-equivalent chamber annulus",
                        "role": "baseline_candidate",
                        "g_cm2": 10.0,
                        "notes": "Hydrogen-rich local mass.",
                        "source_ids": ["S-07"],
                        "threat_class": "SPE",
                        "material_family": "water_equivalent",
                    },
                ],
            }
        ],
    }


def test_load_json_reads_object(tmp_path: Path) -> None:
    config_path = tmp_path / "config.json"
    payload = _base_config()
    _write_json(config_path, payload)

    loaded = load_json(config_path)

    assert loaded["repo"] == "IX-GCR-SPE"
    assert loaded["configuration"] == "test_config"


def test_valid_config_has_no_errors() -> None:
    issues = validate_config(_base_config())
    errors = [issue for issue in issues if issue.severity == "error"]

    assert errors == []


def test_missing_schema_version_emits_warning_only() -> None:
    payload = _base_config()
    payload.pop("schema_version")

    issues = validate_config(payload)
    warnings = [issue for issue in issues if issue.severity == "warning"]
    errors = [issue for issue in issues if issue.severity == "error"]

    assert any(issue.location == "schema_version" for issue in warnings)
    assert errors == []


def test_duplicate_zone_name_is_error() -> None:
    payload = _base_config()
    payload["zones"].append(
        {
            "name": "Shadow Vault sidewall",
            "description": "Duplicate zone name.",
            "layers": [
                {
                    "name": "Crew-side low-Z liner",
                    "role": "baseline_candidate",
                    "g_cm2": 1.0,
                    "notes": "Duplicate-zone test layer.",
                }
            ],
        }
    )

    issues = validate_config(payload)

    assert any(
        issue.severity == "error" and "Duplicate zone name" in issue.message
        for issue in issues
    )


def test_unknown_role_is_error() -> None:
    payload = _base_config()
    payload["zones"][0]["layers"][0]["role"] = "hero_material"

    issues = validate_config(payload)

    assert any(
        issue.severity == "error" and issue.location.endswith(".role")
        for issue in issues
    )


def test_negative_g_cm2_is_error() -> None:
    payload = _base_config()
    payload["zones"][0]["layers"][0]["g_cm2"] = -2.0

    issues = validate_config(payload)

    assert any(
        issue.severity == "error" and issue.location.endswith(".g_cm2")
        for issue in issues
    )


def test_duplicate_layer_name_in_same_zone_is_warning() -> None:
    payload = _base_config()
    payload["zones"][0]["layers"].append(
        {
            "name": "Outer survivability shell",
            "role": "baseline_candidate",
            "g_cm2": 1.0,
            "notes": "Intentional duplicate name.",
        }
    )

    issues = validate_config(payload)

    assert any(
        issue.severity == "warning" and "Duplicate layer name" in issue.message
        for issue in issues
    )


def test_invalid_orientation_is_error() -> None:
    payload = _base_config()
    payload["zones"][0]["orientation"] = "port_bow"

    issues = validate_config(payload)

    assert any(
        issue.severity == "error" and issue.location.endswith(".orientation")
        for issue in issues
    )


def test_invalid_source_id_is_error() -> None:
    payload = _base_config()
    payload["zones"][0]["layers"][0]["source_ids"] = ["NASA-7"]

    issues = validate_config(payload)

    assert any(
        issue.severity == "error" and ".source_ids[" in issue.location
        for issue in issues
    )
