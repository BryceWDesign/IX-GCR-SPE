# Project Charter

## Project name
IX-GCR-SPE

## Mission
Create an original, traceable, technically serious repository for maximizing
astronaut radiation protection against GCR and SPE without pretending that
current technology solves free-space GCR completely.

## Primary objective
Define, compare, and verify a **Shadow Vault** crew-protection architecture
that concentrates the best available shielding where the crew spends the most
critical time.

## Secondary objectives
- integrate IX-Mirror’s shelter-first and chambered-mass logic,
- integrate AHIS-style shield integrity monitoring and degraded-mode behavior,
- evaluate passive-only and passive-plus-local-active branches,
- preserve a path to OLTARIS and Geant4 verification,
- keep source traceability explicit.

## Non-goals
- claiming 100 percent protection from deep-space GCR,
- presenting vehicle-wide active shielding as mature,
- presenting diamond as the primary bulk shield,
- copying any third-party patent implementation,
- declaring medical or mission approval outcomes.

## Engineering principles

### 1. Crew protection over aesthetic symmetry
Shield the crew zone hardest, not the vehicle prettiest.

### 2. Low-Z / hydrogen-rich first
Hydrogen-rich and low-atomic-mass materials dominate the baseline passive
posture.

### 3. Secondary particles are first-class design drivers
A shield that worsens the mixed field is not “stronger” just because it is thicker.

### 4. Unknown is not healthy
If shield state cannot be estimated, the vehicle shall not report nominal protection.

### 5. Claims are earned by transport and evidence
Modeling is required before stronger performance language appears.

### 6. Patent-aware, not patent-derived
Public patents are used to map directions and failure patterns. This repo does
not exist to paraphrase claims or create infringement bait.

## Deliverables at current stage
- architecture documents
- threat and requirement set
- BOM branches
- verification roadmap
- analysis helpers for shield budgeting
- source traceability map

## Success conditions at current stage
- the repo stays physically serious,
- the repo cleanly separates SPE and GCR logic,
- the repo identifies the strongest plausible architecture branch,
- the repo is readable by a technical reviewer without eye-rolling.
