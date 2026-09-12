import streamlit as st
from agent import Agent


st.set_page_config(
    page_title="Self-Learning AI Agent",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 Self-Learning AI Agent")

st.caption(
    "A self-learning AI agent built with Python, "
    "using Ollama/Qwen3 locally and Gemini for cloud deployment"
)

if "agent" not in st.session_state:
    st.session_state.agent = Agent("MyAgent")


agent = st.session_state.agent


goal = st.text_area(
    "🎯 Give your agent a goal",
    placeholder=(
        "Example: Calculate 2500 + 3500, "
        "save the result to final.txt, then read the file"
    ),
    height=100
)


if st.button("🚀 Run Agent", type="primary"):

    if not goal.strip():

        st.warning("Please enter a goal.")

    else:

        with st.spinner("Agent is creating a plan..."):
            plan = agent.plan(goal)

        st.subheader("📋 Plan")
        st.code(plan)

        steps = plan.split("\n\n")

        previous_result = ""
        overall_success = True

        for step_number, step in enumerate(steps, start=1):

            if not step.strip():
                continue

            st.markdown(f"### 🔹 Step {step_number}")
            st.code(step)

            task = ""
            planned_tool = ""

            for line in step.splitlines():

                if line.startswith("TASK:"):
                    task = line.replace(
                        "TASK:",
                        ""
                    ).strip()

                elif line.startswith("TOOL:"):
                    planned_tool = line.replace(
                        "TOOL:",
                        ""
                    ).strip()

            if not task:

                st.error(
                    "Could not find a task for this step."
                )

                overall_success = False
                break

            if not planned_tool:

                st.error(
                    "Could not find a planned tool for this step."
                )

                overall_success = False
                break

            st.info(
                f"🛠️ Planned tool: {planned_tool}"
            )

            max_attempts = 2
            step_success = False

            for attempt in range(1, max_attempts + 1):

                with st.spinner(
                    f"Executing step {step_number} "
                    f"(attempt {attempt}/{max_attempts})..."
                ):

                    thinking = agent.think(
                        task,
                        previous_result
                    )

                    result = agent.act(
                        task,
                        thinking,
                        planned_tool
                    )

                    agent.observe(result)

                    success = agent.evaluate(result)

                with st.expander(
                    f"🧠 Brain decision - "
                    f"Step {step_number}, "
                    f"Attempt {attempt}"
                ):

                    st.code(thinking)

                st.write("📤 Result:")

                st.code(str(result))

                if success:

                    agent.learn(
                        task,
                        result,
                        True
                    )

                    st.success(
                        f"✅ Step {step_number} "
                        f"completed successfully."
                    )

                    previous_result = result
                    step_success = True

                    break

                else:

                    agent.learn(
                        task,
                        result,
                        False
                    )

                    st.error(
                        f"❌ Step {step_number} "
                        f"failed on attempt {attempt}."
                    )

            if not step_success:

                st.error(
                    f"❌ Step {step_number} "
                    f"failed after {max_attempts} attempts."
                )

                overall_success = False
                break

        st.divider()

        if overall_success:

            st.success(
                "🎯 Goal completed successfully! 🚀"
            )

        else:

            st.error(
                "❌ Goal could not be completed."
            )