# intertest

Engineering quality disciplines — systematic debugging, test-driven development, and verification gates.

## Overview

3 skills, 0 agents, 0 commands, 0 hooks. Standalone plugin extracted from Clavain.

## Skills

| Skill | What it does |
|-------|-------------|
| `systematic-debugging` | 4-phase root-cause investigation — read, reproduce, analyze, verify |
| `test-driven-development` | Strict RED-GREEN-REFACTOR — no production code without a failing test |
| `verification-before-completion` | Iron-law evidence gates — no completion claims without fresh evidence |

## Quick Commands

```bash
python3 -c "import json; json.load(open('.claude-plugin/plugin.json'))"  # Manifest check
ls skills/*/SKILL.md | wc -l  # Should be 3
```

## Design Decisions (Do Not Re-Ask)

- General-purpose engineering disciplines — not tied to any specific framework
- Extracted from Clavain — quality methodology is a separable concern
- Skills reference each other (TDD ↔ verification) — they belong together
