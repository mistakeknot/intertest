# intertest — Vision and Philosophy

**Version:** 0.1.0
**Last updated:** 2026-02-28

## What intertest Is

intertest provides three engineering quality disciplines: systematic debugging, test-driven development, and verification gates. These are not suggestions — each skill enforces an iron law. Systematic debugging: no fixes without root cause. TDD: no production code without a failing test first. Verification: no completion claims without fresh evidence. The three disciplines are independent but complementary: debugging prevents guessing, TDD prevents regression, verification closes completion loops.

The skills are extracted from Clavain and kept general-purpose — applicable to any language, framework, or project structure. They cross-reference each other where the disciplines naturally compose: TDD's bug-fix workflow calls systematic-debugging for root-cause investigation; all three converge on verification-before-completion as the final gate.

## Why This Exists

Agent workflows are especially prone to three failure modes: guessing at fixes without evidence, writing code that "should work" without confirming it does, and claiming completion without running a verification command. intertest addresses all three with the same mechanism — a mandatory gate function that cannot be bypassed through rationalization. The skills make explicit what good engineering practice already requires, and hold that line under time pressure.

## Design Principles

1. **Evidence over narrative.** Test results, verification output, and root-cause traces are receipts. "Should work," "probably passes," and "agent reported success" are narratives. The iron laws enforce the distinction.

2. **Three independent quality layers.** Debugging, TDD, and verification operate at different stages: defect investigation, implementation, and completion assertion. Any single layer can be skipped by circumstance; having three makes cascading failures much harder.

3. **Strong defaults, explicit exceptions.** The methodology is strict by default. Exceptions exist (throwaway prototypes, generated code) but require explicit human partner approval — not silent rationalization.

4. **Discipline is faster than its absence.** Systematic debugging beats guess-and-check thrashing. TDD beats debugging in production. Verification beats rework after false completion. The skills rebut every "I'm in a hurry" rationalization because rushing is slower in practice.

5. **Architectural escalation, not endless patches.** Three failed fixes signals an architectural problem, not a harder implementation problem. The protocol stops compounding failure by forcing a design conversation before a fourth attempt.

## Scope

**Does:** Enforce root-cause investigation before fixes. Enforce test-first discipline for features and bugfixes. Enforce evidence gates before completion claims. Cross-reference between skills where disciplines naturally compose.

**Does not:** Provide a test framework, test runner, or language-specific tooling. Enforce code coverage targets or test quality metrics. Handle CI/CD integration or deployment gates — those are separate concerns.

## Direction

- Add compact skill summaries (SKILL-compact.md) to reduce token overhead in sessions where all three skills are loaded simultaneously.
- Evaluate whether the shared iron-law gate pattern belongs in interbase as a reusable primitive or stays skill-specific.
- Explore a pre-commit hook that prompts verification-before-completion when tests have not been run in the current session.
