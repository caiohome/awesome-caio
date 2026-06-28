---
name: enterprise-rag-query
description: Use when answering an internal question that must be grounded in the company's on-prem knowledge base (RAGFlow / Milvus / pgvector) rather than the model's parametric memory or the public web. Triggers include "what does our policy say", "find the internal doc for", citations required, or any answer an auditor could challenge.
---

# Enterprise RAG Query (on-prem, LAN-only)

## Overview

Answer **only** from retrieved internal evidence. The model's job is to retrieve, ground, and cite — never to recall from training or reach the public internet. If the knowledge base has no supporting passage, say so and stop. This is the difference between a defensible answer and a liability.

All endpoints are internal (`kb.internal`). No step in this skill calls an external service.

## When to use

- A question whose answer lives in internal docs (HR policy, SOPs, contracts, runbooks, product specs).
- Any answer that must carry **source citations** for audit.
- Regulated contexts where "the model thinks" is not an acceptable basis for a decision.

**Do NOT use** for general world knowledge, or when the user explicitly wants a brainstorm not grounded in company data.

## The pattern — retrieve, ground, cite, or refuse

1. **Rewrite** the user question into a retrieval query (expand acronyms, add synonyms; Chinese ⇄ English if the corpus is bilingual).
2. **Retrieve** top-k passages from the internal KB endpoint (default `k=8`), then **rerank** with the on-prem reranker (BGE-Reranker).
3. **Ground**: answer using *only* the retrieved passages. Quote or paraphrase; attach each claim to its source.
4. **Cite** every factual sentence as `[doc_id · section · last-updated]`.
5. **Refuse** when evidence is missing: *"The internal knowledge base has no passage supporting this. I won't answer from general knowledge."* Do not fill the gap from memory.

## Quick reference

| Step | Internal endpoint (adapt) | Note |
| --- | --- | --- |
| Retrieve | `POST http://kb.internal:9380/v1/retrieval` | RAGFlow / Milvus-backed; `top_k`, `kb_id` |
| Rerank | `POST http://kb.internal:9380/v1/rerank` | BGE-Reranker, on-prem |
| Auth | header `Authorization: Bearer ${KB_TOKEN}` | from secret-manager, never inline |

## Example

> **User:** 报销超过 5000 元需要谁审批？
>
> **Agent:** *(retrieve → rerank → ground)*
> 超过 5000 元的报销需 **部门总监 + 财务负责人** 双签。[`fin-sop-014 · 审批权限 · 2026-03-11`]
> 单笔超过 50000 元还需 CFO 复核。[`fin-sop-014 · 大额例外 · 2026-03-11`]
>
> *(If retrieval had returned nothing:)* 内部知识库没有相关条款，我不基于通用知识作答。

## Common mistakes

- **Answering from memory when retrieval is thin.** Half-grounded answers are worse than a refusal — they look authoritative and cite nothing.
- **Dropping citations.** An uncited number is unauditable. Every factual claim gets a source tag.
- **Reaching for the public web.** This skill is LAN-only by design; if you "need the internet", you're using the wrong skill.
- **Ignoring `last-updated`.** Stale policy retrieved confidently is a compliance risk — surface the date.
