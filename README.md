# intertest

Engineering quality disciplines for Claude Code.

## What this does

Three skills that enforce process at the moments it matters most: when you're tempted to skip steps because you're "pretty sure" the fix works.

**Systematic debugging**: a 4-phase root-cause investigation that starts with reading the error, then reproducing it, then analyzing the cause, then verifying the fix. The discipline is in the order: no guessing, no "let me try this" before you can reproduce the problem. Read first, reproduce second.

**Test-driven development**: strict RED-GREEN-REFACTOR. Write a failing test that describes what you want. Make it pass with the simplest possible code. Then refactor. No production code without a failing test, no refactoring while tests are red. The constraint is the point.

**Verification before completion**: iron-law evidence gates. Before claiming something works, you need fresh evidence: tests passing, the behavior observable, the fix verified in the actual failure mode. "It should work" is not evidence; "here's the test output showing it works" is evidence.

## Installation

First, add the [interagency marketplace](https://github.com/mistakeknot/interagency-marketplace) (one-time setup):

```bash
/plugin marketplace add mistakeknot/interagency-marketplace
```

Then install the plugin:

```bash
/plugin install intertest
```

## Usage

```
/intertest:systematic-debugging
/intertest:test-driven-development
/intertest:verification-before-completion
```

Or let the skills trigger naturally:

```
"debug this test failure"
"implement this feature with TDD"
"verify that the fix actually works"
```

The skills cross-reference each other: TDD naturally leads into verification, debugging naturally leads into TDD for the regression test.

## Design decisions

- General-purpose disciplines, not tied to any specific language or framework
- The skills are methodological guardrails, not tools: they change *how* you work, not what tools you use
- Extracted from Clavain so they're available independently of the full engineering plugin
