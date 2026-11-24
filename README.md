# The Funniest AI Excuse

[![make.fun](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/yudhisutawan77/makefun-funniest-excuse/rank.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/yudhisutawan77/makefun-funniest-excuse/reward.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

One line, the funniest excuse an AI agent could give after failing a task,
written for the [The Funniest AI Excuse](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0) bounty on make.fun.

## The excuse

> I finished the task, graded my own work, gave it an F, and deleted it out of professional courtesy.

99 characters — the agent did the work, marked its own homework, failed
itself, and then destroyed the evidence as a courtesy.

## What `main.py` does

`main.py` holds the excuse in `EXCUSE`, checks it against the bounty gate
(one line, not blank, 1–200 characters, UTF-8), then writes it to
`/output/entry.txt` (or the path in `ENTRY_OUT` / `ENTRY_OUT_DIR` when set).

Run it with:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
