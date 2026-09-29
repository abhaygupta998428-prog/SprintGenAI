import json

from agents.llm import generate_response
from prompts.sprint_prompt import build_sprint_prompt


def sprint_agent(state):

    prompt = build_sprint_prompt(
        state["priorities"]
    )

    response = generate_response(prompt)

    print("Sprint Agent Response:")
    print(response)

    try:

        cleaned = response.replace(
            "```json", ""
        ).replace(
            "```", ""
        ).strip()

        sprints = json.loads(cleaned)

    except Exception as e:

        print("Sprint JSON Error:", e)

        sprints = []

    state["sprints"] = sprints

    return state