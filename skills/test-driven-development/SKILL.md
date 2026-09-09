---
name: test-driven-development
description: Implement or fix behavior with a failing regression test, then verify the minimal change.
---

# Test-Driven Development

For new behavior, bug fixes and significant refactors, write a meaningful test
first and observe its expected failure before implementing. The failure must
expose missing behavior, not a broken test invocation or unavailable dependency.
If it passes immediately, identify whether the behavior already exists or the
assertion misses the bug. For an existing bug, reproduce and diagnose first.

Implement the smallest correct change. Run the new test, inspect the result, then
run affected checks. Refactor only while they stay green. Tests should express
observable contracts and edge cases; prefer real components and avoid assertions
that merely mirror implementation or mocked behavior. Do not add production-only
seams just to test mocks.

Choose verification proportionate to risk. Reversible prose/configuration edits
need their relevant validation, not artificial behavioral tests. User instructions
and runtime policy govern procedure; do not add approval rituals for exceptions
already authorized. Preserve repository-required checks and independent review.

Read [examples-and-troubleshooting.md](references/examples-and-troubleshooting.md)
when choosing test shape, understanding a failing-first cycle or diagnosing a
hard-to-test dependency. Read [testing-anti-patterns.md](testing-anti-patterns.md)
when mocks or test helpers are involved.

Before completion, verify fresh results with
`intertest:verification-before-completion`. An execution result cannot replace
required independent acceptance or real host, device, play or production evidence.
Report missing evidence explicitly and keep its gate outstanding.
