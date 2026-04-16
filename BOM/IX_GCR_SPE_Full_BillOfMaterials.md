# IX-GCR-SPE Full Bill of Materials

**Important:** This is a concept-stage BOM. It is not procurement-ready and
does not imply flight qualification.

## 1. Baseline candidates

### 1.1 Outer survivability shell
- structural shell materials appropriate to the host vehicle
- MMOD / thermal protection layers as needed
- local specialty wear coating only where justified

### 1.2 Hydrogen-rich passive shielding
- water or water-equivalent chamber media
- polyethylene-family structural shielding panels
- UHMWPE liner components
- hatch and penetration low-Z inserts

### 1.3 Secondary-management branch
- boron-bearing polymer panels
- BNNT-aware low-Z composite inserts
- neutron-conscious inner transition panels

### 1.4 Shadow Vault interior
- compact refuge shell
- integrated sleeping / command accommodations
- low-Z interior-facing boundary panels

### 1.5 Shield health monitoring
- pressure sensors
- temperature sensors
- level / fill-state estimation hardware
- strain / seam-state sensing where useful
- internal dosimeters
- data-acquisition and logging hardware
- alerting interface

## 2. Aggressive branches

### 2.1 Cryogenic hydrogen branch
- annular cryogenic vessel
- toroidal end-cap cryogenic vessels
- insulation system
- thermal shield
- cryogenic plumbing and valve isolation
- boiloff and pressure instrumentation

### 2.2 Hydride branch
- encapsulated hydride cartridges
- modular carrier trays
- contamination / containment barrier
- thermal and compatibility hardware

### 2.3 Active augmentation branch
- superconducting coil set
- cryogenic support hardware
- current supply and protection electronics
- quench detection
- thermal rejection support
- structural restraint and field-safe support hardware

## 3. Instrumentation branch

### 3.1 Diamond detector lane
- diamond dosimeter or detector elements
- readout electronics
- calibration and mounting hardware

## 4. Labels used in config files
- `baseline_candidate`
- `aggressive_branch`
- `speculative_branch`
- `instrumentation`

## 5. Deliberate exclusions
- lead-heavy bulk crew shielding
- stacked diamond bulk wall concepts
- vehicle-wide mandatory active shield
- unsupported electrostatic or resonance shield hardware
