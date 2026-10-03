import pytest

from sage.api import SAGEConfig, compute_scene_adaptive_weight


def test_public_config_has_no_paper_specific_defaults():
    config = SAGEConfig()
    assert config.local_weight is None
    assert config.manhattan_weight is None
    assert config.coverage_weight is None


def test_withheld_implementation_is_explicit():
    with pytest.raises(NotImplementedError):
        compute_scene_adaptive_weight({}, SAGEConfig())
