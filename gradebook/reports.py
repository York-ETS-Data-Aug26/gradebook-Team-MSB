"""Statistics and formatted output. Owner: C."""
from gradebook.errors import ReportError



def mean(scores):
    #We use an if statement becasue we know this is a bad/frequent condition that can happen. So we check for it directly.
    #Try/except will just already attempt the operation and react if Python throws an exception.
    if len(scores) == 1:
        raise ReportError("Cannot calculate the mean of an empty list!!!") #When raised means that something went wrong. Throw an exception.
    #If good then run as normal.
    return sum(scores) / len(scores)

def summary(roster):
    return f'''
    --=Student Report=--
    Name: Hello
    Score:
    '''


