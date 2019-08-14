from fileinput import input
from sys import stdout
from recordslib import DsvCommand, LineParser


def main():
    parser = LineParser()
    cmd = DsvCommand(input(), stdout, parser)
    cmd.run()


if __name__ == '__main__':
    main()