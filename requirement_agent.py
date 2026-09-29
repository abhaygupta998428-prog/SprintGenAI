import json

from agents.llm import generate_response
from prompts.requirement_prompt import build_requirement_prompt


def requirement_agent(state):

    prompt = build_requirement_prompt(
        state["requirements"]
    )

    response = generate_response(prompt)

    print("Requirement Agent Response:")
    print(response)

    try:

        cleaned = response.replace(
            "```json", ""
        ).replace(
            "```", ""
        ).strip()

        parsed = json.loads(cleaned)

    except Exception as e:

        print("JSON Error:", e)

        parsed = {
            "features": [],
            "roles": [],
            "functional_requirements": []
        }

    state["features"] = parsed.get(
        "features",
        []
    )

    state["roles"] = parsed.get(
        "roles",
        []
    )

    state["functional_requirements"] = parsed.get(
        "functional_requirements",
        []
    )

    return state