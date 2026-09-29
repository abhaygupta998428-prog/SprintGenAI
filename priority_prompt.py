def build_priority_prompt(stories):

    return f"""
You are a Product Manager.

Prioritize the following stories.

Priority values:

High
Medium
Low

Stories:
{stories}

Return ONLY valid JSON.

Format:

[
    {{
        "title":"",
        "priority":""
    }}
]
"""