"""All gradebook exceptions live here."""


class GradebookError(Exception):
    """Base class for every error this package raises."""



class RosterError(GradebookError):
    """StudentNotFound"""


class InvalidGrade(GradebookError):
    """InvalidGradeError"""

class StorageError(GradebookError):
    """StorageError"""

