---
name: systematic-debugging
description: Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes
---

# Systematic Debugging

## Overview

**Core principle:** ALWAYS find root cause before attempting fixes. Symptom fixes are failure.

**Violating the letter of this process is violating the spirit of debugging.**

## The Iron Law

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

If you haven't completed Phase 1, you cannot propose fixes.

## When to Use

Use for ANY technical issue:
- Test failures
- Bugs in production
- Unexpected behavior
- Performance problems
- Build failures
- Integration issues

**Use this ESPECIALLY when:**
- Under time pressure (emergencies make guessing tempting)
- "Just one quick fix" seems obvious
- You've already tried multiple fixes
- Previous fix didn't work
- You don't fully understand the issue

**Don't skip when:**
- Issue seems simple (simple bugs have root causes too)
- You're in a hurry (rushing guarantees rework)
- Manager wants it fixed NOW (systematic is faster than thrashing)

## The Four Phases

You MUST complete each phase before proceeding to the next.

### Phase 1: Root Cause Investigation

**BEFORE attempting ANY fix:**

1. **Read Error Messages Carefully**
   - Read each error and warning
   - They often contain the exact solution
   - Read stack traces completely
   - Note line numbers, file paths, error codes
   - **Done when:** The exact symptom and its location are recorded.

2. **Reproduce Consistently**
   - Build one command that exposes this exact bug, aiming for a run measured in seconds.
   - For intermittent failures, use a bounded loop that reports failures/runs; record its attempt limit and elapsed time. The rate can vary between runs.
   - Run the command and record the observed failure. If a fast reproduction is impractical, record why and use the fastest available command.
   - Begin causal explanations only after this command is established.
   - **Done when:** One executed command exposes this bug, with its failure count, run count, elapsed time, and any speed limitation recorded.

3. **Check Recent Changes**
   - What changed that could cause this?
   - Git diff, recent commits
   - New dependencies, config changes
   - Environmental differences
   - **Done when:** Relevant changes and environmental differences are recorded.

4. **Gather Evidence in Multi-Component Systems**

   Use `DEBUG-TEMP:` on every temporary debug log in source, or on both ends of a temporary diagnostic block. Find all sites from the repository root with `rg -n --hidden 'DEBUG-TEMP:' .` for cleanup.

   **WHEN system has multiple components (CI → build → signing, API → service → database):**

   **BEFORE proposing fixes, add diagnostic instrumentation:**
   ```
   For EACH component boundary:
     - Log what data enters component
     - Log what data exits component
     - Verify environment/config propagation
     - Check state at each layer

   Run once to gather evidence showing WHERE it breaks
   THEN analyze evidence to identify failing component
   THEN investigate that specific component
   ```

   **Example (multi-layer system):**
   ```bash
   # DEBUG-TEMP: begin temporary diagnostic block
   set -o pipefail
   {
   # Layer 1: Workflow
   echo "=== Secrets available in workflow: ==="
   echo "IDENTITY: ${IDENTITY:+SET}${IDENTITY:-UNSET}"

   # Layer 2: Build script
   echo "=== Env vars in build script: ==="
   env | grep IDENTITY || echo "IDENTITY not in environment"

   # Layer 3: Signing script
   echo "=== Keychain state: ==="
   security list-keychains
   security find-identity -v

   # Layer 4: Actual signing
   codesign --sign "$IDENTITY" --verbose=4 "$APP"
   } 2>&1 | sed 's/^/DEBUG-TEMP: /'
   # DEBUG-TEMP: end temporary diagnostic block
   ```

   **This reveals:** Which layer fails (secrets → workflow ✓, workflow → build ✗)
   - **Done when:** Boundary evidence locates the failing layer, or the system is confirmed to have one component; every temporary log carries the prefix.

5. **Trace Data Flow**

   **WHEN error is deep in call stack:**

   See `root-cause-tracing.md` in this directory for the complete backward tracing technique.

   **Quick version:**
   - Where does bad value originate?
   - What called this with bad value?
   - Keep tracing up until you find the source
   - Fix at source, not at symptom
   - **Done when:** The bad value is traced to its origin, or the error is confirmed to be local.

