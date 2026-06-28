# Internal MCP — gatewayed, audited, LAN-only

[`servers.json`](servers.json) is an MCP client manifest for an air-gapped deployment. The rule it encodes: **no agent talks to an MCP server directly — every call goes through the gateway.** The gateway is where auth, RBAC, rate-limiting, timeouts and the audit trail live. Without it you have tools but no governance.

## The shape

```
agent ──▶ MCP gateway (gw.internal) ──▶ knowledge-base server ──▶ Milvus/RAGFlow
              │  auth · RBAC · audit · timeout         filesystem-readonly (stdio)
              └──────────────────────────────────────▶ ticketing server
```

Pick one gateway and stand it up first:

- **[MCP Gateway (Microsoft)](https://github.com/microsoft/mcp-gateway)** — K8s control plane, OAuth2 / Entra ID + RBAC, session-aware routing. The natural fit for Azure/K8s shops.
- **[ContextForge (IBM)](https://github.com/IBM/mcp-context-forge)** — Apache-2.0 registry + proxy for MCP/A2A/REST; ships an air-gapped container build.
- **[MCP Gateway (lasso-security)](https://github.com/lasso-security/mcp-gateway)** + **[mcpo](https://github.com/open-webui/mcpo)** — lightweight gateway / OpenAPI bridge.

## Rules baked into the manifest

| Rule | Why |
| --- | --- |
| All HTTP servers point at `gw.internal`, not the backend | one front door = one audit log, one auth point |
| Auth via `${MCP_GATEWAY_TOKEN}` from a secret-manager | no tokens in files or git history |
| Minimal scopes (`kb:read`, `tickets:comment`, no delete) | least privilege; an over-scoped tool is a standing risk |
| `filesystem` is `--read-only` and `--root`-confined | a tool that can write anywhere is an incident waiting |

## Hardening

- [ ] Enable the gateway's **audit log** and ship it to your SIEM — every tool call, who, what, when.
- [ ] Set a **per-call timeout** at the gateway (a hung MCP call silently consumes the whole agent — see [`incident-runbook`](../skills/incident-runbook/SKILL.md)).
- [ ] Bind gateway and servers to internal interfaces only; **deny outbound egress**.
- [ ] Review each server's scopes against the calling agent's role — don't grant write where read suffices.
- [ ] For a governed, versioned catalog of *internal* MCP servers, front this with a private registry ([Archestra](https://github.com/archestra-ai/archestra) / ContextForge).
