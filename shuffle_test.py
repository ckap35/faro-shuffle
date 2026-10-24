"""Count the perfect out-shuffles needed to restore an even-sized deck."""

import argparse
from pathlib import Path


def intershuffle(lst):
    """Interleave equal halves, keeping the first and last cards in place."""
    if len(lst) < 2 or len(lst) % 2:
        raise ValueError("A deck must contain an even number of cards, at least two")
    half = len(lst) // 2
    output = list(lst)
    output[::2] = lst[:half]
    output[1::2] = lst[half:]
    return output


def checkshufflecycle(lst):
    """Return the first positive shuffle count that restores the input list."""
    count = 1
    shuffled = intershuffle(lst)
    while shuffled != lst:
        shuffled = intershuffle(shuffled)
        count += 1
    return count


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Save the plot instead of opening a window")
    args = parser.parse_args(argv)

    import matplotlib.pyplot as plt

    deck_sizes = list(range(2, 1000, 2))
    periods = [checkshufflecycle(list(range(n))) for n in deck_sizes]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(deck_sizes, periods, s=12, alpha=0.6)
    for divisor in range(1, 9):
        ax.plot(deck_sizes, [n / divisor for n in deck_sizes],
                color="0.75", linewidth=0.7)
    ax.set_xlabel("Cards in deck")
    ax.set_ylabel("Shuffles to restore order")
    ax.set_title("Perfect out-shuffle periods")
    ax.grid(alpha=0.2)
    fig.tight_layout()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(args.output, dpi=160)
        plt.close(fig)
    else:
        plt.show()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
