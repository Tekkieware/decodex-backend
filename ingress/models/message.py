class Message:
    def __init__(self, code: str, language: str, user_id: str):
        self._code = code
        self._language = language
        self._user_id = user_id

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        self._language = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value

    def json(self):
        import json
        return json.dumps({
            "code": self._code,
            "language": self._language,
            "user_id": self._user_id
        })
