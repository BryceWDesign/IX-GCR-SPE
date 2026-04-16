# Public Repo Landscape

These public repositories and tools are relevant to IX-GCR-SPE. They are used
for orientation, not copied implementation.

## 1. Geant4
**Why it matters:** industry-standard open toolkit for particle transport
through matter and mixed-field interaction studies.

**Use in IX-GCR-SPE:** primary Monte Carlo path for later geometry and dose
comparison.

## 2. ICRP110_HumanPhantoms_GCR
**Why it matters:** example Geant4 application for simulating GCR effects on a
human phantom.

**Use in IX-GCR-SPE:** reference direction for human-phantom dose scoring and
geometry coupling.

## 3. radiation-shielding (john9francis)
**Why it matters:** small Geant4 application for varying material and thickness.

**Use in IX-GCR-SPE:** useful as a public example of how material-thickness
comparisons can be scaffolded without pretending to solve spacecraft geometry.

## 4. OLTARIS
**Why it matters:** NASA online radiation assessment environment using HZETRN.

**Use in IX-GCR-SPE:** fast initial screening before heavier Geant4 work.

## 5. What this repo will not do
- it will not vendor third-party code into the repository without license review,
- it will not repackage public repos as original work,
- it will not cite a public repo as proof of a mission-level shielding result.
