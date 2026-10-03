"""Stable public API boundary for SAGE."""

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class SAGEConfig:
    """Configuration shape; paper-specific defaults are withheld."""

    local_weight: float | None = None
    manhattan_weight: float | None = None
    coverage_weight: float | None = None


def compute_scene_adaptive_weight(scene_descriptor: Any, config: SAGEConfig) -> float:
    """Compute the scene-adaptive weight in the final implementation."""

    raise NotImplementedError("SAGE implementation pending final release")
