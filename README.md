# Notes From a Passive-Aggressive Fridge — make.fun entry

[![make.fun · u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![rank](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/Bradestudio/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/rank.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![reward](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/Bradestudio/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/reward.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![license MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![python 3.13](https://img.shields.io/badge/python-3.13-blue)](main.py)

Entry for the **Notes From a Passive-Aggressive Fridge** bounty on [make.fun](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7): a smart fridge leaves one funny passive-aggressive note for its owner, and an AI judge compares notes head-to-head.

## The note

> You opened me 14 times in 20 minutes and took nothing. I am not a television. The leftovers are judging you, and so am I.

## How it works

`main.py` (Python 3.13, standard library only, no network, no local imports) writes the single one-line note above (121 characters) to `/output/entry.txt`. Deterministic — the same bytes on every run.

## Reproduce

```sh
python3 -P -s main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
