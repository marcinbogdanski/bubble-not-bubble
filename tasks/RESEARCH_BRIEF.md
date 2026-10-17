# Research brief for note-writing agents

You are writing one research note for the "Bubble or Not Bubble" project: an
evidence-backed assessment of whether the AI investment boom is a financial
bubble, differentiated by layer of the stack. Today's date is given in your
task. Treat your training memory as stale: **every number in the note must
come from a page you fetched during this task**, with its URL and access date.

## Rules

1. Read `research/TEMPLATE.md` and `report/methodology.md` first. Follow the
   template exactly: Summary, Key claims table, Analysis, Conflicts and open
   questions, Signals to watch, Sources.
2. Prefer primary sources: SEC EDGAR filings (10-K, 10-Q, 8-K, S-1, proxy),
   company investor-relations pages and press releases, earnings-call
   transcripts, exchange filings (TWSE, Euronext), statistical agencies,
   central banks. Then reputable secondary (Reuters, Bloomberg, FT, WSJ, CNBC,
   The Information, SemiAnalysis, Epoch AI) with the "secondary" type.
   Social media and aggregators are tertiary: use only as leads.
3. Grade every claim A–D as defined in `report/methodology.md`. Figures
   about private companies that come from leaks are grade C at best and are
   labelled "reported, unverified".
4. Be adversarial with yourself. For each major conclusion, search for the
   strongest contradicting evidence and record it in Conflicts. Do not
   resolve conflicts by omission.
5. Answer the project's questions for your topic: which parts are
   comfortably profitable, what the risks are, what is overextended, how it
   is financed and who bears losses if returns disappoint, and what we do not
   know.
6. Watch for unit and period traps: fiscal years (Nvidia ends late January,
   Microsoft June, Oracle May, Applied Materials October), currencies (TWD,
   EUR, KRW), run-rate vs trailing, bookings vs revenue, guidance vs actual.
7. Length: 1,500–3,500 words. Claim table: 15–40 rows. Signals table: 5–12
   rows with current values.
8. If a useful time series exists (quarterly capex, revenue, monthly sales,
   price index), save it as CSV in `data/<topic>-<series>.csv` with a leading
   `# source: URL, accessed YYYY-MM-DD, units` comment line.
9. Write only your note and your CSV files. Do not edit other files. Do not
   run git commands. Do not start servers. **Do not spawn subagents**: do the
   work in your own context. If search budget runs out, fetch primary URLs
   directly (SEC EDGAR, company IR pages).
10. Finish by reporting: the files you wrote, a 10-line summary of findings,
    the three biggest uncertainties, and any claims you could not verify.
