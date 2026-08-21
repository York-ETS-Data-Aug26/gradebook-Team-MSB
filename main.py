"""Gradebook command line interface."""
import sys

from gradebook.errors import GradebookError
from gradebook.roster import  find_student
DATA_FILE = "roster.json"


def show_help(roster, args):
    print("commands:", ", ".join(sorted(COMMANDS)))
def show_find (roster, args):
    if not args:
        print("find <name>", args[0])
        return
    scores = find_student(roster[args[0]])
    print (args[0],scores)

COMMANDS = {
    "help": show_help,
    "find": show_find,
}


def main(argv):
    command = argv[1] if len(argv) > 1 else "help"
    roster = {}
    try:
        COMMANDS[command](roster, argv[2:])
    except KeyError:
        print(f"unknown command: {command}", file=sys.stderr)
        return 1
    except GradebookError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))