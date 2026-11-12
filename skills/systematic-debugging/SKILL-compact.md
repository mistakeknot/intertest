# Systematic Debugging (compact)

Establish a fast failing command, then investigate the root cause before fixing it.

## When to Invoke

Any bug, test failure, unexpected behavior, or performance issue — especially under time pressure or after a failed fix attempt.

## Iron Law

**No fixes without root cause investigation first.** If Phase 1 is incomplete, you cannot propose fixes.

## Four Phases

1. **Root Cause Investigation**
   - Read error messages completely (line numbers, stack traces, error codes)
   - Establish one command that fails on this exact bug in seconds; run and repeat it, recording elapsed time and failures/runs. Gather evidence until each run gives the same failure. Begin causal explanations after this gate.
   - Shrink inputs, setup, and operations one part at a time; rerun after each reduction and keep reductions that preserve the exact failure
   - Check recent changes (git diff, deps, config, environment)
   - In multi-component systems: add diagnostic logging at each boundary, run once, identify failing layer. Prefix every temporary debug log with `DEBUG-TEMP:` for one-search cleanup.
   - Trace data flow backward from symptom to source
   - **Done when:** The command has run and repeated with the same bug-specific failure in seconds, every remaining part of the case is necessary, and the failing path is traced.

2. **Pattern Analysis**
   - Find working examples of similar code in the codebase
   - Compare working vs broken — list every difference
   - Read reference implementations completely
   - Map dependencies, config, and assumptions
   - **Done when:** Working and failing paths, their differences, dependencies, and assumptions are recorded.

3. **Hypothesis and Testing**
   - Before testing any guess, write 3 to 5 possible causes in `investigation-notebook.md`, ranked by evidence, each with a prediction and an observation that would disprove it
   - Make the smallest possible change to test it
   - Test one variable at a time using the Phase 1 command, starting with the highest-ranked remaining guess
   - Log each prediction, command, result, and verdict (supported, ruled out, or inconclusive); restore experimental changes before testing the next guess. If all guesses are exhausted, gather evidence and write a fresh ranked list before testing again.
   - **Done when:** The notebook records experimental verdicts and evidence identifying the cause for Phase 4.

4. **Implementation**
   - Create a failing test case first (use TDD skill)
   - Implement a single fix addressing root cause
   - Re-run the same reproduction and report the rate after; label any timeout or retry as a workaround
   - Report must have a **Falsified hypotheses** section
   - Verify fix and check no other tests broke (verification-before-completion skill before claiming success)
   - Find temporary diagnostics with `rg -n 'DEBUG-TEMP:'` and remove each site; retain permanent skill instructions describing the prefix
   - **If 3+ fixes failed:** stop — question the architecture, discuss with human partner
   - **Done when:** The reproduction and relevant tests pass and the prefix search finds no temporary logs; after three failed fixes, further fixes wait for architectural discussion and an agreed next action.

## Red Flags — Return to Phase 1

- "Quick fix for now" / "Just try changing X"
- Proposing solutions before tracing data flow
- Each fix reveals a new problem in a different place
- "One more fix attempt" after 2+ failures

## Supporting Techniques

- `root-cause-tracing.md` — backward call-stack tracing
- `investigation-notebook.md` — notebook template and report shape
- `defense-in-depth.md` — multi-layer validation
- `condition-based-waiting.md` — replace arbitrary timeouts

---
*For examples and the rationalizations table, read SKILL.md.*
