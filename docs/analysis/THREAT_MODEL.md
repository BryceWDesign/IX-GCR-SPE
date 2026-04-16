# Threat Model

## 1. Radiation threats in scope

### 1.1 Galactic Cosmic Rays (GCR)
GCR is the chronic deep-space radiation problem. It includes high-energy ions,
including heavy ions, that are difficult to stop and can generate damaging
secondaries when they strike shielding.

Primary implications:
- bulk shielding helps only modestly in practical free-space mass ranges,
- material choice matters because high-Z strategies can worsen secondaries,
- geometry and occupied-zone placement matter heavily.

### 1.2 Solar Particle Events / Solar Energetic Particles (SPE / SEP)
SPE is the acute-event problem. It is operationally more actionable than GCR
because warning, sheltering, and reconfiguration can materially reduce dose.

Primary implications:
- storm shelter is mandatory architecture, not an afterthought,
- water-equivalent shielding is highly valuable,
- state transitions and alerting matter.

### 1.3 Secondary radiation field
Nuclear interactions in the shield can produce:
- neutrons,
- light ions,
- pions,
- gammas,
- electrons,
- positrons.

This means “more thickness” is not enough by itself. Secondary management must
be part of the stack and the verification plan.

## 2. Non-radiation threats that affect radiation protection

### 2.1 Cryogenic shield failure
Relevant if cryogenic hydrogen branch is used:
- boiloff,
- thermal leak,
- vessel breach,
- insulation degradation,
- hatch-path thinning,
- mass redistribution away from the occupied zone.

### 2.2 Water / hydride / retained-mass loss
Relevant to water-wall or hydride branches:
- leak onset,
- void formation,
- uneven fill,
- trapped gas,
- unmonitored partial depletion.

### 2.3 Superconducting active-augmentation failure
Relevant to local magnetic branch:
- quench,
- field collapse,
- stored-energy discharge,
- recovery delay,
- thermal burden,
- crew-zone electromagnetic compatibility limits.

### 2.4 Sensor and state-estimation failure
The crew can be harmed if the architecture reports nominal protection while:
- shield cells are depleted,
- hatch covers are open or misaligned,
- dosimetry is blind,
- forecast input is stale,
- state transitions fail.

### 2.5 Geometry weak zones
The worst regions are usually not the middle of the wall. They are:
- hatches,
- viewports,
- penetrations,
- feedthroughs,
- structural seams,
- corners,
- local standoff gaps,
- active-field openings.

## 3. Environmental and mission-context threats

### 3.1 Solar-cycle timing
Mission timing changes the background risk. Deep-space transit during solar
maximum can reduce GCR exposure relative to solar minimum, but SPE management
still remains necessary.

### 3.2 Vehicle attitude and directional environment
Direction matters. Orientation can change effective protection because the
particle environment is not always isotropic and because the vehicle itself is
not uniformly shielded.

### 3.3 EVA exposure
EVA remains much less protected than interior sheltering. Event detection,
forecast awareness, abort timelines, and access to shelter become critical.

## 4. Out-of-scope threats unless later added

- biological countermeasure efficacy claims,
- pharmaceutical mitigations,
- propulsion-system-specific mission radiation budgets,
- crew career-risk acceptance policy,
- classified or export-controlled shielding concepts.

## 5. Design consequences of this threat model

1. The architecture must separate SPE and GCR logic.
2. The best-protected zone must be physically small and highly occupied.
3. Shield fill state must be monitored.
4. Hatch and penetration design must be first-class.
5. Modeling must treat secondaries explicitly.
6. Active augmentation must degrade gracefully to a survivable passive baseline.
