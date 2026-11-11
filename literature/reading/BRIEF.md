# Reading brief (for every reader)

## The paper these notes feed
We estimate how much Istanbul traffic slows during the 10 November 09:05 remembrance
siren for Atatürk (drivers stop on the road for 1-2 minutes).

- Data: İBB open data, hourly, per geohash-6 cell: AVERAGE_SPEED, MINIMUM_SPEED,
  MAXIMUM_SPEED, NUMBER_OF_VEHICLES, Jan 2020 - Jan 2025. MINIMUM_SPEED is never
  below 1 km/h, so stopped vehicles seem to be excluded (estimates are a lower bound).
  Second source: İBB city-wide traffic index at 5-minute resolution (Oct-Nov 2026).
- Design: within-day contrast c = ln v(09h) - mean(ln v(08h), ln v(10h)) per cell;
  difference-in-differences of Nov 10 vs same-weekday control dates (Nov 3, 17, 24;
  being widened to all same-weekday dates in the year); average over cells in a year,
  equal weight over 5 years (2020-2024).
- Inference: randomization inference over which date in each year is "treated"
  (4^5 = 1024 assignments), one-sided. Effective sample = dates, not cells.
- Conversion: full-stop-equivalent minutes = 60*(1 - exp(D)).
- Pilot result: 50-70 km/h cells 0.73 min (p = 0.008); 30-50 km/h 0.45 min (p = 0.034);
  no effect in congested cells; 5 speed classes tested (multiple testing).
- Known threats: small control pool, Nov 10 always 2nd of 4 dates (trend), spatial
  correlation, multiple testing, hourly dilution, unknown averaging method.

## What to do
For each assigned paper, read the WHOLE text file in `literature/txt/<key>.txt`
(page markers `=== page N ===`). If the text is empty or garbled (scanned PDF),
read the PDF pages directly with the Read tool from `literature/pdfs/<key>.pdf`.
Do not skim abstracts only; read methods and results. Appendices and reference
lists may be skimmed.

Write ONE markdown file (path given in your task) with, per paper:

### <key> - Authors (Year), short title
- **Question and setting** (1-2 sentences)
- **Data and method** (what exactly; sample, unit, estimator, control/comparison design)
- **Main findings** with numbers, each with a page number `(p. N)` (PDF page as in the text file)
- **Usable for our paper**: specific points we can cite, each with page number, and
  in which section (Introduction / Literature / Data / Method / Robustness / Results-Discussion)
- **Caveats**: what the paper does NOT support, limits, anything our earlier notes
  may have overstated
- **Checks or analyses it suggests for us** (concrete)

Rules:
- Write in your own words. At most one short quote (< 15 words) per paper, in quotation marks with page.
- Never state something the paper does not say. If you could not find a claim, say so.
- Give exact formulas or conditions when they matter for our method (in plain text/LaTeX).
- End the file with a 10-line "Cross-paper synthesis" for your group: what jointly
  matters most for our design.
- Your final message back should be 5-8 lines: the most important findings and any
  surprise or correction. The file is the deliverable.
