"""Student roster operations. Owner: A."""

from gradebook.errors import RosterError ,InvalidGrade

def find_student (roster,name):
    try:
        return roster[name]
    except KeyError as x:
        raise RosterError(f"NO STUDENT NAMED {name}") from x

def add_student (roster,name,scores):
    for score in scores:
        if not (0<= score <= 100):
            raise InvalidGrade(f"NO STUDENT SCORED {score}")
        roster[name] = list(score)