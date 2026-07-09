## Governance and Change Proposals

- **Owner**: design-system owner — TBD. Until named, route proposals to the brand team lead.
- **How to propose a change**:
  1. State which token(s)/section(s) change and why.
  2. Tag **additive** (new token/component/pose) or **breaking** (renamed/removed token, or a value change to an *existing* token).
  3. Additive → one reviewer approves; bump MINOR; add a Changelog entry.
  4. Breaking, or anything touching colors/logo/core typography sourced from the official guideline PDF → requires brand-team sign-off; bump MAJOR; grep the codebase for the old token name before merging.
  5. Purely derived sections (spacing, radii, elevation, breakpoints, motion, focus, ramps) can be adjusted with design-team-only approval unless the change visibly shifts brand feel.
