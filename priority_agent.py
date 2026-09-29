import json

from agents.llm import generate_response
from prompts.priority_prompt import build_priority_prompt


def priority_agent(state):

    prompt = build_priority_prompt(
        state["stories"]
    )

    response = generate_response(prompt)

    print("Priority Agent Response:")
    print(response)

    try:

        cleaned = response.replace(
            "```json", ""
        ).replace(
            "```", ""
        ).strip()

        priorities = json.loads(cleaned)

    except Exception as e:

        print("Priority JSON Error:", e)

        priorities = []

    state["priorities"] = priorities

    return state