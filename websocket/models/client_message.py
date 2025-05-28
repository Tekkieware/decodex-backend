import json
from typing import List


class ClientMessage:
    """
    Represents the result message sent to a client after analysis,
    including the user ID, pass status, and any errors.
    """

    def __init__(self, user_id: str, passed: bool, errors: List[str]):
        """
        Initialize the ClientMessage.

        Args:
            user_id (str): The ID of the user.
            passed (bool): Whether the analysis passed.
            errors (List[str]): List of error messages.
        """
        self.user_id = user_id
        self.passed = passed
        self.errors = errors

    @property
    def user_id(self) -> str:
        """Get the user ID."""
        return self._user_id

    @user_id.setter
    def user_id(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("user_id must be a string")
        self._user_id = value

    @property
    def passed(self) -> bool:
        """Get the pass status."""
        return self._passed

    @passed.setter
    def passed(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise TypeError("passed must be a boolean")
        self._passed = value

    @property
    def errors(self) -> List[str]:
        """Get the list of errors."""
        return self._errors

    @errors.setter
    def errors(self, value: List[str]) -> None:
        if not isinstance(value, list) or not all(isinstance(e, str) for e in value):
            raise TypeError("errors must be a list of strings")
        self._errors = value

    def to_json(self, *, pretty: bool = False) -> str:
        """
        Serialize the message to a JSON string.

        Args:
            pretty (bool): Whether to pretty-print the JSON.

        Returns:
            str: JSON representation of the message.
        """
        data = {
            "user_id": self._user_id,
            "passed": self._passed,
            "errors": self._errors,
        }
        return json.dumps(data, indent=2 if pretty else None)

    def __repr__(self) -> str:
        return (
            f"ClientMessage(user_id={self._user_id!r}, passed={self._passed!r}, "
            f"errors={self._errors!r})"
        )
