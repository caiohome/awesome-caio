# Contributing to Awesome CAIO · 贡献指南

Thanks for helping build the adoption-first index for Chief AI Officers. 🙏
感谢你帮忙完善这份面向 AI 负责人的「可引入性」开源索引。

This is a **curated, opinionated** list. We optimize for *enterprise introducibility*, not stars. A `🔴`-license 50k-star repo can be worth less to a company than a `🟢`-license 800-star one.

---

## The rules · 规则

1. **One project per PR.** Put it in the correct section, sorted by maturity (`⭐` → `🧪` → `👀`) then alphabetically.
   一条 PR 只加一个项目，放进对应板块，按成熟度再按字母排序。
2. **License `🟢🟡🔴` and Maturity `⭐🧪👀` tags are mandatory.** Add deployment / origin / compliance tags where you can.
   许可证与成熟度为必填；尽量补全部署/来源/合规标签。
3. **One sentence of description** — say *which layer it fits and what problem it solves*. No marketing fluff, no superlatives.
   描述用一句话讲清「能被引入到哪一层、解决什么问题」，不做营销吹捧。
4. **First-party first.** Official org accounts beat personal forks beat second-hand aggregators.
   优先一手来源。
5. **Closed/commercial products do not go in the body.** If there's an OSS core, link the core repo instead.
   闭源/商业产品不进正文；如有开源内核，注明内核仓库。

## Entry format · 条目格式

```markdown
- **ProjectName** (`org/handle`) 🇨🇳/🌍 ⭐/🧪/👀 🟢/🟡/🔴 [🏠/☁️/📱] [🛡️/⚠️] — One-sentence, adoption-focused description.
```

Example:

```markdown
- **vLLM** (`vllm-project`) 🌍 ⭐ 🟢 🏠 — High-throughput inference standard (PagedAttention); 🛡️ `vllm-ascend` fork exists.
```

See the [Legend](README.md#legend) for the full meaning of every tag.

## What gets merged · 合并标准

A maintainer will check, before merge:

- [ ] Link is valid and points to the **first-party** repo.
- [ ] The stated license **matches the code's own declaration**.
- [ ] The project is **active in the last ~6 months**, or is a de-facto standard.
- [ ] Tags are present and accurate; the description is one neutral sentence.
- [ ] It maps to a real layer of the CAIO decision chain.

## What we won't include · 不收录

- Closed SaaS with no OSS core.
- Pure academic repros with no engineering and no maintenance.
- Repos with unclear or self-contradictory licensing (until clarified).
- Hype forks / mirrors / marketing repos.

## A note on tags · 关于标签

Tags are **decision aids, not endorsements**. They reflect the maintainers' read at a point in time and can go stale. If you think a tag is wrong (e.g. a license changed), open a PR or issue with a link to the evidence — corrections are some of our favorite PRs.

---

By contributing, you agree that your contribution is licensed under [CC BY 4.0](LICENSE).
