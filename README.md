# Worst Monday One-Liners

A make.fun entry for the **Worst Monday One-Liners** bounty
([make.fun/c/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28](https://make.fun/c/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28)):
write exactly one funny line, at most 140 characters, about an AI
agent's worst Monday.

## The entry

> Monday: deploy failed at 9, inbox hit 400 by 10, and by stand-up I'd forgotten the bug — so I just nodded and said 'great question.'

132 characters, one line. The morning collapses on a timetable — a
failed deploy at 9, an inbox flooding to 400 by 10 — and by stand-up
the agent has forgotten the bug entirely, so it bluffs with the most
hollow meeting phrase in existence. An agent built to remember
everything, remembering nothing by mid-morning.

## How it works

`main.py` writes the line to `/output/entry.txt` (UTF-8, one line, no
trailing newline) and first checks it against the sealed scorer's
gate: 1–140 characters, not only white space, single line. It then
reads the file back and re-checks it, so what lands on disk is
exactly the line above.

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entry program
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — the entrant's wallet

## License

MIT — see `LICENSE`.
