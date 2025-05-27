class AnalysisResult:
    def __init__(self, user_id: str, passed: bool, errors: list[str]):
        self._user_id = user_id
        self._passed = passed
        self._errors = errors

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    @property
    def passed(self):
        return self._passed

    @passed.setter
    def passed(self, value):
        self._passed = value

    @property
    def errors(self):
        return self._errors

    @errors.setter
    def errors(self, value):
        self._errors = value

    def json(self):
        import json
        return json.dumps({
            "user_id": self._user_id,
            "passed": self._passed,
            "errors": self._errors
        })
