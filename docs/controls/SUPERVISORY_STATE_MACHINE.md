# Supervisory State Machine

IX-GCR-SPE treats operations as part of shielding.

## States

### 1. Standby
Vehicle power-up, calibration, or inactive mission phase.
No protection performance claim beyond static passive configuration.

### 2. Nominal
Conditions:
- shield state known,
- no alerting event,
- passive architecture intact,
- dosimetry normal.

### 3. Advisory
Trigger examples:
- rising external event risk,
- stale forecast feed,
- directional hotspot,
- minor shield-state uncertainty.

Crew actions:
- reduce nonessential exposure,
- verify vault readiness,
- confirm hatch and shield-zone status.

### 4. Shelter Preparation
Trigger examples:
- elevated SPE likelihood,
- warning from space-weather stream,
- vault configuration incomplete,
- active augmentation precharge needed.

Crew actions:
- reconfigure local mass,
- move crew-essential equipment to vault,
- confirm protection map.

### 5. Shelter Active
Trigger examples:
- SPE event in progress,
- event threshold crossed,
- crew refuge required.

Crew actions:
- occupy Shadow Vault,
- minimize hatch cycles,
- maintain shield state awareness.

### 6. Degraded Protection
Trigger examples:
- partial chamber depletion,
- hatch-path compromise,
- sensor blindness in one zone,
- active field unavailable but passive shielding retained.

Crew actions:
- use best remaining protected volume,
- re-evaluate occupancy and mission timeline,
- update dose forecast.

### 7. Compromised Vault
Trigger examples:
- vault boundary breach,
- severe fill loss,
- unrecoverable monitoring uncertainty.

Crew actions:
- transition to contingency posture,
- preserve crew in highest remaining areal-density shadow,
- initiate emergency mission review.

### 8. Recovery and Review
Trigger examples:
- event ends,
- shield state re-verified,
- dosimetry and anomaly log available.

## Design rule
Unknown is not healthy. Unknown pushes the state machine upward, not downward.
