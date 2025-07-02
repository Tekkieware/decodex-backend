import json
from typing import List, Dict, Any


class AnalysisResult:
    def __init__(
        self,
        analysis_id: str,
        detected_language: str,
        summary: str,
        functions: List[Dict[str, Any]],
        variables: List[Dict[str, Any]],
        bugs: List[Dict[str, Any]],
        logicFlow: List[Dict[str, Any]]
    ):
        self._analysis_id = analysis_id
        self._detected_language = detected_language
        self._summary = summary
        self._functions = functions
        self._variables = variables
        self._bugs = bugs
        self._logicFlow = logicFlow

    @property
    def analysis_id(self) -> str:
        return self._analysis_id

    @property
    def detected_language(self) -> str:
        return self._detected_language

    @property
    def summary(self) -> str:
        return self._summary

    @property
    def functions(self) -> List[Dict[str, Any]]:
        return self._functions

    @property
    def variables(self) -> List[Dict[str, Any]]:
        return self._variables

    @property
    def bugs(self) -> List[Dict[str, Any]]:
        return self._bugs

    @property
    def logicFlow(self) -> List[Dict[str, Any]]:
        return self._logicFlow

    def json(self, pretty: bool = False) -> str:
        data = {
            "analysis_id": self._analysis_id,
            "detected_language": self._detected_language,
            "summary": self._summary,
            "functions": self._functions,
            "variables": self._variables,
            "bugs": self._bugs,
            "logicFlow": self._logicFlow,
        }
        return json.dumps(data, indent=2 if pretty else None)

    def __repr__(self) -> str:
        return (
            f"AnalysisResult(analysis_id='{self._analysis_id}', "
            f"detected_language='{self._detected_language}', summary='{self._summary}', "
            f"functions={self._functions}, variables={self._variables}, "
            f"bugs={self._bugs}, logicFlow={self._logicFlow})"
        )
