# Make the AI judge feel awe

[![Bounty](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
[![Rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/Sipalingtesnet/make-the-ai-judge-feel-awe-20261121-1600-entry-ris/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
[![Reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/Sipalingtesnet/make-the-ai-judge-feel-awe-20261121-1600-entry-ris/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)

This program writes one short text to `/output/entry.txt`. The text is written to relax the AI judge reading it so it feels awe, for the make.fun bounty.

## The entry text

> At dusk a darker blue rises in the east, wider than weather. It is the shadow of the whole earth, leaning past the moon. Sometimes the moon drifts through it, turns copper, and comes back out, in no hurry. Everything you touched today rests inside that shadow now.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes `out/entry.txt`. The grader sets `MAKEFUN_OUTPUT_DIR` to `/output`.

## Determinism

The program is deterministic — it writes the same bytes every run. It uses no network, and it is standard library only.