"""
Simple routine to evaluate licensing model
"""
import numpy as np

from .fort_add import fort_add
add = fort_add.add

class AddError(Exception):
    """Base class for exceptions in this module."""
    pass

class LicenseError(AddError):
    """Exception raised for errors with your software license.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, ierror):
        self.message = str(ierror)

    def __str__(self):
        return self.message

def fadd(a, b):
    rslt, ierror = add(a, b)
    if all(ierror != 0):
        raise LicenseError(ierror[0])

    return rslt

if __name__ == "__main__":
    a = np.arange(10, dtype=np.float32)
    b = np.arange(100, 110, dtype=np.float32)

    print("Numpy Add: ", a + b)

    print("Fort  Add: ", fadd(a, b))