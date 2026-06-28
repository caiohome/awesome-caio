# Offline reference stack

[`docker-compose.air-gap.yml`](docker-compose.air-gap.yml) wires the minimum coherent air-gap stack:

| Service | Role | List entry |
| --- | --- | --- |
| `ollama` | offline model serving | [Ollama](../../README.md#15--private--xinchuang--edge-deployment) (swap → vLLM / Xinference for scale / 信创) |
| `vectordb` | vector store (lowest ops) | [pgvector](../../README.md#10--rag--knowledge-base--data-processing) (swap → Milvus at scale) |
| `mcp-gateway` | the single front door for tools | [ContextForge](../../README.md#09--mcp--tools--skills) / [MCP Gateway](https://github.com/microsoft/mcp-gateway) |
| `open-webui` | chat + RAG UI | Open WebUI (⚠️ custom license) |

It is a **reference skeleton** — the value is the topology and the air-gap defaults (internal network, telemetry off, secrets via env, digests at staging), not a one-command production deploy.

## Stage → transfer → run

1. **Stage** (connected host): pull every image, mirror to `registry.internal`, capture `@sha256` digests, and pre-pull model weights into the `ollama-models` volume.
2. **Pin**: replace each `:tag` with the captured digest in the compose file.
3. **Transfer** artifacts across approved media to the LAN.
4. **Run** with outbound egress denied: `docker compose -f docker-compose.air-gap.yml up -d`.
5. **Register** the [`../mcp/servers.json`](../mcp/servers.json) servers with the gateway, and publish the [`../skills/`](../skills/) packages to your skill registry.

## Pre-pull list (adapt versions)

```
ollama/ollama            # + your model weights (e.g. qwen2.5, bge-m3, bge-reranker)
pgvector/pgvector:pg16
ibm/mcp-context-forge
open-webui/open-webui
```

## Don't skip

- **Egress-deny** at the network policy — the compose's `internal: true` is a backstop, not a substitute.
- **Telemetry off** is set here; verify after upgrades (defaults can flip).
- **Heavier RAG** (deep PDF/table parsing): add [RAGFlow](../../README.md#10--rag--knowledge-base--data-processing) + [MinerU](../../README.md#10--rag--knowledge-base--data-processing) — out of scope for this minimal skeleton.
