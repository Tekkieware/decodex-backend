import json
from typing import List


class AnalysisResult:
    def __init__(self, user_id: str, passed: bool, errors: List[str]):
        """
        Initialize the AnalysisResult entity with a user ID, pass status, and list of error messages.
        """
        self._user_id = user_id     # Private attribute for user ID
        self._passed = passed       # Private attribute to indicate if the analysis passed
        self._errors = errors       # Private attribute to hold a list of errors

    # --- user_id property ---
    @property
    def user_id(self) -> str:
        """
        Get the user ID.
        """
        return self._user_id

    @user_id.setter
    def user_id(self, value: str):
        """
        Set the user ID, ensuring it's a string.
        """
        if not isinstance(value, str):
            raise TypeError("user_id must be a string")
        self._user_id = value

    # --- passed property ---
    @property
    def passed(self) -> bool:
        """
        Get the analysis pass status.
        """
        return self._passed

    @passed.setter
    def passed(self, value: bool):
        """
        Set the analysis pass status, ensuring it's a boolean.
        """
        if not isinstance(value, bool):
            raise TypeError("passed must be a boolean")
        self._passed = value

    # --- errors property ---
    @property
    def errors(self) -> List[str]:
        """
        Get the list of errors.
        """
        return self._errors

    @errors.setter
    def errors(self, value: List[str]):
        """
        Set the list of errors, ensuring it's a list of strings.
        """
        if not isinstance(value, list) or not all(isinstance(err, str) for err in value):
            raise TypeError("errors must be a list of strings")
        self._errors = value

    def json(self, pretty: bool = False) -> str:
        """
        Return a JSON string representation of the analysis result.
        
        Args:
            pretty (bool): If True, return pretty-printed JSON.
        
        Returns:
            str: JSON representation of the object.
        """
        data = {
            "user_id": self._user_id,
            "passed": self._passed,
            "errors": self._errors
        }
        return json.dumps(data, indent=2 if pretty else None)

    def __repr__(self) -> str:
        """
        Return a developer-friendly string representation of the object.
        Useful for logging and debugging.
        """
        return f"AnalysisResult(user_id='{self._user_id}', passed={self._passed}, errors={self._errors})"
