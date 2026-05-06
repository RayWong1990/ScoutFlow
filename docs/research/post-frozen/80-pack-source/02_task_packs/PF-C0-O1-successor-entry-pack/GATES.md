# Pack Gates

## Enter condition

- `live_authority_readback_after_PR194` must be true.
- Frozen boundary must be acknowledged.
- No hidden true-write/runtime/browser/migration claim.

## Do-not-enter-if

- Any task claims old Dispatch126-176 can be reopened.
- Any task treats placeholder/dry-run/candidate docs as product proof.
- Any task touches forbidden paths without explicit scoped dispatch.

## Pass condition

Each opened task must satisfy its own pass bar and validation.

## Partial pass

A task may produce a useful artifact but remains `partial` if proof_kind is missing or human gate is pending.

## Fail condition

A task fails if it expands scope, weakens blocked runtime lanes, or produces only docs while claiming proof.

## Kill signals

- preview false closure
- second inbox behavior
- runtime creep
- true-write creep
- over-objectification
