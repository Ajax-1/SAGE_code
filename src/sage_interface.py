"""Public interface sketch for SAGE.

This file is deliberately non-functional. The implementation and
paper-specific configuration will be added after acceptance and internal
review.
"""

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class SAGEConfig:
    """Configuration shape reserved for the future public release.

    Paper-specific defaults are intentionally omitted from this placeholder.
    """

    local_weight: float | None = None
    manhattan_weight: float | None = None
    coverage_weight: float | None = None


def compute_scene_adaptive_weight(
    scene_descriptor: Any, config: SAGEConfig
) -> float:
    """Return the scene-adaptive weight in the future implementation."""

    raise NotImplementedError(
        "The SAGE implementation will be released after acceptance."
    )
