# Architecture Overview

IX-GCR-SPE is built around one brutal design decision:

**Protect a small crew Shadow Vault extremely well, and treat the rest of the
vehicle as a less-protected support envelope.**

## 1. Top-level subsystems

### A. Outer survivability shell
Functions:
- MMOD and general structural survivability,
- thermal and environmental boundary,
- first structural interface for the shield package.

### B. Bulk hydrogen-rich shield annulus
Candidate implementations:
- water / water-equivalent chambers,
- polyethylene / UHMWPE structural volume,
- cryogenic hydrogen annulus in aggressive branch,
- modular hydride cartridges in aggressive branch.

### C. Graded secondary-management layer
Candidate implementations:
- boron-bearing composite transitions,
- BNNT-aware structural layers,
- inner neutron-conscious cleanup panels.

### D. Crew-side low-Z liner
Functions:
- final passive low-Z boundary,
- hatch cover and local weak-zone treatment,
- compatible interior-facing layer around the vault.

### E. Shadow Vault
Functions:
- sleep,
- storm shelter,
- high-occupancy command and refuge,
- most protected dosimetry zone.

### F. Shield health monitoring and dosimetry
Functions:
- fill-state awareness,
- leak / void detection,
- hatch-path status,
- dosimeter trending,
- directional alerting,
- degraded-state declaration.

### G. Optional local active magnetic augmentation
Functions:
- provide bounded charged-particle deflection around the Shadow Vault,
- only as an optional branch,
- never as the sole line of protection.

## 2. Why the Shadow Vault is central

The strongest public signal in this field is not “find the miracle wall.”
It is:
- use hydrogen-rich, low-Z materials,
- place mass intelligently,
- create a storm shelter,
- use operations and alerting,
- stay honest about GCR.

The Shadow Vault turns that into a coherent vehicle logic.

## 3. Protection logic by threat

### 3.1 SPE logic
SPE is attacked by:
- alerting,
- reconfiguration,
- rapid occupancy of the Shadow Vault,
- thick local water-equivalent and hydrogen-rich shielding.

### 3.2 GCR logic
GCR is attacked by:
- low-Z and hydrogen-rich material selection,
- local concentration of useful mass,
- secondary-conscious graded layers,
- mission timing and occupancy strategy,
- optional local magnetic augmentation.

## 4. AHIS integration
AHIS contributes here as the nervous system, not the bulk shield.

AHIS-derived ideas retained:
- leak-onset awareness,
- weak-zone paranoia,
- degraded-mode state estimation,
- evidence-first monitoring,
- no “nominal” state without measurements.

## 5. The architecture does not depend on one branch

IX-GCR-SPE is intentionally branchable:
- baseline passive branch,
- aggressive cryogenic hydrogen branch,
- aggressive hydride-enhanced branch,
- optional local active augmentation branch.

That keeps the repo useful even if one branch proves too ugly to carry.
