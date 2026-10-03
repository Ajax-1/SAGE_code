# SAGE

**Shadow-Adaptive Geometric Supervision for Earth Observation Gaussian Splatting**

This document is the README template for the complete post-review release.
It is kept separately from the current staged README so that the public
landing page can be updated in one controlled commit.

## Contents of the complete release

The complete release will contain the cleaned SAGE implementation, the
EOGS integration, configuration files, installation instructions, input-data
format documentation, evaluation scripts, and a provenance-safe run manifest.

## Reproduction workflow

```bash
conda env create -f environment.yml
conda activate sage
python scripts/train.py --config configs/release.yaml
python scripts/evaluate.py --config configs/release.yaml --checkpoint <checkpoint>
```

The exact release configuration and fixed random seeds will be provided with
the complete package.

## Citation

Please cite the associated SAGE paper when using this implementation.
