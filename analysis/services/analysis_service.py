import json
from typing import Dict
from models.analysis_result import AnalysisResult
from adapters.redis_adapter import RedisAdapter


def fake_analysis(code: str) -> Dict[str, object]:
    """
    Simulates code analysis.
    
    Args:
        code (str): The source code to analyze.

    Returns:
        dict: A dictionary containing analysis result (passed: bool, errors: list).
    """
    return {
        "passed": "error" not in code,
        "errors": [] if "error" not in code else ["Syntax error found"]
    }


def start_analysis() -> None:
    """
    Starts listening to the Redis 'code_channel', analyzes incoming code,
    and publishes the result to the 'result_channel'.
    """
    # Initialize Redis adapter and subscribe to the code channel
    redis_adapter = RedisAdapter()
    pubsub = redis_adapter.subscribe("code_channel")

    print("Listening for messages on 'code_channel'...")

    # Continuously listen for new messages
    for message in pubsub.listen():
        if message['type'] != 'message':
            continue  # Skip subscription and other Redis-internal messages

        try:
            # Parse incoming JSON message
            data = json.loads(message['data'])

            # Validate required keys
            if "code" not in data or "user_id" not in data:
                print("Invalid message format: missing 'code' or 'user_id'")
                continue

            # Perform fake code analysis
            result = fake_analysis(data["code"])

            # Create an AnalysisResult entity
            analysis_result = AnalysisResult(
                user_id=data["user_id"],
                passed=result["passed"],
                errors=result["errors"]
            )

            # Publish analysis result as JSON to result channel
            redis_adapter.publish("result_channel", analysis_result.json())
            print(f"Published result for user {data['user_id']}")

        except (json.JSONDecodeError, KeyError, TypeError) as e:
            # Log error and skip malformed messages
            print(f"Error processing message: {e}")
