# Test Matrix

This matrix covers current repository-level verification intent.

| Test ID | Objective | Tool / method | Output |
|---|---|---|---|
| T-DOC-001 | Validate claim traceability | Manual review | Updated traceability map |
| T-ZON-010 | Validate zone accounting | `areal_density_budget.py` | Zone mass / areal-density report |
| T-OLT-020 | Compare passive vault branches | OLTARIS | SPE and GCR screening results |
| T-G4-030 | Inspect secondaries behind baseline stack | Geant4 | Mixed-field spectra and dose outputs |
| T-G4-031 | Inspect hatch-path weakness | Geant4 | Dose delta for hatch variants |
| T-G4-032 | Inspect degraded fill state | Geant4 | Dose delta for partial depletion |
| T-OPS-040 | Validate state-machine triggers | Tabletop scenario review | Event transition log |
| T-SHM-050 | Validate shield-state observability | Architecture review and future bench planning | Signal list and failure coverage |
| T-ACT-060 | Bound active-augmentation branch | Desk study / future Geant4 coupling | Risk and benefit summary |
