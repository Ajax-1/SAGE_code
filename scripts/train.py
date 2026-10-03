"""Public training entry point for the staged SAGE release."""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="SAGE training entry point")
    parser.add_argument("--config", required=True)
    parser.parse_args()
    raise RuntimeError(
        "The SAGE-specific training implementation is included in the final release."
    )


if __name__ == "__main__":
    main()
