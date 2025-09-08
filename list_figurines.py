"""Simple CLI to list Age of Sigmar figurines."""
from age_of_sigmar.figurines import FIGURINES


def main() -> None:
    for fig in FIGURINES:
        print(f"{fig.faction} - {fig.name}")


if __name__ == "__main__":
    main()
