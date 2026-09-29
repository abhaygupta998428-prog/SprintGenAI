def build_story_prompt(features):

    return f"""
You are an Agile Product Manager.

Convert the features into Agile User Stories.

Features:
{features}

Return ONLY valid JSON.

Format:

[
    {{
        "title":"",
        "story":""
    }}
]
"""