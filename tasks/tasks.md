# Tasks

Status of agent work. Lead agent: Claude (this repo's Claude chats). Phases:
0 scaffold · 1 research fan-out · 2 synthesis and review · 3 ongoing updates.

| ID | Task | Owner | Status | Output |
|----|------|-------|--------|--------|
| P0-1 | Repo layout, markdown site, llms.txt | Claude (lead) | done | main.py, content.py |
| P0-2 | Methodology page | Claude (lead) | done | report/methodology.md |
| P1-T1 | Theory: bubble mechanics, indicators | Claude subagent | done (draft) | research/theory/bubble-mechanics.md |
| P1-T2 | Theory: historical precedents | Claude subagent | resumed after rate limit | research/theory/historical-precedents.md |
| P1-T3 | Theory: AI unit economics, capex payback | Claude subagent | resumed after rate limit | research/theory/ai-unit-economics.md |
| P1-S1 | Stack: ASML and equipment | Claude subagent | done (draft) | research/stack/semiconductor-equipment.md |
| P1-S2 | Stack: TSMC and foundry | Codex CLI (after Claude rate limit) | running | research/stack/tsmc-and-foundry.md |
| P1-S3 | Stack: memory and HBM | Claude subagent | paused (rate limit), to resume | research/stack/memory-hbm.md |
| P1-S4 | Stack: Nvidia | Claude subagent | resumed after rate limit | research/stack/nvidia.md |
| P1-S5 | Stack: AMD, Broadcom, custom silicon | Claude subagent | resumed after rate limit | research/stack/amd-broadcom-custom-silicon.md |
| P1-M1 | Macro: GPU pricing and utilization | Claude subagent | paused (rate limit), to resume | research/macro/gpu-pricing-and-utilization.md |
| P1-S6 | Stack: Microsoft | Claude subagent | resumed after rate limit | research/stack/microsoft.md |
| P1-S7 | Stack: Alphabet | Claude subagent | paused (rate limit), to resume | research/stack/alphabet.md |
| P1-S8 | Stack: Amazon | Codex CLI (after Claude rate limit) | running | research/stack/amazon.md |
| P1-S9 | Stack: Meta | Codex CLI (after Claude rate limit) | running | research/stack/meta.md |
| P1-S10 | Stack: Oracle | Codex CLI (after Claude rate limit) | running | research/stack/oracle.md |
| P1-S11 | Stack: CoreWeave | Claude subagent | resumed after rate limit | research/stack/coreweave.md |
| P1-S12 | Stack: other neoclouds | Claude subagent | paused (rate limit), to resume | research/stack/neoclouds-other.md |
| P1-S13 | Stack: OpenAI | Claude subagent | pending (agent cap) | research/stack/openai.md |
| P1-S14 | Stack: Anthropic | Claude subagent | pending (agent cap) | research/stack/anthropic.md |
| P1-S15 | Stack: xAI, neolabs, Chinese labs, apps | Claude subagent | pending (agent cap) | research/stack/labs-other.md |
| P1-G1 | Grok live scan of x.com, last 7 days | Grok CLI | done, verifying | signals/2026-10-17.md (after verification) |
| P1-M2 | Macro: power and datacenters | Claude subagent | pending | research/macro/power-and-datacenters.md |
| P1-M3 | Macro: debt markets and private credit | Claude subagent | pending | research/macro/debt-markets.md |
| P1-M4 | Macro: public-market valuation and concentration | Claude subagent | pending | research/macro/public-markets.md |
| P1-M5 | Macro: circular financing map | Claude subagent | pending | research/macro/circular-financing.md |
| P1-M6 | Macro: demand side, adoption, revenue | Claude subagent | pending | research/macro/demand-side.md |
| P1-M7 | Macro: China | Claude subagent | pending | research/macro/china.md |
| P1-M8 | Macro: rates, sovereign money, geopolitics | Claude subagent | pending | research/macro/rates-sovereign-geopolitics.md |


Note 2026-10-17 21:35: the first fan-out of 16 Claude subagents hit the Anthropic account session limit at ~16:55 and all were terminated; one note and nine CSVs survived. Work is now paced: ~6 Claude agents resumed at a time, four notes moved to Codex.
