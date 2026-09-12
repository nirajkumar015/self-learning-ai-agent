from agent import Agent


agent = Agent("MyAgent")


while True:

    goal = input("\nGive me a goal: ")

    # ---------------------------------
    # EXIT
    # ---------------------------------

    if goal.lower().strip() == "exit":

        print("\nAgent shutting down.")

        break

    # ---------------------------------
    # SHOW LEARNING
    # ---------------------------------

    if goal.lower().strip() == "learning":

        agent.show_learning()

        continue

    # ---------------------------------
    # CREATE PLAN
    # ---------------------------------

    plan = agent.plan(goal)

    steps = plan.split("\n\n")

    previous_result = ""

    step_results = []

    overall_success = True

    # ---------------------------------
    # EXECUTE PLAN
    # ---------------------------------

    for step_number, step in enumerate(
        steps,
        start=1
    ):

        if not step.strip():

            continue

        print("\n" + "=" * 50)

        print(
            f"CURRENT STEP {step_number}"
        )

        print("=" * 50)

        print(step)

        # ---------------------------------
        # EXTRACT TASK + TOOL
        # ---------------------------------

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

        # ---------------------------------
        # VALIDATE STEP
        # ---------------------------------

        if not task:

            print(
                "\n⚠️ Could not find a task."
            )

            overall_success = False

            break

        if not planned_tool:

            print(
                "\n⚠️ Could not find a planned tool."
            )

            overall_success = False

            break

        # ---------------------------------
        # RETRY
        # ---------------------------------

        max_attempts = 2

        step_success = False

        for attempt in range(
            1,
            max_attempts + 1
        ):

            print(
                f"\n🔄 Attempt "
                f"{attempt}/{max_attempts}"
            )

            # Brain
            thinking = agent.think(
                task,
                previous_result
            )

            # Execute planned tool
            result = agent.act(
                task,
                thinking,
                planned_tool
            )

            # Observe
            agent.observe(
                result
            )

            # Evaluate
            success = agent.evaluate(
                result
            )

            if success:

                print(
                    "\n✅ Step completed successfully."
                )

                agent.learn(
                    task,
                    result,
                    True
                )

                previous_result = result

                step_results.append(
                    result
                )

                step_success = True

                break

            else:

                print(
                    "\n❌ Step failed."
                )

                agent.learn(
                    task,
                    result,
                    False
                )

                if attempt < max_attempts:

                    print(
                        "\n🔁 Retrying the step..."
                    )

        # ---------------------------------
        # STEP FAILED
        # ---------------------------------

        if not step_success:

            print(
                f"\n❌ Step {step_number} failed "
                f"after {max_attempts} attempts."
            )

            overall_success = False

            break

    # ---------------------------------
    # FINAL RESPONSE
    # ---------------------------------

    print("\n" + "=" * 50)

    if overall_success:

        print(
            "🎯 GOAL COMPLETED SUCCESSFULLY ✅"
        )

        final_answer = agent.create_final_response(
            goal,
            step_results
        )

        print("\n🤖 FINAL ANSWER:")
        print(final_answer)

    else:

        print(
            "🎯 GOAL COULD NOT BE COMPLETED ❌"
        )

    print("=" * 50)