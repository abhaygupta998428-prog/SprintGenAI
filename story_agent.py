import json

from agents.llm import generate_response
from prompts.story_prompt import build_story_prompt


def story_agent(state):

    prompt = build_story_prompt(
        state["features"]
    )

    response = generate_response(prompt)

    print("Story Agent Response:")
    print(response)

    try:

        cleaned = response.replace(
            "```json", ""
        ).replace(
            "```", ""
        ).strip()

        stories = json.loads(cleaned)

    except Exception as e:

        print("Story JSON Error:", e)

        stories = []

    state["stories"] = stories

    return state