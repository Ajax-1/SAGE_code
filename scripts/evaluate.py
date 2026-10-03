"""Public evaluation entry point for the staged SAGE release."""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="SAGE evaluation entry point")
    parser.add_argument("--config", required=True)
    parser.add_argument("--checkpoint", required=True)
    parser.parse_args()
    raise RuntimeError(
        "The complete evaluation package is included in the final release."
    )


if __name__ == "__main__":
    main()
