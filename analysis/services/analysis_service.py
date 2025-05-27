import json
from models.analysis_result import AnalysisResult
from adapters.redis_adapter import RedisAdapter

def fake_analysis(code: str) -> dict:
    return {
        "passed": "error" not in code,
        "errors": [] if "error" not in code else ["Syntax error found"]
    }

def start_analysis():
    redis_adapter = RedisAdapter()
    pubsub = redis_adapter.subscribe("code_channel")

    for message in pubsub.listen():
        if message['type'] == 'message':
            data = json.loads(message['data'])
            result = fake_analysis(data["code"])
            analysis_result = AnalysisResult(
                user_id=data["user_id"],
                passed=result["passed"],
                errors=result["errors"]
            )
            redis_adapter.publish("result_channel", analysis_result.json())
