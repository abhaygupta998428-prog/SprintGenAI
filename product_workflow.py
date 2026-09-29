from agents.requirement_agent import (
    requirement_agent
)

from agents.story_agent import (
    story_agent
)

from agents.priority_agent import (
    priority_agent
)

from agents.sprint_agent import (
    sprint_agent
)

from agents.jira_agent import (
    jira_agent
)


def run_workflow(requirements):

    state = {

        "requirements": requirements,

        "features": [],

        "roles": [],

        "functional_requirements": [],

        "stories": [],

        "priorities": [],

        "sprints": [],

        "tickets": []
    }

    state = requirement_agent(state)

    state = story_agent(state)

    state = priority_agent(state)

    state = sprint_agent(state)

    state = jira_agent(state)

    return state