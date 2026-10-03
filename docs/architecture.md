# Software organization

The public package follows five boundaries:

1. input and configuration parsing;
2. EOGS-compatible reconstruction integration;
3. geometry and shadow-feature preparation;
4. adaptive supervision;
5. training and evaluation entry points.

The staged snapshot publishes these boundaries and their interface names. The
paper-specific implementations are kept behind the same boundaries for the
final cleaned release.
