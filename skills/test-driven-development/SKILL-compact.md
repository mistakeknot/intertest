# Test-Driven Development (compact)

Write the test first. Watch it fail. Write minimal code to pass.

## When to Invoke

Any new feature, bug fix, refactoring, or behavior change. Exceptions only with human partner approval (prototypes, generated code, config).

## Iron Law

**No production code without a failing test first.** Code written before the test? Delete it. Don't keep as "reference."

## Red-Green-Refactor Cycle

1. **RED — Write one failing test**
   - One behavior per test, clear descriptive name
   - Use real code, not mocks (unless unavoidable)
   - Run it. Confirm it fails for the right reason (missing feature, not typo)
   - Test passes immediately? You're testing existing behavior — fix the test

2. **GREEN — Write minimal code to pass**
   - Simplest implementation that satisfies the test
   - No extra features, no "while I'm here" improvements
   - Run it, then run the project's full test command, not just this file. Report every failure by name, including ones you didn't cause
   - Test still fails? Fix code, not test

3. **REFACTOR — Clean up while green**
   - Remove duplication, improve names, extract helpers
   - Keep all tests passing. Don't add behavior.

4. **Repeat** — next failing test for next behavior

## Good Tests

- **Minimal**: one thing per test. "and" in the name? Split it.
- **Clear**: name describes behavior, not implementation
- **Real**: test actual code paths, not mock wiring

## Red Flags — Delete Code, Start Over

- Code before test / test after implementation
- Test passes immediately (never saw it fail)
- "Keep as reference" or "adapt existing code"
- "I already manually tested it"
- "Just this once" / "TDD is dogmatic"
- "Deleting X hours of work is wasteful" (sunk cost)

## When Stuck

- Don't know how to test? Write the wished-for API. Assertion first.
- Test too complicated? Design too complicated. Simplify interface.
- Must mock everything? Code too coupled. Use dependency injection.

## Plant a Bug

For tests added after the code, new properties and guards, and tests that pass first run (the one case where tests may follow code; an observed red-first failure already satisfies this step): plant a bug that breaks the named behavior, watch the test fail, undo it, watch it pass. Work on a scratch copy or undo by hand; never destructively revert shared work. Report the bug and the failing output. Green with the bug planted means fix the test. Skip it for reversible prose/config edits, where the relevant validation is enough.

## Verify Before Done

Every function has a test, each test failed before implementing, all pass with pristine output, edge cases covered.

---
*For examples and troubleshooting, read SKILL.md; for test quality and mocks, read writing-good-tests.md.*
