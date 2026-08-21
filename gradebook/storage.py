"""Loading and saving roster data. Owner: B."""

import json
import gradebook.errors as e

def load(path):
    """Load roster data from file."""
    try:
        with open(path, 'r') as file:
            data = json.load(file)
            return data
    # These are treated differently because in the case that no one is on the team the roster would be empty
    except :
        return {}
    except:
        raise e.StorageError("Corrupt JSON file")

def save(path, roster):
    with open(path, 'w') as file:
        json.dump(roster, file)