6. **Shrink the Failing Case**
   - Use the change history and traced path to choose reductions. Remove inputs, setup, and operations one at a time, rerunning the command after each reduction.
   - Keep reductions that preserve the same bug; restore necessary parts. For intermittent failures, compare against the baseline with the same attempt limit; gather more observations when a missing failure is inconclusive.
   - **Done when:** Each remaining part has been checked and is needed to expose the bug; the reduced command and its failure rate are recorded.

**Phase 1 exit — done when:** One executed command exposes this bug with counts, timing, and any speed limitation recorded; every remaining part of the reduced case is needed; the failing path is traced or the error is confirmed to be local. Keep this command for later experiments.

### Phase 2: Pattern Analysis

**Find the pattern before fixing:**

1. **Find Working Examples**
   - Locate similar working code in same codebase
   - What works that's similar to what's broken?
   - **Done when:** A comparable working path is identified, or its absence is recorded.

2. **Compare Against References**
   - If implementing pattern, read reference implementation COMPLETELY
   - Don't skim - read every line
   - Understand the pattern fully before applying
   - **Done when:** The relevant reference is read completely and its behavior is explained.

3. **Identify Differences**
   - What's different between working and broken?
   - List every difference, however small
   - Don't assume "that can't matter"
   - **Done when:** The working and failing paths have an explicit difference list.

4. **Understand Dependencies**
   - What other components does this need?
   - What settings, config, environment?
   - What assumptions does it make?
   - **Done when:** Required components, settings, and assumptions are listed.

### Phase 3: Hypothesis and Testing

**Scientific method:**

1. **Rank 3 to 5 Guesses**
   - Write 3 to 5 specific possible causes in the investigation notebook (`investigation-notebook.md`), ordered by supporting evidence.
   - Give each guess a predicted observation and a result that would disprove it.
   - Complete the ranked list before testing any guess.
   - **Done when:** The notebook contains 3 to 5 ranked causes, each with a falsifiable prediction, before the first experiment.

2. **Test Minimally**
   - Make the SMALLEST possible change to test hypothesis
   - One variable at a time
   - Test the highest-ranked remaining guess with the Phase 1 command.
   - **Done when:** One controlled experiment has a recorded command and result.

3. **Verify Before Continuing**
   - Record whether the prediction was supported, ruled out, or inconclusive; advance to Phase 4 only with evidence identifying the cause.
   - Restore the experimental change before testing the next ranked guess. If the list is exhausted, return to evidence gathering and write a fresh ranked list before testing again.
   - **Done when:** The notebook records a verdict and evidence, with either a supported cause or the next investigation step identified.

4. **When You Don't Know**
   - Say "I don't understand X"
   - Don't pretend to know
   - Ask for help
   - Research more
   - **Done when:** The knowledge gap and the evidence or help needed to resolve it are explicit.

### Phase 4: Implementation

**Fix the root cause, not the symptom:**

1. **Create Failing Test Case**
   - Simplest possible reproduction
   - Automated test if possible
   - One-off test script if no framework
   - MUST have before fixing
   - Use the `intertest:test-driven-development` skill for writing proper failing tests
   - **Done when:** A regression test runs and fails on the reduced case.

2. **Implement Single Fix**
   - Address the root cause identified
   - ONE change at a time
   - No "while I'm here" improvements
   - No bundled refactoring
   - **Done when:** One change addresses the evidenced root cause.

3. **Verify Fix**
   - Re-run the Phase 1 reproduction with the same command and number of runs, and record the rate after
   - Test passes now?
   - No other tests broken?
   - Issue actually resolved?
   - Use the `intertest:verification-before-completion` skill before claiming success
   - From the repository root, find temporary diagnostics with `rg -n --hidden 'DEBUG-TEMP:' .`. Remove tagged temporary statements and entire marked diagnostic blocks, retaining the underlying operation. Inspect every match, keeping permanent skill instructions that describe this prefix.
   - **Done when:** The original command and relevant tests pass, the after-rate is recorded, and the prefix search finds no temporary diagnostic sites.

4. **If Fix Doesn't Work**
   - STOP
   - Count: How many fixes have you tried?
   - If < 3: Return to Phase 1, re-analyze with new information
   - **If ≥ 3: STOP and question the architecture (step 5 below)**
   - DON'T attempt Fix #4 without architectural discussion
   - **Done when:** The failed-fix count is recorded and investigation resumes, or three failures trigger step 5.

