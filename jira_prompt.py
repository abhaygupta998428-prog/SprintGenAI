def build_jira_prompt(stories):

    return f"""
You are a Jira Project Manager.

Convert stories into Jira Tickets.

Stories:
{stories}

Return ONLY valid JSON.

Format:

[
    {{
        "ticket":"",
        "title":"",
        "description":""
    }}
]
"""