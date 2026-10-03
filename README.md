# SAGE

**Shadow-Adaptive Geometric Supervision for Earth Observation Gaussian Splatting**

**Public release status: staged release.**

This repository provides the public project layout, environment metadata, data-interface notes, command-line entry points, and non-core utilities for SAGE. The SAGE-specific training components are temporarily withheld while the implementation and project-specific assets are being cleaned and reviewed. The fixed parameters and random seeds used in the study are reported in the manuscript.

The current snapshot is intended to make the software organization and intended execution flow inspectable. It does not include datasets, checkpoints, run records, result tables, private filesystem paths, or the withheld SAGE-specific optimization implementation. Files marked as a staged placeholder preserve the public API and will be replaced by the cleaned implementation in the final release.

## Repository layout

```text
configs/       configuration templates and data-format notes
docs/          installation, input-format, and release notes
scripts/       public command-line entry points
src/eogs/      integration boundary for the EOGS base implementation
src/sage/      SAGE public interfaces and staged components
```

## Current status

The repository is not intended to reproduce the reported numbers at this interim stage. A complete, cleaned code and configuration package will be published in a later release after internal review and de-identification of project-specific assets and paths. See [`docs/release_notes.md`](docs/release_notes.md) for the current scope.

## Future release

The planned final package will add the cleaned training implementation, complete configuration files, installation instructions, reproducibility instructions, and a provenance-safe run manifest. A draft of the future release documentation is kept in [`docs/README_full_release.md`](docs/README_full_release.md).

## Citation

Please cite the SAGE paper when using or discussing this repository. Citation metadata is provided in [`CITATION.cff`](CITATION.cff).

## License status

Licensing information for the final code release will be added when the complete package is published. See [`LICENSE_STATUS.md`](LICENSE_STATUS.md).
