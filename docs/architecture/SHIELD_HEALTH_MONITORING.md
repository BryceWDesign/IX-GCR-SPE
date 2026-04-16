# Shield Health Monitoring

This document is where AHIS contributes most directly to IX-GCR-SPE.

## 1. Objective

Ensure that the shield the crew believes exists is the shield that actually
exists right now.

## 2. Why this matters

Radiation architecture can fail silently through:
- depleted water tanks,
- voided chambers,
- cryogenic boiloff,
- hatch-path misconfiguration,
- sensor blindness,
- unreported state loss.

A weaker shield with honest state reporting can be safer than a stronger shield
that lies.

## 3. Monitored quantities

### 3.1 Passive shield state
- chamber fill level,
- tank pressure,
- mass distribution,
- temperature,
- leak-rate indicators,
- valve and isolation state.

### 3.2 Structural boundary health
- seam integrity indicators,
- hatch closure confirmation,
- bondline or attachment anomaly indicators,
- penetration path status.

### 3.3 Radiation awareness
- internal dosimetry trend,
- local hotspot identification,
- event onset indicators,
- forecast / alert freshness.

### 3.4 Active branch state
- coil current,
- temperature,
- quench detection,
- field-available flag,
- safe fallback timer.

## 4. Instrumentation philosophy

Use mixed instrumentation, not material dogma:
- pressure sensors,
- temperature sensors,
- mass / level estimation,
- strain or seam-state indicators,
- dosimeters,
- optional diamond detector tiles for fast particle instrumentation.

## 5. State-estimation outputs

The monitoring layer should be able to produce:
- shield zone nominal / degraded / compromised state,
- predicted local areal-density shortfall,
- vault-entry recommendation,
- active-augmentation availability state,
- confidence score for the protection map.

## 6. Operational rule

If the monitoring layer cannot estimate shield state with confidence,
the vehicle shall not report **Nominal Protection**.
