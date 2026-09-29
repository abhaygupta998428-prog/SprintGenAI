import streamlit as st

from workflows.product_workflow import run_workflow

st.set_page_config(
    page_title="SprintGenAI",
    layout="wide"
)

st.markdown("""
<style>

.stButton > button {
    width: 100%;
    height: 60px;
    font-size: 18px;
    font-weight: bold;
    border-radius: 12px;
}

[data-testid="stMetric"] {
    background-color: #262730;
    padding: 15px;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

st.title(" SprintGenAI")
st.subheader(
    "Autonomous AI Product Manager"
)

st.markdown("""
### Transform Requirements into Agile Deliverables

Generate:

 Features

 User Stories

 Sprint Plans

 Jira Tickets

using AI Agents powered by Gemini.
""")

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/5956/5956592.png",
        width=120
    )

    st.title("SprintGenAI")

    st.success(" Gemini Connected")

    st.markdown("""
### Workflow

 Requirements

⬇

 Feature Extraction

⬇

 User Stories

⬇

 Prioritization

⬇

 Sprint Planning

⬇

 Jira Tickets
""")

requirements = st.text_area(
    "Enter Project Requirements",
    height=250,
    placeholder="""
Example:

Build an AI Resume Analyzer.

Users should upload resumes.

System should provide ATS score.

System should generate suggestions.

System should allow PDF export.
"""
)

generate_button = st.button(
    "Generate Product Plan"
)

if generate_button:

    if not requirements.strip():

        st.warning(
            "Please enter requirements."
        )

    else:

        with st.spinner(
            "Generating Product Plan..."
        ):

            result = run_workflow(
                requirements
            )

        st.success(
            "Product Plan Generated!"
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
         st.metric("Features", len(result["features"]))

        with col2:
         st.metric("Stories", len(result["stories"]))

        with col3:
         st.metric("Sprints", len(result["sprints"]))

        with col4:
         st.metric("Tickets", len(result["tickets"]))

        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        [
         " Features",
         " Roles",
         " Stories",
         " Priorities",
         " Sprints",
         " Jira Tickets"
        ]
        )

        with tab1:

          st.header("Generated Features")

          for feature in result["features"]:

           st.success(feature)

        with tab2:

          st.header("User Roles")

          for role in result["roles"]:

           st.info(role)

        with tab3:

           st.header("User Stories")

           for story in result["stories"]:

            with st.expander(
            story.get("title", ""),
            expanded=False
            ):

             st.write(
                story.get("story", "")
             )

        with tab4:

             st.header("Story Priorities")

             for item in result["priorities"]:

              title = item.get(
                "title",
                ""
                )

             priority = item.get(
            "priority",
            ""
                )

        st.write(f"### {title}")

        if priority.lower() == "high":

              st.error(" HIGH")

        elif priority.lower() == "medium":

             st.warning(" MEDIUM")

        else:

             st.success(" LOW")

        with tab5:

          st.header("Sprint Roadmap")

          for sprint in result["sprints"]:

           st.subheader(
            " " +
            sprint.get(
                "sprint",
                ""
            )
            )

           for story in sprint.get(
            "stories",
            []
            ):

            st.write(
                " " + story
            )

            st.divider()

        with tab6:

         st.header("Jira Tickets")

         for ticket in result["tickets"]:

          with st.container():

            st.markdown(
                f"""
        ###  {ticket.get('ticket','')}

        **Title**

        {ticket.get('title','')}

        **Description**
 
        {ticket.get('description','')}
        """
            )

            st.divider()