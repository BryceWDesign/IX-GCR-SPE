# Evidence Package Template

Use this template for any future result package placed under `results/`.

---

## 1. Package identity

- **Package ID:**  
- **Date generated:**  
- **Author / reviewer:**  
- **Repository version or commit:**  
- **Related configuration file(s):**  

## 2. Objective

State exactly what this package is trying to answer.

Examples:
- compare clean baseline vs baseline-plus-cleanup branch,
- compare passive baseline vs extreme branch for a reference SPE case,
- inspect hatch-path weakness under partial depletion,
- inspect field-on vs field-off local augmentation deltas.

## 3. Threat class

Mark one:
- GCR
- SPE / SEP
- mixed-field secondary study
- operational / degraded-state study

## 4. Assumption set

Record all load-bearing assumptions.

### 4.1 Mission assumptions
- mission class:
- mission duration assumption:
- solar-cycle assumption:
- crew occupancy assumption:
- EVA assumption if relevant:

### 4.2 Geometry assumptions
- vault geometry summary:
- hatch / penetration treatment:
- whether corners and seams are explicit:
- whether area scaling is illustrative or geometric:

### 4.3 Material assumptions
- materials included:
- areal densities used:
- whether values are literature-derived, modeled, or illustrative:
- cryogenic or hydride containment assumptions if applicable:

### 4.4 Operational assumptions
- event warning time:
- time to crew shelter:
- hatch cycle assumptions:
- field-on / field-off state if applicable:

## 5. Tooling and methods

- **Primary tool:** OLTARIS / Geant4 / bookkeeping / tabletop / other  
- **Tool version or access date:**  
- **Model type:** deterministic / Monte Carlo / architecture review / scenario review  
- **Any custom scripts used:**  

## 6. Inputs

List every major input used.

- configuration file(s):
- geometry notes:
- spectra or environment selection:
- phantom or dose scoring choice:
- scenario definition:
- degraded-state definition if used:

## 7. Outputs

Record outputs in a structured way.

### 7.1 Primary outputs
- dose-equivalent or effective-dose outputs:
- organ or phantom outputs if available:
- secondary-particle observations:
- zone or path deltas:
- field-on / field-off delta if applicable:

### 7.2 Supporting outputs
- plots:
- tables:
- raw files:
- logs:
- screenshots:

## 8. Pass / fail against objective

State whether the package met its own objective.

- **Pass / fail / partial**
- why:
- what remains uncertain:

## 9. Key interpretation

Write the shortest technically honest interpretation possible.

Examples:
- “The cleanup layer improved the modeled mixed field behind the sidewall in this simplified geometry, but hatch-path treatment still dominated local weakness.”
- “The extreme branch improved local shielding in the studied zone, but the result is too assumption-sensitive to justify stronger claims yet.”

## 10. Limitations

Required section. Be explicit.

Examples:
- simplified geometry,
- hatch omitted,
- no corner treatment,
- no uncertainty sweep,
- not a flight-like mass budget,
- no cryogenic failure modeling,
- absorbed-energy metric only,
- not directly comparable to prior package because assumptions changed.

## 11. Decision outcome

Choose one:
- keep branch as-is
- keep branch with caution
- revise branch
- demote branch
- kill branch
- insufficient evidence

## 12. Follow-on work

List the next highest-value step only.

Examples:
- add hatch-path geometry,
- run degraded fill-state case,
- compare sidewall vs endcap sensitivity,
- add uncertainty sweep,
- repeat using phantom-based scoring.

---

## Minimum artifact rule

A result package is not complete unless it includes:
1. the objective,
2. the assumptions,
3. the exact inputs,
4. the outputs,
5. the limitations,
6. the decision outcome.
