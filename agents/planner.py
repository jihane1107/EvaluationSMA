def planner_agent(state):
    llm = state["llm"]
    context = state["context"]
    question = state["question"]

    plan = llm.invoke(f"Organise ces infos:\n{context}")

    return {
        **state,
        "plan": plan
    }