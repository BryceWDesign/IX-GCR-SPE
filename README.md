# IX-GCR-SPE

A documentation-first, concept-stage aerospace engineering repository focused on a **Shadow Vault** architecture for improving astronaut radiation protection against **Galactic Cosmic Rays (GCR)** and **Solar Particle Events (SPE)** without pretending that current technology “solves” free-space GCR.

This repo is built around one central decision:

> **Protect a small, highly occupied internal refuge extremely well, and treat the rest of the vehicle as a less-protected support envelope.**

That refuge is the **Shadow Vault**.

---

## Current status

| Area | Status |
|---|---|
| Architecture framing | Present |
| Threat model | Present |
| Requirement set | Present |
| BOM/config branches | Present |
| Source traceability | Present, still expandable |
| Validation tooling | Present |
| Unit tests | Present |
| CI | Present |
| OLTARIS / Geant4 result packages | Planned, not yet published |
| Flight-readiness claim | Explicitly out of scope |

---

## What this repo is

IX-GCR-SPE is an original engineering package for exploring a bounded, technically serious radiation-protection direction that combines:

- a **small internal Shadow Vault** rather than a uniformly hardened full cabin,
- **hydrogen-rich, low-Z shielding** as the passive baseline,
- **graded secondary-conscious layers** as optional bounded enhancements,
- **shield health monitoring** so protection state is observable,
- an **optional local magnetic augmentation branch** around the refuge only,
- a verification path through **OLTARIS** and **Geant4**.

---

## What this repo is not

This repo is **not**:

- a claim of 100 percent GCR protection in free space,
- a flight-qualified hardware design,
- a medical or mission-certification package,
- a claim that thick shielding automatically fixes mixed-field problems,
- a claim that diamond is the primary bulk shield answer,
- a claim that vehicle-wide active shielding is mature enough to be the baseline.

---

## Core design posture

The repo keeps several hard rules in place:

1. **SPE and GCR are not the same problem.**  
   SPE is an acute sheltering and operations problem. GCR is a chronic mixed-field problem.

2. **Mass should protect crew, not empty air.**  
   A small heavily shielded refuge can use mass more intelligently than spreading the same mass across a larger cabin.

3. **Low-Z and hydrogen-rich materials lead the passive baseline.**  
   Water-equivalent media and polyethylene-family layers remain the main passive direction.

4. **Secondaries matter.**  
   More thickness is not automatically better. Material choice, stack order, and geometry matter.

5. **Unknown shield state is dangerous.**  
   If retained mass has drifted, leaked, boiled off, or become uncertain, the system should not report nominal protection.

6. **Active augmentation stays bounded.**  
   Local magnetic augmentation is retained only as an optional branch around the Shadow Vault, never as the sole line of protection.

---

## Repository structure

