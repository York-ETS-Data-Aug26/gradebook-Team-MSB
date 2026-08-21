"""All gradebook exceptions live here."""


class GradebookError(Exception):
    """Base class for every error this package raises."""

<<<<<<< HEAD

class RosterError(GradebookError):
    """StudentNotFound"""


class InvalidGrade(GradebookError):
    """InvalidGradeError"""
=======
class StorageError(GradebookError):
    """StorageError"""
>>>>>>> b3268e59a761851a3f92e9e3d61d674f31ee02f7
