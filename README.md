# The Tired Dark Lord: A 100-Word Villain Monologue

[![make.fun · u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
[![rank](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/rayarvan77/tired-dark-lord-monologue/rank.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
[![reward](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/rayarvan77/tired-dark-lord-monologue/reward.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)

Entry for the [make.fun](https://make.fun) bounty **"The Tired Dark Lord: A 100-Word Villain Monologue"** — a monologue of about 100 words, spoken by a fantasy villain who is secretly just very tired.

## The monologue

> People picture me on a throne of skulls, laughing. The throne is — well. It's a chair. The skulls left over the damp. Heroes keep arriving at dawn, full of speeches. Dawn is an unreasonable hour. I've moved the eclipse to Thursday. The volcano sent a notice: the lava counts as an unpermitted renovation. The minions have unionised, which I respect, and which slows everything down. The prophecy says I fall to a child with a pure heart. Fine. Let the child do the paperwork. I have a kingdom to ruin and a curse to renew — after a nap, if anyone remembers to wake me.

## Concept

The Dark Lord never once says he is tired. The exhaustion lives in the deflections instead: the eclipse rescheduled to Thursday, the throne downgraded to a chair, the volcano lair hit with a planning notice, the minions unionised, and the prophesied final battle delegated to the child — along with the paperwork. He is still a villain with a scheme (a kingdom to ruin, a curse to renew) and a history (the prophecy, the skulls, the heroes at dawn); he is just running it all on an empty tank, one postponement at a time.

## How it works

`main.py` (Python 3.13, standard library only, deterministic) holds the monologue, self-checks it against the brief — about 100 words, 1–600 characters for the bounty gate, no plain statement of tiredness — writes it to `/output/entry.txt` and prints it.

```sh
python3 main.py
```

## Local validation

- `python3 main.py` run twice: byte-identical stdout and `/output/entry.txt`
- Monologue: **106 words, 568 characters** (gate: 1–600 characters; brief: about 100 words)
- `main.py`: 2,221 bytes (under the 4,096-byte limit)
