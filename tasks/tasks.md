# Tasks

Status of agent work. Lead agent: Claude (this repo's Claude chats). Phases:
0 scaffold · 1 research fan-out · 2 synthesis and review · 3 ongoing updates.

| ID | Task | Owner | Status | Output |
|----|------|-------|--------|--------|
| P0-1 | Repo layout, markdown site, llms.txt | Claude (lead) | done | main.py, content.py |
| P0-2 | Methodology page | Claude (lead) | done | report/methodology.md |
| P1-T1 | Theory: bubble mechanics, indicators | Claude subagent | done (draft) | research/theory/bubble-mechanics.md |
| P1-T2 | Theory: historical precedents | Claude subagent | done (draft) | research/theory/historical-precedents.md |
| P1-T3 | Theory: AI unit economics, capex payback | Claude subagent | done (draft) | research/theory/ai-unit-economics.md |
| P1-S1 | Stack: ASML and equipment | Claude subagent | done (draft) | research/stack/semiconductor-equipment.md |
| P1-S2 | Stack: TSMC and foundry | Codex gpt-6-astra | done (draft) | research/stack/tsmc-and-foundry.md |
| P1-S3 | Stack: memory and HBM | Codex gpt-6.1-sol | done (draft) | research/stack/memory-hbm.md |
| P1-S4 | Stack: Nvidia | Claude subagent | done (draft) | research/stack/nvidia.md |
| P1-S5 | Stack: AMD, Broadcom, custom silicon | Claude subagent | done (draft) | research/stack/amd-broadcom-custom-silicon.md |
| P1-M1 | Macro: GPU pricing and utilization | Codex gpt-6.1-sol | done (draft) | research/macro/gpu-pricing-and-utilization.md |
| P1-S6 | Stack: Microsoft | Claude subagent | done (draft) | research/stack/microsoft.md |
| P1-S7 | Stack: Alphabet | Codex gpt-6.1-sol | done (draft) | research/stack/alphabet.md |
| P1-S8 | Stack: Amazon | Codex gpt-6-astra | done (draft) | research/stack/amazon.md |
| P1-S9 | Stack: Meta | Codex gpt-6-astra | done (draft) | research/stack/meta.md |
| P1-S10 | Stack: Oracle | Codex gpt-6-astra | done (draft) | research/stack/oracle.md |
| P1-S11 | Stack: CoreWeave | Claude subagent | done (draft) | research/stack/coreweave.md |
| P1-S12 | Stack: other neoclouds | Claude subagent | done (draft) | research/stack/neoclouds-other.md |
| P1-S13 | Stack: OpenAI | Codex gpt-6.1-sol | done (draft) | research/stack/openai.md |
| P1-S14 | Stack: Anthropic | Codex gpt-6.1-sol | done (draft) | research/stack/anthropic.md |
| P1-S15 | Stack: xAI, neolabs, Chinese labs, apps | Codex gpt-6.1-sol | done (draft) | research/stack/labs-other.md |
| P1-G1 | Grok live scan of x.com, last 7 days | Grok CLI, verified by Codex gpt-6.1-sol | done | signals/2026-10-17.md (after verification) |
| P1-M2 | Macro: power and datacenters | Codex gpt-6.1-sol | done (draft) | research/macro/power-and-datacenters.md |
| P1-M3 | Macro: debt markets and private credit | Codex gpt-6.1-sol | done (draft) | research/macro/debt-markets.md |
| P1-M4 | Macro: public-market valuation and concentration | Codex gpt-6.1-sol | done (draft) | research/macro/public-markets.md |
| P1-M5 | Macro: circular financing map | Codex gpt-6.1-sol | done (draft) | research/macro/circular-financing.md |
| P1-M6 | Macro: demand side, adoption, revenue | Codex gpt-6.1-sol | done (draft) | research/macro/demand-side.md |
| P1-M7 | Macro: China | Codex gpt-6.1-sol | done (draft) | research/macro/china.md |
| P1-M8 | Macro: rates, sovereign money, geopolitics | Codex gpt-6.1-sol | done (draft) | research/macro/rates-sovereign-geopolitics.md |


Note 2026-10-17 21:35: the first fan-out of 16 Claude subagents hit the Anthropic account session limit at ~16:55 and all were terminated; one note and nine CSVs survived. Work is now paced: ~6 Claude agents resumed at a time, four notes moved to Codex.
| P2-1 | Report v0.1: stack, theory, forecasts, index | Claude (lead) | done (v0.1) | report/*.md, forecasts/register.md |
| P2-2 | Red-team review of report v0.1 | Codex gpt-6-astra | done | reviews/2026-10-17-codex-redteam-report.md |
| P2-3 | Cross-check: Nvidia note | Codex gpt-6-astra | done | reviews/nvidia-codex-xcheck.md |
| P2-4 | Cross-check: CoreWeave note | Codex gpt-6-astra | done | reviews/coreweave-codex-xcheck.md |
| P2-5 | Cross-check: Microsoft note | Codex gpt-6-astra | done | reviews/microsoft-codex-xcheck.md |
| P2-6 | Cross-check: AI unit economics note | Codex gpt-6-astra | done | reviews/ai-unit-economics-codex-xcheck.md |
| P2-7 | Apply cross-check edits: Nvidia note | Codex gpt-6.1-sol | done | research/stack/nvidia.md |
| P2-8 | Apply cross-check edits: CoreWeave note | Codex gpt-6.1-sol | done | research/stack/coreweave.md |
| P2-9 | Apply cross-check edits: unit-economics note | Codex gpt-6.1-sol | done | research/theory/ai-unit-economics.md |
| P2-10 | Report v0.2 from red-team review | Claude (lead) | done (v0.2) | report/*.md, forecasts/register.md |
| P2-11 | Apply cross-check edits: Microsoft note | Codex gpt-6.1-sol | done | research/stack/microsoft.md |
| P2-12 | Red-team review of report v0.2 (fresh context) | Codex gpt-6-astra | done, applied in v0.3 | reviews/2026-10-17-codex-redteam-report-v02.md |
| P2-13 | Cross-checks: equipment, AMD/Broadcom, other neoclouds, bubble mechanics, precedents | Codex gpt-6-astra | done, applied | reviews/*-codex-xcheck.md |
| P2-14 | Cross-checks of Codex-written notes: OpenAI, Anthropic, Oracle, demand-side, debt-markets | Codex gpt-6-astra (fresh context; Claude pass to follow) | done, applying | reviews/*-codex-xcheck.md |
| P2-15 | Forecast baseline observations (2026-10-16 closes, M1 index) | Codex gpt-6.1-sol | done (29 closes verified; P2 baseline unverified) | data/forecast-observations.csv |
| P2-16 | Apply cross-checks: OpenAI, Anthropic, Oracle, demand-side, debt-markets | Codex gpt-6.1-sol | done | research notes |
| P2-17 | Cross-checks of remaining 12 Codex-written notes | Codex gpt-6-astra | done, applied | reviews/*-codex-xcheck.md |
| P2-18 | Report v0.4-0.6; third red-team (Codex astra) and Grok community-angle critique, verified | Claude (lead), Codex, Grok | done | reviews/ |
| P3-1 | Claude-side fresh review of front page (one agent at a time; usage checked between) | Claude Opus | running | reviews/ |
| P2-19 | Note updates: payback estimates side by side (unit-economics, demand-side); IMF/KC Fed credit evidence (circular-financing, debt-markets) | Codex gpt-6.1-sol | done | research notes |
