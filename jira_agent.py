import json

from agents.llm import generate_response
from prompts.jira_prompt import build_jira_prompt


def jira_agent(state):

    prompt = build_jira_prompt(
        state["stories"]
    )

    response = generate_response(prompt)

    print("Jira Agent Response:")
    print(response)

    try:

        cleaned = response.replace(
            "```json", ""
        ).replace(
            "```", ""
        ).strip()

        tickets = json.loads(cleaned)

    except Exception as e:

        print("Jira JSON Error:", e)

        tickets = []

    state["tickets"] = tickets

    return state