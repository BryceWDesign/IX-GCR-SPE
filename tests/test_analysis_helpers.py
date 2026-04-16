import json
from pathlib import Path

from src.analysis.areal_density_budget import load_config, summarize
from src.analysis.zone_report import build_report


def _sample_config() -> dict:
    return {
        "repo": "IX-GCR-SPE",
        "configuration": "baseline_shadow_vault",
        "schema_version": "1.0.0",
        "notes": [
            "Illustrative concept-stage values for bookkeeping only."
        ],
        "zones": [
            {
                "name": "Shadow Vault sidewall",
                "description": "High-occupancy refuge sidewall.",
                "layers": [
                    {
                        "name": "Outer survivability shell",
                        "role": "baseline_candidate",
                        "g_cm2": 2.0,
                        "notes": "Structural placeholder."
                    },
                    {
                        "name": "Water-equivalent chamber annulus",
                        "role": "baseline_candidate",
                        "g_cm2": 10.0,
                        "notes": "Hydrogen-rich local mass."
                    },
                    {
                        "name": "Crew-side low-Z liner",
                        "role": "baseline_candidate",
                        "g_cm2": 1.5,
                        "notes": "Crew-facing low-Z boundary."
                    }
                ]
            },
            {
                "name": "General vehicle habitable envelope",
                "description": "Lower-protection support envelope.",
                "layers": [
                    {
                        "name": "Vehicle shell",
                        "role": "baseline_candidate",
                        "g_cm2": 2.0,
                        "notes": "Structural shell placeholder."
                    },
                    {
                        "name": "Distributed hydrogen-rich mass",
                        "role": "baseline_candidate",
                        "g_cm2": 6.0,
                        "notes": "Distributed support protection."
                    }
                ]
            }
        ]
    }


def test_load_config_reads_json_file(tmp_path: Path) -> None:
    config_path = tmp_path / "config.json"
    config_path.write_text(json.dumps(_sample_config(), indent=2) + "\n", encoding="utf-8")

    loaded = load_config(config_path)

    assert loaded["repo"] == "IX-GCR-SPE"
    assert loaded["configuration"] == "baseline_shadow_vault"


def test_summarize_computes_zone_totals() -> None:
    summary = summarize(_sample_config())

    assert summary["repo"] == "IX-GCR-SPE"
    assert summary["configuration"] == "baseline_shadow_vault"
    assert summary["zone_count"] == 2
    assert summary["zones"][0]["zone"] == "Shadow Vault sidewall"
    assert summary["zones"][0]["total_g_cm2"] == 13.5
    assert summary["zones"][1]["zone"] == "General vehicle habitable envelope"
    assert summary["zones"][1]["total_g_cm2"] == 8.0
    assert summary["sum_of_zone_totals_g_cm2"] == 21.5


def test_summarize_preserves_layer_details() -> None:
    summary = summarize(_sample_config())

    first_zone_layers = summary["zones"][0]["layers"]

    assert first_zone_layers[0]["name"] == "Outer survivability shell"
    assert first_zone_layers[0]["role"] == "baseline_candidate"
    assert first_zone_layers[1]["g_cm2"] == 10.0
    assert first_zone_layers[2]["notes"] == "Crew-facing low-Z boundary."


def test_build_report_contains_key_sections() -> None:
    report = build_report(_sample_config())

    assert "Repository: IX-GCR-SPE" in report
    assert "Configuration: baseline_shadow_vault" in report
    assert "Zone: Shadow Vault sidewall" in report
    assert "Description: High-occupancy refuge sidewall." in report
    assert "- Water-equivalent chamber annulus: 10.000 g/cm^2 [baseline_candidate]" in report
    assert "Total: 13.500 g/cm^2" in report
    assert "Zone: General vehicle habitable envelope" in report
    assert "Notes:" in report


def test_build_report_ends_with_newline() -> None:
    report = build_report(_sample_config())

    assert report.endswith("\n")
