<div align="center">

# 🧭 Awesome Enterprise AI — the CAIO List

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-0aa8d2.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Website](https://img.shields.io/badge/🌐%20home-caiohome.com-6f42c1.svg)](https://www.caiohome.com)
[![Stars](https://img.shields.io/github/stars/caiohome/awesome-caio?style=flat&color=f5c518)](https://github.com/caiohome/awesome-caio/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/caiohome/awesome-caio?color=blue)](https://github.com/caiohome/awesome-caio/commits/main)
[![Contributors](https://img.shields.io/github/contributors/caiohome/awesome-caio?color=ff69b4)](https://github.com/caiohome/awesome-caio/graphs/contributors)

**An adoption-first index of open-source AI for the enterprise — curated through the eyes of a CAIO.**

*面向 CAIO（首席 AI 官 / AI 负责人）的「可引入性」开源索引。*
*Not the coolest projects — the ones you can actually bring into a company.*

[🌐 caiohome.com](https://www.caiohome.com) · [🏷️ Legend](#legend) · [🧱 Starter Stack](#reference-starter-stack) · [🗺️ Decision Chain](#the-caio-decision-chain) · [🗂️ Contents](#contents) · [🤝 Contribute](CONTRIBUTING.md)

</div>

---

> **The one question this list answers:**
> *"Can this open-source project be brought into my company — to which layer, used by whom, under what license, and at how much compliance risk?"*
>
> 本清单只回答一件事：**「这个开源项目能不能引入公司、引入到哪一层、谁来用、什么许可证、合规风险多大」**。
> Maintained by **CAIO之家 · [caiohome.com](https://www.caiohome.com)** — the home for Chief AI Officers.

Every other `awesome` list organizes by *technical category* or *research topic*, serving engineers and researchers. This one flips the axis: it is organized by the **CAIO adoption decision chain**, and every entry carries a set of **enterprise metadata tags**. Anyone can copy the entries — nobody can copy the *judgment*. That judgment is the only reason this list exists.

<details>
<summary><b>📖 Why another list? · 为什么再做一个清单</b></summary>

<br>

Awesome-LLM, Awesome-LLMOps, awesome-mcp-servers and friends are excellent — but they answer *"what exists?"*. A CAIO needs to answer *"what can I safely ship, and what will legal/security say?"* The market is full of 50k-star projects that no enterprise can touch (wrong license, no air-gap, single-vendor lock-in), and 800-star projects that are perfect to adopt.

So here the organizing principle is the **introduction decision** itself. A `🔴`-license 50k-star repo can be worth *less* to your company than a `🟢`-license 800-star one. Stars are not an inclusion criterion.

市面上的 awesome 清单按技术类别组织，服务工程师与研究者。本清单换一根轴 —— 按 **CAIO 的引入决策链** 分层，并要求每个条目挂一套企业元数据。抄条目容易，抄不走这套「引入判断」。

</details>

---

## Legend

> Tags are **decision aids, not endorsements.** Final adoption rests with your legal, compliance, and security review.
> 标签是判断辅助，不是背书。最终引入决策以公司法务、合规、安全评审为准。
>
> **License `🟢🟡🔴` and Maturity `⭐🧪👀` are required on every entry.** Other tags are best-effort.

| Axis | Values |
| --- | --- |
| **License · 许可证** | 🟢 **Permissive** — Apache-2.0 / MIT / BSD, commercial use out of the box · 🟡 **Conditional** — MPL / LGPL / model "community" licenses, commercial with strings (read the terms) · 🔴 **Restricted** — GPL / AGPL / RAIL / non-commercial / custom, **legal review mandatory** |
| **Maturity · 成熟度** | ⭐ **Production** — proven at scale, de-facto standard · 🧪 **Pilot** — engineering-complete, good for a 30–90 day trial · 👀 **Watch** — important direction, still moving, track before adopting |
| **Deployment · 部署** | 🏠 **Self-hostable** — on-prem / air-gap, data never leaves · ☁️ **Cloud-first** — private deploy is costly · 📱 **Edge** — runs on-device / edge box |
| **Origin · 来源** | 🇨🇳 **China-led** · 🌍 **Global / overseas-led** |
| **Compliance · 合规** | 🛡️ **Xinchuang-ready** — adapted to Ascend / domestic silicon · ⚠️ **Sensitive** — data-residency / privacy / needs medical-affairs or legal sign-off |

<details>
<summary><b>✅ Inclusion criteria · 收录标准</b></summary>

<br>

**Included** — must satisfy *all*:
1. **Open source** with a stated OSS license (and we note the license type).
2. **Enterprise-introducible** — real production or pilot value; not a demo / toy.
3. **Maps to a layer** of the CAIO decision chain (see Contents).
4. **Active or de-facto standard** — meaningful update in the last ~6 months, *or* already the standard in its niche.
5. **Metadata complete** — at minimum license + maturity.
6. **First-party first** — official org accounts beat personal forks beat second-hand aggregators.

**Not included / footnoted only:**
- Closed SaaS (unless it has an OSS core; commercial products appear only as "for comparison" notes).
- Pure academic repros with no engineering, unmaintained and without replacement value.
- Repos with unclear or contradictory licensing (until clarified).
- Hype forks / mirrors / marketing repos.

</details>

---

## The CAIO Decision Chain

> The figure the original notes referred to, drawn for real. Read it top→bottom: each layer is a place where a CAIO makes an *introduce / don't-introduce* call. The private/Xinchuang layer **underpins** everything when data residency is a hard constraint.

```mermaid
flowchart TB
    MOD["🧠 §01 Foundation<br/>open-weight models"]
    TRN["🏗️ §02–03 Train · Tune<br/>fine-tune · RL · kernels"]
    SRV["⚙️ §04–05 Serve · Schedule<br/>inference engines · orchestration"]
    GW["🚪 §06–07 Gateway · Context<br/>routing · keys · token efficiency"]
    APP["🤖 §08–10 · §12 Apps · Agents<br/>agents · RAG · MCP · auto-research"]
    GOV["🛡️ §11 Govern · Observe<br/>eval · tracing · guardrails"]
    INF["🏠 §13 Private · Xinchuang · Edge<br/>air-gap · Ascend · on-device"]
    HUB["🛰️ §14 Source · Host<br/>hubs · clouds · registries"]

    MOD --> TRN --> SRV --> GW --> APP --> GOV
    INF -. underpins .-> MOD
    INF -. underpins .-> SRV
    HUB -. supplies .-> MOD
```

---

## Reference Starter Stack

> 🧱 The list's strongest CAIO opinion: an **assembled, coherent open-source stack** you could actually pilot — not 150 disconnected links. Swap freely, but this is a sane default for a regulated/enterprise pilot with a multi-source model policy.

| Layer | Default pick (OSS) | Xinchuang / air-gap swap | Why |
| --- | --- | --- | --- |
| **Models** | `Qwen` + `DeepSeek` (+ `Llama` backup) | same (all self-hostable) | Multi-source: 2 China-led + 1 global backup |
| **Inference** | [vLLM](#04--inference-engines) | `vllm-ascend` | Throughput standard; Ascend backend exists |
| **Orchestration** | [Ray Serve](#05--compute-scheduling--serving-orchestration) / [llm-d](#05--compute-scheduling--serving-orchestration) | Ray Serve | Autoscaling, multi-model, K8s-native |
| **Gateway** | [LiteLLM](#06--gateway--routing--api--cost-governance) / [One-API](#06--gateway--routing--api--cost-governance) | One-API (self-host) | Keys · quota · billing · audit in one place |
| **Agents / Apps** | [LangGraph](#08--orchestration-frameworks--agents) + [Dify](#08--orchestration-frameworks--agents) | Dify (private) | Controllable, auditable orchestration |
| **RAG** | [RAGFlow](#10--rag--knowledge-base--data-processing) + [Milvus](#10--rag--knowledge-base--data-processing) + [BGE](#10--rag--knowledge-base--data-processing) + [MinerU](#10--rag--knowledge-base--data-processing) | same (all 🏠) | Parsing quality is the real RAG bottleneck |
| **Govern** | [Langfuse](#11--evaluation--observability--guardrails--governance) + [promptfoo](#11--evaluation--observability--guardrails--governance) + [NeMo Guardrails](#11--evaluation--observability--guardrails--governance) | Langfuse (self-host) | Without this layer, nothing is board-defensible |
| **Base** | [MindSpore / CANN](#13--private--xinchuang--edge-deployment) | — | Domestic training/inference stack |

---

## Contents

- [🏷️ Legend](#legend) · [🗺️ Decision Chain](#the-caio-decision-chain) · [🧱 Starter Stack](#reference-starter-stack)
- [01 · Foundation Models & Open Weights](#01--foundation-models--open-weights)
- [02 · Training / Fine-tuning / Post-training (incl. RL)](#02--training--fine-tuning--post-training-incl-rl)
- [03 · High-performance Kernels & Low-level Systems](#03--high-performance-kernels--low-level-systems)
- [04 · Inference Engines](#04--inference-engines)
- [05 · Compute Scheduling & Serving Orchestration](#05--compute-scheduling--serving-orchestration)
- [06 · Gateway / Routing / API & Cost Governance](#06--gateway--routing--api--cost-governance)
- [07 · Context Engineering & Token Efficiency](#07--context-engineering--token-efficiency)
- [08 · Orchestration Frameworks & Agents](#08--orchestration-frameworks--agents)
- [09 · MCP / Tools / Skills](#09--mcp--tools--skills)
- [10 · RAG / Knowledge Base / Data Processing](#10--rag--knowledge-base--data-processing)
- [11 · Evaluation / Observability / Guardrails / Governance](#11--evaluation--observability--guardrails--governance)
- [12 · Autonomous Research & Scientific Discovery](#12--autonomous-research--scientific-discovery)
- [13 · Private / Xinchuang / Edge Deployment](#13--private--xinchuang--edge-deployment)
- [14 · Platforms, Hubs & Registries — where CAIOs source & host](#14--platforms-hubs--registries--where-caios-source--host)
- [15 · Orgs & People to Follow (open-source account index)](#15--orgs--people-to-follow-open-source-account-index)
- [16 · Other Awesome Lists (meta-index)](#16--other-awesome-lists-meta-index)
- [🤝 Contributing](#contributing) · [⚖️ Disclaimer](#disclaimer)

> Each section below gives **representative anchor entries** that demonstrate the tagging format; full coverage is community-driven (see [Contributing](CONTRIBUTING.md)).

---

## 01 · Foundation Models & Open Weights

> **Adoption logic:** fix your base first. A *"2 China-led + 1 global/open backup"* multi-source policy hedges supply risk. **Weight licenses frequently differ from the code license — check each.**
> 引入逻辑：先定底座来源，注意权重许可证常与代码许可证不同。

- **DeepSeek** (`deepseek-ai`) 🇨🇳 ⭐ 🟢 — V/R-series open weights, mostly MIT. Strong reasoning & code.
- **Qwen** (`QwenLM`) 🇨🇳 ⭐ 🟢 — Full size range + multimodal, mostly Apache-2.0; the enterprise-friendly default.
- **GLM** (`zai-org` / `THUDM`) 🇨🇳 ⭐ 🟡 — GLM series; some versions carry usage terms — confirm before commercial use.
- **Kimi** (`moonshotai`) 🇨🇳 ⭐ 🟢 — Long-context & agentic models, open weights.
- **MiniMax** (`MiniMax-AI`) 🇨🇳 ⭐ 🟢 — Open-weight large models with long context.
- **MiniCPM** (`OpenBMB`) 🇨🇳 ⭐ 🟡 📱 — Edge-friendly small models.
- **Llama** (`meta-llama`) 🌍 ⭐ 🟡 — Llama Community License (includes an MAU-threshold clause); **not pure OSS**.
- **Mistral / Gemma / Phi** (`mistralai` / `google` / `microsoft`) 🌍 ⭐ 🟢🟡 — overseas open-weight reference points.

> ⚠️ Verify weight licenses one by one: Apache/MIT are commercial-safe; "community licenses" need legal to read the clauses (commercial caps, naming, acceptable-use).

## 02 · Training / Fine-tuning / Post-training (incl. RL)

> **Adoption logic:** 99% of enterprises do not pretrain. The action is in **fine-tuning** (domain adaptation) and **post-training / RL** (alignment + reasoning gains).
> 引入逻辑：重点是微调（领域适配）与后训练/RL（对齐与推理增强）。

**Distributed pretraining / large-scale training**
- **Megatron-LM** (`NVIDIA`) 🌍 ⭐ 🟢 — A de-facto standard for large-scale parallel training.
- **DeepSpeed** (`microsoft`) 🌍 ⭐ 🟢 — ZeRO optimization; memory & throughput.
- **NeMo** (`NVIDIA`) 🌍 ⭐ 🟢 — End-to-end training framework; 🛡️ evaluate on non-Ascend domestic chips.
- **ColossalAI** (`hpcaitech`) 🧪 🟢 — Parallel-training toolbox.
- **TorchTitan** (`pytorch`) 🧪 🟢 — PyTorch-native large-model training reference.

**Fine-tuning (most common)**
- **LLaMA-Factory** (`hiyouga`) 🇨🇳 ⭐ 🟢 🏠 — One-stop fine-tuning; the most widely deployed in China.
- **ms-swift** (`modelscope`) 🇨🇳 ⭐ 🟢 🏠 🛡️ — ModelScope training/tuning suite; good domestic-ecosystem fit.
- **Unsloth** (`unslothai`) 🌍 ⭐ 🟢 — Efficient single-GPU fine-tuning; saves VRAM.
- **Axolotl** (`axolotl-ai-cloud`) 🌍 ⭐ 🟢 — Config-driven fine-tuning.
- **TRL** (`huggingface`) 🌍 ⭐ 🟢 — HF post-training library (SFT / DPO / GRPO).

**RLHF / RL (the reasoning-boost hot zone)**
- **verl** (`volcengine` / `verl-project`) 🇨🇳 ⭐ 🟢 — ByteDance Seed's production-grade RL framework (HybridFlow).
- **OpenRLHF** (`OpenRLHF`) 🌍 ⭐ 🟢 — Early-popular, approachable RLHF library.
- **ROLL** (`alibaba`) 🇨🇳 🧪 🟢 — Alibaba large-scale RL framework.
- **AReaL** (`inclusionAI` / Ant) 🇨🇳 🧪 🟢 — Asynchronous RL, throughput-focused.
- **slime** (`THUDM`) 🇨🇳 🧪 🟢 — Zhipu/Tsinghua-lineage RL scaling.
- **NeMo-RL** (`NVIDIA`) 🌍 🧪 🟢 — NVIDIA post-training RL.
- **DAPO** (`BytedTsinghua-SIA`) 🇨🇳 👀 🟢 — ByteDance × Tsinghua open RL system/algorithm + dataset (built on verl).

**Learn from scratch (capability-building for your seed engineers)**
- **Karpathy** (`karpathy`) 🌍 ⭐ 🟢 — nanoGPT / llm.c / nanochat / micrograd / minGPT; the best "understand LLMs from zero" teaching code.

## 03 · High-performance Kernels & Low-level Systems

> **Adoption logic:** in-house teams need these; almost everyone else only *uses* them, never *edits* them. Understanding them is what lets you push inference/training cost down.
> 引入逻辑：绝大多数公司只「用」不「改」，但理解它们决定你能不能压低成本。

- **DeepSeek open-infra-index** (`deepseek-ai/open-infra-index`) 🇨🇳 ⭐ 🟢 — Index of **FlashMLA** (MLA decode kernel), **DeepEP** (MoE comm library), **DeepGEMM** (FP8 GEMM), **DualPipe** (bidirectional pipeline parallel), **3FS** (high-perf parallel filesystem). Production-validated, mostly MIT.
- **FlashAttention** (`Dao-AILab`) 🌍 ⭐ 🟢 — The attention-acceleration standard.
- **Triton** (`triton-lang`) 🌍 ⭐ 🟢 — Language for writing GPU kernels.
- **CUTLASS** (`NVIDIA`) 🌍 ⭐ 🟢 — CUDA matrix-op template library.
- **Liger-Kernel** (`linkedin`) 🌍 🧪 🟢 — Fused training kernels; saves VRAM.

## 04 · Inference Engines

> **Adoption logic:** this is the **main cost battleground.** Engine choice directly sets per-GPU throughput and concurrency cost.
> 引入逻辑：降本主战场，引擎选型直接决定单卡吞吐与并发成本。

- **vLLM** (`vllm-project`) 🌍 ⭐ 🟢 🏠 — High-throughput inference standard (PagedAttention); 🛡️ `vllm-ascend` Ascend fork exists.
- **SGLang** (`sgl-project`) 🌍 ⭐ 🟢 🏠 — High-performance serving; common for RAG / structured output.
- **TensorRT-LLM** (`NVIDIA`) 🌍 ⭐ 🟢 — Peak optimization on NVIDIA GPUs.
- **LMDeploy** (`InternLM`) 🇨🇳 ⭐ 🟢 🏠 — InternLM team's deploy stack; domestic-ecosystem friendly.
- **llama.cpp** (`ggml-org`) 🌍 ⭐ 🟢 🏠 📱 — CPU / edge / quantized deployment.
- **Xinference** (`xorbitsai`) 🇨🇳 🧪 🟢 🏠 — Multi-model local inference server.

## 05 · Compute Scheduling & Serving Orchestration

> **Adoption logic:** once you have multi-GPU / multi-node clusters, you need a layer *above* the engine for load balancing, autoscaling, and multi-tenancy.
> 引入逻辑：引擎之上需要调度与编排做负载均衡、扩缩容、多租户。

- **llm-d** (`llm-d`) 🌍 🧪 🟢 🏠 — vLLM/SGLang orchestration on K8s: smart routing, tiered KV-cache, prefill/decode disaggregation, SLO autoscaling.
- **llmaz** (`InftyAI`) 🌍 🧪 🟢 🏠 — Lightweight inference platform on K8s.
- **K8s scheduler-plugins** (`kubernetes-sigs` / `InftyAI`) 🌍 ⭐ 🟢 🏠 — GPU scheduling plugins.
- **Ray / Ray Serve** (`ray-project`) 🌍 ⭐ 🟢 🏠 — Distributed serving & orchestration; elastic, multi-model.
- **KServe** (`kserve`) 🌍 ⭐ 🟢 🏠 — The K8s model-serving standard.
- **NVIDIA Triton + Dynamo** (`triton-inference-server`) 🌍 ⭐ 🟢 — Official inference serving, enterprise support.
- **BentoML / OpenLLM** (`bentoml`) 🌍 ⭐ 🟢 🏠 — Packaging & deployment.

## 06 · Gateway / Routing / API & Cost Governance

> **Adoption logic:** the **first piece of enterprise AI infrastructure** — unify multi-source access, keys/quota/billing, audit, rate-limit, fallback.
> 引入逻辑：企业级 AI「第一块基础设施」，统一接入与治理。

**LLM gateways / API aggregation**
- **LiteLLM** (`BerriAI`) 🌍 ⭐ 🟢 🏠 — Widest ecosystem, fastest to integrate, self-hostable.
- **Portkey Gateway** (`Portkey-AI`) 🌍 ⭐ 🟢 🏠 — Routing / caching / guardrails / observability / budget control.
- **Kong AI Gateway** (`Kong`) 🌍 ⭐ 🟢 — AI features on a mature API gateway; first choice if you already run Kong.
- **Helicone AI Gateway** (`Helicone`) 🌍 🧪 🟢 🏠 — Lightweight, easy to integrate.
- **One-API / New-API** (`songquanpeng` / `Calcium-Ion`) 🇨🇳 ⭐ 🟢 🏠 — Multi-tenant gateways with keys/quota/billing/audit; a top self-host choice in China.

**Model routing (pick a model per prompt — cut cost, raise quality)**
- **RouteLLM** (`lm-sys`) 🌍 🧪 🟢 — Strong/weak model routing framework.
- **Semantic Router** (`aurelio-labs`) 🌍 🧪 🟢 — Routing on semantic embeddings.

> ⚠️ The gateway is where keys and logs converge — design security / audit / PII-redaction *here*; it's the cheapest place to do it.

## 07 · Context Engineering & Token Efficiency

> **Adoption logic:** cuts the API/inference bill directly. As "Vibe Coding" scales across your dev team, token cost rises — this layer is explicit ROI.
> 引入逻辑：直接砍 API/推理账单，显性 ROI。

- **rtk (Rust Token Killer)** (`rtk-ai/rtk`) 🌍 ⭐ 🟢 🏠 — CLI proxy that filters/compresses command output before it enters context; saves 60–90% tokens; transparent hooks into Claude Code / Codex / Cursor / Gemini CLI.
- **LLMLingua** (`microsoft`) 🌍 🧪 🟢 — Prompt / context compression.
- **Repomix** (`yamadashy`) 🌍 ⭐ 🟢 — Pack a repo into a single file to feed a model.
- **files-to-prompt / code2prompt** (`simonw` / `mufeedvh`) 🌍 🧪 🟢 — Code-context assembly.

## 08 · Orchestration Frameworks & Agents

> **Adoption logic:** the main vehicle for internal enablement (sales / support / docs / R&D). In regulated/medical settings, prefer controllable, auditable, deterministic frameworks.
> 引入逻辑：内部赋能落地的主载体；合规场景优先可控、可审计、确定性强的框架。

- **LangGraph** (`langchain-ai`) 🌍 ⭐ 🟢 🏠 — Graph-based agent orchestration; production-ready, highly controllable.
- **LlamaIndex** (`run-llama`) 🌍 ⭐ 🟢 🏠 — RAG / agent data framework.
- **AutoGen** (`microsoft`) 🌍 ⭐ 🟢 — Multi-agent orchestration.
- **DSPy** (`stanfordnlp`) 🌍 🧪 🟢 — Declarative prompt / program optimization.
- **DeerFlow** (`bytedance`) 🇨🇳 🧪 🟢 🏠 — Deep-research multi-agent; production-base candidate.
- **Dify** (`langgenius`) 🇨🇳 ⭐ 🟢 🏠 — LLM app platform; low-code + self-hostable.
- **MetaGPT** (`FoundationAgents`) 🇨🇳 ⭐ 🟢 — Multi-agent "software team" paradigm.
- **OpenHands** (`All-Hands-AI`) 🌍 ⭐ 🟢 🏠 — Open-source coding agent.
- **n8n** (`n8n-io`) 🌍 ⭐ 🟡 🏠 — Workflow automation (Sustainable Use License — confirm terms).

> ⚠️ Medical Class II/III: fully dynamic multi-agent systems conflict with NMPA "deterministic, auditable" requirements — freeze a traceable chain at the orchestration layer.

## 09 · MCP / Tools / Skills

> **Adoption logic:** the protocol + capability layer that lets agents safely touch enterprise systems. The enterprise focus is *gatewayed MCP + audit + permissions*.
> 引入逻辑：让 Agent 安全接入企业系统的协议层与能力层。

- **Model Context Protocol** (`modelcontextprotocol`) 🌍 ⭐ 🟢 — Official protocol + SDKs.
- **awesome-mcp-servers** (`punkpeye/awesome-mcp-servers`) 🌍 — The master index of MCP servers.
- **awesome-mcp-enterprise** (`bh-rat/awesome-mcp-enterprise`) 🌍 — Enterprise-grade MCP subset.
- **MCP Gateway** (e.g. `lasso-security/mcp-gateway`, `mcpo`) 🌍 🧪 🟢 🏠 — MCP gateway / auth / audit.
- **Composio** (`ComposioHQ`) 🌍 🧪 🟢 — Tool integration.
- **awesome-claude-skills** (`ComposioHQ/awesome-claude-skills`) 🌍 — Skills asset index.

## 10 · RAG / Knowledge Base / Data Processing

> **Adoption logic:** the base for internal-knowledge enablement and product RAG. **Document-parsing quality is usually the real make-or-break of RAG.**
> 引入逻辑：文档解析质量往往是 RAG 成败的真正瓶颈。

**Vector DB / retrieval**
- **Milvus** (`milvus-io` / Zilliz) 🇨🇳 ⭐ 🟢 🏠 — Mainstream vector database.
- **Qdrant** (`qdrant`) 🌍 ⭐ 🟢 🏠 — Rust vector DB.
- **pgvector** (`pgvector`) 🌍 ⭐ 🟢 🏠 — Postgres extension; lowest ops overhead.

**Embedding / rerank**
- **BGE** (`FlagOpen` / BAAI) 🇨🇳 ⭐ 🟢 🏠 — BGE-M3 / BGE-Reranker; first choice for Chinese-language RAG retrieval.

**RAG frameworks / app platforms**
- **RAGFlow** (`infiniflow`) 🇨🇳 ⭐ 🟢 🏠 — RAG engine with deep document understanding.
- **LightRAG** (`HKUDS`) 🌍 🧪 🟢 — Graph-augmented RAG.
- **GraphRAG** (`microsoft`) 🌍 🧪 🟢 — Knowledge-graph RAG.
- **FastGPT** (`labring`) 🇨🇳 ⭐ 🟢 🏠 — Knowledge-base Q&A platform.

**Document parsing (the real bottleneck)**
- **MinerU** (`opendatalab`) 🇨🇳 ⭐ 🟢 🏠 — PDF / layout parsing; the domestic first choice.
- **Docling** (`docling-project` / IBM) 🌍 ⭐ 🟢 🏠 — Documents → structured data.
- **Unstructured** (`Unstructured-IO`) 🌍 ⭐ 🟡 — Multi-format parsing.

## 11 · Evaluation / Observability / Guardrails / Governance

> **Adoption logic:** the CAIO's **shield.** Without this layer, everything above is unauditable and indefensible to the board.
> 引入逻辑：CAIO 的「盾」。没有这一层，前面所有引入都不可审计、不可向董事会交代。

**Evaluation**
- **lm-evaluation-harness** (`EleutherAI`) 🌍 ⭐ 🟢 — The academic eval standard.
- **OpenCompass** (`open-compass`) 🇨🇳 ⭐ 🟢 — Comprehensive China-origin eval.
- **promptfoo** (`promptfoo`) 🌍 ⭐ 🟢 🏠 — Engineering-grade prompt/model eval & red-teaming.

**Observability / tracing**
- **Langfuse** (`langfuse`) 🌍 ⭐ 🟢 🏠 — Open-source LLM observability, self-hostable.
- **Phoenix** (`Arize-ai`) 🌍 ⭐ 🟢 🏠 — Tracing & evaluation.
- **OpenLLMetry** (`traceloop`) 🌍 🧪 🟢 — OpenTelemetry semantic conventions for LLMs.

**Guardrails / safety**
- **NeMo Guardrails** (`NVIDIA`) 🌍 ⭐ 🟢 🏠 — Conversational guardrails.
- **Guardrails AI** (`guardrails-ai`) 🌍 🧪 🟢 — Output validation.
- **Llama Guard / PurpleLlama** (`meta-llama`) 🌍 ⭐ 🟡 — Safety classification.
- **garak** (`NVIDIA`) 🌍 🧪 🟢 — LLM vulnerability / red-team scanner.

## 12 · Autonomous Research & Scientific Discovery

> **Adoption logic:** the "research accelerator" for R&D / medical affairs. Mostly 👀 **Watch** for now — mind the non-standard licenses and reproducibility.
> 引入逻辑：研发/医学事务的「研究加速器」，当前多为观察期。

- **AI Scientist / v2** (`SakanaAI/AI-Scientist`) 🌍 👀 🔴 — Pioneering end-to-end autonomous research. ⚠️ **Non-standard license (RAIL-derived, with a mandatory-disclosure clause) — legal review mandatory before any enterprise use.**
- **AI-Researcher** (`HKUDS/AI-Researcher`) 🌍 👀 🟢 — HKU Data Intelligence Lab; autonomous research innovation.
- **open-ai-co-scientist** (`llnl/open-ai-co-scientist`) 🌍 👀 🟢 — Open reproduction of Google's AI co-scientist multi-agent system.
- **GPT-Researcher** (`assafelovic/gpt-researcher`) 🌍 🧪 🟢 🏠 — Autonomous deep-research agent.
- **DeerFlow** (see §08) 🇨🇳 — Deep-research orchestration, self-hostable.

## 13 · Private / Xinchuang / Edge Deployment

> **Adoption logic:** the hard constraints of medical / government / SOE — data never leaves, domestic substitution, edge/on-device. This layer decides whether everything above can *legally land*.
> 引入逻辑：数据不出域、国产化替代、边缘端侧 —— 决定前面所有项目能不能合规落地。

- **awesome-private-ai** (`tdi/awesome-private-ai`) 🌍 — On-prem / air-gap / self-hosted curated list.
- **MindSpore / CANN** (`mindspore-ai` / Huawei Ascend) 🇨🇳 ⭐ 🟢 🏠 🛡️ — Ascend training/inference stack.
- **vllm-ascend** (`vllm-project/vllm-ascend`) 🇨🇳 🧪 🟢 🏠 🛡️ — vLLM Ascend backend; the Xinchuang inference path.
- **LocalAI** (`mudler/LocalAI`) 🌍 ⭐ 🟢 🏠 📱 — OpenAI-compatible local inference.
- **Jan** (`menloresearch/jan`) 🌍 ⭐ 🟢 🏠 📱 — Offline AI assistant.
- **Ollama** (`ollama`) 🌍 ⭐ 🟡 🏠 📱 — Local model runtime (mind the license & commercial terms).

## 14 · Platforms, Hubs & Registries — where CAIOs source & host

> **Adoption logic:** the repos are only half the story. A CAIO also needs the **sourcing & hosting map** — where models actually live, where you pull them behind the firewall, and which managed clouds and domestic silicon you can stand on.
> 引入逻辑：知道仓库还不够，还要知道「去哪取模型、在哪托管、靠哪个国产栈」。
>
> ⚠️ Managed clouds below are listed as **sourcing/hosting venues**, not as OSS entries — included because that is where CAIOs source & host in practice.

**Model hubs & registries · 模型枢纽**
- **Hugging Face** ([huggingface.co](https://huggingface.co)) 🌍 — The default global hub for models, datasets & Spaces.
- **ModelScope 魔搭** ([modelscope.cn](https://modelscope.cn)) 🇨🇳 — Alibaba-backed hub; the de-facto China mirror for weights & datasets.
- **GitCode AI / 模型广场** ([gitcode.com](https://gitcode.com)) 🇨🇳 — CSDN-backed mirror of OSS & models.
- **Kaggle Models** ([kaggle.com/models](https://www.kaggle.com/models)) 🌍 — Hosted models + notebooks.
- **Ollama Library** ([ollama.com/library](https://ollama.com/library)) 🌍 📱 — One-command local model pulls.

**Code hosting · 代码托管**
- **GitHub** ([github.com](https://github.com)) 🌍 — Where most of this list lives.
- **Gitee 码云** ([gitee.com](https://gitee.com)) 🇨🇳 — China's largest host; many domestic OSS mirrors.
- **GitLab** ([gitlab.com](https://gitlab.com)) 🌍 — Self-hostable CE, common behind the firewall.
- **AtomGit** ([atomgit.com](https://atomgit.com)) 🇨🇳 🛡️ — OpenAtom Foundation hosting, Xinchuang-aligned.

**Managed AI clouds — overseas · 海外云**
- **AWS Bedrock / SageMaker** ([aws.amazon.com/bedrock](https://aws.amazon.com/bedrock/)) 🌍 ☁️
- **Azure AI Foundry** ([ai.azure.com](https://ai.azure.com)) 🌍 ☁️
- **Google Vertex AI** ([cloud.google.com/vertex-ai](https://cloud.google.com/vertex-ai)) 🌍 ☁️
- **NVIDIA NGC / NIM** ([catalog.ngc.nvidia.com](https://catalog.ngc.nvidia.com)) 🌍 ☁️ 🏠 — Containers, models, microservices.

**Managed AI clouds — China · 国内云**
- **Alibaba Cloud Model Studio 百炼** ([bailian.console.aliyun.com](https://bailian.console.aliyun.com)) 🇨🇳 ☁️
- **Volcengine Ark 火山方舟** ([volcengine.com/product/ark](https://www.volcengine.com/product/ark)) 🇨🇳 ☁️
- **Baidu Qianfan 千帆** ([cloud.baidu.com/product/wenxinworkshop](https://cloud.baidu.com/product/wenxinworkshop)) 🇨🇳 ☁️
- **Tencent Cloud TI / Hunyuan 腾讯云** ([cloud.tencent.com/product/ti](https://cloud.tencent.com/product/ti)) 🇨🇳 ☁️
- **Huawei Cloud ModelArts 华为云** ([huaweicloud.com/product/modelarts](https://www.huaweicloud.com/product/modelarts.html)) 🇨🇳 ☁️ 🛡️

**Inference-as-a-service / API aggregators · 推理即服务**
- **OpenRouter** ([openrouter.ai](https://openrouter.ai)) 🌍 — Many models behind one key.
- **Together / Fireworks / Groq / DeepInfra** 🌍 — Hosted open-weight inference at speed.
- **SiliconFlow 硅基流动** ([siliconflow.cn](https://siliconflow.cn)) 🇨🇳 — Low-cost hosted open-weight inference.

**Domestic compute stacks · 国产算力栈 (信创)**
- **Huawei Ascend CANN** ([hiascend.com](https://www.hiascend.com)) 🇨🇳 🛡️ — The Ascend NPU compute architecture (the CUDA analog for Xinchuang).
- **MindSpore** ([mindspore.cn](https://www.mindspore.cn)) 🇨🇳 🛡️ — Huawei's AI framework.
- **Cambricon 寒武纪 · Moore Threads 摩尔线程 · Hygon 海光 · Biren 壁仞** 🇨🇳 🛡️ — Domestic accelerators to evaluate for Xinchuang procurement.

## 15 · Orgs & People to Follow (open-source account index)

> **Adoption logic:** follow the *source*, not the repo. Watching these official org accounts gets you the signal earlier than chasing single repos. **Prioritize org accounts; keep personal accounts minimal.**
> 引入逻辑：跟仓库不如跟「源头」。

**Models & low-level — China:** `deepseek-ai` · `QwenLM` · `zai-org` (GLM) · `OpenBMB` · `ByteDanceSeed` · `moonshotai` (Kimi) · `MiniMax-AI` · `FlagOpen` (BAAI) · `InternLM` · `modelscope`

**Models & low-level — global:** `NVIDIA` · `microsoft` · `meta-llama` · `mistralai` · `huggingface` · `google-research`

**Inference / infrastructure:** `vllm-project` · `sgl-project` · `ray-project` · `InftyAI` · `llm-d` · `BerriAI` (LiteLLM)

**Agents / apps / RAG:** `langchain-ai` · `run-llama` · `langgenius` (Dify) · `infiniflow` (RAGFlow) · `HKUDS` · `opendatalab`

**Protocol / tools:** `modelcontextprotocol` · `ComposioHQ`

**People (OSS maintainers, follow as needed):** `karpathy` (understand LLMs from zero) — otherwise track via the org accounts above.

## 16 · Other Awesome Lists (meta-index)

> This list doesn't reinvent the wheel. Below are deeper, domain-specific lists — use them as drill-down entry points.
> 本清单不重复造轮子；以下是各细分领域更深的专门清单。

- **[tensorchord/Awesome-LLMOps](https://github.com/tensorchord/Awesome-LLMOps)** — Full-stack LLMOps; best-structured.
- **[Not-Diamond/awesome-ai-model-routing](https://github.com/Not-Diamond/awesome-ai-model-routing)** — Model-routing focus.
- **[xlite-dev/Awesome-LLM-Inference](https://github.com/xlite-dev/Awesome-LLM-Inference)** — Inference acceleration: papers + code.
- **[tdi/awesome-private-ai](https://github.com/tdi/awesome-private-ai)** — Private / air-gap deployment.
- **[deepseek-ai/open-infra-index](https://github.com/deepseek-ai/open-infra-index)** — DeepSeek's official infra index.
- **[Hannibal046/Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM)** — The classic master LLM list.
- **[EthicalML/awesome-production-machine-learning](https://github.com/EthicalML/awesome-production-machine-learning)** — Production ML / governance, the elder list.
- **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** · **[bh-rat/awesome-mcp-enterprise](https://github.com/bh-rat/awesome-mcp-enterprise)** — MCP ecosystem.
- **[Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)** · **[e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents)** — Apps & agents.

---

## Contributing

PRs welcome — see **[CONTRIBUTING.md](CONTRIBUTING.md)**. The short version:

1. **One project per PR**, in the right section, sorted by maturity then name.
2. **License + maturity tags are mandatory**; add deployment/origin/compliance tags where you can.
3. **Maintainer review before merge:** link validity, license matches the code's own declaration, activity in the last ~6 months.
4. **One sentence** on *which layer it fits and what problem it solves* — no marketing fluff.
5. Closed/commercial products don't go in the body; if there's an OSS core, link the core repo.

## Disclaimer

This list is a **decision aid**, not legal, compliance, or procurement advice. Final license, compliance, and security judgments rest with your company's legal, compliance, and security teams. Tags can go stale as projects evolve — always confirm against the project's current upstream state before adoption.

本清单为引入决策的**辅助参考**，不构成法律、合规或采购建议。引入前请以项目官方仓库的当前状态为准。

---

<div align="center">

### ⭐ Star history

[![Star History Chart](https://api.star-history.com/svg?repos=caiohome/awesome-caio&type=Date)](https://star-history.com/#caiohome/awesome-caio&Date)

**Maintained with ☕ by [CAIO之家 · caiohome.com](https://www.caiohome.com)** — the home for Chief AI Officers.
Content licensed under [CC BY 4.0](LICENSE). *Attribution: "Awesome CAIO — caiohome.com".*

<sub>If this saved you one bad procurement decision, give it a ⭐ and pass it to your AI lead.</sub>

</div>
