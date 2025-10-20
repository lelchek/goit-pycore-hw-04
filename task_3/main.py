import sys
from pathlib import Path
from colorama import Fore, Style


def visualizer(path: Path, spaces: int = 0):
    printed_str = f"{' ' * spaces}{path.name}"

    if path.is_file():
        print(Fore.GREEN + printed_str)
        return

    if path.is_dir():
        print(Fore.BLUE + f"{printed_str}/")
        spaces += 4

        for p in path.iterdir():
            visualizer(p, spaces)


def main():
    try:
        arg = sys.argv[1]

    except IndexError:
        print("Error: argument does not exist")

    else:
        path = Path(arg)

        if not path.exists():
            print("Error: path does not exist")
            return

        if not path.is_dir():
            print("Error: path is not a directory")
            return

        visualizer(path)
        Style.RESET_ALL


if __name__ == "__main__":
    main()