```text
IX-GCR-SPE/
├── .github/
│   ├── CODEOWNERS
│   └── workflows/
│       └── ci.yml
├── BOM/
│   └── IX_GCR_SPE_Full_BillOfMaterials.md
├── configs/
│   ├── bom_baseline_shadow_vault.json
│   ├── bom_baseline_plus_cleanup_shadow_vault.json
│   └── bom_extreme_shadow_vault.json
├── docs/
│   ├── analysis/
│   │   ├── MATERIALS_TRADE_STUDY_FRAMEWORK.md
│   │   ├── MISSION_ASSUMPTIONS.md
│   │   ├── PATENT_LANDSCAPE.md
│   │   ├── PUBLIC_REPO_LANDSCAPE.md
│   │   ├── REQUIREMENTS_AND_ACCEPTANCE_CRITERIA.md
│   │   ├── RISK_REGISTER.md
│   │   ├── SOURCE_TRACEABILITY_MAP.md
│   │   └── THREAT_MODEL.md
│   ├── architecture/
│   │   ├── ARCHITECTURE_OVERVIEW.md
│   │   ├── LAYER_STACK_BASELINE.md
│   │   ├── SHADOW_VAULT_CONCEPT.md
│   │   └── SHIELD_HEALTH_MONITORING.md
│   ├── controls/
│   │   ├── ACTIVE_AUGMENTATION_SAFETY.md
│   │   └── SUPERVISORY_STATE_MACHINE.md
│   ├── governance/
│   │   ├── CLAIM_BOUNDARIES.md
│   │   └── PROJECT_CHARTER.md
│   └── verification/
│       ├── EVIDENCE_PACKAGE_TEMPLATE.md
│       ├── TEST_MATRIX.md
│       ├── TRANSPORT_MODEL_PLAN.md
│       └── VERIFICATION_AND_MODELING_ROADMAP.md
├── results/
│   └── README.md
├── schemas/
│   └── ix_gcr_spe_config.schema.json
├── src/
│   └── analysis/
│       ├── README.md
│       ├── areal_density_budget.py
│       ├── validate_config.py
│       └── zone_report.py
├── tests/
│   ├── test_analysis_helpers.py
│   └── test_validate_config.py
├── .gitignore
├── CONTRIBUTING.md
├── NOTICE
├── SECURITY.md
└── pyproject.toml

Recommended reading order

If you want the fastest path through the repo:

docs/governance/PROJECT_CHARTER.md
docs/governance/CLAIM_BOUNDARIES.md
docs/analysis/THREAT_MODEL.md
docs/architecture/ARCHITECTURE_OVERVIEW.md
docs/architecture/SHADOW_VAULT_CONCEPT.md
docs/architecture/SHIELD_HEALTH_MONITORING.md
docs/analysis/MISSION_ASSUMPTIONS.md
docs/verification/TRANSPORT_MODEL_PLAN.md
configs/bom_baseline_shadow_vault.json
configs/bom_baseline_plus_cleanup_shadow_vault.json
configs/bom_extreme_shadow_vault.json
docs/analysis/SOURCE_TRACEABILITY_MAP.md
Configuration branches

This repo currently carries three main config branches:

1. Clean passive baseline

configs/bom_baseline_shadow_vault.json

Use this when you want the clearest non-hyped starting point:

structural shell,
water-equivalent mass,
PE/UHMWPE shielding,
no cleanup enhancement branch.
2. Baseline plus cleanup

configs/bom_baseline_plus_cleanup_shadow_vault.json

This keeps the baseline structure but adds a bounded:

boron/nitrogen-aware cleanup layer.

Use this branch when evaluating whether a secondary-conscious inner transition layer is worth carrying.

3. Extreme local branch

configs/bom_extreme_shadow_vault.json

This branch exists for aggressive comparison only:

cryogenic hydrogen annulus,
hydride enhancement,
stronger hatch-path treatment,
bounded aggressive local architecture.

This is not the default recommendation. It is a stress-test branch for trade studies.

Quick start

Validate a config
python src/analysis/validate_config.py configs/bom_baseline_shadow_vault.json

Create a JSON areal-density summary
python src/analysis/areal_density_budget.py configs/bom_baseline_shadow_vault.json

Write the JSON summary to a file
python src/analysis/areal_density_budget.py configs/bom_baseline_shadow_vault.json --output results/generated/baseline_summary.json

Create a plain-text zone report
python src/analysis/zone_report.py configs/bom_baseline_shadow_vault.json

Write the plain-text zone report to a file
python src/analysis/zone_report.py configs/bom_baseline_shadow_vault.json --output results/generated/baseline_report.txt

Run tests
pytest

What the Python helpers do

The helpers in src/analysis/ are intentionally modest.

validate_config.py

Checks that a BOM-style configuration is structurally and semantically sane:

required fields present,
roles valid,
positive g_cm2,
duplicate-zone detection,
duplicate-layer warnings,
optional metadata sanity checks.
areal_density_budget.py

Performs transparent zone-level areal-density bookkeeping.

It does not compute radiation dose.

zone_report.py

Builds a human-readable plain-text review report from a config file.

It is meant for design review readability, not physics.

Verification posture

This repo currently stops before pretending to have physics-validated mission results.

The intended evidence ladder is:

claim hygiene and traceability,
zone and stack bookkeeping,
OLTARIS branch screening,
Geant4 geometry and secondary studies,
degraded-state studies,
operational and shelter-timeline studies,
future hardware-relevant bench work.

That path is documented in:

docs/verification/VERIFICATION_AND_MODELING_ROADMAP.md
docs/verification/TRANSPORT_MODEL_PLAN.md
docs/verification/TEST_MATRIX.md
docs/verification/EVIDENCE_PACKAGE_TEMPLATE.md
Why engineers may care

The repo is trying to be useful in the narrow place where a lot of public discussion gets sloppy:

it does not confuse SPE sheltering with GCR suppression,
it does not assume a prettier full-cabin wall is automatically smarter,
it does not treat unknown shield state as acceptable,
it does not pretend active magnetic shielding is cheap or simple,
it does not market a miracle material,
it does try to make the trade space auditable.

The central engineering question here is not:

“What single wall material wins?”

It is:

“What bounded architecture most credibly improves crew protection where the crew actually is, while staying honest about failure modes, degraded states, and verification burden?”

Known limitations

Current limitations are real and intentional:

no published OLTARIS results yet,
no published Geant4 results yet,
no CAD-complete geometry,
no explicit mass-by-area geometry scaling yet,
no bench data yet,
no flight qualification,
no mission-specific acceptance analysis,
traceability map can still become more granular,
config schema exists but is not yet enforced by a separate schema engine in CI,
the current helper scripts are bookkeeping utilities, not physics engines.
Contribution expectations

Contributions should preserve the repo’s discipline.

Good contributions:

tighten traceability,
improve configuration clarity,
improve validation rigor,
improve weak-zone treatment,
improve result packaging,
improve modeling transparency.

Bad contributions:

unsupported shielding claims,
copied patent language,
“100 percent protection” phrasing,
mystery performance numbers,
miracle-material marketing.

See:

CONTRIBUTING.md
SECURITY.md
Results directory rule

Anything eventually placed into results/ should include:

objective,
assumptions,
exact inputs,
outputs,
limitations,
decision outcome.

Use:

docs/verification/EVIDENCE_PACKAGE_TEMPLATE.md
Bottom line

IX-GCR-SPE is a serious architecture repo, not a solved-physics repo.

Its value is in building a tighter, more auditable path toward answering whether a Shadow Vault-first, low-Z / hydrogen-rich, monitorable, and optionally locally augmented protection architecture is a smarter direction than pretending a uniform wall or a miracle material fixes deep-space radiation.

If that answer is going to be strong, it will be strong because the repo stays disciplined enough to earn it.
