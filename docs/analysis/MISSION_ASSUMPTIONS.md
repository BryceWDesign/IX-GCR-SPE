# Mission Assumptions

This document makes the current-stage assumptions explicit so that future
modeling and review do not smuggle hidden conditions into the repo.

## 1. Purpose

IX-GCR-SPE is a concept-stage architecture repository. It is not tied to one
specific flight program, vehicle, or mission approval path.

The assumptions below exist to:
- keep trade studies comparable,
- prevent accidental overclaiming,
- make branch-to-branch review auditable.

## 2. Current baseline assumption set

### A-01 — Mission class
The default mental model is a **crewed deep-space transit / habitation mission**
where free-space radiation protection matters more than terrestrial launch,
LEO-only operations, or fully buried surface habitats.

### A-02 — Threats are separated
The repository treats:
- **GCR** as the chronic background threat,
- **SPE / SEP** as the acute sheltering threat,
- **secondary-particle production** as a first-class design concern.

Any future performance discussion must state which threat class is being discussed.

### A-03 — Shelter-first architecture
The best-protected volume is assumed to be a **small internal Shadow Vault**
rather than a uniformly hardened full cabin.

### A-04 — Occupancy matters
The most protected zone is assumed to be:
- highly occupied during sleep/rest,
- rapidly occupiable during SPE alerts,
- usable as a command refuge during high-radiation conditions.

### A-05 — Passive baseline survives active loss
If a magnetic augmentation branch is present, the architecture still assumes the
crew retains a meaningful passive protection posture when the field is absent.

### A-06 — The geometry is not yet CAD-complete
Current zone definitions are bookkeeping and architecture abstractions.
They are not final CAD, final vehicle packaging, or final structural layouts.

### A-07 — Hatch and penetration weakness are real
Any geometry discussion is assumed to include non-ideal features such as:
- hatches,
- penetrations,
- seams,
- corners,
- local standoff gaps.

A “perfectly continuous wall” assumption is not accepted as baseline truth.

### A-08 — Fill state can drift
Water-equivalent chambers, cryogenic hydrogen, hydride modules, or other retained
mass are assumed to be vulnerable to:
- leak onset,
- partial depletion,
- trapped gas,
- uneven distribution,
- thermal or structural degradation.

### A-09 — Shield state must be observable
The architecture assumes that protection confidence depends on knowing whether
the shielding mass is still where the crew thinks it is.

### A-10 — Timing and orientation matter
The environment is assumed to be sensitive to:
- solar-cycle timing,
- event timing,
- vehicle orientation,
- asymmetric mass placement,
- crew location inside the vehicle.

## 3. What is intentionally not assumed

The repo does **not** assume:
- literal 100 percent GCR protection in free space,
- a fully isotropic environment with no directional sensitivity,
- perfect mass retention forever,
- perfectly benign cryogenic operations,
- that thick shielding automatically improves the mixed field,
- that absorbed dose alone is enough to judge crew protection,
- that public patents equal validated hardware.

## 4. Baseline material assumptions

### M-01 — Low-Z and hydrogen-rich materials lead
The baseline assumes hydrogen-rich, low-Z material systems remain the most
credible passive direction for crew shielding in practical spacecraft mass ranges.

### M-02 — Graded stacks beat monolithic hype
The repo assumes that a layered stack with role separation is more credible than
a single “hero material” marketed as the whole answer.

### M-03 — Diamond is not baseline bulk shielding
Diamond is assumed to be valuable mainly in:
- sensing,
- dosimetry,
- detector roles,
- specialty wear roles.

It is not assumed to be the primary bulk crew-shield answer.

## 5. Baseline operational assumptions

### O-01 — SPE response includes movement
Acute event protection is assumed to depend partly on operational response:
- alert reception,
- crew relocation,
- hatch control,
- mass placement,
- time inside the Shadow Vault.

### O-02 — Unknown state escalates caution
If protection state is unknown, the supervisory posture should move upward toward
advisory, shelter preparation, or degraded logic rather than reporting nominal.

### O-03 — EVA remains less protected
The repo assumes that EVA exposure remains much less protected than interior
Shadow Vault occupancy and therefore requires stricter abort / shelter logic.

## 6. Modeling assumptions for current-stage trade studies

Until replaced by a more specific scenario package, initial model comparisons
should preserve the following discipline:

1. compare branch to branch using the same geometry logic,
2. separate GCR and SPE scenarios,
3. record the assumed occupied zone,
4. record whether hatches and weak zones are explicitly modeled,
5. record whether the active field is on or off,
6. record what degradation state, if any, is being tested.

## 7. Rule for future edits

Any new branch, model, or result package that changes a major assumption must:
- state the changed assumption explicitly,
- identify why the old assumption is no longer adequate,
- note whether prior results are still comparable.
