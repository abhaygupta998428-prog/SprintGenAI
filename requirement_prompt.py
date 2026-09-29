def build_requirement_prompt(requirements):

    return f"""
You are a Senior Product Manager.

Analyze the project requirements.

Requirements:
{requirements}

Return ONLY valid JSON.

Format:

{{
    "features": [],
    "roles": [],
    "functional_requirements": []
}}
"""