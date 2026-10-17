#!/bin/zsh
# Weekly lead scan and verification. Usage: scripts/scan.sh YYYY-MM-DD
set -e
DATE=${1:-$(date +%Y-%m-%d)}
REPO=$(cd "$(dirname "$0")/.." && pwd)
mkdir -p "$REPO/tasks/grok"
RAW="$REPO/tasks/grok/$DATE-scan.md"
grok -p "Today is $DATE. Search x.com and the web for posts and articles from the last 7 days relevant to whether AI investment is a bubble: AI bubble debate; hyperscaler capex and guidance; Nvidia, OpenAI, Anthropic, Oracle, CoreWeave, AMD, Broadcom deals and financing (circular financing, vendor financing, SPVs, bond issuance, private credit); CDS spreads and bond prices of CoreWeave, Oracle and datacenter project bonds; GPU rental price moves; new lab revenue or funding figures; datacenter power constraints; China (DeepSeek, Huawei, export controls); macro (CPI, Fed, rates, oil) as it affects AI names; notable bearish and bullish takes from credible analysts. For each item: date, poster handle or outlet, one-line claim, numbers, and the URL of the primary source if one exists. 25-40 items, grouped by topic, most consequential first. Mark rumours vs sourced. Markdown." > "$RAW"
echo "Grok scan saved to $RAW"
codex exec --skip-git-repo-check -C "$REPO" -m gpt-6.1-sol "Today is $DATE. Read report/methodology.md, signals/README.md and signals/2026-10-17.md (format example). Then read tasks/grok/$DATE-scan.md, a Grok scan of x.com and the web for the past 7 days. Grok output is a lead, never a citation. Trace each substantive item to a primary or reputable secondary source with web search and fetch; record what the source says, with figures and dates, and whether it confirms, partly confirms or does not confirm the claim; grade A-D. Do not cite x.com posts as evidence. Write signals/$DATE.md in the same format as signals/2026-10-17.md, including a 'What changed this week' summary and an 'Implications for research notes and forecasts' section that names the notes under research/ and the forecast IDs in forecasts/register.md each verified fact affects. Append verified CDS and bond-yield observations to data/credit-spreads.csv. Write only those two files. Do not run git."
echo "Signals written to signals/$DATE.md"
