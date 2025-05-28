import json


class Message:
    """
    Represents a message containing code to be analyzed, its programming language,
    and the ID of the user who submitted it.
    """

    def __init__(self, code: str, language: str, user_id: str):
        """
        Initialize a new Message instance.

        Args:
            code (str): The code to be analyzed.
            language (str): The programming language of the code.
            user_id (str): The ID of the user submitting the code.
        """
        self.code = code
        self.language = language
        self.user_id = user_id

    # --- code property ---
    @property
    def code(self) -> str:
        """Return the submitted code."""
        return self._code

    @code.setter
    def code(self, value: str) -> None:
        """Set the submitted code, validating input type."""
        if not isinstance(value, str):
            raise TypeError("code must be a string")
        self._code = value

    # --- language property ---
    @property
    def language(self) -> str:
        """Return the language of the code."""
        return self._language

    @language.setter
    def language(self, value: str) -> None:
        """Set the language of the code, validating input type."""
        if not isinstance(value, str):
            raise TypeError("language must be a string")
        self._language = value

    # --- user_id property ---
    @property
    def user_id(self) -> str:
        """Return the ID of the user who submitted the code."""
        return self._user_id

    @user_id.setter
    def user_id(self, value: str) -> None:
        """Set the user ID, validating input type."""
        if not isinstance(value, str):
            raise TypeError("user_id must be a string")
        self._user_id = value

    def json(self, pretty: bool = False) -> str:
        """
        Return a JSON representation of the message.

        Args:
            pretty (bool): Whether to return a pretty-printed JSON string.

        Returns:
            str: JSON string.
        """
        data = {
            "code": self._code,
            "language": self._language,
            "user_id": self._user_id
        }
        return json.dumps(data, indent=2 if pretty else None)

    def __repr__(self) -> str:
        """
        Return a developer-friendly string representation of the object.

        Returns:
            str: Debug-friendly string.
        """
        return f"Message(user_id='{self._user_id}', language='{self._language}', code=<code>)"
