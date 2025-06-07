import json
from typing import List


class AnalysisResult:
    def __init__(self, user_id: str, analysis_id: str, passed: bool, errors: List[str]):
        self._user_id = user_id
        self._analysis_id = analysis_id
        self._passed = passed
        self._errors = errors

    @property
    def user_id(self) -> str:
        return self._user_id

    @user_id.setter
    def user_id(self, value: str):
        if not isinstance(value, str):
            raise TypeError("user_id must be a string")
        self._user_id = value

    @property
    def analysis_id(self) -> str:
        return self._analysis_id

    @analysis_id.setter
    def analysis_id(self, value: str):
        if not isinstance(value, str):
            raise TypeError("analysis_id must be a string")
        self._analysis_id = value

    @property
    def passed(self) -> bool:
        return self._passed

    @passed.setter
    def passed(self, value: bool):
        if not isinstance(value, bool):
            raise TypeError("passed must be a boolean")
        self._passed = value

    @property
    def errors(self) -> List[str]:
        return self._errors

    @errors.setter
    def errors(self, value: List[str]):
        if not isinstance(value, list) or not all(isinstance(err, str) for err in value):
            raise TypeError("errors must be a list of strings")
        self._errors = value

    def json(self, pretty: bool = False) -> str:
        data = {
            "user_id": self._user_id,
            "analysis_id": self._analysis_id,
            "passed": self._passed,
            "errors": self._errors
        }
        return json.dumps(data, indent=2 if pretty else None)

    def __repr__(self) -> str:
        return f"AnalysisResult(user_id='{self._user_id}', analysis_id='{self._analysis_id}', passed={self._passed}, errors={self._errors})"
