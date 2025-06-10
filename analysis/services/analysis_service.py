import json
from typing import Dict
from models.analysis_result import AnalysisResult
from adapters.redis_adapter import RedisAdapter


def fake_analysis(code: str) -> Dict[str, object]:
    return {
        "passed": "error" not in code.lower(),
        "errors": [] if "error" not in code.lower() else ["Syntax error found"]
    }


def start_analysis() -> None:
    redis_adapter = RedisAdapter()
    pubsub = redis_adapter.subscribe("code_channel")

    if not pubsub:
        print("Failed to subscribe to code_channel.")
        return

    print("Listening for messages on 'code_channel'...")

    for message in pubsub.listen():
        if message['type'] != 'message':
            continue

        try:
            data = json.loads(message['data'])

            if not all(key in data for key in ["code", "analysis_id"]):
                print("Invalid message: missing 'code' or 'analysis_id'")
                continue

            result = fake_analysis(data["code"])

            analysis_result = AnalysisResult(
                analysis_id=data["analysis_id"],
                passed=result["passed"],
                errors=result["errors"]
            )

            redis_adapter.publish("result_channel", analysis_result.json())
            print(f"Published result for analysis with Analysis ID: {data['analysis_id']}")

        except (json.JSONDecodeError, KeyError, TypeError) as e:
            print(f"Error processing message: {e}")
