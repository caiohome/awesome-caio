# Awesome Enterprise AI [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> An adoption-first index of open-source AI for the enterprise, curated through the eyes of a CAIO (Chief AI Officer): not the coolest projects, but the ones you can actually bring into a company.

Every entry answers one question: can this open-source project be brought into a company, to which layer, under what license, and at what compliance risk? Each item notes its license (permissive, conditional or restricted) and maturity (production, pilot or watch). Maintained by [CAIO之家](https://www.caiohome.com).

## Contents

- [Philosophy and Concepts](#philosophy-and-concepts)
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
- [Cybersecurity and AI Security](#cybersecurity-and-ai-security)
- [Autonomous Research](#autonomous-research)
- [Vibe Coding for Enterprise R&D](#vibe-coding-for-enterprise-rd)
- [Internal Knowledge Base](#internal-knowledge-base)
- [Private, Xinchuang and Edge Deployment](#private-xinchuang-and-edge-deployment)
- [Platforms, Hubs and Registries](#platforms-hubs-and-registries)
- [Related](#related)

## Philosophy and Concepts

> Tools change every quarter; judgment compounds. Before the stack, this section collects how leading practitioners think about what these systems are, where they are heading, and how to deploy them. These are ideas rather than adoption entries, so they carry no license or maturity tags; each links to its first-party source.

### Andrej Karpathy

- [Software 2.0](https://karpathy.medium.com/software-2-0-a64152b37c35) - Andrej Karpathy, 2017. Neural nets are a new kind of software where you curate data and optimize weights instead of writing explicit logic.
- [Software Is Changing Again (Software 3.0)](https://www.youtube.com/watch?v=LCEmiRjPEtQ) - Andrej Karpathy, 2025. LLMs are a new computer and English is the programming interface; keep a human on the autonomy slider and build for agents.
- [Intro to Large Language Models (the LLM OS)](https://www.youtube.com/watch?v=zjkBMFhNj_g) - Andrej Karpathy, 2023. The clearest plain-English mental model of an LLM as an operating-system kernel, ideal for onboarding leadership.
- [The hottest new programming language is English](https://x.com/karpathy/status/1617979122625712128) - Andrej Karpathy, 2023. Natural language becomes the primary interface to computers, changing who can build software.
- [The origin of vibe coding](https://x.com/karpathy/status/1886192184808149383) - Andrej Karpathy, 2025. Describe intent and let the model generate, productive for prototypes but output must be verified rather than trusted.
- [AGI is still a decade away (Dwarkesh Podcast)](https://www.dwarkesh.com/p/andrej-karpathy) - Andrej Karpathy, 2025. It is the decade of agents rather than the year, since today's agents lack continual learning and robust multimodality.
- [2025 LLM Year in Review](https://karpathy.bearblog.dev/year-in-review-2025/) - Andrej Karpathy, 2025. The year's real shift was reinforcement learning from verifiable rewards, producing jagged intelligence that is superhuman where outputs can be checked and weak elsewhere.
- [Sequoia AI Ascent 2026 fireside](https://karpathy.bearblog.dev/sequoia-ascent-2026/) - Andrej Karpathy, 2026. December 2025 was the agentic inflection point; durable advantage comes from verifiable business domains, custom RL environments and agent-native products.
- [The Unreasonable Effectiveness of Recurrent Neural Networks](https://karpathy.github.io/2015/05/21/rnn-effectiveness/) - Andrej Karpathy, 2015. The foundational demonstration of generative sequence models and a historical anchor for language modeling.

### OpenAI and Sam Altman

- [The Intelligence Age](https://ia.samaltman.com/) - Sam Altman, 2024. Deep learning works and scales, so plan for abundant intelligence reshaping every industry.
- [Three Observations](https://blog.samaltman.com/three-observations) - Sam Altman, 2025. Intelligence scales with the log of compute while cost per unit of intelligence falls about tenfold a year.
- [The Gentle Singularity](https://blog.samaltman.com/the-gentle-singularity) - Sam Altman, 2025. The takeoff is underway but feels gradual, with agents doing real cognitive work as the near-term inflection.
- [Moore's Law for Everything](https://moores.samaltman.com/) - Sam Altman, 2021. If AI drives the cost of goods and services toward zero, the governance question of who captures the value matters as much as the technology.
- [A Practical Guide to Building Agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) - OpenAI, 2025. A concrete field guide on when to build an agent and how to design tools, orchestration and guardrails.
- [AI in the Enterprise](https://openai.com/index/ai-in-the-enterprise/) - OpenAI, 2025. Seven enterprise-adoption lessons from frontier companies, from starting with evals to setting bold automation goals.
- [The State of Enterprise AI](https://openai.com/index/the-state-of-enterprise-ai-2025-report/) - OpenAI, 2026. The telemetry successor to AI in the Enterprise, with reasoning-token consumption per organization up 320 times year over year and workers saving 40 to 60 minutes a day.
- [Introducing OpenAI Frontier](https://openai.com/index/introducing-openai-frontier/) - OpenAI, 2026. An enterprise platform for deploying and managing agents like employees, signaling that the bottleneck has moved from model intelligence to agent operations.

### Anthropic and Dario Amodei

- [Machines of Loving Grace](https://www.darioamodei.com/essay/machines-of-loving-grace) - Dario Amodei, 2024. The concrete optimistic case that powerful AI could compress decades of scientific progress into years.
- [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) - Anthropic, 2024. Start simple, since most value comes from composable workflows rather than autonomous loops; the most-cited agent-design piece.
- [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) - Anthropic, 2025. Context is a finite, managed resource and curating what enters the window is the core reliability discipline.
- [How We Built Our Multi-Agent Research System](https://www.anthropic.com/engineering/built-multi-agent-research-system) - Anthropic, 2025. Orchestrator-plus-subagent architectures beat a single agent on broad research but cost far more tokens.
- [The Urgency of Interpretability](https://www.darioamodei.com/post/the-urgency-of-interpretability) - Dario Amodei, 2025. We deploy systems we do not fully understand, making interpretability a race to win.
- [The Adolescence of Technology](https://www.darioamodei.com/essay/the-adolescence-of-technology) - Dario Amodei, 2026. The successor to Machines of Loving Grace, mapping five concrete risk classes with pragmatic remedies.
- [Policy on the AI Exponential](https://www.darioamodei.com/post/policy-on-the-ai-exponential) - Dario Amodei, 2026. Five policy pillars for governing the run-up to a country of geniuses in a datacenter.
- [Building Multi-Agent Systems: When and How](https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them) - Anthropic, 2026. Multi-agent systems pay off only for context isolation, parallelization or specialization; most enterprise scenarios are better served by one well-scaffolded agent.
- [Anthropic Economic Index](https://www.anthropic.com/economic-index) - Anthropic, 2026. The only vendor index linking real usage logs to worker surveys, ground truth for what AI is actually used for at work.

### Google and DeepMind

- [Agents (whitepaper)](https://www.kaggle.com/whitepaper-agents) - Google and Lee Boonstra, 2024. The canonical primer on the agent stack of model, tools and orchestration.
- [Real-World Generative-AI Use Cases](https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders) - Google Cloud, 2025. A catalog of 600-plus production deployments by industry, the best reference for use-case discovery.
- [Welcome to the Era of Experience](https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf) - David Silver and Richard Sutton, 2025. The next leap is agents learning from their own streams of experience rather than only human data.
- [AI Agent Trends 2026](https://services.google.com/fh/files/misc/google_cloud_ai_agent_trends_2026_report.pdf) - Google Cloud, 2026. The most-cited agent ROI numbers of the cycle: 52 percent of executives have agents in production and 74 percent see ROI within year one.

### Microsoft and Satya Nadella

- [On AI as a cognitive amplifier](https://x.com/satyanadella/status/2066182223213293753) - Satya Nadella, 2025. Reframes the debate from AI slop and substitution toward AI as a cognitive amplifier that scaffolds human potential.
- [Looking Ahead to 2026](https://snscratchpad.com/posts/looking-ahead-2026/) - Satya Nadella, 2025. Advantage evolves from models to systems, the scaffolding that orchestrates many models and agents reliably.
- [2025: The Year the Frontier Firm Is Born](https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born) - Microsoft Work Trend Index, 2025. A new organizational model of hybrid human and agent teams that most leaders expect within 12 to 18 months.
- [2026 Work Trend Index](https://news.microsoft.com/annual-work-trend-index-2026/) - Microsoft, 2026. The Transformation Paradox: organizational factors drive twice as much of AI's impact as individual behavior, and only 19 percent of organizations sit in the frontier zone.

### Other voices

- [From Hierarchy to Intelligence](https://www.sequoiacap.com/article/from-hierarchy-to-intelligence/) - Jack Dorsey and Roelof Botha, 2026. The AI-era organization needs only three kinds of people, namely individual contributors, directly responsible individuals and player-coaches, with an intelligence layer replacing permanent middle management.
- [What's Next for AI Agentic Workflows](https://www.youtube.com/watch?v=sal78ACtGTc) - Andrew Ng, 2024. Agentic patterns such as reflection, tool use, planning and multi-agent dramatically outperform single-shot prompting.
- [2026: This Is AGI](https://sequoiacap.com/article/2026-this-is-agi/) - Pat Grady and Sonya Huang, 2026. Long-horizon agents are functionally AGI, with coding as the first domino from chat in 2022 to reasoning in 2025 to agents as colleagues in 2026.
- [Stanford AI Index 2026](https://hai.stanford.edu/ai-index/2026-ai-index-report) - Stanford HAI, 2026. The neutral yardstick for any board deck: 88 percent organizational adoption and generative AI at 53 percent population adoption within three years.
- [AI at Work 2026](https://www.bcg.com/publications/2026/ai-at-work-why-strategy-matters-more-than-tools) - BCG, 2026. Regular users save about eight hours a week, and an explicit AI strategy beats better tools roughly five to one on impact.

## Foundation Models and Open Weights

> Fix your base first; a multi-source policy hedges supply risk. Weight licenses often differ from the code license, so check each one.

- [DeepSeek](https://github.com/deepseek-ai) - V and R series open weights through V4 with strong reasoning and code; mostly MIT. China-led, production, permissive.
- [Qwen](https://github.com/QwenLM) - Full size range plus native multimodal across the Qwen3.x ladder, mostly Apache-2.0; the enterprise-friendly default. China-led, production, permissive.
- [GLM](https://github.com/zai-org) - Open model series where GLM-5 ships Apache-2.0 and GLM-5.2 MIT, though some earlier versions carry usage terms, so confirm per model. China-led, production, permissive.
- [Kimi](https://github.com/MoonshotAI) - Long-context and agentic open weights, with the K2.x line under a modified MIT license. China-led, production, permissive.
- [MiniMax](https://github.com/MiniMax-AI) - Open-weight large models with long context; the M2.x agentic line adds office-document fluency. China-led, production, permissive.
- [MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) - Xiaomi open coding model where models and agents co-evolve, shipping weights plus an agent harness under MIT. China-led, pilot, permissive, self-hostable.
- [Step](https://github.com/stepfun-ai/Step-3.7-Flash) - StepFun sparse MoE with native image and video understanding and top-ranked output speed, an open multimodal option for real-time agents. China-led, pilot, permissive.
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
- [NeMo](https://github.com/NVIDIA-NeMo) - End-to-end training framework, now split into per-domain repos such as Speech, RL, Automodel and Megatron-Bridge. Global, production, permissive.
- [ColossalAI](https://github.com/hpcaitech/ColossalAI) - Parallel-training toolbox. Pilot, permissive.
- [TorchTitan](https://github.com/pytorch/torchtitan) - PyTorch-native large-model training reference. Pilot, permissive.

### Fine-tuning

- [LLaMA-Factory](https://github.com/hiyouga/LlamaFactory) - One-stop fine-tuning; the most widely deployed in China. China-led, production, permissive, self-hostable.
- [ms-swift](https://github.com/modelscope/ms-swift) - ModelScope training and tuning suite with good domestic-ecosystem fit. China-led, production, permissive, self-hostable.
- [Unsloth](https://github.com/unslothai/unsloth) - Efficient single-GPU fine-tuning that saves VRAM. Global, production, permissive.
- [Axolotl](https://github.com/axolotl-ai-cloud/axolotl) - Config-driven fine-tuning. Global, production, permissive.
- [TRL](https://github.com/huggingface/trl) - Hugging Face post-training library covering SFT, DPO and GRPO. Global, production, permissive.

### RLHF and reinforcement learning

- [verl](https://github.com/verl-project/verl) - ByteDance Seed production-grade RL framework based on HybridFlow. China-led, production, permissive.
- [OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) - Approachable RLHF library. Global, production, permissive.
- [ROLL](https://github.com/alibaba/ROLL) - Alibaba large-scale RL framework. China-led, pilot, permissive.
- [AReaL](https://github.com/areal-project/AReaL) - Ant Group asynchronous, throughput-focused RL. China-led, pilot, permissive.
- [slime](https://github.com/THUDM/slime) - Zhipu and Tsinghua lineage RL scaling. China-led, pilot, permissive.
- [NeMo-RL](https://github.com/NVIDIA-NeMo/RL) - NVIDIA post-training RL. Global, pilot, permissive.
- [DAPO](https://github.com/BytedTsinghua-SIA/DAPO) - ByteDance and Tsinghua open RL system and dataset built on verl. China-led, watch, permissive.
- [ART (Agent Reinforcement Trainer)](https://github.com/OpenPipe/ART) - GRPO-based reinforcement learning that gives multi-step agents on-the-job training on open weights such as Qwen, gpt-oss and Llama. Global, production, permissive.

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
- [DeepSpec](https://github.com/deepseek-ai/DeepSpec) - DeepSeek full-stack codebase for training and evaluating speculative-decoding algorithms, the reference stack for the biggest current inference cost-cut lever. China-led, pilot, permissive.

## Inference Engines

> The main cost battleground; engine choice directly sets per-GPU throughput and concurrency cost.

- [vLLM](https://github.com/vllm-project/vllm) - High-throughput inference engine using PagedAttention; the de-facto throughput standard, with an Ascend fork. Global, production, permissive, self-hostable.
- [SGLang](https://github.com/sgl-project/sglang) - High-performance serving, common for RAG and structured output. Global, production, permissive, self-hostable.
- [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) - Peak optimization on NVIDIA GPUs. Global, production, permissive.
- [LMDeploy](https://github.com/InternLM/lmdeploy) - InternLM team deploy stack, friendly to the domestic ecosystem. China-led, production, permissive, self-hostable.
- [llama.cpp](https://github.com/ggml-org/llama.cpp) - CPU, edge and quantized deployment. Global, production, permissive, self-hostable, edge.
- [Xinference](https://github.com/xorbitsai/inference) - Multi-model local inference server. China-led, pilot, permissive, self-hostable.
- [KTransformers](https://github.com/kvcache-ai/ktransformers) - Heterogeneous CPU and GPU offload that runs huge MoE models like DeepSeek and Kimi on limited GPU, slashing hardware cost for on-prem serving. China-led, production, permissive, self-hostable.
- [xLLM](https://github.com/jd-opensource/xllm) - Production inference engine for LLM, VLM, DiT and REC models optimized for diverse and domestic AI accelerators, a path for sovereign-chip or non-NVIDIA fleets. China-led, pilot, permissive, self-hostable.
- [ds4](https://github.com/antirez/ds4) - DeepSeek 4 Flash and Pro local inference engine for Metal, CUDA and ROCm by the Redis creator, a single-purpose offline alternative to llama.cpp. Global, pilot, permissive, self-hostable.
- [omlx](https://github.com/jundot/omlx) - Inference server with continuous batching and SSD KV caching for Apple Silicon, turning Mac fleets into viable inference nodes for large MoE models. Global, pilot, permissive, self-hostable, edge.

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
- [Mooncake](https://github.com/kvcache-ai/Mooncake) - KV-cache-centric disaggregated prefill-decode serving platform that powers Kimi in production and pairs with vLLM and SGLang. China-led, production, permissive, self-hostable.
- [GPUStack](https://github.com/gpustack/gpustack) - Self-hosted GPU-cluster manager that schedules and serves models across vLLM, SGLang and Ascend nodes, an air-gappable control plane for heterogeneous fleets. China-led, production, permissive, self-hostable.

## Gateway, Routing and Cost Governance

> The first piece of enterprise AI infrastructure: unify multi-source access, keys, quota, billing, audit, rate-limit and fallback.

### LLM gateways and API aggregation

- [LiteLLM](https://github.com/BerriAI/litellm) - Widest provider ecosystem, fastest to integrate, self-hostable. Global, production, permissive, self-hostable.
- [Portkey Gateway](https://github.com/Portkey-AI/gateway) - Routing, caching, guardrails, observability and budget control. Global, production, permissive, self-hostable.
- [Kong AI Gateway](https://github.com/Kong/kong) - AI features on a mature API gateway; first choice if you already run Kong. Global, production, permissive.
- [Helicone](https://github.com/Helicone/helicone) - Lightweight gateway and observability, easy to integrate. Global, pilot, permissive, self-hostable.
- [One-API](https://github.com/songquanpeng/one-api) - Multi-tenant gateway with keys, quota, billing and audit; a top self-host choice in China, MIT. China-led, production, permissive, self-hostable.
- [New-API](https://github.com/QuantumNous/new-api) - One-API-style multi-tenant gateway under AGPL-3.0, so legal review before SaaS redistribution. China-led, production, restricted, self-hostable.
- [Higress](https://github.com/higress-group/higress) - AI-native API gateway based on Envoy with token rate-limiting, semantic caching and content-safety plugins; China-origin with a good Xinchuang story. China-led, production, permissive, self-hostable.
- [Envoy AI Gateway](https://github.com/envoyproxy/ai-gateway) - CNCF-backed, Envoy-native unified gateway for generative-AI traffic, a natural fit for enterprises already standardized on Envoy and Kubernetes. Global, pilot, permissive, self-hostable.
- [Bifrost](https://github.com/maximhq/bifrost) - High-throughput AI gateway claiming around 50x LiteLLM with adaptive load balancing, cluster mode, guardrails and over 1000 models. Global, production, permissive, self-hostable.
- [Plano](https://github.com/katanemo/plano) - Envoy-based AI-native proxy and data plane for agentic apps with smart LLM routing, safety and observability at the edge of every agent call. Global, production, permissive, self-hostable.

### Model routing

- [RouteLLM](https://github.com/lm-sys/RouteLLM) - Strong and weak model routing framework. Global, pilot, permissive.
- [Semantic Router](https://github.com/aurelio-labs/semantic-router) - Routing on semantic embeddings. Global, pilot, permissive.

## Context Engineering and Token Efficiency

> Cuts the API and inference bill directly; as coding assistants scale across the dev team, this layer is explicit ROI.

- [rtk](https://github.com/rtk-ai/rtk) - CLI proxy that filters and compresses command output before it enters context, saving 60 to 90 percent of tokens; hooks into Claude Code, Codex, Cursor and Gemini CLI. Global, production, permissive, self-hostable.
- [LLMLingua](https://github.com/microsoft/LLMLingua) - Prompt and context compression. Global, pilot, permissive.
- [Headroom](https://github.com/headroomlabs-ai/headroom) - Compresses tool outputs, logs, files and RAG chunks 60 to 95 percent before they reach the LLM, in library, proxy or MCP modes. Global, production, permissive, self-hostable.
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
- [DeerFlow](https://github.com/bytedance/deer-flow) - ByteDance long-horizon SuperAgent harness with sandboxes, memory, skills and subagents, grown from a deep-research system into a full agent base. China-led, production, permissive, self-hostable.
- [AgentScope](https://github.com/agentscope-ai/agentscope) - Alibaba production agent framework with fine-grained permissions, multi-tenancy, sandboxing, MCP and A2A support and Kubernetes deploy, in Python, TypeScript and Java. China-led, production, permissive, self-hostable.
- [Dify](https://github.com/langgenius/dify) - LLM app platform; low-code and self-hostable. China-led, production, permissive, self-hostable.
- [MetaGPT](https://github.com/FoundationAgents/MetaGPT) - Multi-agent software-team paradigm. China-led, production, permissive.
- [OpenHands](https://github.com/OpenHands/OpenHands) - Open-source coding agent. Global, production, permissive, self-hostable.
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
- [Langflow](https://github.com/langflow-ai/langflow) - Visual low-code builder for agents and RAG flows that is self-hostable and can export a flow as an API or an MCP server; telemetry is on by default with an opt-out. Global, production, permissive, self-hostable.
- [Paperclip](https://github.com/paperclipai/paperclip) - Open agent workforce console to assign, review and audit fleets of agents at work, the management layer above agent frameworks. Global, production, permissive, self-hostable.
- [nanobot](https://github.com/HKUDS/nanobot) - Lightweight agent runtime for tools, chats and workflows from the LightRAG group, with a tiny footprint under MIT. Global, production, permissive, self-hostable.
- [OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) - Secure, fast and extensible sandbox runtime for AI agent code execution, a self-hostable alternative to sandbox SaaS. Global, pilot, permissive, self-hostable.

## MCP, Tools and Skills

> The protocol and capability layer that lets agents safely touch enterprise systems; the enterprise focus is gatewayed MCP plus audit and permissions.

- [Model Context Protocol](https://modelcontextprotocol.io) - Open protocol and SDKs for connecting agents to tools and data. Global, production, permissive.
- [MCP Gateway](https://github.com/lasso-security/mcp-gateway) - Security gateway, auth and audit for MCP. Global, pilot, permissive, self-hostable.
- [mcpo](https://github.com/open-webui/mcpo) - Expose MCP servers as OpenAPI endpoints. Global, pilot, permissive, self-hostable.
- [Composio](https://github.com/ComposioHQ/composio) - Tool integration for agents. Global, pilot, permissive.
- [FastMCP](https://github.com/PrefectHQ/fastmcp) - A fast, Pythonic way to build MCP servers and clients. Global, production, permissive.
- [MCP Gateway (Microsoft)](https://github.com/microsoft/mcp-gateway) - Kubernetes reverse proxy and control plane for MCP servers with session-aware stateful routing, lifecycle management and OAuth2 with Entra ID and RBAC. Global, pilot, permissive, self-hostable.
- [ContextForge (MCP Gateway)](https://github.com/IBM/mcp-context-forge) - IBM Apache-2.0 MCP, A2A and REST gateway and registry that federates and proxies tools behind one governed front door with auth and observability, and ships an air-gapped container build; a clean-license alternative to AGPL registries. Global, pilot, permissive, self-hostable.
- [SkillHub](https://github.com/iflytek/skillhub) - Self-hosted enterprise agent-skill registry to publish and version skill packages with team namespaces, RBAC and audit logs, deployable on-premise. China-led, pilot, permissive, self-hostable.
- [Archestra](https://github.com/archestra-ai/archestra) - Enterprise AI platform bundling a private MCP registry, a Kubernetes MCP gateway, deterministic prompt-injection guardrails and agent-to-agent orchestration, under AGPL-3.0 so legal review is needed before SaaS redistribution. Global, pilot, restricted, self-hostable.
- [agent-skills](https://github.com/addyosmani/agent-skills) - Production-grade engineering skill library for AI coding agents curated by Addy Osmani, directly importable into coding-agent fleets. Global, production, permissive.
- [financial-services](https://github.com/anthropics/financial-services) - Anthropic official skill and agent pack for financial-services workflows, the first vendor-maintained regulated-vertical skill pack. Global, pilot, permissive.

## RAG, Knowledge Base and Data Processing

> The base for internal-knowledge enablement and product RAG; document-parsing quality is usually the real make-or-break.

### Vector databases and retrieval

- [Milvus](https://github.com/milvus-io/milvus) - Mainstream vector database. China-led, production, permissive, self-hostable.
- [Qdrant](https://github.com/qdrant/qdrant) - Rust vector database. Global, production, permissive, self-hostable.
- [pgvector](https://github.com/pgvector/pgvector) - PostgreSQL extension for vectors; lowest ops overhead. Global, production, permissive, self-hostable.
- [TurboVec](https://github.com/RyanCodrai/turbovec) - Embedded vector index in the FAISS class, not a server database, built on Google Research TurboQuant; about 16x compression versus float32 with recall on par with FAISS-PQ. New and single-maintainer, MIT. Global, pilot, permissive, self-hostable.
- [zvec](https://github.com/alibaba/zvec) - Alibaba lightweight in-process vector database that removes a whole service tier for embedded and edge RAG. China-led, pilot, permissive, self-hostable.

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
- [ParseBench](https://github.com/run-llama/ParseBench) - Reproducible benchmark to objectively compare document parsers across OCR, tables and layout before standardizing on one. Global, pilot, permissive.

### Web ingestion and memory

- [Crawl4AI](https://github.com/unclecode/crawl4ai) - LLM-friendly web crawler and scraper for RAG data ingestion. Global, production, permissive.
- [mem0](https://github.com/mem0ai/mem0) - Memory layer for agents with persistent user and agent memory across sessions. Global, production, permissive.
- [MemPalace](https://github.com/MemPalace/mempalace) - Benchmark-driven agent memory system with published evaluations, an evidence-backed alternative in the agent-memory space. Global, production, permissive, self-hostable.
- [Hindsight](https://github.com/vectorize-io/hindsight) - Self-improving long-term agent memory that learns from past interactions; a vendor-neutral memory backbone and an alternative to mem0. Global, pilot, permissive, self-hostable.
- [memsearch](https://github.com/zilliztech/memsearch) - Persistent, unified agent memory backed by Markdown and Milvus, pairing governance-friendly plaintext storage with a production vector database. China-led, pilot, permissive, self-hostable.
- [OpenViking](https://github.com/volcengine/OpenViking) - Open context database for agents that unifies memory, resources and skills under a filesystem paradigm with hierarchical, self-evolving context delivery, under AGPL-3.0 so review the license before SaaS redistribution. China-led, pilot, restricted, self-hostable.

### Knowledge formats and context standards

- [OKF (Open Knowledge Format)](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) - Vendor-neutral Google Cloud spec that packages curated enterprise knowledge as portable Markdown and YAML-frontmatter files agents can read and version in Git, formalizing the LLM-wiki and metadata-as-code pattern into a knowledge graph. Global, watch, permissive, self-hostable.

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

- [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) - Conversational guardrails. Global, production, permissive, self-hostable.
- [Guardrails AI](https://github.com/guardrails-ai/guardrails) - Output validation. Global, pilot, permissive.
- [PurpleLlama](https://github.com/meta-llama/PurpleLlama) - Meta trust and safety classification tools. Global, production, conditional.
- [Presidio](https://github.com/data-privacy-stack/presidio) - PII and PHI detection, redaction and anonymization; the gateway-side control for medical and financial data. Global, production, permissive, self-hostable.
- [Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit) - First-party Microsoft policy enforcement, zero-trust agent identity and execution sandboxing for autonomous agents, mapped to all ten of the OWASP Agentic Top 10. Global, pilot, permissive, self-hostable.

## Cybersecurity and AI Security

> Securing the AI stack and the enterprise it runs on; the AI-native attack surface (prompt injection, model-file malware, agent and tool abuse, mapped to OWASP LLM Top 10 and MITRE ATLAS) plus the classic security substrate that models, gateways and RAG deploy onto. Prefer self-hostable, agent-drivable tooling that runs behind the firewall.

### Agent-operated security skill libraries

- [CyberSecurity-Skills](https://atomgit.com/AtomGit/CyberSecurity-Skills) - An AI-operated cybersecurity knowledge base of 39 modules and 195 skills as SKILL.md-style files spanning offense (reconnaissance, exploitation, lateral movement, persistence) and defense (SOC operations, threat hunting, DFIR, IAM, Zero Trust, DevSecOps, container, API, cloud and LLM security, ransomware, governance), shipping an agent manifest, index.json and a skill_query.py CLI so an agent can list and fetch skills on demand, mapped to PTES, OWASP Testing Guide, NIST SP 800-115/61, MITRE ATT&CK and ATLAS, OWASP LLM Top 10, CIS, ISO 27001 and China MLPS 2.0; GitHub mirror at [Hi-FullHouse/CyberSecurity-Skills](https://github.com/Hi-FullHouse/CyberSecurity-Skills). China-led, pilot, permissive, self-hostable.
- [Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) - The large-scale English-first counterpart with 817 agent skills across 29 security domains (web, pentest, DFIR, threat intelligence, cloud, malware, fraud), each a SKILL.md folder on the agentskills.io standard with a validate-skill.py gate, cross-mapped to six frameworks (MITRE ATT&CK, ATLAS, D3FEND, NIST CSF 2.0, NIST AI RMF and MITRE F3) and shipped as an installable Claude Code plugin that also runs in Copilot, Codex CLI, Cursor, Gemini CLI and 20 more; a community project named for the skill format, not an official Anthropic release. Global, production, permissive, self-hostable.

### AI, LLM and agent red-teaming and model security

- [garak](https://github.com/NVIDIA/garak) - The LLM vulnerability scanner covering jailbreak, prompt-injection and data-leak probes; the offensive companion to guardrails. Global, pilot, permissive, self-hostable.
- [PyRIT](https://github.com/microsoft/PyRIT) - Microsoft first-party Python risk-identification toolkit for generative-AI red-teaming that automates adversarial probing at scale, MITRE-aligned. Global, pilot, permissive, self-hostable.
- [Giskard](https://github.com/Giskard-AI/giskard-oss) - Open-source evaluation and vulnerability scan for LLM agents and ML models covering hallucination, injection, bias and robustness, wiring red-teaming into CI. Global, production, permissive, self-hostable.
- [LLM Guard](https://github.com/protectai/llm-guard) - Input and output security toolkit for LLM interactions with prompt-injection, PII, toxicity and secret scanners; a self-hostable gateway-side filter. Global, pilot, permissive, self-hostable.
- [ModelScan](https://github.com/protectai/modelscan) - Scans model files (pickle, H5, SavedModel) for serialization attacks, the supply-chain check for models pulled from a hub. Global, pilot, permissive, self-hostable.
- [NemoClaw](https://github.com/NVIDIA/NemoClaw) - NVIDIA runtime for executing agents more securely inside OpenShell with managed inference, a vendor-backed path for agent sandboxing. Global, pilot, permissive, self-hostable.
- [defending-code-reference-harness](https://github.com/anthropics/defending-code-reference-harness) - Anthropic skills for threat modeling, scanning, triage and patching plus an autonomous scanning harness, the defensive-AI counterpart to the skill packs above. Global, pilot, permissive, self-hostable.
- [AgentAegis](https://github.com/antgroup/agent-aegis) - Ant Group full-lifecycle runtime protection for autonomous agents covering prompt-injection detection, permission gating, behavior audit and resource circuit breakers. China-led, watch, permissive, self-hostable.

### Enterprise security substrate

- [Trivy](https://github.com/aquasecurity/trivy) - All-in-one scanner for container images, IaC, filesystems, SBOM and secrets. Global, production, permissive, self-hostable.
- [Wazuh](https://github.com/wazuh/wazuh) - Open-source unified XDR and SIEM for log analysis, threat detection and compliance monitoring; GPL-2.0, so legal review is mandatory before redistribution. Global, production, restricted, self-hostable.
- [Falco](https://github.com/falcosecurity/falco) - CNCF runtime security that detects anomalous syscalls and behavior in Kubernetes pods. Global, production, permissive, self-hostable.
- [Semgrep](https://github.com/semgrep/semgrep) - Fast multi-language static analysis (SAST); LGPL-2.1 core, so check terms for embedding. Global, production, conditional, self-hostable.
- [Gitleaks](https://github.com/gitleaks/gitleaks) - Secret scanner for Git repositories and CI to stop keys, tokens and credentials leaking into code. Global, production, permissive, self-hostable.
- [Nuclei](https://github.com/projectdiscovery/nuclei) - Fast, template-driven vulnerability scanner for exposed services and endpoints. Global, production, permissive, self-hostable.
- [OWASP ZAP](https://github.com/zaproxy/zaproxy) - The de-facto open dynamic application security testing (DAST) web-app scanner. Global, production, permissive, self-hostable.
- [OSV-Scanner](https://github.com/google/osv-scanner) - Dependency vulnerability scanner over the OSV database for supply-chain checks. Global, production, permissive, self-hostable.

### Standards and frameworks

- [OWASP Top 10 for LLM Applications and GenAI Security](https://genai.owasp.org/) - OWASP, 2025. The canonical risk taxonomy for LLM and GenAI apps plus the Agentic Security initiative.
- [MITRE ATLAS](https://atlas.mitre.org/) - MITRE. Adversarial Threat Landscape for AI Systems, an ATT&CK-style matrix of real-world attacks on ML and AI.
- [MITRE D3FEND](https://d3fend.mitre.org/) - MITRE. The defensive counterpart to ATT&CK, a knowledge graph of security countermeasures and mitigations.
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - NIST, 2023. The govern, map, measure and manage framework for making AI risk board-defensible.
- [NIST Cybersecurity Framework 2.0](https://www.nist.gov/cyberframework) - NIST, 2024. The foundational govern, identify, protect, detect, respond and recover framework for enterprise security programs.
- [Agent Skills standard (agentskills.io)](https://agentskills.io/) - Open spec. A standardized way to give AI agents new capabilities, the cross-vendor SKILL.md format both security-skill libraries above build on, portable across Claude Code, Copilot, Cursor, Codex CLI, Gemini CLI and 20-plus hosts.
- [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) - OWASP, 2025. The formal agentic counterpart to the LLM Top 10, peer-reviewed by over 100 experts, the de-facto checklist for securing agents that plan, act and use tools.
- [OWASP AI Security Solutions Landscape for Agentic AI](https://genai.owasp.org/resource/ai-security-solutions-landscape-for-agentic-ai-q2-2026/) - OWASP, 2026. Quarterly map of agent-security tooling across the agent lifecycle, the procurement companion to the Top 10.
- [NIST COSAiS](https://csrc.nist.gov/projects/cosais) - NIST, 2026. Control Overlays for Securing AI Systems, SP 800-53 overlays covering single-agent and multi-agent AI, the control baseline auditors will map to.
- [EU AI Act regulatory framework](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) - European Commission, 2026. The first-party obligations timeline, with transparency duties from August 2026 and high-risk obligations moved to December 2027.
- [China AI-agent regulation](https://www.cac.gov.cn/2026-05/08/c_1779979789472520.htm) - CAC, NDRC and MIIT, 2026. The first national regulatory framework specifically for AI agents, defining 19 application scenarios and tiered oversight for sensitive sectors.

## Autonomous Research

> The research accelerator for R&D and medical affairs; mostly watch for now, with non-standard licenses and reproducibility caveats.

- [AI-Scientist](https://github.com/SakanaAI/AI-Scientist) - Pioneering end-to-end autonomous research under a non-standard RAIL-derived license, so legal review is mandatory. Global, watch, restricted.
- [AI-Researcher](https://github.com/HKUDS/AI-Researcher) - HKU Data Intelligence Lab autonomous research system. Global, watch, permissive.
- [open-ai-co-scientist](https://github.com/llnl/open-ai-co-scientist) - Open reproduction of the Google AI co-scientist multi-agent system. Global, watch, permissive.
- [GPT-Researcher](https://github.com/assafelovic/gpt-researcher) - Autonomous deep-research agent. Global, pilot, permissive, self-hostable.
- [Arbor](https://github.com/RUC-NLPIR/Arbor) - Generalist autonomous research agent that runs experiments and iteratively self-optimizes; academic and early-stage. China-led, watch, permissive, self-hostable.
- [Tongyi DeepResearch](https://github.com/Alibaba-NLP/DeepResearch) - Alibaba open deep-research agent model plus the full training pipeline, topping open agent-model leaderboards. China-led, pilot, permissive, self-hostable.
- [autoresearch](https://github.com/karpathy/autoresearch) - AI agents autonomously running research experiments on nanochat training, the most-starred reference point for agentic research loops; it carries no license, so it is reference-only and cannot be adopted. Global, watch, restricted.

## Vibe Coding for Enterprise R&D

> The highest-ROI internal rollout: AI that makes your own engineers faster. Prefer self-hostable, bring-your-own-model agents you can point at an internal endpoint. Closed SaaS such as Cursor and Copilot is out of scope; their open-source ecosystem is not.

### Self-hosted Copilot and IDE assistants

- [Tabby](https://github.com/TabbyML/tabby) - Self-hosted Copilot replacement that runs its own completion and chat inference on your GPUs, fully air-gappable; open-core with enterprise features under a separate license. Global, production, conditional, self-hostable.
- [Continue](https://github.com/continuedev/continue) - Self-hostable VS Code and JetBrains assistant plus a governance hub to share approved rules and models across the org. Global, production, permissive, self-hostable.
- [Cline](https://github.com/cline/cline) - Most-starred in-editor autonomous agent with plan-act, MCP and terminal access, runnable against internal self-hosted endpoints. Global, production, permissive, self-hostable.
- [Kilo Code](https://github.com/Kilo-Org/kilocode) - All-in-one agentic VS Code platform in the Roo and Cline lineage, an active migration target now that Roo-Code is archived. Global, production, permissive, self-hostable.

### Terminal coding agents

- [Aider](https://github.com/Aider-AI/aider) - Battle-tested terminal pair-programmer with strong Git integration and repo-map context, bring your own model. Global, production, permissive, self-hostable.
- [Goose](https://github.com/aaif-goose/goose) - Block extensible on-machine agent that installs, edits, runs and tests, with an MCP-based extension model. Global, production, permissive, self-hostable.
- [OpenCode](https://github.com/anomalyco/opencode) - Model-agnostic terminal coding agent that works against OpenAI-compatible endpoints. Global, production, permissive, self-hostable.
- [Qwen Code](https://github.com/QwenLM/qwen-code) - Terminal agent tuned for the open-weight Qwen-Coder family, the cleanest path to a fully on-prem open-weight coding stack. China-led, production, permissive, self-hostable.
- [Codex CLI](https://github.com/openai/codex) - OpenAI Apache-2.0 terminal agent and scriptable harness that defaults to OpenAI-hosted models, so it is not air-gapped by default. Global, production, permissive.
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) - Google Apache-2.0 terminal agent and a popular fork base; an open client with a hosted model by default. Global, production, permissive.
- [Mistral Vibe](https://github.com/mistralai/mistral-vibe) - Minimal CLI coding agent from Mistral, the only EU-vendor first-party open coding agent, relevant under EU data-sovereignty constraints. Global, pilot, permissive, self-hostable.

### Autonomous software engineering and harness

- [SWE-agent](https://github.com/SWE-agent/SWE-agent) - Reference GitHub issue-to-patch agent that runs in your own sandbox, a base for internal issue-automation experiments. Global, pilot, permissive, self-hostable.
- [Superpowers](https://github.com/obra/superpowers) - A curated skills and methodology harness you can vendor internally to standardize how coding agents behave; pin a commit before org-wide use. Global, pilot, permissive.
- [open-code-review](https://github.com/alibaba/open-code-review) - Hybrid deterministic-pipeline and LLM-agent code-review tool battle-tested at Alibaba scale, a production guardrail for AI-generated code entering enterprise repositories. China-led, pilot, permissive, self-hostable.

### Practices and playbooks

- [Equipping Agents for the Real World with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) - Anthropic, 2025. The practice behind Skills, packaging team know-how as composable SKILL.md folders of instructions, scripts and resources, with symptom-to-solution maps and a growing gotchas list that captures each real-world failure.
- [How Anthropic Teams Use Claude Code](https://www.anthropic.com/news/how-anthropic-teams-use-claude-code) - Anthropic, 2025. A field report on how data science, security, design, growth and legal teams wire coding agents into daily work.
- [The Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf) - Anthropic, 2025. The build reference covering a lean SKILL.md with progressive disclosure, deterministic scripts, one job per skill, and skills that evolve from a few lines to gotchas to validation scripts.
- [Agentic Engineering Patterns](https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/) - Simon Willison, 2026. The community's de-facto practice handbook on professional coding-agent work, from "writing code is cheap now" to red-green TDD for agents.
- [Scaling Managed Agents](https://www.anthropic.com/engineering/managed-agents) - Anthropic, 2026. Decouple the brain from the hands: virtualize the harness versus sandboxes, sessions and tools behind stable interfaces so agent systems survive model upgrades.
- [How We Contain Claude](https://www.anthropic.com/engineering/how-we-contain-claude) - Anthropic, 2026. Layered agent containment via gVisor, OS sandboxes, virtual machines and egress controls; the weakest layer is the one you built yourself.
- [2026 Agentic Coding Trends Report](https://resources.anthropic.com/2026-agentic-coding-trends-report) - Anthropic, 2026. The delegation gap: AI touches about 60 percent of work but is fully delegable in only 0 to 20 percent.
- [How Agents Are Transforming Work](https://openai.com/index/how-agents-are-transforming-work/) - OpenAI, 2026. Quantified agent-native work inside a frontier lab, with 97.9 percent of staff using Codex and over 70 percent delegating tasks longer than an hour.

## Internal Knowledge Base

> Turn scattered company knowledge such as documents, wikis, PDFs and the open web into an AI-queryable base: a self-hosted search front, research and literature tooling, and web collection to feed it. Many strong picks are copyleft or open-core, so review the license before any SaaS redistribution.

### Knowledge base and enterprise search apps

- [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) - Local-first all-in-one RAG workspace with document connectors, agents and per-workspace access control; air-gap-friendly. Global, production, permissive, self-hostable.
- [Onyx](https://github.com/onyx-dot-app/onyx) - Enterprise search and chat over 40-plus connectors such as Slack, Drive and Confluence with RBAC and document-level permissions; an open Glean alternative, open-core with a proprietary enterprise edition. Global, production, conditional, self-hostable.
- [MaxKB](https://github.com/1Panel-dev/MaxKB) - Turnkey enterprise knowledge-base and agent platform with a workflow builder, a top on-prem chatbot choice in China; GPL-3.0, so review before redistribution. China-led, production, restricted, self-hostable.
- [Khoj](https://github.com/khoj-ai/khoj) - Self-hostable second-brain search over documents and the web with custom agents and scheduled automations, under network-copyleft AGPL-3.0. Global, production, restricted, self-hostable.
- [DocsGPT](https://github.com/arc53/DocsGPT) - Private document question-answering and enterprise-search platform with agents and API connectivity. Global, pilot, permissive, self-hostable.
- [WeKnora](https://github.com/Tencent/WeKnora) - Tencent LLM knowledge platform combining RAG question answering, a ReAct agent and a self-maintaining wiki, with auto-sync from Feishu, Notion and Yuque; MIT with listed third-party components. China-led, production, permissive, self-hostable.

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
- [openPangu 2.0](https://ai.gitcode.com/ascend-tribe/openPangu-2.0-Flash) - Huawei open-weight Pangu models natively optimized for Ascend, with the 92B Flash release on GitCode shipping weights, inference code and operators and the 505B Pro rolling out through 2026; custom openPangu model license, so legal review before commercial use. China-led, pilot, conditional, self-hostable.
- [LocalAI](https://github.com/mudler/LocalAI) - OpenAI-compatible local inference. Global, production, permissive, self-hostable, edge.
- [Jan](https://github.com/janhq/jan) - Offline AI assistant. Global, production, permissive, self-hostable, edge.
- [Ollama](https://github.com/ollama/ollama) - Local model runtime, MIT; mind trademark and commercial positioning rather than the license. Global, production, permissive, self-hostable, edge.
- [Open WebUI](https://github.com/open-webui/open-webui) - De-facto self-hosted chat and RAG front-end over local models that runs fully offline, under a custom license (BSD-3 plus a branding clause restricting white-labeling above 50 users), so review before rebranding and disable telemetry for true air-gap. Global, production, conditional, self-hostable.
- [GPT4All](https://github.com/nomic-ai/gpt4all) - Desktop offline LLM app needing no GPU or API, MIT and air-gap-clean, though release cadence has slowed so track maturity before standardizing. Global, pilot, permissive, self-hostable, edge.
- [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw) - Rust single-binary autonomous-assistant and agent infrastructure with swappable components and no cloud dependency, ideal for air-gapped and edge estates. Global, production, permissive, self-hostable, edge.
- [llmfit](https://github.com/AlexsJones/llmfit) - One command to determine which of hundreds of models and providers actually run on your hardware, answering the capacity-planning question before procurement. Global, pilot, permissive, self-hostable.

> Air-gap bundle: a self-carried starter kit of SKILL.md packages, an internal MCP manifest, agent definitions and an offline docker-compose lives in the repository at [/bundle](bundle/), assembling the self-hostable picks above into a zero-egress library for LAN deployment.

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
