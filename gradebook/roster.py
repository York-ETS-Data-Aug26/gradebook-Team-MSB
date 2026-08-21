"""Student roster operations. Owner: A."""

import gradebook.errors as e

def find_student (roster,name):
    try:
        return roster[name]
    except KeyError as e:
        raise e.RosterError(f"NO STUDENT NAMED {name}") from e

def add_student (roster,name,scores):
    for score in scores:
        if not (0<= score <= 100):
            raise e.InvalidGrade(f"NO STUDENT SCORED {score}")
        roster[name] = list(score)