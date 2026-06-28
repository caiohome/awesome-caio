---
name: pii-redaction-gate
description: Use when text containing personal names, national IDs, phone numbers, account/card numbers, addresses, health/PHI data, or sensitive contract terms is about to be sent to any model, tool, or log. Triggers include processing customer records, support tickets, medical notes, HR data, or any free text from an untrusted boundary. Fail closed if the redaction service is unavailable.
---

# PII / PHI Redaction Gate (fail-closed, on-prem)

## Overview

A gate that sits **before** the model and **before** the log. Detect sensitive entities with an on-prem detector ([Presidio](https://github.com/microsoft/presidio)), replace them with stable placeholders, then let the redacted text proceed. If the detector is unreachable, **block the operation** — never let raw PII through because a service was down. Fail closed, not open.

Runs entirely on the LAN. No external classifier, no cloud DLP.

## When to use

- Before sending user/customer text to *any* model (even a local one — logs and traces leak too).
- Before writing free text to logs, traces, or analytics.
- Ingesting support tickets, EMR/EHR notes, KYC documents, HR records.

**Do NOT skip** because "it's just a local model" — observability, prompt caches and crash dumps all persist raw input.

## The pattern — detect, redact, gate

1. **Detect** entities via the on-prem analyzer (`PERSON`, `ID`, `PHONE`, `CREDIT_CARD`, `EMAIL`, `LOCATION`, `MEDICAL_*`, plus your custom recognizers).
2. **Redact** each span to a typed, stable token: `<PERSON_1>`, `<ID_1>`. Stable within a request so references stay coherent.
3. **Gate**: only the redacted text moves downstream. Keep the entity map in memory **only** if re-identification is needed for the final user-facing reply, and never log the map.
4. **Fail closed**: detector error / timeout → return a refusal, do not proceed.

## Quick reference

| Concern | Rule |
| --- | --- |
| Service | `POST http://dlp.internal:5001/analyze` then `/anonymize` (Presidio) |
| Threshold | redact at confidence ≥ `0.5`; tune per entity, err toward over-redaction |
| Unknown / low-confidence | treat as sensitive — redact |
| On error | **fail closed** — block, alert, do not send |
| Logging | log the redacted text only; never the entity map or raw input |

## Example

> **Raw:** "Patient 张伟 (ID 110101199003074471) called from 138-0013-8000 re: lab result."
>
> **Redacted (sent onward):** "Patient `<PERSON_1>` (ID `<ID_1>`) called from `<PHONE_1>` re: lab result."
>
> **Service down:** *"Redaction service unavailable — request blocked. Raw PII was not transmitted."*

## Common mistakes

- **Failing open.** "The DLP service timed out so I sent it anyway" is the exact breach this gate exists to prevent.
- **Logging the original.** Redacting the model input but logging the raw request defeats the gate. Redact first, then log.
- **Regex-only detection.** Names and addresses don't match clean patterns — use the model-based recognizers, not just regex.
- **Persisting the entity map.** Re-identify in memory for the reply if needed, then drop it. Never store it next to the redacted text.