5. **If 3+ Fixes Failed: Question Architecture**

   **Pattern indicating architectural problem:**
   - Each fix reveals new shared state/coupling/problem in different place
   - Fixes require "massive refactoring" to implement
   - Each fix creates new symptoms elsewhere

   **STOP and question fundamentals:**
   - Is this pattern fundamentally sound?
   - Are we "sticking with it through sheer inertia"?
   - Should we refactor architecture vs. continue fixing symptoms?

   **Discuss with your human partner before attempting more fixes**

   This is NOT a failed hypothesis - this is a wrong architecture.
   - **Done when:** After three failed fixes, your human partner has discussed the architecture and agreed the next action before another fix.

## Red Flags - STOP and Follow Process

If you catch yourself thinking:
- "Quick fix for now, investigate later"
- "Just try changing X and see if it works"
- "Add multiple changes, run tests"
- "Skip the test, I'll manually verify"
- "It's probably X, let me fix that"
- "I don't fully understand but this might work"
- "Pattern says X but I'll adapt it differently"
- "Here are the main problems: [lists fixes without investigation]"
- Proposing solutions before tracing data flow
- **"One more fix attempt" (when already tried 2+)**
- **Each fix reveals new problem in different place**

**ALL of these mean: STOP. Return to Phase 1.**

**If 3+ fixes failed:** Question the architecture (see Phase 4.5)

## your human partner's Signals You're Doing It Wrong

**Watch for these redirections:**
- "Is that not happening?" - You assumed without verifying
- "Will it show us...?" - You should have added evidence gathering
- "Stop guessing" - You're proposing fixes without understanding
- "Ultra-think this" - Question fundamentals, not just symptoms
- "We're stuck?" (frustrated) - Your approach isn't working

**When you see these:** STOP. Return to Phase 1.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Issue is simple, don't need process" | Simple issues have root causes too. Process is fast for simple bugs. |
| "Emergency, no time for process" | Systematic debugging is FASTER than guess-and-check thrashing. |
| "Just try this first, then investigate" | First fix sets the pattern. Do it right from the start. |
| "I'll write test after confirming fix works" | Untested fixes don't stick. Test first proves it. |
| "Multiple fixes at once saves time" | Can't isolate what worked. Causes new bugs. |
| "Reference too long, I'll adapt the pattern" | Partial understanding guarantees bugs. Read it completely. |
| "I see the problem, let me fix it" | Seeing symptoms ≠ understanding root cause. |
| "One more fix attempt" (after 2+ failures) | 3+ failures = architectural problem. Question pattern, don't fix again. |

## Quick Reference

| Phase | Key Activities | Success Criteria |
|-------|---------------|------------------|
| **1. Root Cause** | Read errors, reproduce, check changes, trace, shrink | Executed bug-specific command, failure rate, timing, and necessary case parts recorded |
| **2. Pattern** | Find working examples, compare | Identify differences |
| **3. Hypothesis** | Rank 3 to 5 falsifiable guesses, test one at a time | Recorded verdicts and an evidenced cause |
| **4. Implementation** | Create test, fix, verify | Bug resolved, tests pass |

## When Process Reveals "No Root Cause"

If systematic investigation reveals issue is truly environmental, timing-dependent, or external:

1. You've completed the process
2. Document what you investigated
3. Implement appropriate handling (retry, timeout, error message)
4. Add monitoring/logging for future investigation

**But:** 95% of "no root cause" cases are incomplete investigation.

## Reporting

The report that closes an investigation must include a **Falsified hypotheses**
section (each hypothesis the notebook ruled out, with what ruled it out), the
reproduction rate before and after the fix, and any timeout, retry or skipped
check labeled as a workaround. Use the template in `investigation-notebook.md`.

## Supporting Techniques

These techniques are part of systematic debugging and available in this directory:

- **`investigation-notebook.md`** - Notebook template: bound the symptom, reproduce with a rate, one hypothesis per entry, label workarounds, report the rate after
- **`root-cause-tracing.md`** - Trace bugs backward through call stack to find original trigger
- **`defense-in-depth.md`** - Add validation at multiple layers after finding root cause
- **`condition-based-waiting.md`** - Replace arbitrary timeouts with condition polling
