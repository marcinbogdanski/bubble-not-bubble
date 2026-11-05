#!/bin/zsh
# Step 1 of an update: Grok lead scan, then Codex verification.
#   zsh process/scan.sh SINCE [TODAY]      e.g. process/scan.sh 2026-10-26
# Writes work/TODAY-scan.md (raw leads) and work/TODAY-verified.md (checked
# facts with an implications table). Both are working files, ignored by git.
set -e
SINCE=$1; TODAY=${2:-$(date +%Y-%m-%d)}
[[ -n "$SINCE" ]] || { echo "usage: process/scan.sh SINCE [TODAY]"; exit 1; }
REPO=${0:A:h:h}; mkdir -p "$REPO/work"
# Grok writes its own working folders into the current directory, so run it
# inside work/ where they are ignored and cleared with everything else.
cd "$REPO/work"
ASK="For each item: date, outlet or poster, one-line claim, numbers, and the URL of the primary source if one exists. 25-40 items, grouped by topic, most consequential first. Mark rumour versus sourced. Markdown."

grok -p "Today is $TODAY. Search x.com and the web for $SINCE to $TODAY on whether AI investment is a bubble: the bubble debate; hyperscaler capex and guidance; circular, vendor and SPV financing; bond issuance and private credit; CDS and bond prices of CoreWeave, Oracle and datacenter project bonds; GPU rental prices; lab revenue and funding; datacenter power; China (DeepSeek, Huawei, export controls); macro (CPI, Fed, rates, oil) as it affects AI names; notable bull and bear takes from credible analysts. $ASK" > $TODAY-scan-a.md &
grok -p "Today is $TODAY. List company events from $SINCE to $TODAY for: Nvidia, AMD, Broadcom, TSMC, ASML, Lam, Applied, KLA, Micron, SK Hynix, Samsung, Microsoft, Alphabet, Amazon, Meta, Oracle, CoreWeave, Nebius, other neoclouds, OpenAI, Anthropic, xAI, Mistral, Vertiv, GE Vernova, Equinix. Earnings and guidance, SEC filings (10-Q, 8-K, S-1), debt and equity raises, rating actions, large contracts, cancellations or deferrals, lawsuits and permits. $ASK" > $TODAY-scan-b.md &
wait
cat $TODAY-scan-a.md $TODAY-scan-b.md > $TODAY-scan.md && rm $TODAY-scan-[ab].md
cd "$REPO"
echo "Leads: work/$TODAY-scan.md"

codex exec --skip-git-repo-check -C "$REPO" -m gpt-6.1-sol "Today is $TODAY. Follow the 'Verify a scan' brief in process/briefs.md. Leads: work/$TODAY-scan.md. Window: $SINCE to $TODAY. Output: work/$TODAY-verified.md."
echo "Verified: work/$TODAY-verified.md"
