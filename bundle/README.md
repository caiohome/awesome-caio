# 🔒 The Air-gap Bundle — a self-carried Skill + MCP + Agent starter kit

> 企业自带的「局域网可落地」起步库：Skill 包、MCP 清单、Agent 定义与一套离线参考栈。
> A **stage-once, run-with-zero-egress** starter library a CAIO can copy behind the firewall.

This directory is the concrete companion to [§15 · The Air-gap Bundle](../README.md#15--private--xinchuang--edge-deployment) in the list. The list tells you *which* OSS to pull; this kit gives you **real files to adapt** so an internal team is not starting from a blank page.

Everything here is **vendor-neutral and LAN-safe**: no template makes an external network call at runtime. Adapt the placeholders (`kb.internal`, `gw.internal`, …) to your own intranet hosts.

## What's inside

| Path | What it is | Covers |
| --- | --- | --- |
| [`skills/`](skills/) | Three production-shaped `SKILL.md` packages (Agent Skills format) | Skill registry & governance |
| [`mcp/`](mcp/) | An internal, gatewayed MCP server manifest + run/audit notes | MCP gateway & audit |
| [`agents/`](agents/) | Two agent definitions wired to the skills + internal MCP | Self-hosted agent platform |
| [`stack/`](stack/) | An offline reference `docker-compose` (model + RAG + gateway + UI) | Offline model + RAG base |

Each maps to one of the four capability areas a CAIO needs to self-host behind a LAN. Publish the `skills/` packages into a self-hosted registry ([SkillHub](https://github.com/iflytek/skillhub)) and route the `mcp/` servers through an on-prem gateway ([MCP Gateway](https://github.com/microsoft/mcp-gateway) / [ContextForge](https://github.com/IBM/mcp-context-forge)).

## The doctrine — stage once, run with zero egress

Air-gap is not "no internet ever" — it is "**no internet at runtime**". The whole bundle assumes two phases:

1. **Stage (on a connected host).** Pull container images, model weights, embedding/rerank models, and skill packages. Mirror them into your internal registry / artifact store. Pin every digest.
2. **Transfer & run (on the LAN).** Move artifacts across approved media, then run with **outbound egress denied** at the network policy. Nothing in this kit needs to phone home.

## Hardening checklist — before you trust it on a real network

- [ ] **Egress-deny by default.** Network policy blocks outbound; allow internal hosts only.
- [ ] **Telemetry off.** Set `ANONYMIZED_TELEMETRY=false` and `DO_NOT_TRACK=1` (Open WebUI / AnythingLLM / Langflow all ship telemetry on-by-default with an opt-out).
- [ ] **MCP behind a gateway.** No agent talks to an MCP server directly — route through the gateway for auth, RBAC and an audit trail.
- [ ] **Fail closed on the redaction gate.** If [`pii-redaction-gate`](skills/pii-redaction-gate/SKILL.md)'s service is down, block the call — never send raw PII/PHI to a model or a log.
- [ ] **Secrets via env / secret-manager.** Never hardcode keys in these files; the placeholders use `${VAR}` for exactly this reason.
- [ ] **License & SBOM review.** Confirm each referenced tool's license against your policy. ⚠️ **Open WebUI** ships a *custom* license (BSD-3 + a branding clause that restricts white-labeling above 50 users) — legal review before rebranding.
- [ ] **Pin digests.** Replace every `:latest` / version tag with an immutable digest captured at staging.

## License

These template files are released under **CC BY 4.0** (same as the [repo](../LICENSE)) — copy, adapt and ship them internally. Each *referenced* tool keeps its own upstream license; see the tags in the [main list](../README.md). Tags are decision aids, not legal advice — your legal/security review is final.
