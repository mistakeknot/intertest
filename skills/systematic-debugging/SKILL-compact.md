# Systematic Debugging (compact)

Root-cause investigation before fixes. No guessing, no quick patches.

## When to Invoke

Any bug, test failure, unexpected behavior, or performance issue — especially under time pressure or after a failed fix attempt.

## Iron Law

**No fixes without root cause investigation first.** If Phase 1 is incomplete, you cannot propose fixes.

## Four Phases

1. **Root Cause Investigation**
   - Read error messages completely (line numbers, stack traces, error codes)
   - Reproduce consistently — if not reproducible, gather more data
   - Check recent changes (git diff, deps, config, environment)
   - In multi-component systems: add diagnostic logging at each boundary, run once, identify failing layer
   - Trace data flow backward from symptom to source

2. **Pattern Analysis**
   - Find working examples of similar code in the codebase
   - Compare working vs broken — list every difference
   - Read reference implementations completely, don't skim
   - Map dependencies, config, and assumptions

3. **Hypothesis and Testing**
   - State one hypothesis: "X is root cause because Y"
   - Make the smallest possible change to test it
   - One variable at a time — don't fix multiple things at once
   - If it fails, form a new hypothesis (don't stack fixes)

4. **Implementation**
   - Create a failing test case first (use TDD skill)
   - Implement a single fix addressing root cause
   - Verify fix and check no other tests broke
   - **If 3+ fixes failed:** stop — question the architecture, discuss with human partner

## Red Flags — Return to Phase 1

- "Quick fix for now" / "Just try changing X"
- Proposing solutions before tracing data flow
- Each fix reveals a new problem in a different place
- "One more fix attempt" after 2+ failures

## Supporting Techniques

- `root-cause-tracing.md` — backward call-stack tracing
- `defense-in-depth.md` — multi-layer validation
- `condition-based-waiting.md` — replace arbitrary timeouts

---
*For examples, rationalizations table, and real-world impact data, read SKILL.md.*
