# Investigation Notebook

Keep this notebook while you debug, not after. Write each entry before you run the
command and fill in the result right after, so the record shows what you tried and
not what you remember trying. Keep it wherever the task keeps scratch notes (a
file in the task's scratch directory, or the bead or card thread) and quote it in
the final report.

## Bound the symptom

State the symptom in one sentence: what fails, where, and how you know. Name what
is not part of it. If you can't bound it, gather data until you can.

## Reproduce with a rate

One failure is an anecdote. Run the reproduction enough times to get a rate
(failures out of runs) and record the exact command. For an intermittent failure,
use a bounded loop and note its attempt limit; a failure that happens 3 times in
50 needs a different test than one that happens every time. Aim for seconds;
when that is impractical, explain why and use the fastest available command.

```
Symptom:        <one sentence>
Repro command:  <exact command>
Rate before:    <failures>/<runs>
Attempt limit:  <maximum runs per command>
Elapsed time:   <measured duration; explain any speed limitation>
```

## Rank causes before testing

Write 3 to 5 guesses ordered by evidence before testing any. For each, record:

```
Rank / ID:       <priority, H<n>>
Possible cause:  <specific cause and supporting evidence>
Prediction:      <observation expected if this cause is correct>
Would disprove:  <observation that would rule it out>
```

Done when: All ranked guesses have predictions and disproof criteria before the
first experiment.

## One entry per hypothesis

Test one ranked hypothesis at a time, starting with the highest remaining rank.
Every entry uses the fields below; the result is what the command printed.

```
H<n>: <"I think X is the cause because Y">
Prediction:      <expected observation from the ranked list>
Would disprove:  <observation that would rule it out>
Command:  <exact command or change>
Result:   <what happened, quoted>
Verdict:  supported | ruled out | inconclusive
Next:     <what this changes>
```

A ruled-out hypothesis stays in the notebook. Do not delete or rewrite it when a
later one works. Restore experimental changes before testing the next guess;
when the list is exhausted, gather evidence and write a fresh ranked list.

## Label workarounds

A timeout, retry, sleep or skipped check is a workaround, not a fix, unless an
earlier entry shows it removes the cause. Record it as `WORKAROUND:` with what it
hides and the entry that would replace it. Prefer condition-based waiting
(`condition-based-waiting.md`) over a longer timeout.

## Report the rate after

After the fix, run the same reproduction command with the same number of runs.

```
Rate after:   <failures>/<runs>   (same command as "Rate before")
```

If the rate did not move, the fix is not proven, whatever else the notes say.
When the failure was diagnosed from a service's logs, read the scheduled run's
evidence (for example `journalctl`) rather than re-running by hand, since a
hand run can overwrite the evidence.

## Final report

The report that closes the investigation contains:

1. Root cause, and the entry whose evidence supported it.
2. **Falsified hypotheses:** every entry marked ruled out, one line each with
   what ruled it out. Write "none" when no hypothesis was actually ruled out;
   inconclusive entries are not falsified, so list them separately if any.
3. Rate before and after, with the command.
4. Any `WORKAROUND:` entries that remain.
