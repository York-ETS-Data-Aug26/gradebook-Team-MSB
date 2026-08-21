"""Gradebook command line interface."""
import sys

#from gradebook.reports import average
from gradebook.errors import GradebookError
from gradebook.storage import load
from gradebook.reports import mean
from gradebook.reports import summary

from gradebook.roster import  find_student
DATA_FILE = "roster.json"


def show_help(roster, args):
    print("commands:", ", ".join(sorted(COMMANDS)))
def top_student (roster, args):
    if not roster:
        print ("no Students in roster")
        return
    name = max(roster, key= lambda name:mean(roster[name]))
    max_avg = mean(roster[name])
    print(f"{name}: {max_avg}")

def find (roster, args):
    if not args:
        print ("USAGE: find <name",file=sys.stderr)
        return
    scores = find_student(roster, args[0])
    print (args[0],scores)

COMMANDS = {
    "help": show_help,
    "load": load,
    "average": mean,
    "find": find,
     "top" : top_student
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