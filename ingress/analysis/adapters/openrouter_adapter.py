import os
import json
import httpx
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise EnvironmentError("OPENROUTER_API_KEY not set in environment.")

HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",  # change this to your actual domain in prod
    "X-Title": "Code Analysis Tool",
}

async def analyze_code_with_openrouter(code: str) -> Dict[str, Any]:
    prompt = f"""
    You are an expert programming assistant. Carefully analyze the following code and return a detailed JSON response with the following keys:

    1. **detected_language**: Identify the programming language of the code. Be precise — e.g., "JavaScript", "TypeScript", "Python", "C++". 

    2. **summary**: Write a high-level overview of what the entire code does. Summarize its purpose and behavior concisely and clearly.

    3. **functions**: List all functions in the code. For each:
        - `name`: Function name
        - `explanation`: Describe the purpose and logic of the function
        - `parameters`: Explain each parameter’s name, type (if known), and its role
        - `returns`: Describe the return value and what it represents

    4. **variables**: List all important variables. For each:
        - `name`: Variable name
        - `type`: Type of the variable, if inferable (e.g., number, string, list)
        - `purpose`: What the variable is used for in context

    5. **bugs**: Analyze the code for errors or risky logic. For each bug:
        - `type`: "error", "warning", or "suggestion"
        - `message`: Describe the issue
        - `line`: The line number if detectable (or best guess)
        - `suggestion`: How to fix or improve it
        - `corrected_Code`: The corrected or improved version of the relevant code

    6. **logicFlow**: Break down the logical steps of the program. Describe them in order of execution. For each step:
        - `step`: Number
        - `description`: A plain-English explanation of what happens

    Only return the final answer as a **valid JSON object**. Do not include extra commentary.

    Analyze this code:
    ```{code}```
    """

    body = {
        "model": "deepseek/deepseek-r1:free",  
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
    }

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=HEADERS,
                json=body
            )
            response.raise_for_status()
            content = response.json()["choices"][0]["message"]["content"]

            # Some models return markdown — clean it if needed
            if content.strip().startswith("```json"):
                content = content.strip().removeprefix("```json").removesuffix("```").strip()

            return json.loads(content)

    except Exception as e:
        print(f"[OpenRouter Error] {e}")
        return {
            "detected_language": None,
            "summary": None,
            "functions": [],
            "variables": [],
            "bugs": [{
                "type": "error",
                "message": f"OpenRouter request failed: {str(e)}",
                "line": None,
                "suggestion": None,
                "corrected_Code": None,
            }],
            "logicFlow": []
        }
