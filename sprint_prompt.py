def build_sprint_prompt(priorities):

    return f"""
You are a Scrum Master.

Create Sprint Planning.

Rules:

High Priority -> Sprint 1

Medium Priority -> Sprint 2

Low Priority -> Sprint 3

Data:
{priorities}

Return ONLY valid JSON.

Format:

[
    {{
        "sprint":"",
        "stories":[]
    }}
]
"""