import json
import asyncio
from typing import Dict, Any
from models.analysis_result import AnalysisResult
from adapters.redis_adapter import RedisAdapter
from adapters.openrouter_adapter import analyze_code_with_openrouter


def start_analysis() -> None:
    redis_adapter = RedisAdapter()
    pubsub = redis_adapter.subscribe("code_channel")

    if not pubsub:
        print("Failed to subscribe to code_channel.")
        return

    print("Listening for messages on 'code_channel'...")

    loop = asyncio.get_event_loop()

    for message in pubsub.listen():
        if message['type'] != 'message':
            continue

        try:
            data = json.loads(message['data'])

            if not all(key in data for key in ["code", "analysis_id"]):
                print("Invalid message: missing 'code' or 'analysis_id'")
                continue

            print(f"Analyzing code for analysis_id: {data['analysis_id']}")

            # Call OpenRouter to analyze code
            result: Dict[str, Any] = loop.run_until_complete(analyze_code_with_openrouter(data["code"]))

            # Build the AnalysisResult object using exact fields
            analysis_result = AnalysisResult(
                analysis_id=data["analysis_id"],
                detected_language=result.get("detected_language", ""),
                summary=result.get("summary", ""),
                functions=result.get("functions", []),
                variables=result.get("variables", []),
                bugs=result.get("bugs", []),
                logicFlow=result.get("logicFlow", [])
            )

            redis_adapter.publish("result_channel", analysis_result.json())
            print(f"Published result for analysis ID: {data['analysis_id']}")

        except (json.JSONDecodeError, KeyError, TypeError) as e:
            print(f"Error processing message: {e}")
