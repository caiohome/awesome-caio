# Awesome Enterprise AI [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> An adoption-first index of open-source AI for the enterprise, curated through the eyes of a CAIO (Chief AI Officer): not the coolest projects, but the ones you can actually bring into a company.

Every entry answers one question: can this open-source project be brought into a company, to which layer, under what license, and at what compliance risk? Each item notes its license (permissive, conditional or restricted) and maturity (production, pilot or watch). Maintained by [CAIO之家](https://www.caiohome.com).

## Contents

- [Foundation Models and Open Weights](#foundation-models-and-open-weights)
- [Training, Fine-tuning and Post-training](#training-fine-tuning-and-post-training)
- [Kernels and Low-level Systems](#kernels-and-low-level-systems)
- [Inference Engines](#inference-engines)
- [Compute Scheduling and Serving Orchestration](#compute-scheduling-and-serving-orchestration)
- [Gateway, Routing and Cost Governance](#gateway-routing-and-cost-governance)
- [Context Engineering and Token Efficiency](#context-engineering-and-token-efficiency)
- [Orchestration Frameworks and Agents](#orchestration-frameworks-and-agents)
- [MCP, Tools and Skills](#mcp-tools-and-skills)
- [RAG, Knowledge Base and Data Processing](#rag-knowledge-base-and-data-processing)
- [Evaluation, Observability and Governance](#evaluation-observability-and-governance)
- [Autonomous Research](#autonomous-research)
- [Vibe Coding for Enterprise R&D](#vibe-coding-for-enterprise-rd)
- [Internal Knowledge Base](#internal-knowledge-base)
- [Private, Xinchuang and Edge Deployment](#private-xinchuang-and-edge-deployment)
- [Platforms, Hubs and Registries](#platforms-hubs-and-registries)
- [Related](#related)

## Foundation Models and Open Weights

> Fix your base first; a multi-source policy hedges supply risk. Weight licenses often differ from the code license, so check each one.

- [DeepSeek](https://github.com/deepseek-ai) - V and R series open weights with strong reasoning and code; mostly MIT. China-led, production, permissive.
- [Qwen](https://github.com/QwenLM) - Full size range plus multimodal, mostly Apache-2.0; the enterprise-friendly default. China-led, production, permissive.
- [GLM](https://github.com/zai-org) - Open model series where some versions carry usage terms, so confirm before commercial use. China-led, production, conditional.
- [Kimi](https://github.com/MoonshotAI) - Long-context and agentic models with open weights. China-led, production, permissive.
- [MiniMax](https://github.com/MiniMax-AI) - Open-weight large models with long context. China-led, production, permissive.
- [MiniCPM](https://github.com/OpenBMB/MiniCPM) - Edge-friendly small models. China-led, production, conditional, edge.
- [LLaMA](https://github.com/meta-llama) - Meta open-weight models under the LLaMA Community License with an active-user threshold clause; not pure open source. Global, production, conditional.
- [Mistral](https://github.com/mistralai) - Overseas open-weight reference models. Global, production, permissive.
- [Gemma](https://ai.google.dev/gemma) - Google open-weight model family. Global, production, conditional.
- [Phi](https://huggingface.co/microsoft) - Microsoft small open-weight models. Global, production, permissive.
- [gpt-oss](https://github.com/openai/gpt-oss) - OpenAI first open-weight models, 120B and 20B, under Apache-2.0; an enterprise-safe Western open-weight anchor. Global, production, permissive.
- [OLMo](https://github.com/allenai/OLMo) - Allen AI fully open model with training data, code and weights; the reference when full reproducibility and auditability is the requirement. Global, pilot, permissive.

## Training, Fine-tuning and Post-training

> Most enterprises never pretrain; the action is in fine-tuning for domain adaptation and post-training or RL for alignment and reasoning gains.

### Distributed pretraining and large-scale training

- [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) - De-facto standard for large-scale parallel training. Global, production, permissive.
- [DeepSpeed](https://github.com/deepspeedai/DeepSpeed) - ZeRO optimization for memory and throughput. Global, production, permissive.
- [NeMo](https://github.com/NVIDIA/NeMo) - End-to-end training framework. Global, production, permissive.
- [ColossalAI](https://github.com/hpcaitech/ColossalAI) - Parallel-training toolbox. Pilot, permissive.
- [TorchTitan](https://github.com/pytorch/torchtitan) - PyTorch-native large-model training reference. Pilot, permissive.

### Fine-tuning

- [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) - One-stop fine-tuning; the most widely deployed in China. China-led, production, permissive, self-hostable.
- [ms-swift](https://github.com/modelscope/ms-swift) - ModelScope training and tuning suite with good domestic-ecosystem fit. China-led, production, permissive, self-hostable.
- [Unsloth](https://github.com/unslothai/unsloth) - Efficient single-GPU fine-tuning that saves VRAM. Global, production, permissive.
- [Axolotl](https://github.com/axolotl-ai-cloud/axolotl) - Config-driven fine-tuning. Global, production, permissive.
- [TRL](https://github.com/huggingface/trl) - Hugging Face post-training library covering SFT, DPO and GRPO. Global, production, permissive.

### RLHF and reinforcement learning

- [verl](https://github.com/volcengine/verl) - ByteDance Seed production-grade RL framework based on HybridFlow. China-led, production, permissive.
- [OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) - Approachable RLHF library. Global, production, permissive.
- [ROLL](https://github.com/alibaba/ROLL) - Alibaba large-scale RL framework. China-led, pilot, permissive.
- [AReaL](https://github.com/inclusionAI/AReaL) - Ant Group asynchronous, throughput-focused RL. China-led, pilot, permissive.
- [slime](https://github.com/THUDM/slime) - Zhipu and Tsinghua lineage RL scaling. China-led, pilot, permissive.
- [NeMo-RL](https://github.com/NVIDIA-NeMo/RL) - NVIDIA post-training RL. Global, pilot, permissive.
- [DAPO](https://github.com/BytedTsinghua-SIA/DAPO) - ByteDance and Tsinghua open RL system and dataset built on verl. China-led, watch, permissive.

### Learning from scratch

- [nanoGPT](https://github.com/karpathy/nanoGPT) - Minimal, readable GPT training code; the best teaching repo to understand LLMs from zero. Global, permissive.
- [llm.c](https://github.com/karpathy/llm.c) - LLM training in raw C and CUDA that teaches the low-level mechanics. Global, permissive.

## Kernels and Low-level Systems

> In-house teams need these; almost everyone else only uses them. Understanding them is what lets you push inference and training cost down.

- [open-infra-index](https://github.com/deepseek-ai/open-infra-index) - DeepSeek production-validated kernels and infra including FlashMLA, DeepEP, DeepGEMM, DualPipe and 3FS; mostly MIT. China-led, production, permissive.
- [FlashAttention](https://github.com/Dao-AILab/flash-attention) - The attention-acceleration standard. Global, production, permissive.
- [Triton](https://github.com/triton-lang/triton) - Language for writing GPU kernels. Global, production, permissive.
- [CUTLASS](https://github.com/NVIDIA/cutlass) - CUDA matrix-operation template library. Global, production, permissive.
- [Liger-Kernel](https://github.com/linkedin/Liger-Kernel) - Fused training kernels that save VRAM. Global, pilot, permissive.
- [FlashInfer](https://github.com/flashinfer-ai/flashinfer) - Kernel library for LLM serving covering attention, MoE and sampling; the de-facto kernel backend under vLLM, SGLang and TensorRT-LLM. Global, production, permissive.

## Inference Engines

> The main cost battleground; engine choice directly sets per-GPU throughput and concurrency cost.

- [vLLM](https://github.com/vllm-project/vllm) - High-throughput inference engine using PagedAttention; the de-facto throughput standard, with an Ascend fork. Global, production, permissive, self-hostable.
- [SGLang](https://github.com/sgl-project/sglang) - High-performance serving, common for RAG and structured output. Global, production, permissive, self-hostable.
- [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) - Peak optimization on NVIDIA GPUs. Global, production, permissive.
- [LMDeploy](https://github.com/InternLM/lmdeploy) - InternLM team deploy stack, friendly to the domestic ecosystem. China-led, production, permissive, self-hostable.
- [llama.cpp](https://github.com/ggml-org/llama.cpp) - CPU, edge and quantized deployment. Global, production, permissive, self-hostable, edge.
- [Xinference](https://github.com/xorbitsai/inference) - Multi-model local inference server. China-led, pilot, permissive, self-hostable.

## Compute Scheduling and Serving Orchestration

> Once you have multi-GPU or multi-node clusters, you need a layer above the engine for load balancing, autoscaling and multi-tenancy.

- [llm-d](https://github.com/llm-d/llm-d) - vLLM and SGLang orchestration on Kubernetes with smart routing, tiered KV-cache, prefill and decode disaggregation and SLO autoscaling. Global, pilot, permissive, self-hostable.
- [llmaz](https://github.com/InftyAI/llmaz) - Lightweight inference platform on Kubernetes. Global, pilot, permissive, self-hostable.
- [scheduler-plugins](https://github.com/kubernetes-sigs/scheduler-plugins) - Kubernetes GPU scheduling plugins. Global, production, permissive, self-hostable.
- [Ray](https://github.com/ray-project/ray) - Distributed serving and orchestration via Ray Serve; elastic and multi-model. Global, production, permissive, self-hostable.
- [KServe](https://github.com/kserve/kserve) - The Kubernetes model-serving standard. Global, production, permissive, self-hostable.
- [Triton Inference Server](https://github.com/triton-inference-server/server) - NVIDIA official inference serving with enterprise support. Global, production, permissive.
- [Dynamo](https://github.com/ai-dynamo/dynamo) - NVIDIA datacenter-scale inference serving. Global, production, permissive.
- [BentoML](https://github.com/bentoml/BentoML) - Model packaging and deployment. Global, production, permissive, self-hostable.
- [OpenLLM](https://github.com/bentoml/OpenLLM) - Run open-weight LLMs as OpenAI-compatible APIs. Global, production, permissive, self-hostable.
- [AIBrix](https://github.com/vllm-project/aibrix) - Cost-efficient, pluggable Kubernetes infrastructure for LLM inference from the vLLM project, with LLM-aware autoscaling, KV-cache offload and routing. Global, pilot, permissive, self-hostable.
- [LMCache](https://github.com/LMCache/LMCache) - KV-cache layer that accelerates serving through cross-request reuse and offload; pairs with vLLM and llm-d. Global, pilot, permissive, self-hostable.
- [OME](https://github.com/ome-projects/ome) - Kubernetes operator for LLM serving with engine-agnostic model lifecycle, GPU scheduling and prefill-decode disaggregation across SGLang, vLLM, TensorRT-LLM and Triton. Global, pilot, permissive, self-hostable.
- [kvcached](https://github.com/ovg-project/kvcached) - Virtualized elastic KV-cache that lets multiple models share GPU memory dynamically to raise utilization on expensive fleets. Global, pilot, permissive, self-hostable.
- [checkpoint-engine](https://github.com/MoonshotAI/checkpoint-engine) - Lightweight middleware to hot-update model weights in running inference engines for RLHF online updates and zero-downtime model swaps. China-led, pilot, permissive, self-hostable.

## Gateway, Routing and Cost Governance

> The first piece of enterprise AI infrastructure: unify multi-source access, keys, quota, billing, audit, rate-limit and fallback.

### LLM gateways and API aggregation

- [LiteLLM](https://github.com/BerriAI/litellm) - Widest provider ecosystem, fastest to integrate, self-hostable. Global, production, permissive, self-hostable.
- [Portkey Gateway](https://github.com/Portkey-AI/gateway) - Routing, caching, guardrails, observability and budget control. Global, production, permissive, self-hostable.
- [Kong AI Gateway](https://github.com/Kong/kong) - AI features on a mature API gateway; first choice if you already run Kong. Global, production, permissive.
- [Helicone](https://github.com/Helicone/helicone) - Lightweight gateway and observability, easy to integrate. Global, pilot, permissive, self-hostable.
- [One-API](https://github.com/songquanpeng/one-api) - Multi-tenant gateway with keys, quota, billing and audit; a top self-host choice in China, MIT. China-led, production, permissive, self-hostable.
- [New-API](https://github.com/Calcium-Ion/new-api) - One-API-style multi-tenant gateway under AGPL-3.0, so legal review before SaaS redistribution. China-led, production, restricted, self-hostable.
- [Higress](https://github.com/higress-group/higress) - AI-native API gateway based on Envoy with token rate-limiting, semantic caching and content-safety plugins; China-origin with a good Xinchuang story. China-led, production, permissive, self-hostable.

### Model routing

- [RouteLLM](https://github.com/lm-sys/RouteLLM) - Strong and weak model routing framework. Global, pilot, permissive.
- [Semantic Router](https://github.com/aurelio-labs/semantic-router) - Routing on semantic embeddings. Global, pilot, permissive.

## Context Engineering and Token Efficiency

> Cuts the API and inference bill directly; as coding assistants scale across the dev team, this layer is explicit ROI.

- [rtk](https://github.com/rtk-ai/rtk) - CLI proxy that filters and compresses command output before it enters context, saving 60 to 90 percent of tokens; hooks into Claude Code, Codex, Cursor and Gemini CLI. Global, production, permissive, self-hostable.
- [LLMLingua](https://github.com/microsoft/LLMLingua) - Prompt and context compression. Global, pilot, permissive.
- [Repomix](https://github.com/yamadashy/repomix) - Pack a repository into a single file to feed a model. Global, production, permissive.
- [files-to-prompt](https://github.com/simonw/files-to-prompt) - Concatenate files into one prompt for code context. Global, pilot, permissive.
- [code2prompt](https://github.com/mufeedvh/code2prompt) - Turn a codebase into an LLM prompt with templates. Global, pilot, permissive.
- [kvpress](https://github.com/NVIDIA/kvpress) - NVIDIA KV-cache compression toolkit offering a library of press methods to shrink long-context memory with minimal accuracy loss. Global, pilot, permissive.

## Orchestration Frameworks and Agents

> The main vehicle for internal enablement; in regulated settings prefer controllable, auditable, deterministic frameworks.

- [LangGraph](https://github.com/langchain-ai/langgraph) - Graph-based agent orchestration; production-ready and highly controllable. Global, production, permissive, self-hostable.
- [LlamaIndex](https://github.com/run-llama/llama_index) - RAG and agent data framework. Global, production, permissive, self-hostable.
- [AutoGen](https://github.com/microsoft/autogen) - Multi-agent orchestration. Global, production, permissive.
- [DSPy](https://github.com/stanfordnlp/dspy) - Declarative prompt and program optimization. Global, pilot, permissive.
- [DeerFlow](https://github.com/bytedance/deer-flow) - ByteDance deep-research multi-agent system; a production-base candidate. China-led, pilot, permissive, self-hostable.
- [Dify](https://github.com/langgenius/dify) - LLM app platform; low-code and self-hostable. China-led, production, permissive, self-hostable.
- [MetaGPT](https://github.com/FoundationAgents/MetaGPT) - Multi-agent software-team paradigm. China-led, production, permissive.
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) - Open-source coding agent. Global, production, permissive, self-hostable.
- [n8n](https://github.com/n8n-io/n8n) - Workflow automation under the Sustainable Use License; confirm terms. Global, production, conditional, self-hostable.
- [CrewAI](https://github.com/crewAIInc/crewAI) - Role-playing multi-agent orchestration for collaborative agent teams. Global, production, permissive.
- [Pydantic AI](https://github.com/pydantic/pydantic-ai) - Type-safe agent framework; strong fit for controllable, testable enterprise agents. Global, production, permissive.
- [Google ADK](https://github.com/google/adk-python) - Code-first Agent Development Kit to build, evaluate and deploy agents. Global, production, permissive.
- [Agno](https://github.com/agno-agi/agno) - High-performance framework to build and run agent platforms. Global, production, permissive.
- [Bisheng](https://github.com/dataelement/bisheng) - Enterprise LLM DevOps platform spanning workflow, RAG, agents, fine-tuning and observability; self-hostable. China-led, production, permissive, self-hostable.
- [Agent Executor](https://github.com/google/ax) - Google open-source distributed agent runtime with durable execution, crash snapshot and resume, and sandboxed isolation for long-running agentic workloads. Global, pilot, permissive, self-hostable.
- [Symphony](https://github.com/openai/symphony) - OpenAI open Codex-orchestration layer that turns tracker tickets into isolated, autonomous coding-agent runs; an engineering preview, so pilot rather than GA. Global, pilot, permissive.
- [Shannon](https://github.com/Kocoro-lab/Shannon) - Production-oriented multi-agent orchestration on Temporal durable workflows with budget and policy enforcement, a Rust sandbox and OpenTelemetry observability. Global, pilot, permissive, self-hostable.
- [agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox) - Official Kubernetes SIG project providing isolated, stateful, singleton sandboxes as a standard execution substrate for agent runtimes. Global, pilot, permissive, self-hostable.

## MCP, Tools and Skills

> The protocol and capability layer that lets agents safely touch enterprise systems; the enterprise focus is gatewayed MCP plus audit and permissions.

- [Model Context Protocol](https://modelcontextprotocol.io) - Open protocol and SDKs for connecting agents to tools and data. Global, production, permissive.
- [MCP Gateway](https://github.com/lasso-security/mcp-gateway) - Security gateway, auth and audit for MCP. Global, pilot, permissive, self-hostable.
- [mcpo](https://github.com/open-webui/mcpo) - Expose MCP servers as OpenAPI endpoints. Global, pilot, permissive, self-hostable.
- [Composio](https://github.com/ComposioHQ/composio) - Tool integration for agents. Global, pilot, permissive.
- [FastMCP](https://github.com/PrefectHQ/fastmcp) - A fast, Pythonic way to build MCP servers and clients. Global, production, permissive.
- [MCP Gateway (Microsoft)](https://github.com/microsoft/mcp-gateway) - Kubernetes reverse proxy and control plane for MCP servers with session-aware stateful routing, lifecycle management and OAuth2 with Entra ID and RBAC. Global, pilot, permissive, self-hostable.
- [SkillHub](https://github.com/iflytek/skillhub) - Self-hosted enterprise agent-skill registry to publish and version skill packages with team namespaces, RBAC and audit logs, deployable on-premise. China-led, pilot, permissive, self-hostable.
- [Archestra](https://github.com/archestra-ai/archestra) - Enterprise AI platform bundling a private MCP registry, a Kubernetes MCP gateway, deterministic prompt-injection guardrails and agent-to-agent orchestration, under AGPL-3.0 so legal review is needed before SaaS redistribution. Global, pilot, restricted, self-hostable.

## RAG, Knowledge Base and Data Processing

> The base for internal-knowledge enablement and product RAG; document-parsing quality is usually the real make-or-break.

### Vector databases and retrieval

- [Milvus](https://github.com/milvus-io/milvus) - Mainstream vector database. China-led, production, permissive, self-hostable.
- [Qdrant](https://github.com/qdrant/qdrant) - Rust vector database. Global, production, permissive, self-hostable.
- [pgvector](https://github.com/pgvector/pgvector) - PostgreSQL extension for vectors; lowest ops overhead. Global, production, permissive, self-hostable.
- [TurboVec](https://github.com/RyanCodrai/turbovec) - Embedded vector index in the FAISS class, not a server database, built on Google Research TurboQuant; about 16x compression versus float32 with recall on par with FAISS-PQ. New and single-maintainer, MIT. Global, pilot, permissive, self-hostable.

### Embedding and rerank

- [BGE](https://github.com/FlagOpen/FlagEmbedding) - Embedding and reranker models (M3 and Reranker variants); first choice for Chinese-language RAG retrieval. China-led, production, permissive, self-hostable.
- [rerankers](https://github.com/AnswerDotAI/rerankers) - One lightweight, low-dependency API across cross-encoder and reranker models, letting teams upgrade retrieval quality with a one-line swap. Global, pilot, permissive.

### RAG frameworks and platforms

- [RAGFlow](https://github.com/infiniflow/ragflow) - RAG engine with deep document understanding. China-led, production, permissive, self-hostable.
- [LightRAG](https://github.com/HKUDS/LightRAG) - Graph-augmented RAG. Global, pilot, permissive.
- [GraphRAG](https://github.com/microsoft/graphrag) - Knowledge-graph RAG. Global, pilot, permissive.
- [FastGPT](https://github.com/labring/FastGPT) - Knowledge-base question-answering platform. China-led, production, permissive, self-hostable.

### Document parsing

- [MinerU](https://github.com/opendatalab/MinerU) - PDF and layout parsing; a domestic first choice under Apache-2.0 with additional terms, so confirm for large-scale commercial use. China-led, production, conditional, self-hostable.
- [Docling](https://github.com/docling-project/docling) - Convert documents into structured data. Global, production, permissive, self-hostable.
- [Unstructured](https://github.com/Unstructured-IO/unstructured) - Multi-format document parsing. Global, production, conditional.
- [markitdown](https://github.com/microsoft/markitdown) - Convert Office, PDF, HTML and more into clean Markdown for LLMs. Global, production, permissive.
- [LiteParse](https://github.com/run-llama/liteparse) - Fast, local, model-free document parser from the LlamaIndex team that turns PDF and Office files into clean structured output with no GPU or API. Global, pilot, permissive, self-hostable.
- [MonkeyOCR](https://github.com/Yuliang-Liu/MonkeyOCR) - Lightweight LMM-based document-parsing model strong on tables, formulas and complex layouts for high-fidelity RAG ingestion. China-led, pilot, permissive, self-hostable.

### Web ingestion and memory

- [Crawl4AI](https://github.com/unclecode/crawl4ai) - LLM-friendly web crawler and scraper for RAG data ingestion. Global, production, permissive.
- [mem0](https://github.com/mem0ai/mem0) - Memory layer for agents with persistent user and agent memory across sessions. Global, production, permissive.
- [Hindsight](https://github.com/vectorize-io/hindsight) - Self-improving long-term agent memory that learns from past interactions; a vendor-neutral memory backbone and an alternative to mem0. Global, pilot, permissive, self-hostable.
- [memsearch](https://github.com/zilliztech/memsearch) - Persistent, unified agent memory backed by Markdown and Milvus, pairing governance-friendly plaintext storage with a production vector database. China-led, pilot, permissive, self-hostable.

### Knowledge formats and context standards

- [OKF (Open Knowledge Format)](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) - Vendor-neutral Google Cloud spec that packages curated enterprise knowledge as portable Markdown and YAML-frontmatter files agents can read and version in git, formalizing the LLM-wiki and metadata-as-code pattern into a knowledge graph. Global, watch, permissive, self-hostable.

## Evaluation, Observability and Governance

> The CAIO shield; without this layer everything above is unauditable and indefensible to the board.

### Evaluation

- [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) - The academic evaluation standard. Global, production, permissive.
- [OpenCompass](https://github.com/open-compass/opencompass) - Comprehensive China-origin evaluation suite. China-led, production, permissive.
- [promptfoo](https://github.com/promptfoo/promptfoo) - Engineering-grade prompt and model evaluation and red-teaming. Global, production, permissive, self-hostable.
- [Ragas](https://github.com/vibrantlabsai/ragas) - Evaluation toolkit for RAG covering faithfulness, answer relevancy and context metrics. Global, production, permissive.
- [DeepEval](https://github.com/confident-ai/deepeval) - LLM evaluation and unit-testing framework with many built-in metrics. Global, production, permissive.

### Observability and tracing

- [Langfuse](https://github.com/langfuse/langfuse) - Open-source LLM observability, self-hostable. Global, production, permissive, self-hostable.
- [Phoenix](https://github.com/Arize-ai/phoenix) - Tracing and evaluation. Global, production, permissive, self-hostable.
- [OpenLLMetry](https://github.com/traceloop/openllmetry) - OpenTelemetry semantic conventions for LLMs. Global, pilot, permissive.
- [LangWatch](https://github.com/langwatch/langwatch) - Fully open-source Apache-2.0 platform for LLM evaluation, agent testing and tracing with OpenTelemetry-style instrumentation, self-hostable. Global, pilot, permissive, self-hostable.

### Guardrails and safety

- [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) - Conversational guardrails. Global, production, permissive, self-hostable.
- [Guardrails AI](https://github.com/guardrails-ai/guardrails) - Output validation. Global, pilot, permissive.
- [PurpleLlama](https://github.com/meta-llama/PurpleLlama) - Meta trust and safety classification tools. Global, production, conditional.
- [garak](https://github.com/NVIDIA/garak) - LLM vulnerability and red-team scanner. Global, pilot, permissive.
- [Presidio](https://github.com/microsoft/presidio) - PII and PHI detection, redaction and anonymization; the gateway-side control for medical and financial data. Global, production, permissive, self-hostable.

## Autonomous Research

> The research accelerator for R&D and medical affairs; mostly watch for now, with non-standard licenses and reproducibility caveats.

- [AI-Scientist](https://github.com/SakanaAI/AI-Scientist) - Pioneering end-to-end autonomous research under a non-standard RAIL-derived license, so legal review is mandatory. Global, watch, restricted.
- [AI-Researcher](https://github.com/HKUDS/AI-Researcher) - HKU Data Intelligence Lab autonomous research system. Global, watch, permissive.
- [open-ai-co-scientist](https://github.com/llnl/open-ai-co-scientist) - Open reproduction of the Google AI co-scientist multi-agent system. Global, watch, permissive.
- [GPT-Researcher](https://github.com/assafelovic/gpt-researcher) - Autonomous deep-research agent. Global, pilot, permissive, self-hostable.

## Vibe Coding for Enterprise R&D

> The highest-ROI internal rollout: AI that makes your own engineers faster. Prefer self-hostable, bring-your-own-model agents you can point at an internal endpoint. Closed SaaS such as Cursor and Copilot is out of scope; their open-source ecosystem is not.

### Self-hosted Copilot and IDE assistants

- [Tabby](https://github.com/TabbyML/tabby) - Self-hosted Copilot replacement that runs its own completion and chat inference on your GPUs, fully air-gappable; open-core with enterprise features under a separate license. Global, production, conditional, self-hostable.
- [Continue](https://github.com/continuedev/continue) - Self-hostable VS Code and JetBrains assistant plus a governance hub to share approved rules and models across the org. Global, production, permissive, self-hostable.
- [Cline](https://github.com/cline/cline) - Most-starred in-editor autonomous agent with plan-act, MCP and terminal access, runnable against internal self-hosted endpoints. Global, production, permissive, self-hostable.
- [Kilo Code](https://github.com/Kilo-Org/kilocode) - All-in-one agentic VS Code platform in the Roo and Cline lineage, an active migration target now that Roo-Code is archived. Global, production, permissive, self-hostable.

### Terminal coding agents

- [Aider](https://github.com/Aider-AI/aider) - Battle-tested terminal pair-programmer with strong git integration and repo-map context, bring your own model. Global, production, permissive, self-hostable.
- [Goose](https://github.com/aaif-goose/goose) - Block extensible on-machine agent that installs, edits, runs and tests, with an MCP-based extension model. Global, production, permissive, self-hostable.
- [OpenCode](https://github.com/anomalyco/opencode) - Model-agnostic terminal coding agent that works against OpenAI-compatible endpoints. Global, production, permissive, self-hostable.
- [Qwen Code](https://github.com/QwenLM/qwen-code) - Terminal agent tuned for the open-weight Qwen-Coder family, the cleanest path to a fully on-prem open-weight coding stack. China-led, production, permissive, self-hostable.
- [Codex CLI](https://github.com/openai/codex) - OpenAI Apache-2.0 terminal agent and scriptable harness that defaults to OpenAI-hosted models, so it is not air-gapped by default. Global, production, permissive.
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) - Google Apache-2.0 terminal agent and a popular fork base; an open client with a hosted model by default. Global, production, permissive.

### Autonomous software engineering and harness

- [SWE-agent](https://github.com/SWE-agent/SWE-agent) - Reference GitHub issue-to-patch agent that runs in your own sandbox, a base for internal issue-automation experiments. Global, pilot, permissive, self-hostable.
- [Superpowers](https://github.com/obra/superpowers) - A curated skills and methodology harness you can vendor internally to standardize how coding agents behave; pin a commit before org-wide use. Global, pilot, permissive.

## Internal Knowledge Base

> Turn scattered company knowledge such as documents, wikis, PDFs and the open web into an AI-queryable base: a self-hosted search front, research and literature tooling, and web collection to feed it. Many strong picks are copyleft or open-core, so review the license before any SaaS redistribution.

### Knowledge base and enterprise search apps

- [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) - Local-first all-in-one RAG workspace with document connectors, agents and per-workspace access control; air-gap-friendly. Global, production, permissive, self-hostable.
- [Onyx](https://github.com/onyx-dot-app/onyx) - Enterprise search and chat over 40-plus connectors such as Slack, Drive and Confluence with RBAC and document-level permissions; an open Glean alternative, open-core with a proprietary enterprise edition. Global, production, conditional, self-hostable.
- [MaxKB](https://github.com/1Panel-dev/MaxKB) - Turnkey enterprise knowledge-base and agent platform with a workflow builder, a top on-prem chatbot choice in China; GPL-3.0, so review before redistribution. China-led, production, restricted, self-hostable.
- [Khoj](https://github.com/khoj-ai/khoj) - Self-hostable second-brain search over documents and the web with custom agents and scheduled automations, under network-copyleft AGPL-3.0. Global, production, restricted, self-hostable.
- [DocsGPT](https://github.com/arc53/DocsGPT) - Private document question-answering and enterprise-search platform with agents and API connectivity. Global, pilot, permissive, self-hostable.

### Scientific research, documents and literature

- [PaperQA2](https://github.com/Future-House/paper-qa) - High-accuracy RAG that answers questions over scientific PDFs with grounded inline citations. Global, production, permissive, self-hostable.
- [Paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) - Self-hosted document management with OCR, tagging and full-text archive, the standard for internal document archival; GPL-3.0. Global, production, restricted, self-hostable.
- [STORM](https://github.com/stanford-oval/storm) - Generates cited, Wikipedia-style research reports from a topic, useful for internal literature synthesis. Global, pilot, permissive, self-hostable.
- [Zotero](https://github.com/zotero/zotero) - The de-facto open reference and literature manager for collecting, annotating and citing sources, anchoring a research knowledge base; AGPL-3.0. Global, production, restricted, self-hostable.

### Web collection, crawlers and scrapers

- [Firecrawl](https://github.com/firecrawl/firecrawl) - Turn whole sites into clean, LLM-ready Markdown, the dominant ingestion tool; AGPL-3.0, so flag before SaaS use. Global, production, restricted, self-hostable.
- [Scrapy](https://github.com/scrapy/scrapy) - The battle-tested production crawling framework for harvesting web data into structured corpora. Global, production, permissive, self-hostable.
- [Crawlee](https://github.com/apify/crawlee) - Reliable Node.js and Python crawler with proxy rotation that explicitly outputs LLM and RAG-ready data. Global, production, permissive, self-hostable.
- [Trafilatura](https://github.com/adbar/trafilatura) - Precise main-content and metadata extraction to clean Markdown and JSON, a gold standard for corpus cleaning. Global, production, permissive, self-hostable.
- [Scrapegraph-ai](https://github.com/ScrapeGraphAI/Scrapegraph-ai) - LLM-driven scraping that turns prompts and URLs into structured extraction pipelines. Global, production, permissive, self-hostable.
- [Crawlab](https://github.com/crawlab-team/crawlab) - Distributed crawler-management platform to run and schedule scraper fleets at scale. China-led, pilot, permissive, self-hostable.

## Private, Xinchuang and Edge Deployment

> The hard constraints of medical, government and state-owned enterprises: data never leaves, domestic substitution, edge and on-device. This layer decides whether everything above can legally land.

- [MindSpore](https://github.com/mindspore-ai/mindspore) - Huawei Ascend training and inference framework. China-led, production, permissive, self-hostable.
- [vllm-ascend](https://github.com/vllm-project/vllm-ascend) - vLLM Ascend backend; the Xinchuang inference path. China-led, pilot, permissive, self-hostable.
- [LocalAI](https://github.com/mudler/LocalAI) - OpenAI-compatible local inference. Global, production, permissive, self-hostable, edge.
- [Jan](https://github.com/menloresearch/jan) - Offline AI assistant. Global, production, permissive, self-hostable, edge.
- [Ollama](https://github.com/ollama/ollama) - Local model runtime, MIT; mind trademark and commercial positioning rather than the license. Global, production, permissive, self-hostable, edge.

## Platforms, Hubs and Registries

> Knowing the repos is half the story; a CAIO also needs the sourcing and hosting map. Managed clouds below are venues, not open-source entries.

### Model hubs and registries

- [Hugging Face](https://huggingface.co) - The default global hub for models, datasets and Spaces.
- [ModelScope](https://modelscope.cn) - Alibaba-backed hub; the de-facto China mirror for weights and datasets.
- [GitCode AI](https://ai.gitcode.com) - CSDN-backed mirror of open source and models.
- [Kaggle Models](https://www.kaggle.com/models) - Hosted models and notebooks.
- [Ollama Library](https://ollama.com/library) - One-command local model pulls.

### Code hosting

- [GitHub](https://github.com) - Where most of this list lives.
- [Gitee](https://gitee.com) - China's largest host with many domestic mirrors.
- [GitLab](https://gitlab.com) - Self-hostable community edition, common behind the firewall.
- [AtomGit](https://atomgit.com) - OpenAtom Foundation hosting, Xinchuang-aligned.

### Managed AI clouds (overseas)

- [AWS Bedrock](https://aws.amazon.com/bedrock/) - Managed foundation-model service on AWS.
- [Azure AI Foundry](https://ai.azure.com) - Microsoft managed AI platform.
- [Google Vertex AI](https://cloud.google.com/vertex-ai) - Google Cloud managed AI platform.
- [NVIDIA NGC](https://catalog.ngc.nvidia.com) - Containers, models and NIM microservices.

### Managed AI clouds (China)

- [Alibaba Cloud Model Studio](https://www.aliyun.com/product/bailian) - Bailian managed model platform.
- [Volcengine Ark](https://www.volcengine.com/product/ark) - ByteDance managed model platform.
- [Baidu Qianfan](https://qianfan.cloud.baidu.com) - Baidu managed model platform.
- [Tencent Cloud TI](https://cloud.tencent.com/product/ti) - Tencent managed AI platform with Hunyuan.
- [Huawei Cloud ModelArts](https://www.huaweicloud.com/product/modelarts.html) - Huawei managed AI platform, Xinchuang-aligned.

### Inference as a service

- [OpenRouter](https://openrouter.ai) - Many models behind one key.
- [Together](https://www.together.ai) - Hosted open-weight inference at speed.
- [Fireworks](https://fireworks.ai) - Fast hosted open-weight inference.
- [Groq](https://groq.com) - Low-latency inference on custom hardware.
- [DeepInfra](https://deepinfra.com) - Low-cost hosted open-weight inference.
- [SiliconFlow](https://siliconflow.cn) - Low-cost hosted open-weight inference from China.

### Domestic compute stacks

- [Huawei Ascend](https://www.hiascend.com) - Ascend NPU compute architecture, the Xinchuang analog of CUDA.
- [Cambricon](https://www.cambricon.com) - Domestic AI accelerators.
- [Moore Threads](https://www.mthreads.com) - Domestic GPUs.
- [Hygon](https://www.hygon.cn) - Domestic accelerators.
- [Biren](https://www.birentech.com) - Domestic GPUs.

## Related

> Deeper, domain-specific awesome lists to drill down from.

- [Awesome-LLMOps](https://github.com/tensorchord/Awesome-LLMOps) - Full-stack LLMOps; one of the best-structured lists.
- [awesome-ai-model-routing](https://github.com/Not-Diamond/awesome-ai-model-routing) - Model-routing focus.
- [Awesome-LLM-Inference](https://github.com/xlite-dev/Awesome-LLM-Inference) - Inference acceleration papers and code.
- [Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) - The classic master LLM list.
- [awesome-production-machine-learning](https://github.com/EthicalML/awesome-production-machine-learning) - Production ML and governance.
- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) - The master index of MCP servers.
- [awesome-mcp-enterprise](https://github.com/bh-rat/awesome-mcp-enterprise) - Enterprise-grade MCP subset.
- [awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) - Claude skills asset index.
- [awesome-private-ai](https://github.com/tdi/awesome-private-ai) - On-prem, air-gap and self-hosted curated list.
- [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) - LLM apps collection.
- [awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) - AI agents collection.

## Contributing

Contributions welcome. See [contributing guidelines](CONTRIBUTING.md). One project per pull request, in the right section; license and maturity are mandatory; every entry must link to its first-party source; one sentence on which layer it fits and what problem it solves.
