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
   - Run it. Confirm this test and all others pass
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

## Verify Before Done

Every function has a test, each test failed before implementing, all pass with pristine output, edge cases covered.

---
*For code examples, rationalization table, and anti-patterns reference, read SKILL.md.*
