""" 
These objects are currently used to print to a results text file but could be used to give information to API
"""

import enum


class test_status(enum.Enum):
    SUCCESS = 1
    FAILURE = 2


class TestResultObject:

    # ex: SWC-101
    _test_name

    # ex: test_status.SUCCESS
    _overall_status_flag

    # ex: {"failed at X", "failed at Y", ...}
    _errors

    def __repr__(self):
        rep = (
            f"Test: {self._test_name}\n"
            + f"Status: {self._overall_status_flag}\n"
            + f"Errors: {self._errors}\n\n"
        )
        return rep
