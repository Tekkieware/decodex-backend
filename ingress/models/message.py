import json


class Message:
    """
    Represents a message containing code to be analyzed and a unique analysis ID.
    """

    def __init__(self, code: str, analysis_id: str):
        """
        Initialize a new Message instance.

        Args:
            code (str): The code to be analyzed.
            analysis_id (str): The unique ID for this analysis.
        """
        self.code = code
        self.analysis_id = analysis_id

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

    # --- analysis_id property ---
    @property
    def analysis_id(self) -> str:
        """Return the unique analysis ID."""
        return self._analysis_id

    @analysis_id.setter
    def analysis_id(self, value: str) -> None:
        """Set the analysis ID, validating input type."""
        if not isinstance(value, str):
            raise TypeError("analysis_id must be a string")
        self._analysis_id = value

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
            "analysis_id": self._analysis_id
        }
        return json.dumps(data, indent=2 if pretty else None)

    def __repr__(self) -> str:
        """
        Return a developer-friendly string representation of the object.

        Returns:
            str: Debug-friendly string.
        """
        return f"Message(analysis_id='{self._analysis_id}', code=<code>)"
