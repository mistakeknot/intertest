# Verification Before Completion (compact)

Evidence before claims, always. No completion claims without fresh verification.

## When to Invoke

Before ANY success/completion claim, commit, PR, task completion, or delegation handoff.

## Iron Law

**No completion claims without fresh verification evidence.** If you haven't run the command in this message, you cannot claim it passes.

## The Gate (5 steps, no shortcuts)

1. **Identify** — what command proves this claim?
2. **Run** — execute the full command (fresh, complete)
3. **Read** — full output, check exit code, count failures
4. **Verify** — does output actually confirm the claim?
5. **Claim** — only now state the result, with evidence

## What Each Claim Requires

| Claim | Requires | Not Sufficient |
|-------|----------|----------------|
| Tests pass | Test output: 0 failures | Previous run, "should pass" |
| Build succeeds | Build command: exit 0 | Linter passing |
| Bug fixed | Original symptom passes | "Code changed" |
| Agent completed | VCS diff shows changes | Agent reports success |
| Requirements met | Line-by-line checklist | Tests passing |

## Red Flags — STOP

- Using "should", "probably", "seems to"
- Expressing satisfaction before verification ("Great!", "Done!")
- Trusting agent success reports without independent check
- Relying on partial verification
- Any wording implying success without having run verification

## Key Patterns

```
Tests:   Run command -> see "34/34 pass" -> claim passes
Build:   Run build -> see exit 0 -> claim succeeds
Regress: Write test -> pass -> revert fix -> MUST FAIL -> restore -> pass
Agent:   Agent reports success -> check VCS diff -> verify changes
```

---
*For rationalization table and real-world failure examples, read SKILL.md.*
