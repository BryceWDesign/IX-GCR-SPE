# Layer Stack Baseline

This document describes the current baseline stack. Thicknesses and areal
densities are tracked in the config files and BOM as illustrative concept
values only unless explicitly sourced.

## Baseline order: outside to inside

### 1. Outer survivability / MMOD / thermal shell
Candidate materials:
- spacecraft structural shell,
- non-heroic thermal protection and survivability materials,
- specialty wear surfaces as needed.

Purpose:
- take the ordinary environmental beating so the shield layers can focus on
  radiation and retained mass.

### 2. Chambered hydrogen-rich annulus
Candidate materials:
- water cells,
- retained-water or water-equivalent chambers,
- polyethylene-family structural shield volume.

Purpose:
- main passive SPE and general low-Z shielding contribution,
- reconfigurable useful mass around the Shadow Vault.

### 3. Aggressive branch insert volume
Candidate materials:
- cryogenic hydrogen vessels,
- encapsulated lithium-hydride or other hydride modules,
- additional local hydrogen-rich slabs near the most occupied sides.

Purpose:
- push local areal density harder where the crew spends critical time.

### 4. Graded boron/nitrogen-aware cleanup layer
Candidate materials:
- boron-bearing polymer composite,
- BNNT-aware low-Z structural insert,
- inner neutron-conscious transition layer.

Purpose:
- reduce secondary management blind spots,
- avoid handing the inner wall a dirtier mixed field than necessary.

### 5. Crew-side low-Z liner
Candidate materials:
- UHMWPE,
- polyethylene-family liner,
- hatch-path shielding inserts.

Purpose:
- crew-facing final passive boundary,
- compatible with the interior and monitored access paths.

### 6. Shadow Vault interior shell
Functions:
- pressure and habitability boundary,
- most protected local refuge,
- command / sleep refuge during events.

## Weak-zone rules

Every layer stack review must answer:
- what happens at the hatch,
- what happens at penetrations,
- what happens at corners and joints,
- what happens if one chamber loses fill.

## What is intentionally not baseline

- thick high-Z bulk shielding
- diamond bulk layers
- vehicle-wide superconducting shield
- uncontrolled dynamic slosh without state awareness
