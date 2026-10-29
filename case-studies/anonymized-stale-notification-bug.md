# Notification Timing: Finding an Outdated Reminder

> `[SANITIZED WORK CASE]` · Example of an anonymized defect report

## Context and confidentiality

This is a public-safe version of a notification-scheduling issue observed in an EdTech workflow. It contains no participant data, product identifiers, event dates, delivery logs, internal URLs, or ticket links.

## Title

Changing an event start date does not refresh an already scheduled pre-event notification.

## Preconditions

- An event has a notification rule scheduled relative to its start time.
- The notification event has already been created by the scheduler.

## Steps to reproduce

1. Create or select an event with a pre-event notification rule.
2. Confirm that the scheduler has created the notification event.
3. Change the event start time.
4. Review the already created notification event.

## Actual result

The existing notification can retain the time calculated from the previous event start time.

## Expected result

After the event start time changes, the dependent notification should be recalculated, replaced, or clearly flagged for operator action so that it cannot be sent at a stale time.

## Risk and handoff

This can affect a time-sensitive learner or participant communication flow. The finding was documented for the team with the scenario, expected behaviour, actual scheduling state, and a recommendation to verify notification recreation or recalculation after a date change.

## Retest boundary

The public case does not claim a release fix or a delivery result. Retest status belongs in the private work tracker after the team confirms the intended behaviour.
