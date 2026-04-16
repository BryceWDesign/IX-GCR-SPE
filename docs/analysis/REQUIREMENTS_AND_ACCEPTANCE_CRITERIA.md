# Requirements and Acceptance Criteria

This document defines current-stage repository requirements. These are design
and evidence requirements, not flight certification requirements.

## RQ-001 — Source traceability
**Requirement:** Every substantive technical claim shall map to at least one
public source or be explicitly labeled as inference or hypothesis.

**Acceptance:** 100 percent of major claims in architecture and analysis docs
appear in `SOURCE_TRACEABILITY_MAP.md`.

## RQ-002 — SPE and GCR separation
**Requirement:** Every protection claim shall identify whether it applies to
GCR, SPE, or both.

**Acceptance:** No performance statement appears without threat-class tagging.

## RQ-003 — Shadow Vault first-class treatment
**Requirement:** The repository shall maintain a dedicated Shadow Vault concept
and not treat sheltering as a side note.

**Acceptance:** The vault appears in architecture, controls, BOM, and test docs.

## RQ-004 — Zone-based shield accounting
**Requirement:** Every shield concept branch shall be expressible by zone and
areal density.

**Acceptance:** Config files and analysis helpers can produce zone-level reports
without hidden parameters.

## RQ-005 — Shield health monitoring
**Requirement:** The architecture shall include means to detect or infer:
- loss of fill,
- leak onset,
- hatch-path degradation,
- sensor blindness,
- degraded protection state.

**Acceptance:** `SHIELD_HEALTH_MONITORING.md` and
`SUPERVISORY_STATE_MACHINE.md` define the signals and state transitions.

## RQ-006 — Passive survivability baseline
**Requirement:** If active augmentation fails, the crew shall still have a
passive survivability concept.

**Acceptance:** The Shadow Vault retains a passive shield stack independent of
magnetic field availability.

## RQ-007 — Active-augmentation discipline
**Requirement:** No active magnetic branch may be described without:
- quench handling,
- stored-energy awareness,
- EMI/EMC note,
- safe fallback state.

**Acceptance:** `ACTIVE_AUGMENTATION_SAFETY.md` exists and is referenced by the
architecture docs.

## RQ-008 — Weak-zone treatment
**Requirement:** Hatches, seams, corners, and penetrations must be explicitly
addressed.

**Acceptance:** Weak-zone treatment appears in architecture and risk docs.

## RQ-009 — Modeling path
**Requirement:** The repository shall define a path through OLTARIS and/or
Geant4 for verification.

**Acceptance:** `TRANSPORT_MODEL_PLAN.md` defines inputs, outputs, and comparison
branches.

## RQ-010 — No fake “100 percent” language
**Requirement:** The repository shall not claim literal 100 percent GCR
protection in free space.

**Acceptance:** `CLAIM_BOUNDARIES.md` prohibits it and no document contradicts it.

## RQ-011 — BOM labeling
**Requirement:** Every BOM item shall be labeled as one of:
- baseline candidate,
- aggressive branch,
- speculative branch,
- instrumentation.

**Acceptance:** `IX_GCR_SPE_Full_BillOfMaterials.md` uses those labels.

## RQ-012 — Analysis-script honesty
**Requirement:** Helper scripts may do mass and areal-density bookkeeping, but
shall not present unvalidated dose estimates as physics truth.

**Acceptance:** Script docstrings state their limited purpose.
